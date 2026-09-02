#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Check internal hyperlinks in a built Hugo site.

Scope: <a href> only. Assets (img/src, srcset, link, script) have different
semantics and exemptions and are deliberately left to the deployed
`linkchecker` job.

Complements that job, which follows redirects and checks external URLs but
never validates URL fragments. This one runs offline on the build output
and reports what it cannot see:

  broken       the target page does not exist
  dead-alias   the link lands on an alias whose chain ends nowhere
  alias-loop   the redirect chain loops back on itself
  lost-anchor  the link lands on an alias AND carries a fragment; a Hugo
               alias is a <meta http-equiv="refresh"> with no JavaScript,
               which drops the fragment, so the reader lands at the top
  anchor       the target exists but has no matching id
  redirect     the link lands on an alias, so it costs an extra hop (note)

Same-origin links outside this build are served by another application and
are simply set aside: `linkchecker` already covers them in CI.

`source_locations` are heuristic candidates: the Markdown lines whose text
contains the offending URL. They can miss a link produced by a template or
by hugo.yaml, so `rendered_pages` is always reported as well.

Notes are summarised as counts by default and only listed with -d: they
need no action here. `--format json` emits a stable machine-readable report
on stdout for tooling and agents; diagnostics go to stderr.

Resolution runs against an exact, case-sensitive index of the files in the
build. macOS is case-insensitive and Linux is not, so an `is_file()` probe
would accept /doc/Foo locally and 404 in CI; the index makes both agree.
URL paths are percent-decoded and normalised before the prefix boundary is
tested, so a link climbing out of the prefix with `..` cannot be validated
against the wrong file.

Ownership: a path under the baseURL prefix belongs to this build and must
resolve, unless it is declared with --external-prefix (other applications
are deployed under the same prefix).

The HTML <base> element is not honoured; the build contains none, and
supporting it would need its own same-origin and ownership checks.

Usage:
  hugo                                       # writes to publishDir
  ./check-internal-links.py                  # defaults to public/developers
  uv run check-internal-links.py -d          # also list the non-blocking notes
  uv run check-internal-links.py --format json   # machine-readable, stdout only
  uv run check-internal-links.py --root some/dir --prefix /developers

Exit codes: 0 clean, 1 problems found, 2 bad invocation or missing build.
"""

from __future__ import annotations

import argparse
import difflib
import json
import os
import posixpath
import re
import shutil
import sys
from collections import Counter, defaultdict
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures.process import BrokenProcessPool
from html.parser import HTMLParser
from pathlib import Path
from time import perf_counter
from typing import TYPE_CHECKING, NamedTuple, NoReturn

if TYPE_CHECKING:
    from collections.abc import Iterable, Sequence

    Attrs = Sequence[tuple[str, str | None]]
from urllib.parse import unquote, urljoin, urlsplit, urlunsplit

# Paths served under the baseURL prefix by something other than this build.
DEFAULT_EXTERNAL = ("/developers/clever-components",)
# Pages whose anchors are generated client-side, absent from static HTML.
DEFAULT_SKIP_ANCHORS = ("api/v2",)
DEFAULT_SOURCES = ("content", "shared")
DEFAULT_CONFIGS = ("hugo.yaml",)

SKIPPED_SCHEMES = ("mailto:", "tel:", "javascript:", "data:")
DEFAULT_PORTS = {"http": "80", "https": "443"}
ALIAS_HOP_LIMIT = 10  # a Hugo alias chain is normally one hop
MAX_SUGGESTIONS = 5  # near-miss anchors offered as a fix
SUGGESTION_CUTOFF = 0.4  # loose enough to catch prefix- -> path-routing
MAX_SOURCE_LINES = 4  # source lines printed per finding
MAX_PAGES_LISTED = 2  # rendered pages printed before "+N more"
CHUNKS_PER_WORKER = 4  # how finely the page list is split across workers
CHUNK_CEILING = 64  # never hand a worker more than this in one go
HELP_WIDTH = 96  # usage and help never wrap wider than this

EXIT_OK, EXIT_FINDINGS, EXIT_MISUSE = 0, 1, 2
GLYPHS = "✓✗·→"  # dropped together when the stream cannot encode them


class Kind(NamedTuple):
    """A category of finding: how to name it, explain it, and how bad it is."""

    name: str
    title: str
    explanation: str
    blocking: bool


KINDS: tuple[Kind, ...] = (
    Kind(
        "broken",
        "Broken targets",
        "The target does not exist in the build.",
        blocking=True,
    ),
    Kind(
        "dead-alias",
        "Redirects to missing pages",
        "The link lands on a redirect whose own destination is missing.",
        blocking=True,
    ),
    Kind(
        "alias-loop",
        "Redirect loops",
        "The chain of redirects comes back on itself and never lands.",
        blocking=True,
    ),
    Kind(
        "lost-anchor",
        "Fragments lost in redirects",
        "A redirect cannot carry a #fragment: the reader lands at the top.",
        blocking=True,
    ),
    Kind(
        "anchor",
        "Missing anchors",
        "The page exists but has no element with that id, usually a renamed heading.",
        blocking=True,
    ),
    Kind(
        "redirect",
        "Redirects",
        "These resolve through an alias. Point them at the destination to save a hop.",
        blocking=False,
    ),
)
KIND_ORDER = [kind.name for kind in KINDS]
BLOCKING = frozenset(kind.name for kind in KINDS if kind.blocking)
NOTE_LABEL = {"redirect": "redirecting"}


# --------------------------------------------------------------------------
# Small pure helpers
# --------------------------------------------------------------------------


def canon_origin(scheme: str, netloc: str) -> str:
    """Canonical scheme://host, lowercased and without a default port."""
    scheme = (scheme or "").lower()
    host = (netloc or "").lower()
    port = DEFAULT_PORTS.get(scheme)
    if port and host.endswith(f":{port}"):
        host = host[: -len(port) - 1]
    return f"{scheme}://{host}" if host else ""


def parse_refresh(content: str) -> str | None:
    """Target of a zero-delay meta refresh, else None.

    Only a zero delay is a Hugo alias. A page with a real timed refresh is
    a normal page and must still be crawled.
    """
    delay, separator, rest = content.partition(";")
    if not separator:
        return None
    try:
        if float(delay.strip()) != 0:
            return None
    except ValueError:
        return None
    rest = re.sub(r"^url\s*=\s*", "", rest.strip(), count=1, flags=re.IGNORECASE)
    if rest[:1] == rest[-1:] and rest[:1] in ("'", '"'):
        rest = rest[1:-1]
    return rest.strip() or None


def wanted_anchor(fragment: str) -> str | None:
    """The id a fragment targets, or None when it targets no id.

    `#top` scrolls to the top of the document with no element of that name,
    and a `:~:` text directive is not an id at all.
    """
    frag = unquote(fragment)
    if ":~:" in frag:
        frag = frag.split(":~:", 1)[0]
    if not frag or frag.lower() == "top":
        return None
    return frag


def under(path: str, prefix: str) -> bool:
    """True if `path` equals `prefix` or lives under it. Never a raw startswith."""
    return path == prefix or path.startswith(prefix.rstrip("/") + "/")


def display_path(path: str) -> str:
    """Path relative to the invocation directory, in POSIX form.

    Always relative when it can be computed: an absolute path would leak
    the local layout into a published JSON artifact and make the report
    differ between runners.
    """
    try:
        return os.path.relpath(path, Path.cwd()).replace(os.sep, "/")
    except ValueError:  # different volume on Windows
        return path.replace(os.sep, "/")


def plural(count: int, singular: str, many: str | None = None) -> str:
    return f"{count:,} {singular if count == 1 else (many or singular + 's')}"


def cpu_limit() -> int:
    return os.cpu_count() or 1


# --------------------------------------------------------------------------
# Parsing
# --------------------------------------------------------------------------


class Page(HTMLParser):
    """Collect hyperlinks, anchor ids and any meta refresh from one page.

    A real parser rather than a regex: it handles uppercase attributes,
    single or unquoted values and character references. It also puts
    <script>/<style> bodies in CDATA mode on its own, so an `id="..."`
    inside a JavaScript string is data and never registers as an anchor.
    """

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.hrefs: list[str] = []
        self.ids: set = set()
        self.refresh: str | None = None

    def handle_starttag(self, tag: str, attrs: Attrs) -> None:
        attributes: dict[str, str] = {}
        for key, value in attrs:
            attributes.setdefault(key.lower(), value or "")  # duplicates: first wins
        if attributes.get("id"):
            self.ids.add(attributes["id"])
        if tag == "a":
            if attributes.get("name"):
                self.ids.add(attributes["name"])
            if attributes.get("href"):
                self.hrefs.append(attributes["href"].strip())
        elif tag == "meta" and self.refresh is None:
            if attributes.get("http-equiv", "").strip().lower() == "refresh":
                self.refresh = parse_refresh(attributes.get("content", ""))

    def handle_startendtag(self, tag: str, attrs: Attrs) -> None:
        # A self-closing tag opens no body; only its attributes matter.
        self.handle_starttag(tag, attrs)


class PageData(NamedTuple):
    hrefs: list[str]
    ids: set
    refresh: str | None


def parse_file(job: tuple[str, str]) -> tuple[str, list[str], list[str], str | None]:
    """Parse one build file.

    Module level and returning plain data so it can run in a worker process.
    """
    root, rel = job
    page = Page()
    page.feed(Path(root, rel).read_text(encoding="utf-8", errors="replace"))
    page.close()
    return rel, page.hrefs, list(page.ids), page.refresh


class AliasChain(NamedTuple):
    status: str  # page | missing | loop | offsite
    chain: list[str]  # normalised URL of every hop, in order
    final_target: str | None
    final_target_file: str | None


# --------------------------------------------------------------------------
# The build under test
# --------------------------------------------------------------------------


class Site:
    """The built site: its files, their contents, and URL resolution."""

    def __init__(
        self, root: str, prefix: str, base_url: str, external: Iterable[str]
    ) -> None:
        self.root = str(Path(root).resolve())
        trimmed = prefix.strip("/")
        self.prefix = f"/{trimmed}" if trimmed else ""
        split = urlsplit(base_url or "")
        self.origin = canon_origin(split.scheme, split.netloc)
        self.external = tuple(f"/{e.strip('/')}" for e in external if e.strip("/"))
        self.files = self._index_files()
        self.pages = sorted(f for f in self.files if f.endswith(".html"))
        self._parsed: dict[str, PageData] = {}

    def _index_files(self) -> set:
        """Every file in the build, POSIX-relative and case-sensitive.

        A symlink pointing outside would otherwise be read as a page.
        """
        root = Path(self.root)
        found = set()
        for path in root.rglob("*"):
            if path.is_file() and str(path.resolve()).startswith(self.root + os.sep):
                found.add(path.relative_to(root).as_posix())
        return found

    # -- contents ----------------------------------------------------------

    def prime(self, jobs: int) -> None:
        """Parse every page up front, across `jobs` processes.

        Parsing HTML is CPU-bound and holds the GIL, so processes are the
        only way to use more than one core. Every page has to be parsed
        anyway: an alias is only recognisable once its meta refresh is read.
        """
        if jobs <= 1 or len(self.pages) <= 1:
            for rel in self.pages:
                self.parse(rel)
            return
        workers = min(jobs, len(self.pages))
        # A few chunks per worker: enough to amortise the hand-off, few
        # enough that one slow chunk cannot become the critical path.
        chunk = max(
            1, min(CHUNK_CEILING, len(self.pages) // (workers * CHUNKS_PER_WORKER))
        )
        with ProcessPoolExecutor(max_workers=workers) as pool:
            jobs_iter = ((self.root, rel) for rel in self.pages)
            parsed = pool.map(parse_file, jobs_iter, chunksize=chunk)
            for rel, hrefs, ids, refresh in parsed:
                self._parsed[rel] = PageData(hrefs, set(ids), refresh)

    def parse(self, rel: str) -> PageData:
        data = self._parsed.get(rel)
        if data is None:
            _, hrefs, ids, refresh = parse_file((self.root, rel))
            data = self._parsed[rel] = PageData(hrefs, set(ids), refresh)
        return data

    # -- URLs --------------------------------------------------------------

    def page_url(self, rel: str) -> str:
        """Site URL path served by a build file."""
        if rel == "index.html":
            return f"{self.prefix}/"
        if rel.endswith("/index.html"):
            return self.prefix + "/" + rel[: -len("index.html")]
        return f"{self.prefix}/{rel}"

    @staticmethod
    def normalize(url_path: str) -> str:
        """Percent-decode then collapse `.` and `..`, keeping a trailing slash."""
        path = unquote(url_path or "/")
        if not path.startswith("/"):
            path = f"/{path}"
        trailing = path.endswith("/")
        path = posixpath.normpath(path)
        if trailing and not path.endswith("/"):
            path += "/"
        return path

    def ownership(self, norm_path: str) -> str:
        """'build', 'external' or 'deferred' for an already normalised path."""
        if self.prefix and not under(norm_path, self.prefix):
            return "deferred"
        if any(under(norm_path, external) for external in self.external):
            return "external"
        return "build"

    def resolve(self, norm_path: str) -> str | None:
        """Map an owned, normalised URL path to a build file, or None."""
        path = norm_path
        if self.prefix:
            if not under(path, self.prefix):
                return None  # never map outside the prefix
            path = path[len(self.prefix) :]
        path = path.lstrip("/")
        page = posixpath.join(path, "index.html") if path else "index.html"
        candidates = (page, path)
        return next((c for c in candidates if c and c in self.files), None)

    def follow_alias(self, rel: str) -> AliasChain:
        """Follow a chain of aliases to the first page that is not one.

        Hugo normally emits direct aliases, but a chain would otherwise be
        reported as a harmless redirect even when it ends nowhere, which
        would leave CI green. Each hop resolves against its own alias page.
        """
        seen: list[str] = []
        chain: list[str] = []
        current = rel
        for _ in range(ALIAS_HOP_LIMIT):
            page = self.parse(current)
            if not page.refresh:
                return AliasChain("page", chain, self.page_url(current), current)
            seen.append(current)
            destination = self.normalize(
                urlsplit(urljoin(self.page_url(current), page.refresh)).path
            )
            chain.append(destination)
            if self.ownership(destination) != "build":
                return AliasChain("offsite", chain, destination, None)
            following = self.resolve(destination)
            if following is None:
                return AliasChain("missing", chain, destination, None)
            if following in seen:
                return AliasChain("loop", chain, destination, following)
            current = following
        return AliasChain("loop", chain, chain[-1] if chain else None, current)


# --------------------------------------------------------------------------
# Collection
# --------------------------------------------------------------------------


class Finding(NamedTuple):
    """Identity of a finding. The normalised target matters: the same
    relative href or self-fragment written on two pages points at two
    different places, and merging them would suggest the wrong fix."""

    kind: str
    link: str
    normalized_path: str
    discriminator: str


def interpret(site: Site, here: str, href: str) -> tuple[str, str] | None:
    """Turn one raw href into (url path, fragment), or None to skip it."""
    if not href or href.lower().startswith(SKIPPED_SCHEMES):
        return None
    split = urlsplit(href)
    if split.netloc:
        # Absolute or protocol-relative. A protocol-relative URL inherits
        # the page scheme, which is the baseURL scheme.
        scheme = split.scheme or urlsplit(site.origin).scheme
        if canon_origin(scheme, split.netloc) != site.origin:
            return None  # genuinely external host
        return split.path or "/", split.fragment
    if split.scheme:
        return None  # unknown scheme without a host
    joined = urlsplit(urljoin(here, href))
    return joined.path, joined.fragment


def alias_kind(chain: AliasChain, *, has_fragment: bool) -> str:
    if chain.status == "missing":
        return "dead-alias"
    if chain.status == "loop":
        return "alias-loop"
    return "lost-anchor" if has_fragment else "redirect"


class Issue(NamedTuple):
    """What is wrong with one link, and the context needed to fix it."""

    kind: str
    target_file: str | None = None
    alias: AliasChain | None = None
    fragment: str = ""
    anchor: str | None = None

    @property
    def discriminator(self) -> str:
        """Tells apart two findings sharing a kind, href and target."""
        final = self.alias.final_target if self.alias else None
        return final or self.anchor or self.fragment or ""


class Entry(NamedTuple):
    """One finding, and how many times each page renders it."""

    issue: Issue
    link: str
    normalized_path: str
    pages: Counter


class FindingStore:
    """Findings keyed by identity, each counting the pages that render it."""

    def __init__(self) -> None:
        self._entries: dict[Finding, Entry] = {}

    def add(self, page: str, link: str, norm: str, issue: Issue) -> None:
        key = Finding(issue.kind, link, norm, issue.discriminator)
        entry = self._entries.get(key)
        if entry is None:
            entry = self._entries[key] = Entry(issue, link, norm, Counter())
        entry.pages[page] += 1

    @property
    def entries(self) -> dict[Finding, Entry]:
        return self._entries


def classify(
    site: Site, norm: str, fragment: str, skip_anchors: Sequence[str]
) -> Issue | None:
    """What is wrong with an owned link, if anything.

    Returns None when the link resolves correctly.
    """
    target = site.resolve(norm)
    if target is None:
        return Issue("broken")
    decoded = unquote(fragment) if fragment else ""
    if site.parse(target).refresh:
        chain = site.follow_alias(target)
        return Issue(
            alias_kind(chain, has_fragment=bool(fragment)),
            target_file=target,
            alias=chain,
            fragment=decoded,
        )
    anchor = wanted_anchor(fragment) if fragment else None
    if anchor is None or any(under(f"/{target}", f"/{s}") for s in skip_anchors):
        return None
    if anchor in site.parse(target).ids:
        return None
    return Issue("anchor", target_file=target, fragment=decoded, anchor=anchor)


def collect(
    site: Site, skip_anchors: Sequence[str]
) -> tuple[dict[Finding, Entry], int]:
    """Walk every real page and classify each internal hyperlink."""
    store = FindingStore()
    checked = 0
    for rel in site.pages:
        page = site.parse(rel)
        if page.refresh:
            continue  # do not crawl redirect stubs
        here = site.page_url(rel)
        for href in page.hrefs:
            interpreted = interpret(site, here, href)
            if interpreted is None:
                continue
            url_path, fragment = interpreted
            norm = site.normalize(url_path)
            if site.ownership(norm) != "build":
                continue  # another build serves it
            checked += 1
            issue = classify(site, norm, fragment, skip_anchors)
            if issue is not None:
                store.add(rel, href, norm, issue)
    return store.entries, checked


def enrich(site: Site, entry: Entry) -> dict:
    """Turn one finding into the JSON object a fixer consumes.

    The result stays a plain dict: optional keys must be absent rather
    than null, which a fixed set of dataclass fields cannot express.
    """
    issue = entry.issue
    out = {
        "kind": issue.kind,
        "severity": "error" if issue.kind in BLOCKING else "note",
        "blocking": issue.kind in BLOCKING,
        "link": entry.link,
        "normalized_path": entry.normalized_path,
        "target_file": issue.target_file,
        "occurrences": sum(entry.pages.values()),
        "rendered_pages": [
            {"path": path, "occurrences": count}
            for path, count in sorted(entry.pages.items())
        ],
    }
    if issue.alias:
        out["redirect_chain"] = issue.alias.chain
        out["final_target"] = issue.alias.final_target
        out["final_target_file"] = issue.alias.final_target_file
    if issue.fragment:
        out["fragment"] = issue.fragment
    if issue.anchor:
        out["wanted_anchor"] = issue.anchor
        ids = sorted(site.parse(issue.target_file).ids) if issue.target_file else []
        # A renamed heading is the usual cause, so the near matches are
        # exactly the fix. The full list would bloat the report for nothing.
        out["suggested_anchors"] = difflib.get_close_matches(
            issue.anchor, ids, n=MAX_SUGGESTIONS, cutoff=SUGGESTION_CUTOFF
        )
        out["available_anchor_count"] = len(ids)
    return out


def front_matter_end(lines: Sequence[str]) -> int:
    """Line number closing the YAML front matter, or 0 when there is none."""
    if not lines or lines[0].strip() != "---":
        return 0
    for number, line in enumerate(lines[1:], 2):
        if line.strip() == "---":
            return number
    return 0


def scan_lines(path: Path, *, skip_front_matter: bool) -> Iterable[tuple[int, str]]:
    """Yield the (number, text) of every line worth searching in a file."""
    try:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return
    # Front matter declares the aliases that CREATE the redirects. Offering
    # one as the place to fix a link points at the destination page instead
    # of the link, and deleting it would break the URL rather than mend it.
    start = front_matter_end(lines) if skip_front_matter else 0
    for number, line in enumerate(lines, 1):
        if number > start:
            yield number, line


class LinkIndex(NamedTuple):
    """The URL spellings to look for, and the pattern that finds them."""

    owners: dict[str, set[str]]  # spelling -> links wanting it
    fragments: dict[str, str]  # link -> fragment it must carry
    pattern: re.Pattern[str]

    @classmethod
    def build(cls, links: Iterable[str], prefix: str) -> LinkIndex | None:
        """Index every wanted link, or None when there is nothing to find.

        Markdown writes internal links without the baseURL prefix (/doc/x)
        while card shortcodes include it (/developers/doc/x), so both
        spellings are indexed.
        """
        owners: dict[str, set[str]] = defaultdict(set)
        fragments: dict[str, str] = {}
        for link in links:
            path, _, fragment = link.partition("#")
            path = path.rstrip("/")
            fragments[link] = fragment
            spellings = {path}
            if prefix and under(path, prefix):
                spellings.add(path[len(prefix) :])
            for spelling in spellings:
                if spelling:
                    owners[spelling].add(link)
        if not owners:
            return None
        # Longest first so the alternation prefers /doc/foobar over
        # /doc/foo; the optional trailing slash keeps /doc/foo/ matching,
        # and the lookahead refuses anything that would continue the path.
        alternation = "|".join(
            re.escape(spelling) for spelling in sorted(owners, key=len, reverse=True)
        )
        return cls(owners, fragments, re.compile(f"({alternation})/?(?![\\w./-])"))

    def matches(self, line: str) -> Iterable[str]:
        """The wanted links this line actually refers to."""
        for match in self.pattern.finditer(line):
            for link in self.owners[match.group(1)]:
                fragment = self.fragments[link]
                if not fragment or f"#{fragment}" in line:
                    yield link


def source_index(
    links: Iterable[str],
    source_dirs: Sequence[str],
    prefix: str,
    configs: Sequence[str] = (),
) -> dict[str, list[str]]:
    """One pass over the sources, mapping each link to file:line.

    Menu entries in the site config produce links too, and they are the
    only source for a link rendered on every page. Matching is anchored on
    a path boundary, so /doc/foo never claims the line of /doc/foobar, and
    every wanted URL is searched in a single pass.
    """
    index = LinkIndex.build(links, prefix)
    if index is None:
        return {}
    targets = [
        (path, True)
        for base in sorted(source_dirs)
        for path in sorted(Path(base).rglob("*.md"))
    ]
    targets += [(Path(config), False) for config in configs if Path(config).is_file()]

    hits: dict[str, list[str]] = defaultdict(list)
    for path, is_markdown in targets:
        for number, line in scan_lines(path, skip_front_matter=is_markdown):
            for link in index.matches(line):
                hits[link].append(f"{display_path(str(path))}:{number}")
    return hits


# --------------------------------------------------------------------------
# Reporting
# --------------------------------------------------------------------------


class Report(NamedTuple):
    grouped: dict[str, list[dict]]
    checked: int
    files: int
    details: bool
    locations: dict[str, list[str]]
    prefix: str = ""
    origin: str = ""
    seconds: float = 0.0

    def of(self, kind: str) -> list[dict]:
        return self.grouped.get(kind, [])

    @property
    def errors(self) -> list[dict]:
        return [
            record
            for kind in KIND_ORDER
            if kind in BLOCKING
            for record in self.of(kind)
        ]


def counts(records: Sequence[dict]) -> dict:
    return {
        "links": len(records),
        "occurrences": sum(record["occurrences"] for record in records),
    }


class Style(NamedTuple):
    """How much the terminal on the other end can take."""

    colour: bool
    unicode: bool

    @classmethod
    def detect(cls, stream: object | None = None) -> Style:
        """What the stream on the other end can actually render.

        NO_COLOR is the convention from no-color.org; a pipe, a file or a
        dumb terminal gets no escape codes either. Unicode is a separate
        question: a redirected UTF-8 stream still renders the glyphs, so
        the test is whether they encode, not whether it is a terminal.
        """
        stream = sys.stdout if stream is None else stream
        colour = (
            bool(getattr(stream, "isatty", bool)())
            and "NO_COLOR" not in os.environ
            and os.environ.get("TERM") != "dumb"
        )
        return cls(colour, cls.encodable(GLYPHS, stream))

    @staticmethod
    def encodable(text: str, stream: object) -> bool:
        try:
            text.encode(getattr(stream, "encoding", None) or "ascii")
        except (UnicodeEncodeError, LookupError):
            return False
        return True

    def paint(self, text: str, code: str) -> str:
        return f"\033[{code}m{text}\033[0m" if self.colour else text

    def dim(self, text: str) -> str:
        return self.paint(text, "2")

    def bold(self, text: str) -> str:
        return self.paint(text, "1")

    def red(self, text: str) -> str:
        return self.paint(text, "31")

    def green(self, text: str) -> str:
        return self.paint(text, "32")

    @property
    def bullet(self) -> str:
        return "·" if self.unicode else "-"

    @property
    def arrow(self) -> str:
        return "→" if self.unicode else "->"

    @property
    def tick(self) -> str:
        return "✓" if self.unicode else "OK"

    @property
    def cross(self) -> str:
        return "✗" if self.unicode else "!!"


def human_url(url: str, prefix: str, origin: str) -> str:
    """Shorten a URL for display: drop the origin, then the baseURL prefix.

    Mirrors what interpret() accepts, so every form it calls internal is
    shortened the same way: absolute, protocol-relative, uppercase host,
    default port. A foreign host or a relative href is left as written,
    since that raw text is what the reader will search for. The prefix is
    trimmed at an exact path boundary, never by string replacement, and
    the JSON report keeps the raw value.
    """
    split = urlsplit(url)
    if split.scheme or split.netloc:
        scheme = split.scheme or urlsplit(origin).scheme
        if canon_origin(scheme, split.netloc) != origin:
            return url
        text = urlunsplit(("", "", split.path or "/", split.query, split.fragment))
    elif url.startswith("/"):
        text = url
    else:
        return url
    path, separator, fragment = text.partition("#")
    if prefix and under(path, prefix):
        path = path[len(prefix) :] or "/"
    return path + separator + fragment


def elapsed(seconds: float) -> str:
    return f"{seconds:.2f}s" if seconds < 1 else f"{seconds:.1f}s"


def describe(record: dict, style: Style, prefix: str, origin: str) -> str:
    label = human_url(record["link"], prefix, origin)
    if not (label.startswith("/") or "://" in label):
        # A relative or same-page href means nothing on its own: the same
        # text resolves elsewhere from another page.
        resolved = human_url(record["normalized_path"], prefix, origin)
        label += style.dim(f"  (resolves to {resolved})")
    if record.get("final_target"):
        label += f"  {style.arrow}  {human_url(record['final_target'], prefix, origin)}"
    return label


def locations_of(record: dict, report: Report) -> list[str]:
    """The lines telling a reader where to go and fix this."""
    lines = report.locations.get(record["link"], [])[:MAX_SOURCE_LINES]
    if not lines:
        # No Markdown source matched: a self, relative or generated link.
        # The rendered page is then the only way to find it.
        pages = [page["path"] for page in record["rendered_pages"]]
        extra = (
            ""
            if len(pages) <= MAX_PAGES_LISTED
            else f"  (+{len(pages) - MAX_PAGES_LISTED} more)"
        )
        lines = [f"rendered in {', '.join(pages[:MAX_PAGES_LISTED])}{extra}"]
    if record.get("suggested_anchors"):
        lines.append("try " + " or ".join(f"#{a}" for a in record["suggested_anchors"]))
    return lines


def notes_line(report: Report, bullet: str) -> str | None:
    """One line standing in for the sections the reader did not ask to see."""
    parts = []
    for kind, label in NOTE_LABEL.items():
        records = report.of(kind)
        if records:
            occurrences = plural(counts(records)["occurrences"], "occurrence")
            parts.append(
                f"{plural(len(records), f'{label} link')}  {bullet}  {occurrences}"
            )
    if not parts:
        return None
    return ", ".join(parts) + " — run with -d for details"


def report_human(report: Report) -> int:
    style = Style.detect(sys.stdout)
    prefix = report.prefix
    errors = report.errors

    head = f"  {style.bullet}  ".join(
        [
            "check-internal-links",
            f"{report.checked:,} link checks",
            f"{report.files:,} files",
            elapsed(report.seconds),
        ]
    )
    print(style.dim(head))
    print()

    if errors:
        print(style.red(f"{style.cross} {plural(len(errors), 'blocking issue')}"))
    else:
        print(style.green(f"{style.tick} no blocking issue"))

    for kind in KINDS:
        records = report.of(kind.name)
        if not records or (not kind.blocking and not report.details):
            continue
        total = counts(records)
        scale = plural(total["links"], "link")
        if total["occurrences"] != total["links"]:
            scale += f"  {style.bullet}  {plural(total['occurrences'], 'occurrence')}"
        print()
        print(
            f"{style.bold(kind.title)}  {style.dim(style.bullet)}  {style.dim(scale)}"
        )
        print(f"  {kind.explanation}")
        for record in records:
            print()
            print(f"  {describe(record, style, prefix, report.origin)}")
            for line in locations_of(record, report):
                print(style.dim(f"    {line}"))

    if not report.details:
        pending = notes_line(report, style.bullet)
        if pending:
            if errors:
                print()  # never let the summary touch the last finding
            print(style.dim(f"  {pending}"))
    return len(errors)


def report_json(report: Report) -> int:
    errors = report.errors
    notes = [
        record
        for kind in KIND_ORDER
        if kind not in BLOCKING
        for record in report.of(kind)
    ]
    document = {
        "schema_version": 1,
        "tool": "check-internal-links",
        "status": "error" if errors else "ok",
        "summary": {
            "html_files": report.files,
            "checked_occurrences": report.checked,
            "blocking": dict(
                counts(errors),
                by_kind={
                    kind: counts(report.of(kind))
                    for kind in report.grouped
                    if kind in BLOCKING
                },
            ),
            "notes": dict(
                counts(notes),
                by_kind={
                    kind: counts(report.of(kind))
                    for kind in report.grouped
                    if kind not in BLOCKING
                },
            ),
        },
        "findings": errors,
        "notes": notes if report.details else [],
    }
    print(json.dumps(document, indent=2))
    return len(errors)


# --------------------------------------------------------------------------
# Entry point
# --------------------------------------------------------------------------


class Parser(argparse.ArgumentParser):
    """Argument parser that shows the help on a mistake.

    The default prints an unwrapped usage line and a bare message, which
    says what is wrong but not what to do instead.
    """

    def error(self, message: str) -> NoReturn:
        print(f"{self.prog}: {message}\n", file=sys.stderr)
        self.print_help(sys.stderr)
        raise SystemExit(EXIT_MISUSE)


def build_parser() -> Parser:
    # Wrap to the terminal, but never so wide that the usage becomes a wall.
    width = min(shutil.get_terminal_size(fallback=(100, 24)).columns - 2, HELP_WIDTH)

    def formatter(prog: str) -> argparse.HelpFormatter:
        return argparse.RawDescriptionHelpFormatter(prog, width=width)

    parser = Parser(description=__doc__, formatter_class=formatter)
    parser.add_argument(
        "--root", default="public/developers", help="built site directory"
    )
    parser.add_argument("--prefix", default="/developers", help="baseURL path prefix")
    parser.add_argument(
        "--base-url",
        default="https://www.clever.cloud",
        help="origin treated as internal for absolute URLs",
    )
    parser.add_argument(
        "--external-prefix",
        action="append",
        help="path under the prefix served by another app (repeatable)",
    )
    parser.add_argument(
        "--source", action="append", help="Markdown source directory (repeatable)"
    )
    parser.add_argument(
        "--config",
        action="append",
        help="site config file that can declare links (repeatable)",
    )
    parser.add_argument(
        "--skip-anchors",
        action="append",
        help="build path with client-rendered anchors (repeatable)",
    )
    parser.add_argument(
        "--format",
        choices=("human", "json"),
        default="human",
        help="human report (default) or a machine-readable one",
    )
    parser.add_argument(
        "-j",
        "--jobs",
        type=int,
        default=0,
        help=f"parallel workers, clamped to 1..{cpu_limit()} (default: all cores)",
    )
    parser.add_argument(
        "-d",
        "--details",
        action="store_true",
        help="list the non-blocking notes instead of counting them",
    )
    # Errors have always been the default; --quiet is kept so an existing
    # invocation does not break.
    parser.add_argument("--quiet", action="store_true", help=argparse.SUPPRESS)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    if not Path(args.root).is_dir():
        print(
            f"build directory not found: {args.root}\nRun `hugo` first.",
            file=sys.stderr,
        )
        return EXIT_MISUSE

    sources = [d for d in (args.source or DEFAULT_SOURCES) if Path(d).is_dir()]
    skip = tuple(s.strip("/") for s in (args.skip_anchors or DEFAULT_SKIP_ANCHORS))
    external = args.external_prefix or list(DEFAULT_EXTERNAL)
    jobs = max(1, min(args.jobs or cpu_limit(), cpu_limit()))
    started = perf_counter()

    try:
        site = Site(args.root, args.prefix, args.base_url, external)
        site.prime(jobs)
    except OSError as error:
        # An unreadable build is a broken invocation, not a finding: saying
        # so on stderr keeps stdout a valid report and the exit code honest.
        where = display_path(error.filename) if error.filename else args.root
        print(f"cannot read {where}: {error.strerror or error}", file=sys.stderr)
        return EXIT_MISUSE
    except BrokenProcessPool:
        print("a worker died while parsing the build; retry with -j 1", file=sys.stderr)
        return EXIT_MISUSE

    raw, checked = collect(site, skip)

    grouped: dict[str, list[dict]] = defaultdict(list)
    for key in sorted(raw):
        grouped[key.kind].append(enrich(site, raw[key]))

    wanted = {
        record["link"]
        for kind, records in grouped.items()
        for record in records
        if kind in BLOCKING or args.details
    }
    configs = args.config or DEFAULT_CONFIGS
    found = source_index(wanted, sources, site.prefix, configs) if wanted else {}
    locations = {link: sorted(set(lines)) for link, lines in found.items()}
    for records in grouped.values():
        for record in records:
            record["source_locations"] = [
                {"path": line.rsplit(":", 1)[0], "line": int(line.rsplit(":", 1)[1])}
                for line in locations.get(record["link"], [])
            ]

    report = Report(
        grouped,
        checked,
        len(site.pages),
        args.details,
        locations,
        site.prefix,
        site.origin,
        perf_counter() - started,
    )
    emit = report_json if args.format == "json" else report_human
    return EXIT_FINDINGS if emit(report) else EXIT_OK


if __name__ == "__main__":
    sys.exit(main())
