---
title: New Relic
position: 2
shortdesc: Configuring Newrelic on Clever Cloud
tags:
- apps
---

[New Relic](http://www.newrelic.com/) is a software analytics company based in San Francisco, California.
New Relic's technology monitors Web and mobile applications in real-time that run in cloud, on-premise, or hybrid
environments. You can easily setup a New Relic based monitoring on your application to monitor it and find
performances problems.

New Relic can be used on Clever Cloud with Java, NodeJS, PHP, Ruby and Scala applications.

## New Relic for NodeJS and Ruby

New Relic is very simple to install in a NodeJS or Ruby application as it is a simple dependency.
Install instructions for
[NodeJS](https://docs.newrelic.com/docs/agents/nodejs-agent/installation-configuration/installing-maintaining-nodejs)
and [Ruby](https://docs.newrelic.com/docs/agents/ruby-agent/installation-configuration/ruby-agent-installation)
are available in [the New Relic documentation](https://docs.newrelic.com/).

## New Relic for Java, Scala and PHP

To use New Relic in Java, Scala or Ruby instances, you need to configure it as it is provided directly inside the
instances.

## New Relic for Python

To use New Relic in Python, you have to add the [newrelic](https://pypi.python.org/pypi/newrelic) dependency into your
`requirements.txt` file.

### Necessary information

Before setting up your app, be sure to have a [New Relic Account](http://www.newrelic.com/).

### Configuration

To configure your New Relic, you can set the environment variables `NEWRELIC_LICENSE` and `NEWRELIC_APPNAME` (optionnal).

You can also create and add a `./clevercloud/newrelic.json` file in your project, with the
following fields:

```javascript
{
  "license": "licenceID",
  "appname": "NameOfYourApp(optional)"
}
```

If the `appname` is not specified, we use your application Id for the name.

Deploy your application on Clever Cloud for the changes to take effect. A few minutes later, your application will begin sending data
to New Relic. Once newrelic receives the data, your application will be listed in your dashboard.



