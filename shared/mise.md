### Install tools with Mise package manager

[Mise](https://mise.jdx.dev) installs tools and their versions on every Clever Cloud runtime. Add a `mise.toml` file at the root of your project: Clever Cloud installs the tools it lists before the build phase. It can also define [environment variables](https://mise.jdx.dev/environments/) and [tasks](https://mise.jdx.dev/tasks/).

To place this file in another folder, set its path in `CC_MISE_FILE_PATH`, such as `config/mise.toml`: Mise runs from this folder.

To disable Mise, set `CC_DISABLE_MISE=true`: Clever Cloud then installs no tool from `mise.toml`, and the Linux runtime ignores Mise tasks.

- [Learn more about Mise configuration](https://mise.jdx.dev/configuration.html)
