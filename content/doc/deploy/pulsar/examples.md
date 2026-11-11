---
type: docs
linkTitle: Code examples
title: Apache Pulsar code examples
description: Use a Pulsar add-on of Clever Cloud from Java, Node.js, Python, and Rust, to share work between instances, broadcast events, delay messages, retry them, replay the history, and type messages
keywords:
- pulsar
- examples
- java
- node.js
- python
- rust
- producer
- consumer
- key_shared
- delayed delivery
- dead letter topic
- schema
aliases:
- /doc/pulsar/examples
---

The examples below read the [environment variables](/doc/deploy/pulsar/#connect-to-pulsar) of the add-on, which your application gets when you link the add-on to it. To run an example on your computer, export them first, with the ID of the add-on or its real ID, here `pulsar_xxx`:

```bash
eval "$(clever addon env pulsar_xxx -F shell)"
```

The first section publishes and consumes a message, and the next ones show the other features of Pulsar. A topic keeps the [schema](https://pulsar.apache.org/docs/schema-overview/) of the first client that uses it. Use a different topic for each example, or the same schema in each client.

## Publish and consume

Each program subscribes to a topic, publishes a message to it, then receives and acknowledges this message:

{{< tabs >}}
{{< tab name="Java" icon="java" >}}

Add the official [Java client](https://pulsar.apache.org/docs/client-libraries/java/) to your `pom.xml`:

```xml {filename="pom.xml"}
<dependency>
  <groupId>org.apache.pulsar</groupId>
  <artifactId>pulsar-client</artifactId>
  <version>4.2.0</version>
</dependency>
```

```java {filename="Hello.java"}
import org.apache.pulsar.client.api.*;

public class Hello {
    public static void main(String[] args) throws PulsarClientException {
        String topic = "persistent://" + System.getenv("ADDON_PULSAR_TENANT") + "/"
            + System.getenv("ADDON_PULSAR_NAMESPACE") + "/java-topic";

        try (PulsarClient client = PulsarClient.builder()
                .serviceUrl(System.getenv("ADDON_PULSAR_BINARY_URL"))
                .authentication(AuthenticationFactory.token(System.getenv("ADDON_PULSAR_TOKEN")))
                .build();
             Consumer<String> consumer = client.newConsumer(Schema.STRING)
                .topic(topic)
                .subscriptionName("my-subscription")
                .subscriptionInitialPosition(SubscriptionInitialPosition.Earliest)
                .subscribe();
             Producer<String> producer = client.newProducer(Schema.STRING)
                .topic(topic)
                .create()) {
            producer.send("Hello from Java");
            Message<String> message = consumer.receive();
            System.out.println("Received: " + message.getValue());
            consumer.acknowledge(message);
        }
    }
}
```

{{< /tab >}}
{{< tab name="Node.js" icon="simple:nodedotjs" >}}

Add the official [Node.js client](https://pulsar.apache.org/docs/client-libraries/node/) to your `package.json`. A script of this package installs its native module: npm 12 only runs it once the `allowScripts` field of your `package.json` approves it:

```json {filename="package.json"}
{
  "name": "pulsar-hello",
  "type": "module",
  "dependencies": {
    "pulsar-client": "^1.18.0"
  },
  "allowScripts": {
    "pulsar-client": true
  }
}
```

```javascript {filename="main.js"}
import Pulsar from 'pulsar-client';

const env = process.env;
const topic = `persistent://${env.ADDON_PULSAR_TENANT}/${env.ADDON_PULSAR_NAMESPACE}/node-topic`;

const client = new Pulsar.Client({
  serviceUrl: env.ADDON_PULSAR_BINARY_URL,
  authentication: new Pulsar.AuthenticationToken({ token: env.ADDON_PULSAR_TOKEN }),
});

const consumer = await client.subscribe({
  topic,
  subscription: 'my-subscription',
  subscriptionInitialPosition: 'Earliest',
});
const producer = await client.createProducer({ topic });
await producer.send({ data: Buffer.from('Hello from Node.js') });

const message = await consumer.receive();
console.log('Received:', message.getData().toString());
await consumer.acknowledge(message);

await producer.close();
await consumer.close();
await client.close();
```

{{< /tab >}}
{{< tab name="Python" icon="simple:python" >}}

Add the official [Python client](https://pulsar.apache.org/docs/client-libraries/python/) to your `requirements.txt`:

```text {filename="requirements.txt"}
pulsar-client>=3.13
```

```python {filename="main.py"}
import os
import pulsar

client = pulsar.Client(
    os.environ["ADDON_PULSAR_BINARY_URL"],
    authentication=pulsar.AuthenticationToken(os.environ["ADDON_PULSAR_TOKEN"]),
)
topic = f"persistent://{os.environ['ADDON_PULSAR_TENANT']}/{os.environ['ADDON_PULSAR_NAMESPACE']}/python-topic"

consumer = client.subscribe(topic, "my-subscription", initial_position=pulsar.InitialPosition.Earliest)
producer = client.create_producer(topic)
producer.send(b"Hello from Python")

message = consumer.receive()
print("Received:", message.data().decode())
consumer.acknowledge(message)
client.close()
```

{{< /tab >}}
{{< tab name="Rust" icon="simple:rust" >}}

Add [Magnetar](https://github.com/CleverCloud/magnetar), the Rust client that Clever Cloud maintains as an alternative to [pulsar-rs](https://github.com/streamnative/pulsar-rs). Its crates.io package is `magnetar-driver`, and your code imports it as `magnetar`, as in the example below:

```toml {filename="Cargo.toml"}
[dependencies]
magnetar-driver = "1.8"
tokio = { version = "1", features = ["macros", "rt-multi-thread", "time"] }
```

```rust {filename="src/main.rs"}
use std::sync::Arc;

use magnetar::proto::auth::TokenAuth;
use magnetar::{OutgoingMessage, PulsarClient};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let env = |name: &str| std::env::var(name).unwrap();
    let topic = format!(
        "persistent://{}/{}/rust-topic",
        env("ADDON_PULSAR_TENANT"),
        env("ADDON_PULSAR_NAMESPACE")
    );

    let client = PulsarClient::builder()
        .service_url(env("ADDON_PULSAR_BINARY_URL"))
        .auth(Arc::new(TokenAuth::from_env("ADDON_PULSAR_TOKEN")?))
        .build()
        .await?;

    let consumer = client.consumer(&topic).subscription("my-subscription").subscribe().await?;
    let producer = client.producer(&topic).create().await?;
    producer
        .send(OutgoingMessage::with_payload(b"Hello from Rust".as_slice()).into())
        .await?;

    let message = consumer.receive().await?;
    println!("Received: {}", String::from_utf8_lossy(&message.payload));
    consumer.ack(message.message_id).await?;
    Ok(())
}
```

{{< /tab >}}
{{< /tabs >}}

## Common code

The next examples start with this code: a client, and a `topic()` function that builds the full name of a topic. Put the code of each example where the comment shows it, in `main` for Java and Rust:

{{< tabs >}}
{{< tab name="Java" icon="java" >}}

```java {filename="Main.java"}
import java.util.concurrent.TimeUnit;
import org.apache.pulsar.client.api.*;

public class Main {
    static String topic(String name) {
        return "persistent://" + System.getenv("ADDON_PULSAR_TENANT") + "/"
            + System.getenv("ADDON_PULSAR_NAMESPACE") + "/" + name;
    }

    public static void main(String[] args) throws Exception {
        try (PulsarClient client = PulsarClient.builder()
                .serviceUrl(System.getenv("ADDON_PULSAR_BINARY_URL"))
                .authentication(AuthenticationFactory.token(System.getenv("ADDON_PULSAR_TOKEN")))
                .build()) {
            // The code of the example goes here
        }
    }
}
```

{{< /tab >}}
{{< tab name="Node.js" icon="simple:nodedotjs" >}}

```javascript {filename="main.js"}
import Pulsar from 'pulsar-client';

const env = process.env;
const client = new Pulsar.Client({
  serviceUrl: env.ADDON_PULSAR_BINARY_URL,
  authentication: new Pulsar.AuthenticationToken({ token: env.ADDON_PULSAR_TOKEN }),
});
const topic = (name) => `persistent://${env.ADDON_PULSAR_TENANT}/${env.ADDON_PULSAR_NAMESPACE}/${name}`;

// The code of the example goes here
await client.close();
```

{{< /tab >}}
{{< tab name="Python" icon="simple:python" >}}

```python {filename="main.py"}
import os
import pulsar

client = pulsar.Client(
    os.environ["ADDON_PULSAR_BINARY_URL"],
    authentication=pulsar.AuthenticationToken(os.environ["ADDON_PULSAR_TOKEN"]),
)

def topic(name):
    return f"persistent://{os.environ['ADDON_PULSAR_TENANT']}/{os.environ['ADDON_PULSAR_NAMESPACE']}/{name}"

# The code of the example goes here
client.close()
```

{{< /tab >}}
{{< tab name="Rust" icon="simple:rust" >}}

```rust {filename="src/main.rs"}
use std::sync::Arc;

use magnetar::proto::auth::TokenAuth;
use magnetar::{OutgoingMessage, PulsarClient};

fn topic(name: &str) -> String {
    let env = |var: &str| std::env::var(var).unwrap();
    format!("persistent://{}/{}/{name}", env("ADDON_PULSAR_TENANT"), env("ADDON_PULSAR_NAMESPACE"))
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = PulsarClient::builder()
        .service_url(std::env::var("ADDON_PULSAR_BINARY_URL")?)
        .auth(Arc::new(TokenAuth::from_env("ADDON_PULSAR_TOKEN")?))
        .build()
        .await?;

    // The code of the example goes here
    Ok(())
}
```

The producers, consumers, and readers of Magnetar need a topic without partitions. When a Magnetar producer uses a topic first, the cluster creates it with one partition. Create the topics of your Rust programs beforehand with [`pulsarctl-addon`](/doc/deploy/pulsar/#manage-topics-and-policies), such as `pulsarctl-addon topics create "persistent://$NS/orders" 0`, or use `partitioned_producer` and `partitioned_consumer`.

{{< /tab >}}
{{< /tabs >}}

## Share the work

A `Shared` subscription spreads the messages between its consumers. Run the same worker on several instances of your application, such as with `clever scale --instances 3`: each message goes to one of them. A `Key_Shared` subscription also sends the messages that share a key to the same consumer, in their order: here, all the events of an order.

Each tab holds two programs: the worker, then the producer, which groups the messages of its batches by key for the `Key_Shared` subscription.

{{< tabs >}}
{{< tab name="Java" icon="java" >}}

```java
Consumer<byte[]> consumer = client.newConsumer()
    .topic(topic("orders"))
    .subscriptionName("billing")
    .subscriptionType(SubscriptionType.Key_Shared)
    .subscribe();

while (true) {
    Message<byte[]> message = consumer.receive();
    System.out.println(message.getKey() + ": " + new String(message.getData()));
    consumer.acknowledge(message);
}
```

```java
Producer<byte[]> producer = client.newProducer()
    .topic(topic("orders"))
    .batcherBuilder(BatcherBuilder.KEY_BASED)
    .create();
producer.newMessage().key("order-42").value("Order paid".getBytes()).send();
```

{{< /tab >}}
{{< tab name="Node.js" icon="simple:nodedotjs" >}}

```javascript
const consumer = await client.subscribe({
  topic: topic('orders'),
  subscription: 'billing',
  subscriptionType: 'KeyShared',
});

for (;;) {
  const message = await consumer.receive();
  console.log(`${message.getPartitionKey()}: ${message.getData()}`);
  await consumer.acknowledge(message);
}
```

```javascript
const producer = await client.createProducer({ topic: topic('orders'), batchingType: 'KeyBasedBatching' });
await producer.send({ data: Buffer.from('Order paid'), partitionKey: 'order-42' });
```

{{< /tab >}}
{{< tab name="Python" icon="simple:python" >}}

```python
consumer = client.subscribe(topic("orders"), "billing", consumer_type=pulsar.ConsumerType.KeyShared)

while True:
    message = consumer.receive()
    print(f"{message.partition_key()}: {message.data().decode()}")
    consumer.acknowledge(message)
```

```python
producer = client.create_producer(topic("orders"), batching_type=pulsar.BatchingType.KeyBased)
producer.send(b"Order paid", partition_key="order-42")
```

{{< /tab >}}
{{< tab name="Rust" icon="simple:rust" >}}

```rust
use magnetar::proto::pb::command_subscribe::SubType;

let consumer = client
    .consumer(topic("orders"))
    .subscription("billing")
    .subscription_type(SubType::KeyShared)
    .subscribe()
    .await?;

loop {
    let message = consumer.receive().await?;
    let key = message.metadata.partition_key.as_deref().unwrap_or_default();
    println!("{key}: {}", String::from_utf8_lossy(&message.payload));
    consumer.ack(message.message_id).await?;
}
```

```rust
let producer = client.producer(topic("orders")).create().await?;
producer
    .send(OutgoingMessage::with_payload(b"Order paid".as_slice()).key("order-42").into())
    .await?;
```

{{< /tab >}}
{{< /tabs >}}

## Broadcast

Each subscription receives every message of the topic. Give each service its own subscription: next to the `billing` workers of the previous example, another application reads the same orders with a `notifications` subscription. The producer doesn't know the subscriptions: you add a service without changing the producer.

{{< tabs >}}
{{< tab name="Java" icon="java" >}}

```java
Consumer<byte[]> notifications = client.newConsumer()
    .topic(topic("orders"))
    .subscriptionName("notifications")
    .subscribe();

Message<byte[]> message = notifications.receive();
System.out.println(new String(message.getData()));
notifications.acknowledge(message);
```

{{< /tab >}}
{{< tab name="Node.js" icon="simple:nodedotjs" >}}

```javascript
const notifications = await client.subscribe({ topic: topic('orders'), subscription: 'notifications' });

const message = await notifications.receive();
console.log(message.getData().toString());
await notifications.acknowledge(message);
```

{{< /tab >}}
{{< tab name="Python" icon="simple:python" >}}

```python
notifications = client.subscribe(topic("orders"), "notifications")

message = notifications.receive()
print(message.data().decode())
notifications.acknowledge(message)
```

{{< /tab >}}
{{< tab name="Rust" icon="simple:rust" >}}

```rust
let notifications = client.consumer(topic("orders")).subscription("notifications").subscribe().await?;

let message = notifications.receive().await?;
println!("{}", String::from_utf8_lossy(&message.payload));
notifications.ack(message.message_id).await?;
```

{{< /tab >}}
{{< /tabs >}}

## Deliver later

A message can wait before its delivery, such as a reminder sent one minute later. Only `Shared` and `Key_Shared` subscriptions wait: an `Exclusive` or `Failover` subscription gets the message at once, without the delay.

{{< tabs >}}
{{< tab name="Java" icon="java" >}}

```java
Consumer<byte[]> consumer = client.newConsumer()
    .topic(topic("reminders"))
    .subscriptionName("mailer")
    .subscriptionType(SubscriptionType.Shared)
    .subscribe();
Producer<byte[]> producer = client.newProducer()
    .topic(topic("reminders"))
    .create();
producer.newMessage()
    .value("Send the payment reminder".getBytes())
    .deliverAfter(1, TimeUnit.MINUTES)
    .send();

Message<byte[]> message = consumer.receive();
System.out.println(new String(message.getData()));
consumer.acknowledge(message);
```

{{< /tab >}}
{{< tab name="Node.js" icon="simple:nodedotjs" >}}

```javascript
const consumer = await client.subscribe({
  topic: topic('reminders'),
  subscription: 'mailer',
  subscriptionType: 'Shared',
});
const producer = await client.createProducer({ topic: topic('reminders') });
await producer.send({ data: Buffer.from('Send the payment reminder'), deliverAfter: 60 * 1000 });

const message = await consumer.receive();
console.log(message.getData().toString());
await consumer.acknowledge(message);
```

{{< /tab >}}
{{< tab name="Python" icon="simple:python" >}}

```python
from datetime import timedelta

consumer = client.subscribe(topic("reminders"), "mailer", consumer_type=pulsar.ConsumerType.Shared)
producer = client.create_producer(topic("reminders"))
producer.send(b"Send the payment reminder", deliver_after=timedelta(minutes=1))

message = consumer.receive()
print(message.data().decode())
consumer.acknowledge(message)
```

{{< /tab >}}
{{< tab name="Rust" icon="simple:rust" >}}

```rust
use std::time::{SystemTime, UNIX_EPOCH};

use magnetar::proto::pb::command_subscribe::SubType;

let consumer = client
    .consumer(topic("reminders"))
    .subscription("mailer")
    .subscription_type(SubType::Shared)
    .subscribe()
    .await?;
let producer = client.producer(topic("reminders")).create().await?;
let now_ms = SystemTime::now().duration_since(UNIX_EPOCH)?.as_millis() as i64;
let message = OutgoingMessage::with_payload(b"Send the payment reminder".as_slice());
producer.send(message.deliver_after_ms(now_ms, 60_000).into()).await?;

let message = consumer.receive().await?;
println!("{}", String::from_utf8_lossy(&message.payload));
consumer.ack(message.message_id).await?;
```

{{< /tab >}}
{{< /tabs >}}

## Retry and dead letter

A consumer that can't process a message acknowledges it negatively, and Pulsar delivers it again after a delay, here 10 seconds. If it still fails after three new deliveries, the client moves it to a dead letter topic, `jobs-dlq`. The client also creates the `dlq` subscription on this topic, which keeps these messages until a consumer of `dlq` acknowledges them. A [reader](#replay-the-history) shows them without removing them from this subscription. The dead letter topic counts in the [limits](/doc/deploy/pulsar/#manage-topics-and-policies) of the namespace, like the other topics.

{{< tabs >}}
{{< tab name="Java" icon="java" >}}

`process` stands for the code of your application that handles a job, a static method of `Main` that throws an exception when it fails:

```java
Consumer<byte[]> consumer = client.newConsumer()
    .topic(topic("jobs"))
    .subscriptionName("workers")
    .subscriptionType(SubscriptionType.Shared)
    .negativeAckRedeliveryDelay(10, TimeUnit.SECONDS)
    .deadLetterPolicy(DeadLetterPolicy.builder()
        .maxRedeliverCount(3)
        .deadLetterTopic(topic("jobs-dlq"))
        .initialSubscriptionName("dlq")
        .build())
    .subscribe();

while (true) {
    Message<byte[]> message = consumer.receive();
    try {
        process(message.getData());
        consumer.acknowledge(message);
    } catch (Exception e) {
        consumer.negativeAcknowledge(message);
    }
}
```

{{< /tab >}}
{{< tab name="Node.js" icon="simple:nodedotjs" >}}

`processJob` stands for the code of your application that handles a job, an asynchronous function that throws an error when it fails:

```javascript
const consumer = await client.subscribe({
  topic: topic('jobs'),
  subscription: 'workers',
  subscriptionType: 'Shared',
  nAckRedeliverTimeoutMs: 10000,
  deadLetterPolicy: { deadLetterTopic: topic('jobs-dlq'), maxRedeliverCount: 3, initialSubscriptionName: 'dlq' },
});

for (;;) {
  const message = await consumer.receive();
  try {
    await processJob(message.getData());
    await consumer.acknowledge(message);
  } catch {
    consumer.negativeAcknowledge(message);
  }
}
```

{{< /tab >}}
{{< tab name="Python" icon="simple:python" >}}

`process` stands for the code of your application that handles a job, a function that raises an exception when it fails:

```python
consumer = client.subscribe(
    topic("jobs"),
    "workers",
    consumer_type=pulsar.ConsumerType.Shared,
    negative_ack_redelivery_delay_ms=10_000,
    dead_letter_policy=pulsar.ConsumerDeadLetterPolicy(
        max_redeliver_count=3,
        dead_letter_topic=topic("jobs-dlq"),
        initial_subscription_name="dlq",
    ),
)

while True:
    message = consumer.receive()
    try:
        process(message.data())
        consumer.acknowledge(message)
    except Exception:
        consumer.negative_acknowledge(message)
```

{{< /tab >}}
{{< tab name="Rust" icon="simple:rust" >}}

`process` stands for the code of your application that handles a job, a function that returns an error when it fails. Magnetar keeps the messages to move instead of sending them: `republish_dead_letters` publishes them to the dead letter topic, after each message or each `receive` that times out. It creates no subscription on this topic: create one before the first failure, with [`pulsarctl-addon`](/doc/deploy/pulsar/#manage-topics-and-policies):

```bash
pulsarctl-addon subscriptions create "persistent://$NS/jobs-dlq" dlq
```

```rust
use std::time::Duration;

use magnetar::proto::pb::command_subscribe::SubType;

let consumer = client
    .consumer(topic("jobs"))
    .subscription("workers")
    .subscription_type(SubType::Shared)
    .negative_ack_redelivery_delay(Duration::from_secs(10))
    .dead_letter_policy(3, Some(topic("jobs-dlq")))
    .subscribe()
    .await?;
let dead_letters = client.producer(topic("jobs-dlq")).create().await?;

loop {
    if let Ok(message) = tokio::time::timeout(Duration::from_secs(10), consumer.receive()).await {
        let message = message?;
        match process(&message.payload) {
            Ok(()) => consumer.ack(message.message_id).await?,
            Err(_) => consumer.negative_ack(message.message_id),
        }
    }
    consumer.republish_dead_letters(&dead_letters).await?;
}
```

{{< /tab >}}
{{< /tabs >}}

## Replay the history

A reader goes through a topic from a position you choose, such as its first message, without a subscription or acknowledgments. It reads as far back as the [retention](/doc/deploy/pulsar/#retention-and-cold-storage) of the namespace allows, Cellar included: a new service can rebuild its state from the past events.

{{< tabs >}}
{{< tab name="Java" icon="java" >}}

```java
Reader<byte[]> reader = client.newReader()
    .topic(topic("orders"))
    .startMessageId(MessageId.earliest)
    .create();

while (reader.hasMessageAvailable()) {
    System.out.println(new String(reader.readNext().getData()));
}
```

{{< /tab >}}
{{< tab name="Node.js" icon="simple:nodedotjs" >}}

```javascript
const reader = await client.createReader({
  topic: topic('orders'),
  startMessageId: Pulsar.MessageId.earliest(),
});

while (reader.hasNext()) {
  console.log((await reader.readNext()).getData().toString());
}
```

{{< /tab >}}
{{< tab name="Python" icon="simple:python" >}}

```python
reader = client.create_reader(topic("orders"), pulsar.MessageId.earliest)

while reader.has_message_available():
    print(reader.read_next().data().decode())
```

{{< /tab >}}
{{< tab name="Rust" icon="simple:rust" >}}

```rust
use magnetar::proto::MessageId;

let reader = client.reader(topic("orders")).start_message_id(MessageId::EARLIEST).create().await?;

while reader.has_message_available().await? {
    let message = reader.read_next().await?;
    println!("{}", String::from_utf8_lossy(&message.payload));
}
```

{{< /tab >}}
{{< /tabs >}}

A subscription can also go back to a date, here 24 hours earlier: all its consumers then receive the messages again from there.

{{< tabs >}}
{{< tab name="Java" icon="java" >}}

```java
Consumer<byte[]> consumer = client.newConsumer()
    .topic(topic("orders"))
    .subscriptionName("analytics")
    .subscribe();
consumer.seek(System.currentTimeMillis() - TimeUnit.HOURS.toMillis(24));

Message<byte[]> message = consumer.receive();
System.out.println(new String(message.getData()));
consumer.acknowledge(message);
```

{{< /tab >}}
{{< tab name="Node.js" icon="simple:nodedotjs" >}}

```javascript
const consumer = await client.subscribe({ topic: topic('orders'), subscription: 'analytics' });
await consumer.seekTimestamp(Date.now() - 24 * 3600 * 1000);

const message = await consumer.receive();
console.log(message.getData().toString());
await consumer.acknowledge(message);
```

{{< /tab >}}
{{< tab name="Python" icon="simple:python" >}}

```python
import time

consumer = client.subscribe(topic("orders"), "analytics")
consumer.seek(int((time.time() - 24 * 3600) * 1000))

message = consumer.receive()
print(message.data().decode())
consumer.acknowledge(message)
```

{{< /tab >}}
{{< tab name="Rust" icon="simple:rust" >}}

```rust
use std::time::{SystemTime, UNIX_EPOCH};

let consumer = client.consumer(topic("orders")).subscription("analytics").subscribe().await?;
let now_ms = SystemTime::now().duration_since(UNIX_EPOCH)?.as_millis() as u64;
consumer.seek_to_timestamp(now_ms - 24 * 3600 * 1000).await?;

let message = consumer.receive().await?;
println!("{}", String::from_utf8_lossy(&message.payload));
consumer.ack(message.message_id).await?;
```

{{< /tab >}}
{{< /tabs >}}

## Typed messages

A schema describes the messages of a topic. The first client that uses the topic registers its schema, and the cluster then refuses the producers and consumers whose schema doesn't match. Here, a JSON schema for orders, on its own topic: `orders-typed`.

{{< tabs >}}
{{< tab name="Java" icon="java" >}}

Add the `Order` class to `Main`:

```java
public static class Order {
    public String id;
    public int amount;
}
```

```java
Consumer<Order> consumer = client.newConsumer(Schema.JSON(Order.class))
    .topic(topic("orders-typed"))
    .subscriptionName("billing")
    .subscribe();
Producer<Order> producer = client.newProducer(Schema.JSON(Order.class))
    .topic(topic("orders-typed"))
    .create();

Order order = new Order();
order.id = "A-42";
order.amount = 1299;
producer.send(order);

Message<Order> message = consumer.receive();
System.out.println(message.getValue().id + " " + message.getValue().amount);
consumer.acknowledge(message);
```

{{< /tab >}}
{{< tab name="Node.js" icon="simple:nodedotjs" >}}

```javascript
const schema = {
  schemaType: 'Json',
  schema: JSON.stringify({
    type: 'record',
    name: 'Order',
    fields: [
      { name: 'id', type: 'string' },
      { name: 'amount', type: 'int' },
    ],
  }),
};
const consumer = await client.subscribe({ topic: topic('orders-typed'), subscription: 'billing', schema });
const producer = await client.createProducer({ topic: topic('orders-typed'), schema });
await producer.send({ data: Buffer.from(JSON.stringify({ id: 'A-42', amount: 1299 })) });

const message = await consumer.receive();
const order = JSON.parse(message.getData());
console.log(order.id, order.amount);
await consumer.acknowledge(message);
```

{{< /tab >}}
{{< tab name="Python" icon="simple:python" >}}

```python
from pulsar.schema import Integer, JsonSchema, Record, String

class Order(Record):
    id = String()
    amount = Integer()

consumer = client.subscribe(topic("orders-typed"), "billing", schema=JsonSchema(Order))
producer = client.create_producer(topic("orders-typed"), schema=JsonSchema(Order))
producer.send(Order(id="A-42", amount=1299))

message = consumer.receive()
print(message.value().id, message.value().amount)
consumer.acknowledge(message)
```

{{< /tab >}}
{{< tab name="Rust" icon="simple:rust" >}}

`Order` derives the traits of the `serde` and `schemars` crates. Add them to the `[dependencies]` of your `Cargo.toml`:

```toml {filename="Cargo.toml"}
schemars = "1"
serde = { version = "1", features = ["derive"] }
```

```rust
#[derive(serde::Serialize, serde::Deserialize, schemars::JsonSchema)]
struct Order {
    id: String,
    amount: i32,
}
```

```rust
use magnetar::proto::schema::JsonSchema;

let schema = Arc::new(JsonSchema::<Order>::new());
let consumer = client
    .typed_consumer(topic("orders-typed"), schema.clone())
    .subscription("billing")
    .subscribe()
    .await?;
let producer = client.typed_producer(topic("orders-typed"), schema).create().await?;
producer.send(&Order { id: "A-42".into(), amount: 1299 }, None).await?;

let message = consumer.receive().await?;
println!("{} {}", message.value.id, message.value.amount);
consumer.ack(message.message_id).await?;
```

{{< /tab >}}
{{< /tabs >}}
