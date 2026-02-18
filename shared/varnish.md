## Use Varnish as cache

Varnish is a powerful HTTP accelerator that can be used to cache your web application's responses, improving performance and reducing load. To use it, create a Varnish configuration file in `clevercloud/varnish.vcl` and configure your application to listen on port `8081`.
