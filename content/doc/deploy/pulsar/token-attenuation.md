---
type: docs
linkTitle: Token attenuation
title: Pulsar token attenuation
description: Restrict the Eclipse Biscuit token of a Pulsar add-on of Clever Cloud to some topics or to a period of time, before you hand it to a client
keywords:
- pulsar
- biscuit
- token
- attenuation
- authorization
- topics
aliases:
- /doc/pulsar/token-attenuation
---

The token of a Pulsar add-on is an [Eclipse Biscuit](https://doc.biscuitsec.org/) token: the Pulsar clusters of Clever Cloud check it with [biscuit-pulsar](https://github.com/CleverCloud/biscuit-pulsar). Clients send it as a usual token, with the token authentication of their library. Anyone who holds a Biscuit can attenuate it: add a block of checks that restricts what the new token allows, without contacting Clever Cloud. A client that gets the new token can't remove these checks.

To give access to a single topic, the [Clever Cloud API](/doc/deploy/pulsar/#restrict-the-token) creates a token for it. Attenuate the token yourself for other restrictions, without calling the Clever Cloud API. You can limit its topics, its operations, or its period of validity.

## Inspect the token

Install [biscuit-cli](https://github.com/biscuit-auth/biscuit-cli), save the token in a file, then inspect it:

```bash
printf '%s' "$ADDON_PULSAR_TOKEN" > addon.biscuit
biscuit inspect addon.biscuit
```

Delete this file once you've attenuated the token: it holds the token of the whole namespace.

The first block grants the rights of the cluster, and the second one restricts them to the namespace of the add-on and its topics:

```text
Authority block:
== Datalog v3.0 ==
right("admin");

Block n°1:
== Datalog v3.0 ==
check if namespace("user_xxx", "pulsar_xxx") or topic("user_xxx", "pulsar_xxx", $topic);
```

## Limit topics

Add a block that only allows the topics whose name starts with `my-own-prefix-`:

```bash
biscuit attenuate addon.biscuit \
  --block 'check if topic($tenant, $namespace, $topic), $topic.starts_with("my-own-prefix-")' \
  > attenuated.biscuit
```

`attenuated.biscuit` holds the new token: give its content to the client as its token. The client can produce to and consume from `my-own-prefix-orders`, not from `other-topic`. This check needs a topic: the token can't list the topics of the namespace.

## Limit operations

The cluster gives each check the operation that the client asks for, such as `produce` or `consume`. A token for a client that only reads messages:

```bash
biscuit attenuate addon.biscuit --block 'check if topic_operation("consume")' > reader.biscuit
```

A token for a client that only publishes them:

```bash
biscuit attenuate addon.biscuit --block 'check if topic_operation("produce")' > writer.biscuit
```

These tokens connect to the topics of the namespace, but refuse the other operation. Attenuate a new token again to combine restrictions, such as a prefix of topics and `consume`. The cluster doesn't give the checks the address of the client: a token can't restrict the IP addresses that use it.

## Limit in time

Add `--add-ttl` with a duration or a date to make the new token expire, here after one hour:

```bash
biscuit attenuate addon.biscuit --add-ttl 1h \
  --block 'check if topic_operation("consume")' \
  > attenuated.biscuit
```

Once this time has passed, the cluster refuses the new producers and consumers of this token. Those created before keep working until they disconnect: the expiry doesn't close an open connection.

Attenuate a topic token from the Clever Cloud API, such as `orders.biscuit`, the same way: the tokens of Pulsar add-ons don't expire. Inspect the new token to check its blocks before you hand it to a client.
