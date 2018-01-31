---
title: Deploying haskell apps
shortdesc: Haskell is love, haskell is life
tags:
- haskell
keywords:
- haskell
- stack
---

<div class="panel panel-warning">
  <div class="panel-heading">
     <h4>Haskell support is in public beta</h4>
  </div>
  <div class="panel-body">
    Haskell support is still new and rough around the edges, so please contact
the support to give feedback (good or bad).
  </div>
</div>

Clever Cloud allows you to deploy haskell web applications. This page will explain
you how to set up your application to run it on our service.

## Overview

Haskell is a purely functional language, especially suited for robust web
applications. There are many ways to write web applications in haskell, from
raw [WAI](https://hackage.haskell.org/package/wai) to full-stack frameworks
like [Yesod](http://www.yesodweb.com/), simple libraries like
[scotty](https://hackage.haskell.org/package/scotty) or
type-safe solutions like [servant](https://haskell-servant.github.io/).

Clever Cloud uses stack to build haskell applications.

## Create an application

Refer to the page [Deploy an application on Clever Cloud](/doc/clever-cloud-overview/add-application/).

## Necessary information

Be sure that:

* you have pushed in <b>master branch</b>
* you listen on <b>port 8080</b>
* you have one and only one binary target in your `.cabal` file
* your project has a `stack.yaml` file

## Requirements

The steps ran in order are:

 - `stack setup`
 - `stack install --only-dependencies`
 - `stack install`
 - `./<path>/my-exe` (or the contents of `CC_RUN_COMMAND`)

The executable built by `stack build` (or the command you specify) must start a
web server listening on `0.0.0.0:8080`.

For instance, a minimal scotty application can look like this:

```haskell
{-# LANGUAGE OverloadedStrings #-}

import Web.Scotty

main = scotty 8080 $ do
  get "/" $ do
    html $ "Hello world"
```

### Dependencies

Make sure to list all your dependencies in your `.cabal` file. For the example
above, you need:

```
  build-depends:       base
                     , scotty
```

Compiled dependencies are cached by default to speed up deployments. You can
disable dependencies caching completely by removing the `CACHE_DEPENDENCIES`
environment variable. If you want to rebuild your application from scratch,
you can select "rebuild and restart" from the console or launch `clever
restart --without-cache` from CLI.

## Environment injection

Clever Cloud can inject environment variables that are defined in the
dashboard and by add-ons linked to your application.

You can access environment variables with `getEnv :: String -> IO String` in
`System.Environment`.

If environment variables are needed for your application to work properly, the
best solution is to load them in your `main` function and crash with a helpful
error message if they're not properly defined.

```haskell
{-# LANGUAGE OverloadedStrings #-}
module Main where

import Data.Text.Lazy (pack)
import System.Environment (getEnv)
import Web.Scotty (get, html, scotty)

envVar = getEnv "MY_VAR"

main = do
  myVar <- envVar
  scotty 8080 $ do
    get "/" $ do
      html . pack $ "Hello world " ++ myVar
```

This way, the application will refuse to start if `MY_VAR` is not defined.

For more information, you can read about [environment variables on Clever
Cloud](/doc/admin-console/environment-variables/).

## Custom run command

If you need to run a custom command (or just pass options to the binary built
by stack), you can specify it through the `CC_RUN_COMMAND` environment variable.

For instance, for a hakyll website, you can put

```
CC_RUN_COMMAND=~./local/bin/site server --host 0.0.0.0 --port 8080
```

## Deploy on Clever Cloud

Application deployment on Clever Cloud is via Git. Follow [these
steps](/doc/clever-cloud-overview/add-application/) to deploy your
application.
