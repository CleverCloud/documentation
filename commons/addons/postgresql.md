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

- on shared plans (DEV and S) : PostgreSQL 9.2.8
- on newly created dedicated databases (plans M and above) : Postgresql 9.6.1

## PostgreSQL plans

<table class="table table-bordered table-striped dataTable"><caption>PostgreSQL pricing plans</caption>
<tr>
<th>Name</th>
<th>Memory</th>
<th>DB size</th>
<th>Conn. limit</th>
<th>Price /mo</th>
</tr>
<tr>
<td class="cc-col__price"><span class="label cc-label__price label-info">DEV</span></td>
<td>SHARED</td>
<td>256 MB</td>
<td>5</td>
<td>Free</td>
</tr>
<tr>
<td class="cc-col__price"><span class="label cc-label__price label-info">S</span></td>
<td>SHARED</td>
<td>1 GB</td>
<td>10</td>
<td>10 €</td>
</tr>
<tr>
<td class="cc-col__price"><span class="label cc-label__price label-info">M</span></td>
<td>1 GB</td>
<td>100 GB</td>
<td>75</td>
<td>30 €</td>
</tr>
<tr>
<td class="cc-col__price"><span class="label cc-label__price label-info">L</span></td>
<td>8 GB</td>
<td>450 GB</td>
<td>500</td>
<td>240 €</td>
</tr>
<tr>
<td class="cc-col__price"><span class="label cc-label__price label-info">XL</span></td>
<td>32 GB</td>
<td>600 GB</td>
<td>1000</td>
<td>700 €</td>
</tr>
</table>

## Migrating from an old database

Some applications require a populated database to run properly.
If you want to import your **SQL** dump, you can use several methods:

1. [Our WebGUI (Adminer)](https://dbms-adminer.clever-cloud.com/adminer/).
2. Command line tool for PostgreSQL administration like `psql`.
3. Any PostgreSQL client such as [pgAdmin](http://www.pgadmin.org/).
