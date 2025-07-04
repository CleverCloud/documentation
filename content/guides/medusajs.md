---
title: 'Medusa.js'
date: 2023-11-13T11:00:11+01:00
draft: true
type: docs
---

## Create your Medusa.js project from scratch

1. Deploy a PostgreSQL add-on and a Redis add-on
2. Copy the value of `POSTGRESQL_ADDON_URI`
3. In your terminal, run `npx create-medusa-app@latest --db-url <POSTGRESQL_ADDON_URI_value>`
4. Follow the steps to configure your Medusa project
5. In your code, replace `DB_URL` by `POSTGRESQL_ADDON_URI`
6. Create a Node.js app in Clever Cloud
7. Inject your environment variables
8. Set a domain name and inject it as an environment variable: `MEDUSA_URL`=`<your-domain-name`
9. In your project, run `git init` and add the git remote
10. The run `npm run build`
11. Connect your app to your database
12. In `medusa-config.js`, set the ssl database options:

```javascript{filename="medusa-config.js"}
module.exports = {
  projectConfig: {
    // …
    database_extra: { ssl: { rejectUnauthorized: false } },
  },
}
```

13. Add the admin to enable deploying with the backend: `npm install @medusajs/admin`
14. Set the port:

```javascript
const plugins = [
  // …
  {
    resolve: "@medusajs/admin",
    /** @type {import('@medusajs/admin').PluginOptions} */
    options: {
      port: 8080,
    },
  },
]
```
