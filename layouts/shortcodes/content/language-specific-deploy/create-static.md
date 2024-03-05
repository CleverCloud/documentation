
## Create a static application

You can create an application in our [Console](https://console.clever-cloud.com) or through [Clever Tools](https://github.com/CleverCloud/clever-tools/):

```bash
npm i -g clever-tools
clever login

cd myStaticApp
clever create -t static-apache myStaticApp
```

To deploy on Clever Cloud, your local folder need to be a git repository (if not, `git init`) linked to an application. If you already have an application on Clever Cloud and want to link it to the current local folder:

```bash
clever link your_app_name_or_ID
```
