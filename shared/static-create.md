
## Deploy a static application

You can create an application in our [Console](https://console.clever-cloud.com) or through [Clever Tools](/developers/doc/cli). Install them with `npm` or [any supported package manager](/developers/doc/cli/install/):

```bash
# Install with npm or any supported method
npm i -g clever-tools

# Login to Clever Cloud and check it worked
clever login
clever profile
```

Go to the folder where you want to create your application, and run the following command:

```bash
cd myStaticApp
clever create -t static

# If the folder is not a git repository, initialize it:
git init
```

To deploy on Clever Cloud, your local folder need to be an initialized git repository linked to an application. If you already have an application on Clever Cloud and want to link it to the current local folder:

```bash
clever link your_app_name_or_ID
```
