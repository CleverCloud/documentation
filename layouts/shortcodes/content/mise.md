## Install tools with Mise package manager

Mise package manager is a powerful tool to install and manage dependencies on Clever Cloud. Just add a `mise.toml` file at the root of your project and set the `CC_RUN_MISE_INSTALL` environment variable to `true`. All tools will be installed at the defined version before the build phase and available for your scripts. You can also use Mise to define [environment variables](https://mise.jdx.dev/environments/) and alias ([tasks](https://mise.jdx.dev/tasks/)) in a declarative way.

- [Learn more about Mise package manager](https://mise.jdx.dev/configuration.html)
