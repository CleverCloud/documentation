## Create an application on Clever Cloud

### via the web console

1. Select the proper organization you want to add the application to. At this point you should only have the Personal Space, click on the **Me** button in the left sidebar.
2. Create a new application by clicking on the **Create...** button in the sidebar, then select **an application**.
3. Select a brand new instance (or a repository from GitHub if your account is linked).
4. Then select @application-type@ in the platform list.
5. Configure your scaling options.
6. Enter your application's name and description and click "Next". You can also select the region you want (North America or Europe).

Refer to the [getting started]({{< ref "/getting-started/" >}}) for more details on application creation via the console.

### via the Clever Tools CLI

1. Make sure you have clever-tools installed locally. Report to the [getting started]({{< ref "/reference/clever-tools/getting_started.md" >}}).
2. In your code folder, do `clever create --type <type> <app-name> --region <zone> --org <org>` where `type` is the type of technology you rely on, `app-name` the name you want for your application, `zone` deployment zone (`par` for Paris and `mtl` for Montreal), and `org` the organization ID the application will be created under.

Refer to the [documentation]({{< ref "/reference/clever-tools/create.md" >}}) for more details on application creation with Clever Tools.