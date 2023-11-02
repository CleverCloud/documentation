### Cached dependencies

#### Enabling dependencies caching

You can enable dependencies caching by adding the `CC_CACHE_DEPENDENCIES=true` [environment variable](#setting-up-environment-variables-on-clever-cloud) in your application. It is enabled by default only for rust and haskell applications.

#### Disabling dependencies caching

You can disable dependencies caching completely by removing the `CC_CACHE_DEPENDENCIES` environment variable from the Clever Cloud console, in the **Environment variables** menu of your application.

Or by setting it to `CC_CACHE_DEPENDENCIES=false`

To fully remove cached dependencies, you have to rebuild your application from scratch.

You can select "rebuild and restart" from the Clever Cloud console or launch `clever restart --without-cache` with the Clever Tools CLI.
