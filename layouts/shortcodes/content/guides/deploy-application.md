
### Deploy you application

{{< tabs items="Using the Console,Using the CLI" >}}

  {{< tab >}}
    If you're deploying from **GitHub**, your deployment should start automatically. If you're using **Git**, copy the remote and push on the **master** branch.

    {{< callout emoji="💡" >}}
      To deploy from branches other than `master`, use `git push clever <branch>:master`. For example, if you want to deploy your local `main` branch without renaming it, use `git push clever main:master`.
    {{< /callout >}}
  {{< /tab >}}

  {{< tab >}}
    Once you complete these steps, commit your content to the local repository and deploy it:

    ```bash
    git add .
    git commit -m "First deploy"
    clever deploy
    clever open
    ```

    You can display your website's URL or add a custom domain to it (you'll need to configure DNS):

    ```bash
    clever domain
    clever domain add your.website.tld
    ```
  {{< /tab >}}

{{< /tabs >}}
