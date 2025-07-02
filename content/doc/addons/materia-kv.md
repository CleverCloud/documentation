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

Materia KV is the first publicly available product of this family. It's a key-value database which comes with simplicity in mind. You have no instance size to choose, no storage capacity to worry about. We simply provide you with a host address, a port and a token: you’re ready to go! Once our servers send a reply message, your data is durable: it's synchronously replicated over 3 data centers in Paris.

You don't have to configure leaders, followers: high availability is included, by design.

{{< callout type="info" >}}

**Materia KV is in Alpha testing phase:** your insights and suggestions are crucial in shaping the future of this platform. To share your feedback, please visit us at [our community page](https://github.com/CleverCloud/Community/discussions/categories/materia). Thank you for being a part of our journey towards innovation and improvement!
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

```bash
clever addon create kv DATABASE_NAME
source <(clever addon env addon ADDON_ID -F shell)
redis-cli -h $KV_HOST -p $KV_PORT --tls PING
```

Here is an example of what you can expect:

```
$ clever addon create kv testKV

Add-on created successfully!
ID: addon_4997cfe3-f104-4d05-9fe4-xxxxxxxxx
Real ID: kv_01HV6NCSRDxxxxxxxxxxxxxxxx
Name: testKV

/!\ The Materia KV provider is in Alpha testing phase, don't store sensitive or production grade data
You can easily use Materia KV with 'redis-cli', with such commands:
source <(clever addon env addon_4997cfe3-f104-xxxx-xxxx-xxxxxxxxx -F shell)
redis-cli -h $KV_HOST -p $KV_PORT --tls
```

You can also deploy Materia KV add-ons with [Terraform provider](https://registry.terraform.io/providers/CleverCloud/clevercloud/latest/docs/resources/materiadb_kv) (OpenTofu compatible).

{{< callout type="info" >}}

**Materia KV is in Alpha testing phase** Each add-on is limited to 128 MB of storage, requests sent to the server can't exceed 5 MB. As we fine-tune and enhance its capabilities, we advise against using the alpha release for production purposes. During alpha testing we can delete data or renew token, don't store sensitive or production grade data.

{{< /callout >}}

{{< content "kv-explorer" >}}

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

{{< callout type="info" >}}
By default, Materia KV uses TLS on the 6379 port. You can use non-TLS connections on the 6378 port for testing purposes.
{{< /callout >}}

### Clever KV

We're exploring how [Clever Tools](https://github.com/CleverCloud/clever-tools/) can natively support Materia KV and helps you to manage such add-ons without any additional software or configuration. The `clever kv` command is available since [version 3.11](https://github.com/CleverCloud/clever-tools/releases/tag/3.11.0).

* [Learn more about Clever KV](/developers/doc/cli/kv-stores/)

### Demos and examples

We've prepared a few examples to help you get started with Materia KV:

* [Materia KV Go client](https://github.com/CleverCloud/mkv-go-cli)
* [Materia KV raw TCP V demo](https://github.com/CleverCloud/mkv-raw-tcp-v)
* [Materia KV raw TCP Ruby demo](https://github.com/CleverCloud/mkv-raw-tcp-ruby)
* [Materia KV PHP sessions with TTL demo](https://github.com/CleverCloud/php-sessions-kv-example)
*
### Supported types and commands

During this alpha stage, we don't provide 100% compatibility with the Redis API. Currently supported value types are:

- String

Find below the list of currently supported commands:

| <div style="width:99px">Commands</div>  | Description |
| ------- | ----------- |
| `APPEND` | If `key` already exists and is a string, this command appends the value at the end of the string. If `key` doesn't exist it is created and set as an empty string, so `APPEND` will be similar to `SET` in this special case. |
| `AUTH` | Authenticate the current connection using the biscuit token as `password`. |
| `CLIENT ID` | Returns the `ID` of the current connection. A connection ID has is never repeated and is monotonically incremental. |
| `COMMAND` | Return an array with details about every supported command. |
| `COMMAND DOCS` | Return documentary information about commands. By default, the reply includes all the server's commands. You can use the optional command-name argument to specify the names of one or more commands. The reply includes a map for each returned command. |
| `COMMAND INFO` | Returns an array reply of details about multiple Materia KV commands. Same result format as `COMMAND` except you can specify which commands get returned. If you request details about non-existing commands, their return position will be `nil`. |
| `COMMAND LIST` | Return an array of the server's command names. |
| `DBSIZE` | Return the number of keys in the currently-selected database. |
| `DECR` | Decrements the number stored at `key` by one. If the `key` doesn't exist, it is set to `0` before performing the operation. An error is returned if `key` contains a value of the wrong type or contains a string that can not be represented as integer. This operation is limited to 64-bit signed integers. |
| `DECRBY` | Decrements the number stored at `key` by the given `decrement`. If the `key` doesn't exist, it is set to `0` before performing the operation. An error is returned if `key` contains a value of the wrong type or contains a string that can not be represented as integer. This operation is limited to 64-bit signed integers. |
| `DEL` | Removes the specified `key`. A key is ignored if it doesn't exist. |
| `EXISTS` | Returns if `key` exists. |
| `EXPIRE` | Set a `key` time to live in seconds. After the timeout has expired, the `key` will be automatically deleted.  The time to live can be updated using the `EXPIRE` command or cleared using the `PERSIST` command. |
| `FLUSHALL` | Delete all the keys of all the existing databases, not just the currently selected one. This command never fails. |
| `FLUSHDB` | Delete all the keys of the currently selected DB. This command never fails. |
| `GET` | Get the value of `key`. If the `key` doesn't exist the special value nil is returned. An error is returned if the value stored at `key` is not a string, because `GET` only handles string values. |
| `GETBIT` | Returns the bit value at offset in the string value stored at `key`. |
| `GETRANGE` | Returns the substring of the string value stored at `key`, determined by the offsets start and end (both are inclusive). Negative offsets can be used in order to provide an offset starting from the end of the string. So `-1` means the last character, `-2` the penultimate and so forth. |
| `HELLO` | Switch to a different protocol, optionally authenticating and setting the connection's name, or provide a contextual client report. It always replies with a list of current server and connection properties. |
| `INCR` | Increments the number stored at `key` by one. If the `key` doesn't exist, it is set to `0` before performing the operation. An error is returned if `key` contains a value of the wrong type or contains a string that can not be represented as integer. This operation is limited to 64-bit signed integers. |
| `INCRBY` | Increments the number stored at `key` by the given `increment`. If the `key` doesn't exist, it is set to `0` before performing the operation. An error is returned if `key` contains a value of the wrong type or contains a string that can not be represented as integer. This operation is limited to 64-bit signed integers. |
| `INFO` | The `INFO` command returns information and statistics about the server in a format that is simple to parse by computers and easy to read by humans. |
| `JSON.DEL` | Deletes JSON value at path from key. Returns the number of paths deleted. Can delete array elements or object fields. |
| `JSON.GET` | Gets JSON value at path from key. Supports both single and multiple path queries with different path notations. |
| `JSON.SET` | Sets JSON value at root path (`$`) and updating existing paths in key. Creates new key if it doesn't exist. |
| `KEYS` | Returns all keys matching `pattern`, can be `*` |
| `LOLWUT` | Returns Materia KV's version and might be hiding an easter egg 👀 |
| `MGET` | Returns the values of all specified keys. For every key that doesn't hold a string value or doesn't exist, the special value `nil` is returned. Because of this, the operation never fails. |
| `MSET` | Sets the given keys to their respective values. `MSET` replaces existing values with new values, just as regular `SET`. `MSET` is atomic, so all given keys are set at once. It is not possible for clients to see that some keys were updated while others are unchanged. |
| `PERSIST` | Remove the existing time to live associated with the `key`. |
| `PEXPIRE` | Set a `key` time to live in milliseconds. After the timeout has expired, the `key` will be automatically deleted.  The time to live can be updated using the `PEXPIRE` command or cleared using the `PERSIST` command. |
| `PING` | Returns `PONG` if no argument is provided, otherwise return a copy of the argument as a bulk. |
| `PTTL` | RReturns the remaining time to live of a `key`, in milliseconds. |
| `SCAN` | Incrementally iterate over a collection of elements. It is a cursor based iterator, this means that at every call of the command, the server returns an updated cursor that the user needs to use as the cursor argument in the next call. An iteration starts when the cursor is set to `0`, and terminates when the cursor returned by the server is `0`. |
| `SET` | Set `key` to hold the string `value`. If key already holds a value, it is overwritten, regardless of its type. |
| `SETBIT` | Sets or clears the bit at offset in the string value stored at `key`. |
| `STRLEN` | Returns the length of the string value stored at `key`. An error is returned when key holds a non-string value. |
| `TTL` | Returns the remaining time to live of a `key`, in seconds. |
| `TYPE` | Returns the string representation of the type of the value stored at `key`. Can be: `hash`, `list` or `string`. |

### JSON commands

Materia KV provides preliminary support for JSON data type operations, compatible with Redis API JSON commands and clients. Unlike Redis JSON which uses a dedicated data type, our implementation works directly with classic string data types while maintaining API compatibility.

#### Path Syntax and Behavior
- `$`: Root element (required for setting values, optional for `GET`/`DEL`)
- `$.field`: Access field in object
- `$..field`: Recursively search for all matching fields
- `$.array[index]`: Access array element by index
- `.field`: Shorthand notation (without `$`) returns a direct value instead of an array wrapper

#### Examples

```bash
# Setting and getting JSON
> JSON.SET myJsonKey $ '{"a":"23"}'
OK
> JSON.GET myJsonKey
"{\"a\":\"23\"}"
> JSON.GET myJsonKey $
"[{\"a\":\"23\"}]"
> JSON.GET myJsonKey $.a
"[\"23\"]"

# Multiple paths with different notations
> JSON.SET myJsonKey $ '{"f1":{"k1":["foo",42],"k2":["bar",53]},"f2":{"k1":["Hello",61]}}'
OK
> JSON.GET myJsonKey $.f1 $.f2
"{\"$.f1\":[{\"k1\":[\"foo\",42],\"k2\":[\"bar\",53]}],\"$.f2\":[{\"k1\":[\"Hello\",61]}]}"
> JSON.GET myJsonKey .f1 .f2
"{\".f1\":{\"k1\":[\"foo\",42],\"k2\":[\"bar\",53]},\".f2\":{\"k1\":[\"Hello\",61]}}"

# Recursive search
> JSON.GET myJsonKey $..k1
"[[\"foo\",42],[\"Hello\",61]]"

# Array manipulation
> JSON.SET myJsonKey $ '{"a":[1,2,3,4]}'
OK
> JSON.DEL myJsonKey $.a[1]
(integer) 1
> JSON.GET myJsonKey
"{\"a\":[1,3,4]}"
```

#### Current Limitations
- `JSON.SET` can only create new documents at root path (`$`)
- `JSON.SET` can't create new fields in existing documents
- Nested path creation is not supported (e.g., `$.new.child.field`)
- Keys in your JSON must not contains characters like `..`, `*`, `[?(`
