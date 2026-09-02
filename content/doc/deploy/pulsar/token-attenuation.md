---
type: docs
weight: 20
linkTitle: Token Attenuation
title: Pulsar Token Attenuation
description: Restrict a Pulsar add-on Biscuit token to specific topics or operations before handing it to a client
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

Pulsar add-on uses [Biscuit for Pulsar](https://github.com/CleverCloud/biscuit-pulsar) implementation which is directly pluggable to the Pulsar authentication and authorization system. Each add-on exposes its own Biscuit token.

As Biscuit is a token, you can use `AuthenticationToken($ADDON_PULSAR_TOKEN)` provided by [clients libraries](https://pulsar.apache.org/docs/en/client-libraries/) to authenticate to our clusters without any tweak.

## Attenuation

The Pulsar add-on given Biscuit token can be attenuated, here is an attenuation example using [biscuit-cli](https://github.com/biscuit-auth/biscuit-cli) from the given Biscuit token to produce/consume topics starting with a custom topic prefix called `"my-own-prefix"`.

Put your Biscuit token in a file:

```bash
echo $ADDON_PULSAR_TOKEN > addon.biscuit
```

Inspect your Biscuit token:

```bash
biscuit inspect addon.biscuit
Authority block:
== Datalog ==
right("admin");

== Revocation id ==
0392cdc4dbda294fd254269ad0ce5d1ad2e9c6301b189945074dd051890e495dd16bf5390f84e8499a2045bde85795636f2e156309f9b425270979957e50280a

==========

Block n°1:
== Datalog ==
check if namespace("user_1235678-f54e-4e09-848c-1953af6e3e89", "pulsar_1235678-6b36-4af2-be1f-d97862c0c41c") or topic("user_1235678-f54e-4e09-848c-1953af6e3e89", "pulsar_1235678-6b36-4af2-be1f-d97862c0c41c", $topic);

== Revocation id ==
4a72ca17001b173853f5cd6cce7b46ba4113b1d6e934a3e13e717f91e276c3230861ee49c843c4aafd7d11b14903a7ff32f9e2b35bd6f84794ba3dc6e3c0450c

==========
```

- The authority block is the cluster authentication block (the cluster admin Biscuit token).
- The block n°1 is an attenuation of the authority block to only authorize operations on `tenant = "user_1235678-f54e-4e09-848c-1953af6e3e89"` and `namespace = "pulsar_1235678-6b36-4af2-be1f-d97862c0c41c"`.

Attenuate it:

```bash
biscuit attenuate addon.biscuit
```

This will open your `$EDITOR` to type the attenuation.

Put

```bash
check if topic_operation($operation), $topic.starts_with("my-own-prefix")
```

Then it outputs the attenuated token. Inspect it to ensure your attenuation:

```bash
Authority block:
== Datalog ==
right("admin");

== Revocation id ==
0392cdc4dbda294fd254269ad0ce5d1ad2e9c6301b189945074dd051890e495dd16bf5390f84e8499a2045bde85795636f2e156309f9b425270979957e50280a

==========

Block n°1:
== Datalog ==
check if namespace("user_1235678-f54e-4e09-848c-1953af6e3e89", "pulsar_1235678-6b36-4af2-be1f-d97862c0c41c") or topic("user_1235678-f54e-4e09-848c-1953af6e3e89", "pulsar_1235678-6b36-4af2-be1f-d97862c0c41c", $topic);

== Revocation id ==
4a72ca17001b173853f5cd6cce7b46ba4113b1d6e934a3e13e717f91e276c3230861ee49c843c4aafd7d11b14903a7ff32f9e2b35bd6f84794ba3dc6e3c0450c

==========

Block n°2:
== Datalog ==
check if topic_operation($operation), $topic.starts_with("my-own-prefix");

== Revocation ids ==
3b71ba17001b173853f5cd6cce7b46ba4113b1d6e934a3e13e717f91e276c3230861ee49c843c4aafd7d11b14903a7ff32f9e2b35bd6f84794ba3dc6e3c0450d

==========
```

Now the block n°2 ensures that topics must start with `"my-own-prefix"`.

You can find more examples on the [biscuit-pulsar authorization java tests](https://github.com/CleverCloud/biscuit-pulsar/blob/master/src/test/java/com/clevercloud/biscuitpulsar/AuthorizationProviderBiscuitTest.java).
