---
type: docs
title: Pulsar
description: A distributed messaging and streaming platform on the publish/subscribe model
tags:
- addons
keywords:
- pulsar
- messaging
- cold storage
- queue
- hot storage
- biscuit
- rabbitmq
- kafka
aliases:
- /doc/deploy/addon/pulsar
---

{{< callout type="warning" >}} Pulsar is still in beta. {{< /callout >}}

## Overview

[Pulsar](https://pulsar.apache.org/) works on a publisher/subscriber model. It allows services to communicate asynchronously, with latencies ranging around 100 milliseconds. It is used for streaming analytics and data integration pipelines to ingest and distribute data. It's equally effective as messaging-oriented middleware for service integration or as a queue to parallelize tasks. It also enables you to create systems of event producers and consumers. Publishers communicate with subscribers asynchronously by broadcasting events.

```mermaid
%%{
  init: {
    'theme': 'base',
    'themeVariables': {
      'fontFamily':'Arial',
      'primaryColor': '#FFFFFF',
      'primaryTextColor': '#6b7280',
      'primaryBorderColor': '#e5e7eb',
      'lineColor': '#545191',
      'secondaryColor': '#FFFFFFCC',
      'tertiaryColor': '#e5e7eb'
    }
  }
}%%

flowchart RL
    B("Pulsar Topic"):::pulsar
    direction LR
        C[Client producer] -- publishes to --> B
    direction RL
        D["Client consumer"]-- subscribes to --> B

    classDef pulsar stroke:#188FFF
```

There are several modes of subscription. A consumer may subscribe exclusively, or share the subscription with other consumers. Here are the four subscription types:

- Exclusive (only one consumer for the subscription)
- Failover (if a consumer fails, another one receives the message)
- Shared (messages are distributed to several consumers)
- Key_Shared (messages come with keys and go to consumers with the corresponding key)

More on this in the [official documentation](https://pulsar.apache.org/docs/en/concepts-messaging/#subscriptions).

A topic is defined this way:

`{persistent|non-persistent}://tenant/namespace/topic`

Tenants and namespaces allow for grouping and sub-grouping of topics.

A Clever Cloud Pulsar add-on is basically an immutable `tenant/namespace` where the tenant is your organisation ID, and the namespace is the add-on ID.
It allows you to create and use topics following this pattern:

`{persistent|non-persistent}://<CLEVERCLOUD_TENANT_ID>/<ADDON_ID>/<TOPIC_NAME>`

## Version

We maintain up-to-date Pulsar clusters based on the official Apache Pulsar release process. Your Pulsar add-on version is available in your add-on dashboard. Updates will be notified using Clever Cloud weekly updates on the [blog](https://www.clever-cloud.com/blog/).

## Common use cases

- **Replicating data among databases** using [Pulsar IO](https://pulsar.apache.org/docs/en/io-overview/) is commonly used to distribute change events from databases.
- **Parallel processing and workflows**. You can efficiently distribute a large number of tasks among multiple workers (compressing text files, sending email notifications).
- **Data streaming from IoT devices**. For example, a residential sensor can stream data to backend servers.
- **Refreshing distributed caches**. For example, an application can publish invalidation events to update the IDs of objects that have changed.
- **Real-time event distribution**. Events, raw or processed, may be made available to multiple applications across your team and organisation for real time processing.

## Create a Pulsar add-on

It is as simple and straightforward as creating any other add-on. In your personal space, click on *Create* > *an add-on* > *Pulsar*. Choose your plan, link an app to it (or not), give it a name and a zone, and it's done.

## Authorization

Pulsar add-on uses [Biscuit for Pulsar](https://github.com/CleverCloud/biscuit-pulsar) implementation which is directly pluggable to the Pulsar authentication and authorization system. Each add-on exposes its own Biscuit token.

As Biscuit is a token, you can use `AuthenticationToken($ADDON_PULSAR_TOKEN)` provided by [clients libraries](https://pulsar.apache.org/docs/en/client-libraries/) to authenticate to our clusters without any tweak.

### Attenuation

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

## Usage

We advise you to use [`pulsarctl`](https://github.com/streamnative/pulsarctl) provided by StreamNative. Here is an example to list topics in your add-on (in your namespace):

```bash
pulsarctl --admin-service-url $ADDON_PULSAR_HTTP_URL \
          --auth-params $ADDON_PULSAR_TOKEN \
          --auth-plugin org.apache.pulsar.client.impl.auth.AuthenticationToken \
          namespaces topics $ADDON_PULSAR_TENANT/$ADDON_PULSAR_NAMESPACE
```

### Rust example

Clever Cloud maintains pulsar's [asynchronous Rust client](https://github.com/wyyerd/pulsar-rs), which support biscuits.
Here is a minimal example that produces (publishes) a *"Hello, World!"* on the topic `my-own-topic`:

```toml
# Cargo.toml
[dependencies]
tokio = {version = "1.9.0", features = ["full"] }
pulsar = "4.0.0"
serde_json = "1.0.66"
serde = { version = "1.0.127", features = ["derive"] }
```

```rust
use pulsar::{
  message::proto, producer, Error as PulsarError, Pulsar, SerializeMessage, TokioExecutor,
};
use serde::{Deserialize, Serialize};

#[derive(Serialize, Deserialize)]
struct TestData {
  data: String,
}

impl SerializeMessage for TestData {
  fn serialize_message(input: Self) -> Result<producer::Message, PulsarError> {
    let payload = serde_json::to_vec(&input).map_err(|e| PulsarError::Custom(e.to_string()))?;
    Ok(producer::Message {
        payload,
        ..Default::default()
    })
  }
}

#[tokio::main]
async fn main() -> Result<(), pulsar::Error> {
  let pulsar_addon_url = std::env::var("ADDON_PULSAR_BINARY_URL").unwrap();
  let biscuit = std::env::var("ADDON_PULSAR_TOKEN").unwrap();
  let tenant = std::env::var("ADDON_PULSAR_TENANT").unwrap();
  let namespace = std::env::var("ADDON_PULSAR_NAMESPACE").unwrap();

  let topic = format!("non-persistent://{}/{}/my-own-topic", tenant, namespace);

  let auth = pulsar::Authentication {
    name: "token".to_string(),
    data: biscuit.clone().into_bytes(),
  };

  let pulsar: Pulsar<_> = Pulsar::builder(pulsar_addon_url, TokioExecutor)
    .with_auth(auth)
    .build()
    .await?;

  let mut producer = pulsar
    .producer()
    .with_topic(topic)
    .with_name("my-producer")
    .with_options(producer::ProducerOptions {
      schema: Some(proto::Schema {
          r#type: proto::schema::Type::String as i32,
          ..Default::default()
      }),
      ..Default::default()
    })
    .build()
    .await?;

  producer
    .send(TestData {
        data: "Hello world!".to_string(),
    })
    .await?;

  Ok(())
}
```

### Java example

There is an official [Java Pulsar Client](https://pulsar.apache.org/docs/en/client-libraries-java/), import it in your `pom.xml`:

```xml
<dependency>
  <groupId>org.apache.pulsar</groupId>
  <artifactId>pulsar-client</artifactId>
  <version>2.8.0</version>
</dependency>
```

```java
PulsarClient client = PulsarClient.builder()
  .authentication(new AuthenticationToken("ADDON_PULSAR_TOKEN"))
  .serviceUrl("ADDON_PULSAR_BINARY_URL")
  .build();

String TOPIC = "non-persistent://{}/{}/my-own-topic"

Producer<String> producer = client.newProducer(Schema.STRING)
  .topic(TOPIC)
  .create();

  producer.send("Hello world!");

Consumer consumer = client.newConsumer()
  .topics(Arrays.asList(TOPIC))
  .consumerName("my-consumer-name")
  .subscriptionName("my-subscription-name")
  .subscriptionInitialPosition(SubscriptionInitialPosition.Earliest)
  .subscribe();

while (!consumer.hasReachedEndOfTopic()) {
  Message<String> msg = consumer.receive();
  // Got the message!
}
```

### Python example

There is an official [Python Pulsar Client](https://pulsar.apache.org/docs/en/client-libraries-python/), import it in your `requirements.txt`:

```text
pulsar-client==2.10.2
```

```python
import pulsar
import os
import json
from pulsar import AuthenticationToken
from transfer import transfer

client = pulsar.Client(
    os.getenv("ADDON_PULSAR_BINARY_URL"),
    authentication=AuthenticationToken(os.getenv("ADDON_PULSAR_TOKEN")),
)

tenant = os.getenv("ADDON_PULSAR_TENANT")
namespace = os.getenv("ADDON_PULSAR_NAMESPACE")
topic = "persistent://{}/{}/TOPIC_NAME".format(tenant, namespace)

producer = client.create_producer(topic)
for i in range(10):
    producer.send(('Hello-%d' % i).encode('utf-8'))

while True:
    msg = consumer.receive()
    print("Received message id='{}' with data\n{}\n".format(msg.message_id(), msg.data()))
    # Acknowledge successful processing of the message
    consumer.acknowledge(msg)
    # Message failed to be processed
client.close()
```

### Operations

The Biscuit token provided by the Pulsar add-on allows you to run several operations on the add-on's namespace, its policies and the related topics.

These operations might change in the future. Don't hesitate to write to our support to ask for new operations!

#### Namespace

Authorized namespace operations:

```text
CREATE_TOPIC
GET_TOPIC
GET_TOPICS
DELETE_TOPIC
GET_BUNDLE
CLEAR_BACKLOG
UNSUBSCRIBE
```

#### Topics

Authorized topics operations:

```text
LOOKUP
PRODUCE
CONSUME
COMPACT
EXPIRE_MESSAGES
OFFLOAD
PEEK_MESSAGES
RESET_CURSOR
SKIP
TERMINATE
GET_BUNDLE_RANGE
SUBSCRIBE
GET_SUBSCRIPTIONS
UNSUBSCRIBE
GET_STATS
GET_METADATA
GET_BACKLOG_SIZE
SET_REPLICATED_SUBSCRIPTION_STATUS
```

### Namespace and topic policies

Authorized namespace/topic policies operations:

```text
ALL_READ
ANTI_AFFINITY_READ
AUTO_SUBSCRIPTION_CREATION_READ
AUTO_SUBSCRIPTION_CREATION_WRITE
AUTO_TOPIC_CREATION_READ
AUTO_TOPIC_CREATION_WRITE
BACKLOG_READ
BACKLOG_WRITE
COMPACTION_READ
COMPACTION_WRITE
DEDUPLICATION_READ
DEDUPLICATION_SNAPSHOT_READ
DEDUPLICATION_SNAPSHOT_WRITE
DEDUPLICATION_WRITE
DELAYED_DELIVERY_READ
DELAYED_DELIVERY_WRITE
ENCRYPTION_READ
ENCRYPTION_WRITE
INACTIVE_TOPIC_READ
INACTIVE_TOPIC_WRITE
MAX_CONSUMERS_READ
MAX_CONSUMERS_WRITE
MAX_PRODUCERS_READ
MAX_PRODUCERS_WRITE
MAX_SUBSCRIPTIONS_READ
MAX_SUBSCRIPTIONS_WRITE
MAX_TOPICS_READ
MAX_TOPICS_WRITE
MAX_UNACKED_READ
MAX_UNACKED_WRITE
OFFLOAD_READ
PARTITION_READ
PARTITION_WRITE
PERSISTENCE_READ
PERSISTENCE_WRITE
RATE_READ
RATE_WRITE
REPLICATION_RATE_READ
REPLICATION_READ
RESOURCEGROUP_READ
RESOURCEGROUP_WRITE
RETENTION_READ
RETENTION_WRITE
SCHEMA_COMPATIBILITY_STRATEGY_READ
SCHEMA_COMPATIBILITY_STRATEGY_WRITE
SUBSCRIPTION_AUTH_MODE_READ
SUBSCRIPTION_AUTH_MODE_WRITE
SUBSCRIPTION_EXPIRATION_TIME_READ
SUBSCRIPTION_EXPIRATION_TIME_WRITE
TTL_READ
TTL_WRITE
```

## Storage

### Retention

A Pulsar add-on is provided with infinite retention policies, which can be changed using:

```bash
# Example to set retention of namespace to 2 weeks and/or 100 GB
pulsarctl --admin-service-url $ADDON_PULSAR_HTTP_URL \
          --auth-params $ADDON_PULSAR_TOKEN \
          --auth-plugin org.apache.pulsar.client.impl.auth.AuthenticationToken \
          namespaces set-retention $ADDON_PULSAR_TENANT/$ADDON_PULSAR_NAMESPACE --time 2w --size 100G
```

### Offload storage to Cellar (S3)

Pulsar has a [tiered storage feature](https://pulsar.apache.org/docs/en/tiered-storage-overview/) allowing to offload heavy data to cold storage once a threshold is reached.

For each Pulsar add-on we provide, we also provide a hidden [Cellar add-on](../cellar), our object storage add-on. This Cellar add-on is bound to the Pulsar namespace offload policies and will store your offloaded data.

The offload threshold of the namespace is deactivated by default, you can activate it with:

```bash
# Example to set offload to run when hot storage is > 10G and put data to Cellar Addon
pulsarctl --admin-service-url $ADDON_PULSAR_HTTP_URL \
          --auth-params $ADDON_PULSAR_TOKEN \
          --auth-plugin org.apache.pulsar.client.impl.auth.AuthenticationToken \
          namespaces set-offload-treshold $ADDON_PULSAR_TENANT/$ADDON_PULSAR_NAMESPACE 10G
```
