## Private Composer repositories

Composer can authenticate with private package repositories through the `COMPOSER_AUTH` [environment variable](/doc/develop/env-variables/). Its value is a JSON object containing Composer authentication settings, such as HTTP Basic, OAuth or an access token.

For example, to use [Private Packagist](https://packagist.com/), add its repository to your `composer.json`, replacing `ORGANISATION` with its short name:

```json
{
  "repositories": [
    {
      "type": "composer",
      "url": "https://repo.packagist.com/ORGANISATION"
    },
    {
      "packagist.org": false
    }
  ]
}
```

Then define `COMPOSER_AUTH` for your application with the username and token provided by Private Packagist:

```json
{
  "http-basic": {
    "repo.packagist.com": {
      "username": "PACKAGIST_USERNAME",
      "password": "PACKAGIST_TOKEN"
    }
  }
}
```

Composer reads this variable automatically during `composer install`. Never commit credentials to your repository. If you use a local `auth.json` file, add it to `.gitignore`. See the [Composer authentication documentation](https://getcomposer.org/doc/articles/authentication-for-private-packages.md) for other providers and authentication methods. For a private Git repository accessed over SSH, configure a [private SSH key](/doc/reference/common-configuration/#private-ssh-key) instead.
