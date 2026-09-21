## Enable health check during deployment

The healthcheck allows you to limit downtimes. Indeed, you can provide Clever Cloud with paths to check. If these paths don't return a `2xx` response code, the deployment fails.

Add one (or several) environment variable as such:

```bash
CC_HEALTH_CHECK_PATH=/my/awesome/path
```

Or

```bash
CC_HEALTH_CHECK_PATH_0=/my/awesome/path
CC_HEALTH_CHECK_PATH_1=/my/other/path
```

The deployment process checks all paths. All of them must reply with a `2xx` response code, such as `200 OK` or `204 No Content`. Clever Cloud retries with an increasing delay before it marks the deployment as failed, so an application that needs some time to start isn't rejected on the first attempt.

When no health check path is configured, Clever Cloud requests the root path `/` and accepts any response code from `200` to `499`: a `404` or a `401` means your application is up and answering. For Java applications, the `deploy.pingPaths` of the `clevercloud/*.json` file also count as configured paths.

Before any HTTP request, Clever Cloud checks that a service listens on the public port, `8080`, on a public interface. Depending on your configuration, it's your application, the port Docker maps from `CC_DOCKER_EXPOSED_HTTP_PORT`, or the first Request Flow middleware. A service on this port bound only to `localhost` or `127.0.0.1` makes the deployment fail with `Your application is listening on localhost instead of publicly`: listen on `0.0.0.0` instead.

On runtimes supporting [Request Flow](/doc/develop/request-flow/), when middleware runs in front of your application, Clever Cloud also checks that each middleware port and your application port are listening. With `CC_REQUEST_FLOW="block"`, Clever Cloud only checks the service answering on the public port, not your application.

### Example

With the preceding paths, here are the logs of a failing health check:

```text
Checking public port (8080) is listening as expected
Response from GET /my/awesome/path is 200 (within expected range 200...300)
Response from GET /my/other/path is 500, expected 200...300
Error while checking /my/awesome/path, /my/other/path
```

In this example, the first path is OK, but the second one failed. This gives you a hint on what failed in your application.

### Best practice for healthcheck endpoints

To make the most of a healthcheck endpoint, have it check your critical dependencies. For example:

- execute `SELECT 1 + 1;` on your database
- retrieve a specific Cellar file
- ping a specific IP through a VPN
