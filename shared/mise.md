### Install tools with Mise package manager

[Mise](https://mise.jdx.dev) is available on all Clever Cloud runtimes to install and manage tools and dependencies. Add a `mise.toml` file at the root of your project and all defined tools are installed at the specified version before the build phase. To place this file in a subdirectory, set the `CC_MISE_FILE_PATH` environment variable to its relative path (e.g. `config/mise.toml`). You can also use Mise to define [environment variables](https://mise.jdx.dev/environments/) and [tasks](https://mise.jdx.dev/tasks/) in a declarative way.

To disable Mise tool installation, set `CC_DISABLE_MISE` environment variable to `true`.

- [Learn more about Mise configuration](https://mise.jdx.dev/configuration.html)
