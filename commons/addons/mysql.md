---
title: MySQL add-on
position: 6
shortdesc: MySQL is an open-source relational database management system (RDBMS).
tags:
- addons
keywords:
- sql
- mysql
- mariadb
- RDBMS
---

MySQL is an open-source relational database management system (RDBMS).

## MySQL version

The version currently installed by the add-on is :

- on shared plans (DEV and S) : MySQL 5.5.28
- on newly created dedicated databases (plans M and above) : MySQL 5.7.20

## MySQL plans

<div class="panel panel-warning">
  <div class="panel-heading">
    <h4 class="panel-title">Note for Shared databases</h4>
  </div>
  <div class="panel-body">
    As Shared databases (DEV and S plans) are shared between multiple applications and delays could appear in case of
  an high demand.<br />
  If this delays create problems in your application or are problematcs, we recommend you to use a dedicated database
  (M plans and above).
  </div>
</div>

<table class="table table-bordered table-striped dataTable"><caption>MySQL pricing plans</caption>
<tr>
<th>Name</th>
<th>Cache (Memory)</th>
<th>Disk</th>
<th>Conn. limit</th>
<th>Price /mo</th>
</tr>
<tr>
<td class="cc-col__price "><span class="label cc-label__price label-info">DEV</span></td>
<td>SHARED</td>
<td>10 MB</td>
<td>5</td>
<td>Free</td>
</tr>
<tr>
<td class="cc-col__price "><span class="label cc-label__price label-info">S</span></td>
<td>SHARED</td>
<td>256 MB</td>
<td>10</td>
<td>15 €</td>
</tr>
<tr>
<td class="cc-col__price "><span class="label cc-label__price label-info">M</span></td>
<td>1 GB</td>
<td>10 GB</td>
<td>75</td>
<td>45 €</td>
</tr>
<tr>
<td class="cc-col__price "><span class="label cc-label__price label-info">L</span></td>
<td>2 GB</td>
<td>200 GB</td>
<td>500</td>
<td>300 €</td>
</tr>
</table>

### Migrating from an old database

Some applications require a populated database to run properly.
If you want to import your **SQL** dump, you can use several methods:

1. [Our WebGUI (PHP My Admin)](https://dbms-pma.clever-cloud.com/).
2. Command line tool for MySQL administration.
3. Any MySQL client such as [MySQL Workbench](https://www.mysql.fr/products/workbench/).

If you need to import a very large dump, please send an email to <support@clever-cloud.com>.
