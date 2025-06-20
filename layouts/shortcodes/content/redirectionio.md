## Use Redirection.io as a proxy

[Redirection.io](https://redirection.io) can help reduce HTTP traffic issues on your website. It gives a complete control on how HTTP requests are handled, which helps make it SEO-friendly. It can perform redirections and comes with lots of features. You can link any application to a Redirection.io project easily, setting up the proxy mode with following environment variables:

|  Name  |  Description  |  Default value  |
|-----------------------|------------------------------|--------------------------------|
| `CC_ENABLE_REDIRECTIONIO` | Enable Redirection.io support | `false` |
| `CC_REDIRECTIONIO_PROJECT_KEY` | The Redirection.io project key |  |
| `CC_REDIRECTIONIO_FORWARD_PORT` | The listening port of your application |  |
| `CC_REDIRECTIONIO_INSTANCE_NAME` | The name of your application (optional) |  |

The Redirection.io agent will start as a service, listen to `8080` port and forward the traffic to your application port.

- [Learn more about Redirection.io](https://redirection.io/)
