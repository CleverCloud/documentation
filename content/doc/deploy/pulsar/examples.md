---
type: docs
weight: 10
linkTitle: Examples
title: Pulsar Examples
description: Produce and consume messages on a Pulsar add-on from Rust, Java and Python, and manage namespaces, topics and their policies
keywords:
- pulsar
- examples
- pulsarctl
- rust
- java
- python
- topics
aliases:
- /doc/pulsar/examples
---

We advise you to use [`pulsarctl`](https://github.com/streamnative/pulsarctl) provided by StreamNative. Here is an example to list topics in your add-on (in your namespace):

```bash
pulsarctl --admin-service-url $ADDON_PULSAR_HTTP_URL \
          --auth-params $ADDON_PULSAR_TOKEN \
          --auth-plugin org.apache.pulsar.client.impl.auth.AuthenticationToken \
          namespaces topics $ADDON_PULSAR_TENANT/$ADDON_PULSAR_NAMESPACE
```

## Rust example

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

## Java example

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

## Python example

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

## Operations

The Biscuit token provided by the Pulsar add-on allows you to run several operations on the add-on's namespace, its policies and the related topics.

These operations might change in the future. Don't hesitate to write to our support to ask for new operations!

### Namespace

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

### Topics

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

## Namespace and topic policies

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
