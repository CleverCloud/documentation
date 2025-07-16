## Setting up environment variables on Clever Cloud

### With the Clever Cloud console

1. Go to the Clever Cloud console, and find the app you want to fine tune under it's organisation.
2. Find the **Environment variables** menu and select it.
3. In this menu, you will see a form with *VARIABLE_NAME* and *variable value* fields.
4. Fill them with the desired values then select **Add**.
5. Don't forget to "Update Changes" at the end of the menu.

### With the Clever Tools CLI

1. Make sure you have clever-tools installed locally. Refer to our [CLI getting started](/developers/doc/cli/).
2. In your code folder, do `clever env set <variable-name> <variable-value>`

Refer to [environment variables reference](/developers/doc/reference/reference-environment-variables) for more details on available environment variables on Clever Cloud.

You can of course create custom ones with the interface we just demonstrated, they will be available for your application.
