---
type: docs
title: Roles and Organizations
weight: 4
shortdesc: Managing users and roles in organizations
tags:
- dashboard-setup
keyworkds:
- roles
- users
- accounts
- organizations
- organizations
- collaboration
---

In order to improve team collaboration between developers, accountants, managers and admins, we have introduced organizations. Each organization has its own billing, leaning that you can create as much as orgnanization you'd like. Most use-cases include the billing separation of private and business applications, several businesses or business units (within one company, for instance).

Once you create an organization, you can add collaborators and assign them [roles](#roles-and-privileges) which gives them rights.

Each organization have its own identifier looking like `orga_xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`.


## Add an organization

Organization names are unique. It means that you cannot use an already used organization name.

In order to add an organization, just click on "Add an organization" in the top left sidebar.


## Roles and privileges

The table below describes rights assigned to roles:

<table class="table table-condensed table-bordered table-hover text-center">
	<thead>
		<tr>
			<th> </th>
			<th class="text-center">Admin</th>
			<th class="text-center">Manager</th>
			<th class="text-center">Developer</th>
			<th class="text-center">Accountant</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<th scope="row">Add Member</th>
			<td>x</td>
			<td>x</td>
			<td> </td>
			<td> </td>
		</tr>
		<tr>
			<th scope="row">Remove Member</th>
			<td>x</td>
			<td>x</td>
			<td> </td>
			<td> </td>
		</tr>
		<tr>
			<th scope="row">Add Application</th>
			<td>x</td>
			<td>x</td>
			<td>x</td>
			<td> </td>
		</tr>
		<tr>
			<th scope="row">Remove Application</th>
			<td>x</td>
			<td>x</td>
			<td> </td>
			<td> </td>
		</tr>
		<tr>
			<th scope="row">Add / Remove add-on</th>
			<td>x</td>
			<td>x</td>
			<td></td>
			<td> </td>
		</tr>
		<tr>
			<th scope="row">Edit Organization</th>
			<td>x</td>
			<td>x</td>
			<td> </td>
			<td> </td>
		</tr>
		<tr>
			<th scope="row">Delete Organization</th>
			<td>x</td>
			<td> </td>
			<td> </td>
			<td> </td>
		</tr>
		<tr>
			<th scope="row">Access Bills & Receive Invoices</th>
			<td>x</td>
			<td> </td>
			<td> </td>
			<td>x</td>
		</tr>
		<tr>
			<th scope="row">Access Repositories</th>
			<td>x</td>
			<td>x</td>
			<td>x</td>
			<td> </td>
		</tr>
	</tbody>
</table>
