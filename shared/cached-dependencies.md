### Cached dependencies

#### Enabling dependencies caching

You can enable dependencies caching by adding the `CC_CACHE_DEPENDENCIES=true` [environment variable](#setting-up-environment-variables-on-clever-cloud) in your application. It's enabled by default only for Haskell and Rust applications.

To add folders to the dependencies cache, use `CC_CACHE_DEPENDENCIES_EXTRA_PATHS`. These paths should comply with the following rules:
- Be a subdirectory of the `$HOME` directory, but not the whole `$HOME` directory
- Be a sibling or a child of the whole `$APP_HOME` directory, but not the whole `$APP_HOME` directory
- Be relative to the application root directory (e.g. `vendor`, `../dependencies`)
- Be separated by a `:` if you want to add multiple paths (e.g. `CC_CACHE_DEPENDENCIES_EXTRA_PATHS=vendor:../dependencies`)

#### Disabling dependencies caching

You can disable dependencies caching completely by removing the `CC_CACHE_DEPENDENCIES` environment variable from the Clever Cloud console, in the **Environment variables** menu of your application.

Or by setting it to `CC_CACHE_DEPENDENCIES=false`

To fully remove cached dependencies, you have to rebuild your application from scratch.

You can select "rebuild and restart" from the Clever Cloud console or launch `clever restart --without-cache` with the Clever Tools CLI.
