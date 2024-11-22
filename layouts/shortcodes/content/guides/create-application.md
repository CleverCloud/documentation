
### Create an application

You need to create an application for the {{ .Get "runtime" }} runtime.

{{< tabs items="Using the Console,Using the CLI" >}}

  {{< tab >}}
    In this step, you set up the following parameters:

    - Deployment : using {{ if eq (.Get "runtime) "PHP" }}FTP, {{ end }}Git or GitHub
    - Application : {{ .Get "runtime" }}
    - Instance size and scalability options : {{ .Get "framework" }} sites can typically be deployed using the **{{ .Get "flavor" }}** instance
    - Region
    - Dependencies, if needed

    Refer to [Quickstart](/doc/quickstart) for more details on application creation via the console.
  {{< /tab >}}

  {{< tab >}}
    Make sure you have clever-tools installed locally or follow our [CLI getting started](/doc/cli/getting_started) guide.

    ```bash
    cd myApp
    clever create --type {{ .Get "runtime" | lowercase }} "My {{ .Get "runtime" }} application" --region <region>"
    clever scale --flavor {{ .Get "flavor" }}
    ```

    Refer to [clever create](/doc/cli/create) for more details on application creation with Clever Tools.
  {{< /tab >}}


{{< /tabs >}}

