## Enable health check during deployment

The healthcheck allows you to limit downtimes. Indeed, you can provide us with paths to check. If these paths return something other than 200, we will consider the deployment as failed.

All you need is add one (or several) environment variable as such:

```bash
CC_HEALTH_CHECK_PATH=my/awesome/path
```

Or

```bash
CC_HEALTH_CHECK_PATH_0=my/awesome/path
CC_HEALTH_CHECK_PATH_1=my/other/path
```

The deployment process will check all given paths. All of them must reply with a `200 OK` response code.

### Example

Using the path listed above, below are the expected logs:

```text
Response from GET /my/awesome/path is 200
Response from GET /my/other/path is 500
Health check failed:
- GET /my/other/path returned 500.
If the deployment fails after this message, please update your configuration and redeploy.
```

In this example, the 1st path is OK, but the 2nd one failed. This give you a hint on what failed in your application.

### Best practice for healthcheck endpoints

To make the most of a healthcheck endpoint, you should have it check your critical dependencies. For example:

- execute `SELECT 1 + 1;` on your database
- retrieve a specific Cellar file
- ping a specific IP through a VPN
