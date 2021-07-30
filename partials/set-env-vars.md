## Setting up environment variables on Clever Cloud

### With the Clever Cloud console

1. Go to the Clever Cloud console, and find the app you want to fine tune under it's organization.
2. Find the **Environment variables** menu and select it.
3. In this menu, you will see a form with *VARIABLE_NAME* and *variable value* fields. Fill them with the desired values then select **Create**.

### With the Clever Tools CLI

1. Make sure you have clever-tools installed locally. Report to the [getting started]({{< ref "/reference/clever-tools/getting_started.md" >}})
2. In your code folder, do `clever env set <variable-name> <variable-value>`

Refer to [environment variables reference]({{< ref "/reference/reference-environment-variables.md" >}}) for more details on available environment variables on Clever Cloud.
You can of course create custom ones with the interface we just demonstrated, they will be available for your application.
