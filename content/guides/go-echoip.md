---
title: Go - Echoip
description: Deploy EchoIP on Clever Cloud
tags:
- guides
keywords:
- go
- echoip
type: "docs"
#date: 2024-05-06T09:11:52+01:00
draft: false
type: docs
---

[Echoip](https://github.com/mpolden/echoip) is a sumple service for looking up
 your ip address.


This doc explains how to install and configure Echoip from source.


## How to Configure and Deploy EchoIP on Clever Cloud

{{% steps %}}


### Download EchoIP

You can download EchoIP from <https://github.com/mpolden/echoip> and create a new origin.


First clone EchoIP's repository:
```
$ git clone https://github.com/mpolden/echoip
$ cd echoip
```

### Configure `clevercloud/go.json`

Create the necessary files to build and run the application:
```
$ mkdir clevercloud
$ cat << EOF > clevercloud/go.json
{
  "deploy": {
    "makefile": "Makefile",
    "main": "../go_home/bin/echoip"
  }
}
EOF
$ git add clevercloud/
$ git commit -m "add clevercloud files" clevercloud/
```

### Configure the environment

 {{% content/set-env-vars %}}



Define necessary environment variables (this is specific to EchoIP):
```
$ clever env set CC_RUN_COMMAND "~/go_home/bin/echoip -H X-Forwarded-For"
Your environment variable has been successfully saved
```


 {{% content/deploy-git %}}



Add the clevercloud git remote:
```
$ git remote add clevercloud $(jq -r '.apps[0].git_ssh_url' < .clever.json)
```

Push the app for deployment:
```
$ git push clevercloud master
```

Check the deployment logs:
```
$ clever logs
```

