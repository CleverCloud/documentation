---
type: docs
title: MateriaDB KV
description: MateriaDB KV is a key-value database service based on our serverless offer MateriaDB
tags:
- addons
keywords:
- KV
- redis
type: docs
draft: false
---


{{< hextra/hero-subtitle >}}
  
MateriaDB KV is a key-value database service based on Clever Cloud serverless offer MateriaDB.

MateriaDB KV features compatibility layers allowing you to communicate with the database using well known and widely used protocols, SDKs, and clients. The first layer is compatible with Redis (and its variants as Reddict or Valkey) clients and SDKs.

{{< /hextra/hero-subtitle >}}

{{< callout type="warning" >}}

**MateriaDB KV is an alpha stage product.** At Clever Cloud, we're really excited to introduce you to MateriaDB KV, currently in its alpha stage. As we fine-tune and enhance its capabilities, we invite you to join us in testing and providing valuable feedback. While MateriaDB KV holds immense potential, we advise against using the alpha release for production purposes. During this alpha phase, **all data stored within MateriaDB KV may be subject to wiping**. Your insights and suggestions are crucial in shaping the future of this platform. To share your feedback, please visit us at [our MAteriaDB community page](https://github.com/CleverCloud/Community/discussions/categories/materiadb). Thank you for being a part of our journey towards innovation and improvement!

{{< /callout >}}

## Creating a MateriaDB KV database

You can use the Clever CLI to create your MateriaDB KV add-on: `clever addon create kv DATABASE_NAME`

Then you can set the environment variables you need to connect to your MateriaDB KV, `source <(clever addon env addon ADDON_ID -F shell)`.

Example:

```
$ clever addon create kv test

Add-on created successfully!
ID: addon_4997cfe3-f104-4d05-9fe4-xxxxxxxxx
Real ID: kv_01HV6NCSRD1TV2AJW4RKFBJ07R
Name: test

/!\ The MateriaDB KV provider is in Alpha testing phase, don't store sensitive or production grade data
You can easily use MateriaDB KV with 'redis-cli', with such commands:
source <(clever addon env addon_4997cfe3-f104-4d05-9fe4-xxxxxxxxx -F shell)
redis-cli -h $KV_HOST -p $KV_PORT
```

## Setting the environment variables

In order to connect to your MateriaDB KV addon, you need 3 parameters: the host, the port and a biscuit token. 
As explained in the response to the creation command, you can set these parameters as environment variables by doing `source <(clever addon env addon <ADDON_ID> -F shell)`. The variables set are:

- `$KV_HOST` and its alias `$REDIS_HOST`
- `$KV_PORT` and its alias `$REDIS_PORT`
- `KV_TOKEN` and its alias `$REDISCLI_AUTH`

## Using the Redis layer 

### Redis-cli usage

You can directly use the environement variables to connect to MateriaDB KV using `redis-cli`:

```bash
redis-cli -h $KV_HOST -p $KV_PORT --tls
```

### GUI usage

We have tested the compatibilitywith some of the most popular Redis GUI:

- [Redis Insight](https://redis.com/redis-enterprise/redis-insight/)

- [Another Redis Desktop Client](https://goanother.com/)

- [Redis Commander](https://github.com/joeferner/redis-commander)

- [PX3 Redis UI](https://github.com/patrikx3/redis-ui)

- [Qredis](https://github.com/tiagocoutinho/qredis)

In all these GUI, for the authentication, leave the user empty and use as password the value of `$REDISCLI_AUTH`. 

Most other Redis GUI should also work.


### Supported types

During this alpha stage, please note that we don't provide 100% compatibility with the Redis value types. Currently supported value types are:

- String
- List
- Hash


### Supported commands

During this alpha stage, please note that we don't provide 100% compatibility with the Redis API. Here you have the list of we currently supported commands:

- `APPEND`: If `key` already exists and is a string, this command appends the value at the end of the string. If `key` does not exist it is created and set as an empty string, so `APPEND` will be similar to `SET` in this special case.

- `AUTH`: Authenticate the current connection using the biscuit token as `password`

- `CLUSTER INFO`: Indicates that cluster support is disabled, i.e. MateriaDB KV is naturally distributed and doesn't support or needs Redis clustering.

- `COMMAND`: Return an array with details about every supported command.

- `DBSIZE`: Return the number of keys in the currently-selected database.

- `DECR`: Decrements the number stored at `key` by one. If the `key` does not exist, it is set to 0 before performing the operation. An error is returned if `key` contains a value of the wrong type or contains a string that can not be represented as integer. This operation is limited to 64 bit signed integers.

- `DEL` : Removes the specified `key`. A key is ignored if it does not exist.

- `EXIST`: Returns if `key` exists.

- `GET` : Get the value of key. If the key does not exist the special value nil is returned. An error is returned if the value stored at key is not a string, because `GET` only handles string values.

- `GETRANGE`: Returns the substring of the string value stored at key, determined by the offsets start and end (both are inclusive). Negative offsets can be used in order to provide an offset starting from the end of the string. So -1 means the last character, -2 the penultimate and so forth.

The function handles out of range requests by limiting the resulting range to the actual length of the string.

- `FLUSHDB`: Delete all the keys of the currently selected DB. This command never fails. Currently we only support the synchronous mode of `FLUSHDB`.

- `HGET`: Returns the values associated with the specified fields in the hash stored at `key`. For every field that does not exist in the hash, a `nil` value is returned. Because non-existing keys are treated as empty hashes, running `HMGET` against a non-existing `key` will return a list of nil values.

- `HMSET`: Sets the specified fields to their respective values in the hash stored at `key`. This command overwrites any specified fields already existing in the hash. If `key` does not exist, a new key holding a hash is created.

- `HSCAN`: Incrementally iterate over fields of Hash types and their associated values. It is a cursor based iterator, this means that at every call of the command, the server returns an updated cursor that the user needs to use as the cursor argument in the next call. An iteration starts when the cursor is set to 0, and terminates when the cursor returned by the server is 0.

- `INCR`: Increments the number stored at `key` by one. If the `key` does not exist, it is set to 0 before performing the operation. An error is returned if `key` contains a value of the wrong type or contains a string that can not be represented as integer. This operation is limited to 64 bit signed integers.

- `KEYS`: Returns all keys matching `pattern`.

- `LLEN`: Returns the length of the list stored at `key`. If `key` does not exist, it is interpreted as an empty list and 0 is returned. An error is returned when the value stored at `key` is not a list.

- `LPOP`: Removes and returns the first elements of the list stored at `key`.

- `LPUSH`: Insert all the specified values at the head of the list stored at `key`. If `key` does not exist, it is created as empty list before performing the push operations. When `key` holds a value that is not a list, an error is returned.

- `LPUSHX`: Inserts specified values at the head of the list stored at `key`, only if `key` already exists and holds a list. In contrary to `LPUSH`, no operation will be performed when `key` does not yet exist.

- `LRANGE`: Returns the specified elements of the list stored at `key`. The offsets `start` and `stop` are zero-based indexes, with 0 being the first element of the list (the head of the list), 1 being the next element and so on. These offsets can also be negative numbers indicating offsets starting at the end of the list. For example, -1 is the last element of the list, -2 the penultimate, and so on.

- `LSET`: Sets the list element at `index` to `element`.

- `MEMORY USAGE`: The `MEMORY USAGE` command reports the number of bytes that a key and its value require to be stored in RAM.

- `MGET`: Returns the values of all specified keys. For every key that does not hold a string value or does not exist, the special value `nil` is returned. Because of this, the operation never fails.

- `MSET`: Sets the given keys to their respective values. `MSET` replaces existing values with new values, just as regular `SET`. `MSET` is atomic, so all given keys are set at once. It is not possible for clients to see that some of the keys were updated while others are unchanged.

- `PING`: Returns `PONG` if no argument is provided, otherwise return a copy of the argument as a bulk.

- `RPOP`: Removes and returns the last elements of the list stored at `key`. By default, the command pops a single element from the end of the list. When provided with the optional count argument, the reply will consist of up to count elements, depending on the list's length.

- `RPUSH`: Insert all the specified values at the tail of the list stored at `key`. If `key` does not exist, it is created as empty list before performing the push operation. When `key` holds a value that is not a list, an error is returned.

- `RPUSHX`: Inserts specified values at the tail of the list stored at `key`, only if `key` already exists and holds a list. In contrary to `RPUSH`, no operation will be performed when `key` does not yet exist.

- `SCAN`: Incrementally iterate over a collection of elements. It is a cursor based iterator, this means that at every call of the command, the server returns an updated cursor that the user needs to use as the cursor argument in the next call. An iteration starts when the cursor is set to 0, and terminates when the cursor returned by the server is 0.

- `SET`: Set `key` to hold the string `value`. If `key` already holds a value, it is overwritten, regardless of its type. Value length is currently limited to 1 kb.

- `STRLEN`: Returns the length of the string value stored at `key`. An error is returned when key holds a non-string value.

- `TTL`: Returns the remaining time to live of a key that has a timeout. During the alpha phase, key timeouts aren't implemented. Nevertheless, for compatibility reasons, we support the `TTL` command. The command returns -2 if the key does not exist, it returns -1 if the key exists with no defined timeout.

- `TYPE`: Returns the string representation of the type of the value stored at `key`. The different types that can be returned are: `string`, `list` and `hash`.
