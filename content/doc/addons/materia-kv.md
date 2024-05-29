---
type: docs
title: Materia KV
description: Materia KV is a serverless key-value database, with high availability and open compatibility
tags:
- addons
keywords:
- materia
- kv
- dynamodb
- graphql
- redis
aliases:
- /doc/addons/materia-db-kv/
type: docs
draft: false
---

Materia is a new serverless databases offering by Clever Cloud. A whole range of services meeting the needs expressed by our customers in recent years, with an open and resilient approach. It includes deployment across multiple availability zones, compatibility with existing protocols, clients, and pay-as-you-go billing. It's built on the [FoundationDB](https://www.foundationdb.org/) open source transactional engine. A distributed and robust solution, notably thanks to its high simulation capacity.

Materia KV is the first publicly available product of this family. It's a key-value database which comes with simplicity in mind. You have no instance size to choose, no storage capacity to worry about. We simply provide you with a host address, a port and a token: you’re ready to go! Once our servers send a reply message, your data is durable: it's synchronously replicated over 3 datacenters in Paris.

You don't have to configure leaders, followers: high availability is included, by design.

{{< callout type="info" >}}

* Materia KV is in Alpha testing phase** Your insights and suggestions are crucial in shaping the future of this platform. To share your feedback, please visit us at [our community page](https://github.com/CleverCloud/Community/discussions/categories/materia). Thank you for being a part of our journey towards innovation and improvement!

{{< /callout >}}

## Compatibility layers

We didn’t want this Materia KV to come at the cost of complex configuration, requiring the use of special clients and ORMs. That’s why we’ve developed its compatibility layers. To “talk” to it, you don’t need a special API or tools specific to Clever Cloud. You'll be able to use it with existing solutions for **DynamoDB, GraphQL or Redis**. The first available layer is compatible with Redis API (and its variants as Reddict or Valkey).

Thus, you can use a Materia KV add-on with any compatible client within your applications, `redis-cli` or alternatives such as [iredis](https://github.com/laixintao/iredis). You can also use it with graphical interface (GUI). We tested many of them with success:

- [Another Redis Desktop Client](https://goanother.com/)
- [PX3 Redis UI](https://github.com/patrikx3/redis-ui)
- [Qredis](https://github.com/tiagocoutinho/qredis)
- [Redis Commander](https://github.com/joeferner/redis-commander)
- [Redis Insight](https://redis.com/redis-enterprise/redis-insight/)

## Create a Materia KV add-on

You can create a Materia KV add-on as simply as any other Clever Cloud service in the Console, [following this link](https://console.clever-cloud.com/users/me/addons/new). Select the Alpha plan (free during testing phase), an application to link to (or none), give it a name, and you'll get access to its dashboard giving you connection details. Environment variables shared with a linked application are listed in the `Service dependencies` section.

We included them with the `REDIS_` format. Thus, you can just try to replace a Redis instance by Materia KV. It's as simple as linking the new add-on, unlinking the old one and restarting your application! (Check commands you'll need first).

You can also use clever tools to create a Materia KV add-on and set environment variables to test it with a `PING` command:

```
clever addon create kv DATABASE_NAME
source <(clever addon env addon ADDON_ID -F shell)
redis-cli -h $KV_HOST -p $KV_PORT --tls PING
```

Here is an example of what you can expect:

```
$ clever addon create kv testKV

Add-on created successfully!
ID: addon_4997cfe3-f104-4d05-9fe4-xxxxxxxxx
Real ID: kv_01HV6NCSRD1TV2AJW4RKFBJ07R
Name: testKV

/!\ The Materia KV provider is in Alpha testing phase, don't store sensitive or production grade data
You can easily use Materia KV with 'redis-cli', with such commands:
source <(clever addon env addon_4997cfe3-f104-xxxx-xxxx-xxxxxxxxx -F shell)
redis-cli -h $KV_HOST -p $KV_PORT --tls
```


You can also deploy Materia KV add-ons with [Terraform provider](https://registry.terraform.io/providers/CleverCloud/clevercloud/latest/docs/resources/materiadb_kv) (OpenTofu compatible).

{{< callout type="info" >}}

**Materia KV is in Alpha testing phase** Each add-on is limited to 128 MB of storage, requests sent to the server can't exceed 1 kB. As we fine-tune and enhance its capabilities, we advise against using the alpha release for production purposes. During alpha testing we can delete data or renew token, don't store sensitive or production grade data.

{{< /callout >}}

## Using the Redis API compatible layer

### Environment variables and CLI usage

To connect to a Materia KV add-on, you need 3 parameters: the host, the port and a ([biscuit](https://biscuitsec.org) based) token. You can set these parameters as environment variables by doing `source <(clever addon env addon ADDON_ID -F shell)`. The variables set are:

* `$KV_HOST` and its alias `$REDIS_HOST`
* `$KV_PORT` and its alias `$REDIS_PORT`
* `$KV_TOKEN` and its alias `$REDIS_PASSWORD`
* `$REDIS_CLI_URL`
* `$REDISCLI_AUTH`

You can directly use these environment variables to connect to a Materia KV add-on using `redis-cli` if `REDISCLI_AUTH` is set:

```bash
redis-cli -h $KV_HOST -p $KV_PORT --tls
```

Materia KV is also compatible with alternatives such as [iredis](https://github.com/laixintao/iredis).

### Fish shell users

If you use the Fish shell, you can use the following command to set the environment variables:

```fish
clever addon env ADDON_ID -F shell | source
```

### Supported types and commands

During this alpha stage, we don't provide 100% compatibility with the Redis API. Curently supported value types are:

- Hash
- List
- String

Find below the list of currently supported commands:

| <div style="width:99px">Commands</div>  | Description |
| ------- | ----------- |
| `APPEND` | If `key` already exists and is a string, this command appends the value at the end of the string. If `key` does not exist it is created and set as an empty string, so `APPEND` will be similar to `SET` in this special case. |
| `AUTH` | Authenticate the current connection using the biscuit token as `password`. |
| `CLUSTER INFO` | Indicates that cluster support is disabled, i.e. Materia KV is naturally distributed and doesn't support or needs Redis clustering. |
| `COMMAND` | Return an array with details about every supported command. |
| `COMMAND INFO` | Returns @array-reply of details about multiple Materia KV commands. Same result format as `COMMAND` except you can specify which commands get returned. If you request details about non-existing commands, their return position will be `nil`. |
| `COMMAND LIST` | Return an array of the server's command names. |
| `COMMAND DOCS` | Return documentary information about commands. By default, the reply includes all the server's commands. You can use the optional command-name argument to specify the names of one or more commands. The reply includes a map for each returned command. |
| `DBSIZE` | Return the number of keys in the currently-selected database. |
| `DECR` | Decrements the number stored at `key` by one. If the `key` does not exist, it is set to 0 before performing the operation. An error is returned if `key` contains a value of the wrong type or contains a string that can not be represented as integer. This operation is limited to 64-bit signed integers. |
| `DEL` | Removes the specified `key`. A key is ignored if it does not exist. |
| `EXISTS` | Returns if `key` exists. |
| `GET` | Get the value of key. If the key does not exist the special value nil is returned. An error is returned if the value stored at key is not a string, because `GET` only handles string values. |
| `GETRANGE` | Returns the substring of the string value stored at key, determined by the offsets start and end (both are inclusive). Negative offsets can be used in order to provide an offset starting from the end of the string. So -1 means the last character, -2 the penultimate and so forth. The function handles out of range requests by limiting the resulting range to the actual length of the string. |
| `FLUSHDB` | Delete all the keys of the currently selected DB. This command never fails. Curently we only support the synchronous mode of `FLUSHDB`. |
| `HDEL` | Removes the specified fields from the hash stored at `key`. Specified fields that do not exist within this hash are ignored. If `key` does not exist, it is treated as an empty hash and this command returns `0`. |
| `HGET` | Returns the value associated with `field` in the hash stored at `key`. |
| `HGETALL` | Returns all fields and values of the hash stored at `key`. In the returned value, every field name is followed by its value, so the length of the reply is twice the size of the hash. |
| `HLEN` | Returns the number of fields contained in the hash stored at `key`. |
| `HMGET` | Returns the values associated with the specified fields in the hash stored at `key`. For every field that does not exist in the hash, a `nil` value is returned. Because non-existing keys are treated as empty hashes, running `HMGET` against a non-existing `key` will return a list of nil values. |
| `HMSET` | Sets the specified fields to their respective values in the hash stored at `key`. This command overwrites any specified fields already existing in the hash. If `key` does not exist, a new key holding a hash is created. |
| `HSCAN` | Incrementally iterate over fields of Hash types and their associated values. It is a cursor based iterator, this means that at every call of the command, the server returns an updated cursor that the user needs to use as the cursor argument in the next call. An iteration starts when the cursor is set to 0, and terminates when the cursor returned by the server is 0. |
| `HSET` | Sets the specified fields to their respective values in the hash stored at `key`. This command overwrites the values of specified fields that exist in the hash. If `key` doesn't exist, a new key holding a hash is created. |
| `INCR` | Increments the number stored at `key` by one. If the `key` does not exist, it is set to 0 before performing the operation. An error is returned if `key` contains a value of the wrong type or contains a string that can not be represented as integer. This operation is limited to 64-bit signed integers. |
| `INFO` | The `INFO` command returns information and statistics about the server in a format that is simple to parse by computers and easy to read by humans. |
| `KEYS` | Returns all keys matching `pattern`, can be `*` |
| `LLEN` | Returns the length of the list stored at `key`. If `key` does not exist, it is interpreted as an empty list and 0 is returned. An error is returned when the value stored at `key` is not a list. |
| `LPOP` | Removes and returns the first elements of the list stored at `key`. |
| `LPUSH` | Insert all the specified values at the head of the list stored at `key`. If `key` does not exist, it is created as empty list before performing the push operations. When `key` holds a value that is not a list, an error is returned. |
| `LPUSHX` | Inserts specified values at the head of the list stored at `key`, only if `key` already exists and holds a list. In contrary to `LPUSH`, no operation will be performed when `key` does not yet exist. |
| `LRANGE` | Returns the specified elements of the list stored at `key`. The offsets `start` and `stop` are zero-based indexes, with 0 being the first element of the list (the head of the list), 1 being the next element and so on. These offsets can also be negative numbers indicating offsets starting at the end of the list. For example, -1 is the last element of the list, -2 the penultimate, and so on. |
| `LSET` | Sets the list element at `index` to `element`. |
| `MEMORY USAGE` | The `MEMORY USAGE` command reports the number of bytes that a key and its value require to be stored in RAM. |
| `MGET` | Returns the values of all specified keys. For every key that does not hold a string value or does not exist, the special value `nil` is returned. Because of this, the operation never fails. |
| `MODULE LIST` | Returns information about the modules loaded to the server (currently none). |
| `MSET` | Sets the given keys to their respective values. `MSET` replaces existing values with new values, just as regular `SET`. `MSET` is atomic, so all given keys are set at once. It is not possible for clients to see that some keys were updated while others are unchanged. |
| `PING` | Returns `PONG` if no argument is provided, otherwise return a copy of the argument as a bulk. |
| `QUIT` | Ask the server to close the connection. The connection is closed as soon as all pending replies have been written to the client. |
| `RPOP` | Removes and returns the last elements of the list stored at `key`. By default, the command pops a single element from the end of the list. When provided with the optional count argument, the reply will consist of up to count elements, depending on the list's length. |
| `RPUSH` | Insert all the specified values at the tail of the list stored at `key`. If `key` does not exist, it is created as empty list before performing the push operation. When `key` holds a value that is not a list, an error is returned. |
| `RPUSHX` | Inserts specified values at the tail of the list stored at `key`, only if `key` already exists and holds a list. In contrary to `RPUSH`, no operation will be performed when `key` does not yet exist. |
| `SCAN` | Incrementally iterate over a collection of elements. It is a cursor based iterator, this means that at every call of the command, the server returns an updated cursor that the user needs to use as the cursor argument in the next call. An iteration starts when the cursor is set to 0, and terminates when the cursor returned by the server is 0. |
| `SET` | Set `key` to hold the string `value`. If `key` already holds a value, it is overwritten, regardless of its type. |
| `SELECT` | Select the logical database having the specified zero-based numeric index. In Materia KV only SELECT 0 can be used. |
| `STRLEN` | Returns the length of the string value stored at `key`. An error is returned when key holds a non-string value. |
| `TTL` | Returns the remaining time to live of a key that has a timeout. During the alpha phase, key timeouts aren't implemented. Nevertheless, for compatibility reasons, we support the `TTL` command. The command returns -2 if the key does not exist, it returns -1 if the key exists with no defined timeout. |
| `TYPE` | Returns the string representation of the type of the value stored at `key`. Can be: `hash`, `list` or `string`.
