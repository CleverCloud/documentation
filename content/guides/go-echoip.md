---
title: Go - Echoip
description: Deploy EchoIP on Clever Cloud
tags:
- guides
keywords:
- go
- echoip
- EchoIP
type: "docs"
#date: 2024-05-06T09:11:52+01:00
draft: false
type: docs
---

[EchoIP](https://github.com/mpolden/echoip) is a simple service for looking up
 your IP address.

This doc explains how to install and configure EchoIP from source, and how to deploy it as a [Go application]({{< ref "doc/applications/golang" >}} "Go documentation") on Clever Cloud.

## How to Configure and Deploy EchoIP on Clever Cloud


### Download EchoIP

You can download EchoIP from <https://github.com/mpolden/echoip> and create a new origin.


First clone EchoIP's repository:
```
~ $ git clone https://github.com/mpolden/echoip.git
~ $ cd echoip
```

### Configure `clevercloud/go.json`

Create the necessary files to build and run the application:
```
echoip/ ~ $ mkdir clevercloud
echoip/ ~ $ cat << EOF > clevercloud/go.json
{
  "deploy": {
    "makefile": "Makefile",
    "main": "../go_home/bin/echoip"
  }
}
EOF
echoip/ ~ $ git add clevercloud/
echoip/ ~ $ git commit -m "add clevercloud files" clevercloud/
```


 {{< content "set-env-vars" >}}



Define necessary environment variables (this is specific to EchoIP):
```
echoip/ ~ $ clever env set CC_RUN_COMMAND "~/go_home/bin/echoip -H X-Forwarded-For"
Your environment variable has been successfully saved
```


 {{< content "deploy-git" >}}



Add the clevercloud git remote:
```
echoip/ ~ $ git remote add clevercloud $(jq -r '.apps[0].git_ssh_url' < .clever.json)
```

Push the app for deployment:
```
echoip/ ~ $ git push clevercloud master
```

Check the deployment logs:
```
echoip/ ~ $ clever logs
```

