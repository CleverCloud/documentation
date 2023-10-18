## Create an application on Clever Cloud

### With the web console

Refer to [our getting started]({{< ref "/doc/quickstart" >}}) for more details on application creation via the console.

### With the Clever Tools CLI

1. Make sure you have clever-tools installed locally or follow our [CLI getting started]({{< ref "doc/reference/clever-tools/getting_started.md" >}}) guide.
2. In your code folder, do `clever create --type <type> <app-name> --region <zone> --org <org>` where :
   1. `type` is the type of technology you rely on
   2. `app-name` the name you want for your application,
   3. `zone` deployment zone (`par` for Paris and `mtl` for Montreal)
   4. `org` the organization ID the application will be created under.

Refer to [clever create]({{< ref "doc/reference/clever-tools/create.md" >}}) for more details on application creation with Clever Tools.
