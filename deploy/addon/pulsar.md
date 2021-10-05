---
title: Pulsar
shortdesc: A distributed messaging and streaming platform on the publish/subsribe model
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
---

## Overview

[Pulsar](https://pulsar.apache.org/) works on a publisher/subscriber model. It allows services to communicate asynchronously, with latencies ranging around 100 milliseconds. It is used for streaming analytics and data integration pipelines to ingest and distribute data. It is equally effective as messaging-oriented middleware for service integration or as a queue to parallelize tasks. It also enables you to create systems of event producers and consumers. Publishers communicate with subscribers asynchronously by broadcasting events.

```
client               Pulsar             client
publishes to   =>    topic      <=  subscribes to

"producer"                           "consumer"
```

They are several modes of subscription. A consumer may subscribe exclusively, or share the subscription with other consumers. There is the subscription mode types:

- Exclusive (only one consumer for the subscription)
- Failover (if a consumer fails, another one receives the message)
- Shared (messages are distributed to several consumers)
- Key_Shared (messages come with keys and go to consumers with the corresponding key)

More on this in the [official documentation](https://pulsar.apache.org/docs/en/concepts-messaging/#subscriptions).

A topic is defined this way:

`{persistent|non-persistent}://tenant/namespace/topic`

Tenants and namespaces allow for grouping and subgrouping of topics.

A Clever Cloud Pulsar add-on is basically an immutable `tenant/namespace` where the tenant is your user id, and the namespace is the add-on id.
It allows you to create and use topics following this pattern:

`{persistent|non-persistent}://<CLEVERCLOUD_TENANT_ID>/<ADDON_ID>/<TOPIC_NAME>`

## Version

We maintain up-to-date Pulsar clusters based on the official Apache Pulsar release process. Your Pulsar add-on version is available in your add-on dashboard. Updates will be notified using Clever Cloud weekly updates on the [blog](https://www.clever-cloud.com/blog/).

## Common use cases

- **Replicating data among databases** using [Pulsar IO](https://pulsar.apache.org/docs/en/io-overview/) is commonly used to distribute change events from databases.
- **Parallel processing and workflows**. You can efficiently distribute a large number of tasks among multiple workers (compressing text files, sending email notifications).
- **Data streaming from IoT devices**. For example, a residential sensor can stream data to backend servers.
- **Refreshing distributed caches**. For example, an application can publish invalidation events to update the IDs of objects that have changed.
- **Real-time event distribution**. Events, raw or processed, may be made available to multiple applications across your team and organization for real time processing.

## Create a Pulsar add-on

It is as simple and straightforward as creating any other add-on.
In your personnal space, click on *Create* > *an add-on* > *Pulsar*.
Choose your plan, link an app to it (or not), give it a name and a zone, and it's done.

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
right(#authority, #admin);

== Revocation ids ==
Content-based: fe7526a27b43fa7d5386c31b3efb6c53b551b4a8e3e969f4dc074497b3942a57
Unique:        faf6cab8a4dffad77633181d6f924414980bb6d76c5298b88f700c11659c7407

==========

Block n°1:
== Datalog ==
check if topic_operation(#ambient, "user_1235678-f54e-4e09-848c-1953af6e3e89", "pulsar_1235678-6b36-4af2-be1f-d97862c0c41c", $2, $3) or namespace_operation(#ambient, "user_12345668-f54e-4e09-848c-1953af6e3e89", "pulsar_1235678-6b36-4af2-be1f-d97862c0c41c", $2);

== Revocation ids ==
Content-based: a35a92a278a3ad9ec5db8dc3e905cfbc17f5a8e2cb13ff39b69b003500fe6c46
Unique:        17dfec62b62da36562a0998d496bb3aa30f229138ec810a070084bdf1c55be3a

==========
```

* The authority block is the cluster authentication block (the cluster admin Biscuit token).
* The block n°1 is an attenuation of the authority block to only authorize operations on `tenant = "user_1235678-f54e-4e09-848c-1953af6e3e89"` and `namespace = "pulsar_1235678-6b36-4af2-be1f-d97862c0c41c"`.

Attenuate it:

```bash
biscuit attenuate addon.biscuit
```

This will open your `$EDITOR` to type the attenuation.

Put

```bash
check if topic_operation(#ambient, "user_12345678-f54e-4e09-848c-1953af6e3e89", "pulsar_12345678-6b36-4af2-be1f-d97862c0c41c", $topic, $operation), $topic.starts_with("my-own-prefix")
```

Then it outputs the attenuated token. Inspect it to ensure your attenuation:

```bash
Authority block:
== Datalog ==
right(#authority, #admin);

== Revocation ids ==
Content-based: fe7526a27b43fa7d5386c31b3efb6c53b551b4a8e3e969f4dc074497b3942a57
Unique:        faf6cab8a4dffad77633181d6f924414980bb6d76c5298b88f700c11659c7407

==========

Block n°1:
== Datalog ==
check if topic_operation(#ambient, "user_12345678-f54e-4e09-848c-1953af6e3e89", "pulsar_50ee8f69-6b36-4af2-be1f-d97862c0c41c", $2, $3) or namespace_operation(#ambient, "user_12345678-f54e-4e09-848c-1953af6e3e89", "pulsar_12345678-6b36-4af2-be1f-d97862c0c41c", $2);

== Revocation ids ==
Content-based: a35a92a278a3ad9ec5db8dc3e905cfbc17f5a8e2cb13ff39b69b003500fe6c46
Unique:        17dfec62b62da36562a0998d496bb3aa30f229138ec810a070084bdf1c55be3a

==========

Block n°2:
== Datalog ==
check if topic_operation(#ambient, "user_12345678-f54e-4e09-848c-1953af6e3e89", "pulsar_12345678-6b36-4af2-be1f-d97862c0c41c", $topic, $operation), $topic.starts_with("my-own-prefix");

== Revocation ids ==
Content-based: 8eaaa639d5b94c3e053ad840e8dcca6fe66a621442ecc99eadf1df03d6138f1d
Unique:        f608dc2f724fc14faf0daf50774ef0b9425cda26f56ee93317ca80ca13736027

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
          topics list $ADDON_PULSAR_TENANT/$ADDON_PULSAR_NAMESPACE
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

### Operations

The Biscuit token provided by the Pulsar add-on allows you to run several operations on namespace, its policies and the related topics.

These operations might change in the future. Don't hesitate to write to our support to ask for new operations!

#### Namespace

Authorized namespace operations:

```
CREATE_TOPIC
GET_TOPIC
GET_TOPICS
DELETE_TOPIC
ADD_BUNDLE
DELETE_BUNDLE
GET_BUNDLE
CLEAR_BACKLOG
UNSUBSCRIBE
```

Authorized namespace policies operations:

```
ALL_READ
ANTY_AFFINITY_READ
BACKLOG_READ
BACKLOG_WRITE
COMPACTION_READ
COMPACTION_WRITE
DELAYED_DELIVERY_READ
DELAYED_DELIVERY_WRITE
DEDUPLICATION_READ
DEDUPLICATION_WRITE
MAX_CONSUMERS_READ
MAX_CONSUMERS_WRITE
MAX_PRODUCERS_READ
MAX_PRODUCERS_WRITE
MAX_UNACKED_READ
MAX_UNACKED_WRITE
OFFLOAD_READ
PERSISTENCE_READ
PERSISTENCE_WRITE
RATE_WRITE
RATE_READ
RETENTION_READ
RETENTION_WRITE
REPLICATION_READ
REPLICATION_RATE_READ
SCHEMA_COMPATIBILITY_STRATEGY_READ
SCHEMA_COMPATIBILITY_STRATEGY_WRITE
SUBSCRIPTION_AUTH_MODE_READ
SUBSCRIPTION_AUTH_MODE_WRITE
ENCRYPTION_READ
ENCRYPTION_WRITE
TTL_READ
TTL_WRITE
```

#### Topics

Authorized topics operations:

```
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
SUBSCRIBE
GET_SUBSCRIPTIONS
UNSUBSCRIBE
GET_STATS
```

Authorized topics policies operations:

```
PARTITION_READ
PARTITION_WRITE
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

For each Pulsar add-on we provide, we also provide a hidden [Cellar add-on]({{< ref "deploy/addon/cellar.md" >}}), our object storage add-on. This Cellar add-on is bound to the Pulsar namespace offload policies and will store your offloaded data.

The offload threshold of the namespace is deactivated by default, you can activate it with:

```bash
# Example to set offload to run when hot storage is > 10G and put data to Cellar Addon
pulsarctl --admin-service-url $ADDON_PULSAR_HTTP_URL \
          --auth-params $ADDON_PULSAR_TOKEN \
          --auth-plugin org.apache.pulsar.client.impl.auth.AuthenticationToken \
          namespaces set-offload-treshold $ADDON_PULSAR_TENANT/$ADDON_PULSAR_NAMESPACE 10G
```

## Pricing

Clever Cloud Pulsar add-on pricing is comsumption based, here is a pricing simulator:

{{< pricingConsumption "pulsar" >}}
