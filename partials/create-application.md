## Create an application on Clever Cloud

### via the web console
1. Create a new app by clicking on the **Add an Application** button, in the sidebar.
2. Select a brand new instance (or a repository from GitHub if your account is linked).
3. Then select @application-type@ in the platform list.
4. Configure your scaling options.
5. Enter your application's name and description and click "Next". You can also select the region you want (North America or Europe).

Refer to {{< ref "/getting-started/" >}} for more details on application creation via the console.

### via the Clever Tools CLI
1. Make sure you have clever-tools installed locally. Report to {{< ref "/reference/clever-tools/getting_started.md" >}}
2. In your code folder, do `clever create --type <type> <app-name> --region <zone> --org <org>` where `type` is the type of technology you rely on, `app-name` the name you want for your application, `zone` deloyment zone (`par` for Paris and `mtl` for Montreal), and `org` the organization ID the application will be created under.

Refer to {{< ref "/reference/clever-tools/create.md" >}} for more details on application creation with Clever Tools.