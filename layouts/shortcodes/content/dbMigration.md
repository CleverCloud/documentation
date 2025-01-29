## Migrate your database

Clever Cloud provides an add-on Migration/Upgrade tool. You can access it from the [Console](https://console.clever-cloud.com), in the left menu when an add-on is selected. It allows to choose a higher plan, a new version or another deployment zone.

A migration process creates new instances, moves your data into it and stops the old ones if the process ended correctly. In case of a failure during migration, new instances are deleted and you go back to the original ones.
The duration may vary depending on how much data your add-on has. Your database becomes read only for the entire duration.

If you want to restart your add-on or update to the last supported version of the current branch, migrate it to the same plan, version, zone. 

- [More Clever Cloud Tips and Tricks](/developers/doc/best-practices/tips_and_tricks/)
