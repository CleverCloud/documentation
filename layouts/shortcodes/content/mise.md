### Install tools with Mise package manager

Mise package manager is a powerful tool to install and manage dependencies on Clever Cloud. Just add a `mise.toml` file at the root of your project or set the `CC_MISE_FILE_PATH` environment variable. All tools will be installed at the defined version before the build phase and available for your scripts. You can also use Mise to define [environment variables](https://mise.jdx.dev/environments/) and alias ([tasks](https://mise.jdx.dev/tasks/)) in a declarative way.

To disable Mise, set `CC_DISABLE_MISE` environment variable to `true`.

- [Learn more about Mise package manager](https://mise.jdx.dev/configuration.html)
