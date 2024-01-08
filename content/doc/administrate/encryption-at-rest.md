---
type: docs
title: Encryption at rest
tags:
- encryption
- rest
- security
type: docs
---

## Introduction

Encrypting your data at rest provides another security layer to protect your data from various security threats. By default and unless you implemented it in your code, the data stored on disk is not encrypted. Enabling encryption at rest allows you to make sure your data can't be read by anyone having a physical access to the hard drive.

Encryption at rest only protects the data "at rest", meaning that if your data is sent over an unencrypted channel on the network, it could be read on the fly. The scenario encryption at rest covers are mostly hard drives stealing or unauthorized access once the hard drive got removed.

Here at Clever Cloud, before removing a hard drive, either because it is faulty or not used anymore, we first [shred](https://linux.die.net/man/1/shred) the hard drive with multiple passes. Then it is physically damaged by the data center operators before being thrown away. If one of those steps are missing or fail for some reason, your data could still be read if you didn't use encryption at rest. If you did, no one will be able to access it.

## Technical details

Encryption at rest works by decrypting the encrypted data disk and exposing it to the system in an unencrypted volume. Each time you read data on this unencrypted volume, the system will fetch the data on the encrypted disk and decrypt it. If you write data, the opposite happens: the data to be written is encrypted and then its encrypted content is written to the encrypted disk.

Each add-on has a randomly generated encryption key used to encrypt the data disk. The key will stay the same during the add-on life but can be changed if needed. In that case, a migration will use the new passphrase.

We use the [cryptsetup tool](https://gitlab.com/cryptsetup/cryptsetup) to operate encrypted disks. Cryptsetup's current default is [LUKS2](https://gitlab.com/cryptsetup/LUKS2-docs) with `aes-xts` as the encryption algorithm. This may be subject to change as cryptsetup and the security algorithms evolve.

The encryption key is only stored encrypted on our systems and is not stored on your add-on. When your add-on boots, the key is downloaded over HTTPS from our systems and the disk is then mounted.

We also have a small swap partition on add-ons to allow more available RAM for background services. This swap file is also encrypted to avoid any encrypted data leak.

### Performances

Performances may be a bit degraded with encryption enabled but in most of the cases under regular load, it is usually insignificant and an acceptable tradeoff.

Also, depending on whether you are using a single vCPU add-on or a multiple vCPU one, numbers can greatly vary. Single vCPU instances will switch between decrypting/encrypting the data and reading/writing it to the disk while multiple vCPU instances will be able to parallelize those operations, leading to better performance.

Note that most of the databases either have an in-memory cache or use the system's file cache so if the same data is often read, it may be available in the cache and no decryption occur leading to fast reads.

Those tests were made using a 4 vCPU instance with 4 GiB of RAM.
Before each test, the system's cache was dropped to avoid having reads that are faster than they should be: `sync; echo 1 > /proc/sys/vm/drop_caches`.

Note: The `dd` tool wasn't used for this benchmark as it does not represent a valid workload, leading to results that can greatly vary depending on disk performance.

#### Using pgbench for PostgreSQL

Using `pgbench` with 20 jobs and 20 clients, we see a difference between 3% and 5% less transactions per second on the encrypted disk and no real CPU difference.

With encrypted disk, the number of transactions per second was 315. On the unencrypted one, it was 330 per second.

#### Using sysbench for MySQL

Using `sysbench` with 6 threads, the difference is between 5% and 10% less transactions per second. The CPU usage is also between 5% and 10% higher depending on the work load (reads or writes).

With encrypted disk, the number of transactions per second was 635. On the unencrypted one, it was 703 per second.

## Availability

Encryption at rest is currently available for the following add-ons:

- PostgreSQL
- MySQL
- MongoDB
- Redis
- Elastic Stack
- Jenkins

Only dedicated add-ons have the option. If your add-on is not encrypted, you can ask our support team to configure it. A migration will then be needed to encrypt your disk.
