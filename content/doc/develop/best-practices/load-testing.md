---
type: docs
linkTitle: Load testing
title: Load testing
description: Prepare and run a load test of your Clever Cloud application, watch its metrics and autoscaling, and pick a load testing tool
keywords:
- load testing
- stress testing
- performance
- autoscaling
- metrics
- k6
aliases:
- /doc/best-practices/load-testing
- /doc/develop/load-testing
---

A load test sends many requests to your application to measure how it behaves under heavy traffic: how many requests it serves, with which response time, and where it breaks. Run one before a launch or an expected peak, to size your instances and your add-ons.

## Prepare the test

Test a staging application rather than production, with the same runtime and [scaling](/doc/manage/scaling/). Give it its own add-ons, with the same plans and representative data: a test on the production add-ons loads and modifies them.

The public load balancers are shared between customers: a heavy load from a few addresses looks like an attack, and the network protection can block it. [Contact the Support](https://console.clever-cloud.com/ticket-center-choice) before the test, with its date, its duration, the expected request rate, and the target domain.

With a [dedicated load balancer](/doc/network/load-balancers/), the load stays on it, but it also affects the other applications behind this load balancer.

## Define the test

Choose the requests that matter, such as the journey of a user who browses, searches, then orders, and a load close to the one you expect. Set success criteria before the test: the response time most users must get, the error rate you accept, and the request rate to reach. The test then tells you whether your application meets them, rather than only where it breaks.

## Watch the application

Follow the test from the [metrics](/doc/develop/observability/metrics/) and the [access logs](/doc/develop/observability/access-logs/) of your application: CPU and memory of the instances, response times, and status codes.

- Autoscaling reacts after a few minutes of sustained load: increase the load gradually, and watch `UPSCALE` in the [activity](/doc/develop/observability/activity/)
- Code on a single thread uses one vCPU per process: see [both ranges](/doc/manage/scaling/#both-ranges) to use all of them
- Each instance opens its own connections to your add-ons: check that the connection limit of their plan covers all your instances
- The load balancer applies a [180-second timeout](/doc/find-help/troubleshooting/) to the operations of your application

## Act on the results

Find what limits your application first: its code, such as a slow query, the size or the number of its instances, or the plan of an add-on. Change one thing, then run the same test again to compare the results.

## Load testing tools

To send many requests to a single URL, a command-line tool such as [hey](https://github.com/rakyll/hey) or [oha](https://github.com/hatoo/oha) is enough.

To script user journeys, use [k6](https://github.com/grafana/k6), [Gatling](https://gatling.io), [Locust](https://locust.io), [JMeter](https://jmeter.apache.org), or [Drill](https://github.com/fcsonline/drill), which run on your workstation or your own servers.

Online services run the test for you, from their own servers: [Grafana Cloud k6](https://grafana.com/docs/k6/latest/), [Loader.io](https://loader.io), or [OctoPerf](https://octoperf.com).
