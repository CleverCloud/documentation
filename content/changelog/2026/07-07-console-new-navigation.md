---
title: The Console gets a new navigation, search bar, and homepage
description: A new sidebar groups your resources by type or project, a global search bar and keyboard shortcuts get you anywhere, themes change the colors of the Console, and a new homepage helps you get started
date: 2026-07-07
tags:
  - console
  - navigation
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

The [Clever Cloud Console](https://console.clever-cloud.com) gets a new navigation. A sidebar lists the resources of your organisation, a header shows where you are, and tabs reach every page of the current application or add-on. A global search bar and keyboard shortcuts help you move faster, and a new homepage welcomes you when you log in.

## Sidebar and projects

The sidebar holds the organisation switcher, the button to create a resource, and a filter. It groups resources in collapsible sections: applications, add-ons, Kubernetes clusters, Network Groups, OAuth consumers, and add-on providers. Archived applications get their own section. The filter matches names and IDs, and keywords such as `is:app`, `is:addon`, `is:cke`, `is:node`, or `is:running` narrow the list by type, product, or status.

To group resources by project rather than by type, add a `project:` tag to your applications and add-ons, such as `project:billing`. They then move to a section named after the project. You can edit the tags of an application from its information page, and those of an add-on from its settings.

At the top of each page, the header shows the name and ID of the resource, ready to copy. Its menu leads to support, documentation, changelog, your profile, and logout. Below it, tabs list the pages of the resource, such as overview, logs, metrics, or domain names. The ones that don't fit move to an overflow menu.

## Search and keyboard shortcuts

Press `/` to open the search bar. It finds resources of the current organisation and of the other ones, organisations, and Console pages, and offers shortcuts to the main documentation pages. It understands the same `is:` keywords as the sidebar filter, so `is:app is:running` lists the running applications of the current organisation.

Press `?` to list every keyboard shortcut. Single keys jump to a page of the current application or add-on, such as `l` for logs, `m` for metrics, `e` for environment variables, or `d` for domain names. `<` and `>` collapse or expand the sidebar.

## Themes

The Console comes with several color themes. Aurora is the default, and you can pick Nebula, Horizon, Ember, Clarity, or Cobalt from the [Labs](https://console.clever-cloud.com/users/me/feature-list) page of your profile menu. Press `Alt+T` to cycle through them, `Alt+Shift+T` to go backwards.

## A new homepage

The homepage adapts to your account. Cards guide new users through their first steps: deploy a resource, install [Clever Tools](/doc/manage/cli/), add a payment method or an SSH key, enable two-factor authentication. It also offers ready-to-deploy templates, a short video, and the latest news, and links to the documentation of each runtime.

- [Share your feedback on the Console](https://github.com/CleverCloud/Community/discussions/categories/console)
