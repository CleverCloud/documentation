---
title: PostgreSQL add-on
position: 7
shortdesc: PostgreSQL is an open-source relational database management system (RDBMS).
tags:
- addons
keywords:
- sql
- postgresql
- pg
- pgsql
- mariadb
---

PostgreSQL is an object-relational database management system (ORDBMS) with an emphasis on extensibility
and on standards-compliance.

## PostgreSQL version

The version currently installed by the add-on is :

- on shared plans (DEV) : PostgreSQL 11.1
- on newly created dedicated databases (plans XS Small Space and above) : PostgreSQL 9.6, 10.4 or 11.1

## PostgreSQL plans

<table class="table table-bordered table-striped dataTable"><caption>PostgreSQL pricing plans</caption>
<tr>
<th>Name</th>
<th>Logs</th>
<th>DB size</th>
<th>Conn. limit</th>
<th>Memory</th>
<th>Type</th>
<th>VCPUS</th>
<th>Price /mo</th>
</tr>
<tr>
<td class="cc-col__price"><span class="label cc-label__price label-info">DEV</span></td>
<td>no</td>
<td>256 MB</td>
<td>5</td>
<td>Shared</td>
<td>Shared</td>
<td>Shared</td>
<td>Free</td>
</tr>
<tr>
<td class="cc-col__price"><span class="label cc-label__price label-info">XS Small Space</span></td>
<td>yes</td>
<td>5 GB</td>
<td>75</td>
<td>1 GB</td>
<td>Dedicated</td>
<td>1</td>
<td>17.50 €</td>
</tr>
<tr>
<td class="cc-col__price"><span class="label cc-label__price label-info">XS Medium Space</span></td>
<td>yes</td>
<td>10 GB</td>
<td>75</td>
<td>1 GB</td>
<td>Dedicated</td>
<td>1</td>
<td>20.00 €</td>
</tr>
<tr>
<td class="cc-col__price"><span class="label cc-label__price label-info">XS Big Space</span></td>
<td>yes</td>
<td>15 GB</td>
<td>75</td>
<td>1 GB</td>
<td>Dedicated</td>
<td>1</td>
<td>30.00 €</td>
</tr>
<tr>
<td class="cc-col__price"><span class="label cc-label__price label-info">S Small Space</span></td>
<td>yes</td>
<td>10 GB</td>
<td>125</td>
<td>2 GB</td>
<td>Dedicated</td>
<td>2</td>
<td>35.00 €</td>
</tr>
<tr>
<td class="cc-col__price"><span class="label cc-label__price label-info">S Medium Space</span></td>
<td>yes</td>
<td>15 GB</td>
<td>125</td>
<td>2 GB</td>
<td>Dedicated</td>
<td>2</td>
<td>37.50 €</td>
</tr>
<tr>
<td class="cc-col__price"><span class="label cc-label__price label-info">S Big Space</span></td>
<td>yes</td>
<td>20 GB</td>
<td>125</td>
<td>2 GB</td>
<td>Dedicated</td>
<td>2</td>
<td>40.00 €</td>
</tr>
<tr>
<td class="cc-col__price"><span class="label cc-label__price label-info">M Small Space</span></td>
<td>yes</td>
<td>20 GB</td>
<td>250</td>
<td>4 GB</td>
<td>Dedicated</td>
<td>4</td>
<td>82.00 €</td>
</tr>
<tr>
<td class="cc-col__price"><span class="label cc-label__price label-info">M Medium Space</span></td>
<td>yes</td>
<td>40 GB</td>
<td>250</td>
<td>4 GB</td>
<td>Dedicated</td>
<td>4</td>
<td>92.00 €</td>
</tr>
<tr>
<td class="cc-col__price"><span class="label cc-label__price label-info">M Big Space</span></td>
<td>yes</td>
<td>80 GB</td>
<td>250</td>
<td>4 GB</td>
<td>Dedicated</td>
<td>4</td>
<td>112.00 €</td>
</tr>
<tr>
<td class="cc-col__price"><span class="label cc-label__price label-info">L Small Space</span></td>
<td>yes</td>
<td>40 GB</td>
<td>500</td>
<td>8 GB</td>
<td>Dedicated</td>
<td>6</td>
<td>164.00 €</td>
</tr>
<tr>
<td class="cc-col__price"><span class="label cc-label__price label-info">L Medium Space</span></td>
<td>yes</td>
<td>80 GB</td>
<td>500</td>
<td>8 GB</td>
<td>Dedicated</td>
<td>6</td>
<td>184.00 €</td>
</tr>
<tr>
<td class="cc-col__price"><span class="label cc-label__price label-info">L Big Space</span></td>
<td>yes</td>
<td>120 GB</td>
<td>500</td>
<td>8 GB</td>
<td>Dedicated</td>
<td>6</td>
<td>204.00 €</td>
</tr>
<tr>
<td class="cc-col__price"><span class="label cc-label__price label-info">XL Small Space</span></td>
<td>yes</td>
<td>80 GB</td>
<td>750</td>
<td>16 GB</td>
<td>Dedicated</td>
<td>8</td>
<td>328.00 €</td>
</tr>
<tr>
<td class="cc-col__price"><span class="label cc-label__price label-info">XL Medium Space</span></td>
<td>yes</td>
<td>160 GB</td>
<td>750</td>
<td>16 GB</td>
<td>Dedicated</td>
<td>8</td>
<td>368.00 €</td>
</tr>
<tr>
<td class="cc-col__price"><span class="label cc-label__price label-info">XL Big Space</span></td>
<td>yes</td>
<td>320 GB</td>
<td>750</td>
<td>16 GB</td>
<td>Dedicated</td>
<td>8</td>
<td>448.00 €</td>
</tr>
<tr>
<td class="cc-col__price"><span class="label cc-label__price label-info">XXL Small Space</span></td>
<td>yes</td>
<td>160 GB</td>
<td>900</td>
<td>32 GB</td>
<td>Dedicated</td>
<td>10</td>
<td>796.00 €</td>
</tr>
<tr>
<td class="cc-col__price"><span class="label cc-label__price label-info">XXL Medium Space</span></td>
<td>yes</td>
<td>320 GB</td>
<td>900</td>
<td>32 GB</td>
<td>Dedicated</td>
<td>10</td>
<td>892.00 €</td>
</tr>
<tr>
<td class="cc-col__price"><span class="label cc-label__price label-info">XXL Big Space</span></td>
<td>yes</td>
<td>640 GB</td>
<td>900</td>
<td>32 GB</td>
<td>Dedicated</td>
<td>10</td>
<td>1084.00 €</td>
</tr>
<tr>
<td class="cc-col__price"><span class="label cc-label__price label-info">XXL Huge Space</span></td>
<td>yes</td>
<td>960 GB</td>
<td>900</td>
<td>32 GB</td>
<td>Dedicated</td>
<td>10</td>
<td>1276.00 €</td>
</tr>
<tr>
<td class="cc-col__price"><span class="label cc-label__price label-info">XXXL Small Space</span></td>
<td>yes</td>
<td>640 GB</td>
<td>1200</td>
<td>64 GB</td>
<td>Dedicated</td>
<td>12</td>
<td>1598.00 €</td>
</tr>
<tr>
<td class="cc-col__price"><span class="label cc-label__price label-info">XXXL Medium Space</span></td>
<td>yes</td>
<td>960 GB</td>
<td>1200</td>
<td>64 GB</td>
<td>Dedicated</td>
<td>12</td>
<td>1822.00 €</td>
</tr>
<tr>
<td class="cc-col__price"><span class="label cc-label__price label-info">XXXL Big Space</span></td>
<td>yes</td>
<td>1200 GB</td>
<td>1200</td>
<td>64 GB</td>
<td>Dedicated</td>
<td>12</td>
<td>1990.00 €</td>
</tr>
</table>

## Migrating from an old database

Some applications require a populated database to run properly.
If you want to import your **SQL** dump, you can use several methods:

1. [Our WebGUI (Adminer)](https://dbms-adminer.clever-cloud.com/).
2. Command line tool for PostgreSQL administration like `psql`.
3. Any PostgreSQL client such as [pgAdmin](http://www.pgadmin.org/).

## Direct access

All our dedicated PostgreSQL databases are served via a proxy. To reduce the latency you can bypass this proxy by generating direct hostname and port for the addon. You can do it by clicking the "Generate direct hostname and port" on the addon dashboard.

This action will add new environment variables to reach the addon without any proxy.

Keep in mind that usage of direct access is a trade-off: when you migrate your addon, you will need to to generate hostname and port again so your application must update these environment while proxy usage changes nothing.

## Default extensions

Every PostgreSQL database mananged by Clever Cloud comes with the following default extensions:
`adminpack`,
`autoinc`,
`btree_gin`,
`btree_gist`,
`citext`,
`cube`,
`dblink`,
`dict_int`,
`dict_xsyn`,
`earthdistance`,
`file_fdw`,
`fuzzystrmatch`,
`hstore`,
`insert_username`,
`intagg`,
`intarray`,
`isn`,
`lo`,
`ltree`,
`moddatetime`,
`pageinspect`,
`pg_buffercache`,
`pgcrypto`,
`pg_freespacemap`,
`pgrowlocks`,
`pg_stat_statements`,
`pgstattuple`,
`pg_trgm`,
`plcoffee`,
`plls`,
`plv8`,
`postgis`,
`postgis_tiger_geocoder`,
`postgis_topology`
`postgres_fdw`,
`refint`,
`seg`,
`sslinfo`,
`tablefunc`,
`tcn`,
`timetravel`,
`unaccent`,
`"uuid-ossp"`,
`xml2`

## Encryption at rest

PostgreSQL dedicated addons can be encrypted using LUKS with `aes-xts`.

The passphrase is encrypted in our database using Cipher and Nonce as bytes arrays.

To enable it, you need to ask to our support then we will perform invoicing configuration (more informations about pricing are available through support) and enable the encryption for your addon. Once it's done, you will need to migrate your addon then the encryption at rest will be up.
