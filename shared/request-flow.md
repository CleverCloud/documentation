## Request Flow: Varnish, Redirection.io, custom proxy

Request Flow automatically chains reverse proxies between port `8080` (public) and your application, managing port allocation with no manual configuration. Supported services are activated by their presence in your project:

- **Otoroshi Challenge**: set `OTOROSHI_CHALLENGE_SECRET`
- **Varnish**: add a `clevercloud/varnish.vcl` file or set `CC_VARNISH_FILE`
- **Redirection.io**: set `CC_REDIRECTIONIO_PROJECT_KEY`

All three can be active simultaneously. To control the order, set `CC_REQUEST_FLOW` (e.g. `redirectionio,varnish`). To add a custom middleware, include `custom` in the chain and define `CC_REQUEST_FLOW_CUSTOM` with `@@LISTEN_PORT@@` and `@@FORWARD_PORT@@` placeholders. To block public access, set `CC_REQUEST_FLOW=block`.

When at least one middleware is active, your application must listen on port `9000` instead of `8080`.

- [Learn more about Request Flow](/doc/develop/request-flow/)
- [Learn more about Varnish on Clever Cloud](/doc/develop/varnish/)
- [Learn more about Redirection.io](https://redirection.io/)
