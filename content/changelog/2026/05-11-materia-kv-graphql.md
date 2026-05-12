---
title: "Materia KV: query your data through GraphQL"
description: Read your Materia KV add-on through a typed GraphQL endpoint, in addition to the Redis API. Same keyspace, same token, served from a shared per-region URL.
date: 2026-05-11
tags:
  - addons
  - materia
  - kv
  - graphql
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

[Materia KV](/doc/addons/materia-kv/) gains a second compatibility layer: a **GraphQL** endpoint that reads from the same keyspace as the Redis API. Every key you write through a Redis/Valkey compatible client is immediately queryable through GraphQL, with no synchronization in between. Both interfaces authenticate with the same token (`$KV_TOKEN` / `$REDIS_PASSWORD`), passed as a bearer token.

As Materia KV is a distributed cluster, the GraphQL endpoint is a single URL shared by every add-on in a given region. For Paris:

```
https://materiakv-graphql.eu-fr-1.services.clever-cloud.com/graphql
```

The schema exposes a single root type, `MateriaKvQuery`, with queries for strings, hashes and sets — single-key lookups, batched reads, pattern matching, and server-side set algebra (`setIntersection`, `setDifference`, `setUnion`). Introspection is enabled, so you can browse the full schema in the embedded **GraphiQL** playground (open the URL in a browser) or pull it as SDL with any introspection tool.

The GraphQL layer is **read-only** for now — mutations aren't supported yet. Use the Redis API for writes. Have a look at [this end-to-end example](https://github.com/CleverCloud/kv-graphql-example) combining both layers: writes via the Redis API, reads via GraphQL.

- [Learn more about the GraphQL compatibility layer](/doc/addons/materia-kv/#using-the-graphql-compatibility-layer)
- [Materia KV write via Redis API, read via GraphQL](https://github.com/CleverCloud/kv-graphql-example)
