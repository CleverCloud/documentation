## Migrate your database

To apply security updates, change the plan, upgrade the version, or move the add-on to another region, migrate it from its **Migrate / Upgrade** menu in the [Console](https://console.clever-cloud.com). A migration creates a new server, copies your data to it, then switches the add-on to it.

The duration depends on how much data the add-on holds. During the migration, the database is read-only, except Redis, which accepts writes until the switch. If a step fails, Clever Cloud tries to roll the migration back to the original server.

- [Learn more about database migrations](/doc/develop/database-migration/)
- [More Clever Cloud Tips and Tricks](/doc/tips-and-tricks/)
