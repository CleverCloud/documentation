## Request Flow: Varnish, Redirection.io, OAuth2 Proxy, custom proxy

Request Flow automatically chains reverse proxies between port `8080` (public) and your application, allocating middleware ports automatically. Some services are detected from your configuration, while others must be listed explicitly in `CC_REQUEST_FLOW`:

- **Otoroshi Challenge**: set `OTOROSHI_CHALLENGE_SECRET`
- **Varnish**: add a `clevercloud/varnish.vcl` file or set `CC_VARNISH_FILE`
- **Redirection.io**: set `CC_REDIRECTIONIO_PROJECT_KEY`
- **OAuth2 Proxy**: set `CC_REQUEST_FLOW=oauth2-proxy` and its `OAUTH2_PROXY_*` settings

Multiple services can run simultaneously. Setting `CC_REQUEST_FLOW` replaces automatic detection, so list every service you need in order (e.g. `oauth2-proxy,varnish`). To add a custom middleware, include `custom` in the chain and define `CC_REQUEST_FLOW_CUSTOM` with `@@LISTEN_PORT@@` and `@@FORWARD_PORT@@` placeholders. To block public access, set `CC_REQUEST_FLOW=block`.

If your application manages its own HTTP server, configure it to listen on port `9000` instead of `8080` when at least one middleware is active. Clever Cloud handles this automatically for runtimes with a managed web server.

- [Learn more about Request Flow](/doc/develop/request-flow/)
- [Learn more about Varnish on Clever Cloud](/doc/develop/request-flow/varnish/)
- [Learn more about OAuth2 Proxy on Clever Cloud](/doc/develop/request-flow/oauth2-proxy/)
- [Learn more about Redirection.io](https://redirection.io/)
