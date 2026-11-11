---
type: docs
linkTitle: Pulsar
title: Apache Pulsar
description: Publish and consume messages with an Apache Pulsar namespace on Clever Cloud, manage its topics and policies with the admin API, and keep old data on Cellar
keywords:
- apache pulsar
- message queue
- pub-sub messaging
- pulsarctl
- event streaming
- tiered storage
- biscuit
aliases:
- /addons/pulsar
- /deploy/addon/pulsar
- /doc/addons/pulsar
- /doc/deploy/addon/pulsar
- /doc/pulsar
- /doc/storage/pulsar
---

[Apache Pulsar](https://pulsar.apache.org) is an open source messaging and streaming platform. Producers publish messages to topics, and consumers read them through subscriptions. Each subscription receives every message of the topic. Give each application its own subscription to broadcast messages, or share one subscription between several consumers to spread the work.

Use Pulsar to distribute tasks between workers, to stream events from devices or between services, or to notify applications of changes. A Pulsar add-on gives you a namespace on a Pulsar cluster that Clever Cloud manages, with a token to reach it from your applications.

The add-on is serverless: you don't choose a size, a number of brokers, or a storage capacity, and Clever Cloud runs and updates the cluster. You pay per use, for the data you store on the cluster and on Cellar, and for the traffic in and out. You never pay for an idle machine.

## How it works

Pulsar names each topic after its tenant and namespace:

```text
{persistent|non-persistent}://<tenant>/<namespace>/<topic>
```

The tenant is the ID of the organisation or personal space that owns the add-on, such as `orga_xxx` or `user_xxx`. The namespace is the real ID of the add-on, such as `pulsar_xxx`. You create your topics in this namespace, but no other namespace or tenant.

A persistent topic keeps each message until all its subscriptions acknowledge it, then as long as the [retention](#retention-and-cold-storage) of the namespace allows. A non-persistent topic only delivers messages to the consumers connected when they arrive, without storing them. Each subscription has a [type](https://pulsar.apache.org/docs/concepts-messaging/#subscription-types) that sets how the consumers of this subscription share its messages:

- `Exclusive`: a single consumer reads the subscription
- `Failover`: one consumer reads the subscription, another one takes over if it fails
- `Shared`: consumers share the messages, each one gets some of them
- `Key_Shared`: consumers share the messages, each key going to the same consumer

## Create a Pulsar add-on

In the [Console](https://console.clever-cloud.com), click **Create**, then **Add-on**, and select **Pulsar**. With [Clever Tools](/doc/tools/cli/install/), add `--org` to create it in an organisation, `--region` to choose its region, `par` by default, and `--link` to link it to an application:

```bash
clever addon create addon-pulsar my-pulsar
```

See the [pricing page](https://www.clever.cloud/pricing/) for the rates of storage and traffic. By default, messages never expire: the stored data grows until you set a [retention](#retention-and-cold-storage).

## Connect to Pulsar

Link the add-on to your application with `clever service link-addon my-pulsar`, or from the **Service dependencies** tab of the add-on in the Console. Your application gets these environment variables at its next deployment:

| Variable                   | Value                                                             |
| -------------------------- | ----------------------------------------------------------------- |
| `ADDON_PULSAR_BINARY_URL`  | URL of the Pulsar protocol with TLS, `pulsar+ssl://`, for clients |
| `ADDON_PULSAR_HTTP_URL`    | URL of the admin API, over HTTPS                                  |
| `ADDON_PULSAR_HOSTNAME`    | Host of these URLs                                                |
| `ADDON_PULSAR_BINARY_PORT` | Port of `ADDON_PULSAR_BINARY_URL`                                 |
| `ADDON_PULSAR_HTTP_PORT`   | Port of `ADDON_PULSAR_HTTP_URL`                                   |
| `ADDON_PULSAR_TENANT`      | Tenant of the add-on                                              |
| `ADDON_PULSAR_NAMESPACE`   | Namespace of the add-on                                           |
| `ADDON_PULSAR_TOKEN`       | Token of the add-on, which clients and the admin API accept       |

In the dashboard of the add-on, the **Access** panel has two tabs. **API** shows the URL of the admin API, and **CLI** the URL of the Pulsar protocol. Both add the namespace, as `tenant/namespace`, and the token.

Use an official [client library](https://pulsar.apache.org/docs/client-libraries/) with token authentication. In Python, with the `pulsar-client` package:

```python {filename="main.py"}
import os
import pulsar

client = pulsar.Client(
    os.environ["ADDON_PULSAR_BINARY_URL"],
    authentication=pulsar.AuthenticationToken(os.environ["ADDON_PULSAR_TOKEN"]),
)
topic = f"persistent://{os.environ['ADDON_PULSAR_TENANT']}/{os.environ['ADDON_PULSAR_NAMESPACE']}/orders"

consumer = client.subscribe(topic, "my-subscription")
producer = client.create_producer(topic)
producer.send(b"Hello from Clever Cloud")

message = consumer.receive()
print(message.data().decode())
consumer.acknowledge(message)
client.close()
```

By default, the cluster creates a topic the first time a producer or a consumer uses it, as a partitioned topic with one partition: `orders-partition-0`. To choose the number of partitions, [create the topic](#manage-topics-and-policies) first. See the [code examples](/doc/deploy/pulsar/examples/) to share work between instances, delay or retry messages, and replay the history of a topic, Cellar included.

## Manage topics and policies

[`pulsarctl`](https://github.com/streamnative/pulsarctl) manages the namespace and its topics with the token of the add-on. On your computer, load the variables of the add-on with its ID or real ID, here `pulsar_xxx`. Then create an alias with the options that connect it to the add-on:

```bash
eval "$(clever addon env pulsar_xxx -F shell)"
alias pulsarctl-addon='pulsarctl --admin-service-url "$ADDON_PULSAR_HTTP_URL" \
  --auth-plugin org.apache.pulsar.client.impl.auth.AuthenticationToken \
  --auth-params "$ADDON_PULSAR_TOKEN"'
NS="$ADDON_PULSAR_TENANT/$ADDON_PULSAR_NAMESPACE"
```

Then list, create, and delete topics, here a topic with three partitions, up to 12:

```bash
pulsarctl-addon namespaces topics "$NS"
pulsarctl-addon topics create "persistent://$NS/payments" 3
pulsarctl-addon subscriptions list "persistent://$NS/payments"
pulsarctl-addon topics delete "persistent://$NS/payments"
```

Add `--non-partitioned` to delete a topic without partitions. `namespaces topics` lists the persistent topics only. The token also lets you set the policies of the namespace. For instance, the time to live of unacknowledged messages, the backlog quota, or the removal of duplicate messages:

```bash
pulsarctl-addon namespaces set-message-ttl "$NS" --messageTTL 3600
pulsarctl-addon namespaces set-backlog-quota "$NS" --limit-size 1G --policy producer_request_hold
pulsarctl-addon namespaces set-deduplication "$NS" --enable
pulsarctl-addon namespaces policies "$NS"
```

Set the retention with the [Clever Cloud API](#retention-and-cold-storage) rather than with `set-retention`: it checks that Pulsar doesn't delete data before moving it to Cellar. The [admin REST API](https://pulsar.apache.org/admin-rest-api/) of Pulsar offers the same operations as `pulsarctl`, with the token in an `Authorization: Bearer` header. For instance, this request lists all the topics of the namespace, including the non-persistent ones:

```bash
curl -H "Authorization: Bearer $ADDON_PULSAR_TOKEN" \
  "$ADDON_PULSAR_HTTP_URL/admin/v2/namespaces/$ADDON_PULSAR_TENANT/$ADDON_PULSAR_NAMESPACE/topics?mode=ALL"
```

The token can't create namespaces, manage permissions, change the [offload threshold](#retention-and-cold-storage), or these limits:

- 100 topics, each partition counting as one
- 100 producers per topic
- 200 consumers per topic, and 50 per subscription

## Retention and cold storage

A new namespace keeps the messages of its persistent topics without limit of time or size. A few minutes after its creation, each add-on also gets a Cellar bucket for [tiered storage](https://pulsar.apache.org/docs/tiered-storage-overview/). Clever Cloud manages it, and you don't see it among your add-ons.

By default, the add-on moves each segment of a topic to this bucket once the segment closes, which can take hours on a quiet topic. The segment leaves the cluster four hours later, and consumers read it from Cellar like the others. Set the retention and the offload thresholds with the Clever Cloud API, here through [`clever curl`](/doc/tools/cli/#curl). For each topic partition, this request keeps acknowledged messages up to 30 days and 100 GiB, Cellar included. It moves data to Cellar beyond 1 GiB on the cluster, or after one day:

```bash
clever curl -X PATCH -H "Content-Type: application/json" \
  "https://api.clever-cloud.com/v4/addon-providers/addon-pulsar/addons/$ADDON_PULSAR_NAMESPACE/storage-policies" \
  -d '{"retentionPolicies":{"sizeInBytes":107374182400,"durationInMinutes":43200},"offloadPolicies":{"sizeInBytes":1073741824,"durationInMinutes":1440}}'
```

The Console doesn't set these policies: use the API. Pulsar applies a new retention to the messages it already holds. Change the offload thresholds once the bucket is ready, when a `GET` request on the same URL returns `offloadPolicies`: linking the bucket resets them. These requests need the admin or manager role in an organisation.

Send both policies with all their values. A value you leave out removes this limit or this offload trigger, and leaving out `retentionPolicies` removes both limits of the retention. Leaving out `offloadPolicies` keeps the current offload thresholds, while an empty `offloadPolicies` stops moving data from the cluster to Cellar for this namespace.

Each offload threshold must stay lower than the retention limit of the same kind: size against size, duration against duration. This holds even when you only change the retention. Otherwise the API refuses the request, as Pulsar would delete the data before moving it. To delete acknowledged messages at once, as a queue does, set both retention values to `0` and send an empty `offloadPolicies`.

## Restrict the token

The [Eclipse Biscuit](https://doc.biscuitsec.org/) token of the add-on gives access to the whole namespace, its topics, and its policies.

To limit a client to one topic, create a token for this topic with the Clever Cloud API:

```bash
clever curl -s -X POST \
  "https://api.clever-cloud.com/v4/addon-providers/addon-pulsar/addons/$ADDON_PULSAR_NAMESPACE/topics/orders/token" \
  | jq -r . > orders.biscuit
```

The API returns a JSON string: `jq -r .` saves it without its quotes. Use the name of the topic, without the `-partition-N` suffix of its partitions. The token covers the persistent and the non-persistent topic of this name, with all their partitions. It produces, consumes, reads statistics, manages subscriptions, and can even terminate the topic, but can't create or delete it. [Attenuate it](/doc/deploy/pulsar/token-attenuation/#limit-operations) to only let a client produce or consume.

These tokens don't expire, and you can't revoke them: [limit one in time](/doc/deploy/pulsar/token-attenuation/#limit-in-time) before you hand it out. [Token attenuation](/doc/deploy/pulsar/token-attenuation/) also restricts the token of the add-on to a prefix of topics, without a request to the API.

## Version and deletion

Clever Cloud updates the Pulsar version of the cluster. The **Information** panel of the dashboard shows it, with the creation date of the add-on. To check the version of the brokers, query the admin API:

```bash
curl -H "Authorization: Bearer $ADDON_PULSAR_TOKEN" "$ADDON_PULSAR_HTTP_URL/admin/v2/brokers/version"
```

Rename, tag, or delete the add-on at the bottom of its dashboard, or delete it with `clever addon delete`. When you delete the add-on, Clever Cloud deletes its namespace, with its topics and messages, and its Cellar bucket, at least three days later.

## Go Further

{{< cards >}}
  {{< card link="/developers/doc/deploy/pulsar/examples" title="Code examples" subtitle="Work queues, broadcast, delays, retries, replay, and schemas" icon="code-bracket" >}}
  {{< card link="/developers/doc/deploy/pulsar/token-attenuation" title="Token attenuation" subtitle="Restrict a token to topics, operations, or a period of time" icon="key" >}}
  {{< card link="https://pulsar.apache.org/docs/concepts-overview/" title="Apache Pulsar documentation" subtitle="Concepts and features: messaging, subscriptions, schemas, tiered storage" icon="simple:apachepulsar" >}}
{{< /cards >}}
