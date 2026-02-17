---
type: docs
linkTitle: Otoroshi Advanced Features
title: Otoroshi Advanced Features Guide
description: Configure and use Otoroshi advanced features including WAF, Reverse Proxy, Rate Limiting, and Canary Deployments with detailed tutorials and best practices
keywords:
- otoroshi
- api gateway
- waf
- reverse proxy
- canary deployment
- rate limiting
- load balancing
---

Otoroshi is a modern API Gateway that provides powerful features to secure, manage, and optimize your services. 

This guide covers the main features tested and validated for deployment on Clever Cloud.

---

## WAF (Web Application Firewall)

Otoroshi integrates **Coraza**, an open-source WAF compatible with ModSecurity rules and compliant with OWASP recommendations. It filters and blocks malicious requests before they reach your applications.

### Configuration

#### Step 1: Create a WAF Item

1. Navigate to **Categories → WAF → WAF Config**
2. Click **Add item**
3. Add your security directives

#### Example Directives

```
SecDefaultAction "phase:2,deny,status:403,log,auditlog"
SecRule REMOTE_ADDR "@ip xxxxxxxxxxxxx" "id:1001,phase:1,deny,msg:'Blocking IP xxxxxxxxxxxxxxxxxxxxxx'"
SecRule ARGS "@rx attack1" "phase:2,id:102,deny,status:403,log"

```

**Directive Explanations:**

- **SecDefaultAction**: Default action that blocks the request (`deny`), returns a 403 error, logs the event, and records the complete transaction in the audit module
- **SecRule REMOTE_ADDR**: Rule applied in phase 1 (header analysis) that blocks a specific IP address
- **SecRule ARGS**: Rule applied in phase 2 (GET/POST parameters analysis) that detects an attack pattern in arguments

#### Step 2: Create and Configure a Route

1. Navigate to **Shortcuts → Routes → Create new route**
2. Configure the **Frontend** (public entry point):
   - Public URL used by your clients (set on Otoroshi addon)
3. Configure the **Backend** (actual service):
   - Internal URL of your application that will process requests (set on your application)
4. Add the **WAF** in the "Plugins" section

{{< callout type="info" >}}
The frontend DNS must point to Otoroshi, not directly to your application. The backend URL is used by Otoroshi to proxy requests after applying WAF rules.
{{< /callout >}}

---
## Reverse Proxy

### Overview

Otoroshi natively supports multiple protocols:

- **HTTP/HTTPS**: Standard web requests
- **TCP**: Raw TCP connections (databases, custom services)
- **gRPC**: Modern RPC protocol based on HTTP/2

### Configuring a Simple Reverse Proxy

Otoroshi's versatile protocol support allows it to act as a reverse proxy for various types of services:

1. **Create a route** in Otoroshi
2. **Configure the Frontend**:
   - Public hostname, port, and path (set on Otoroshi addon)
3. **Configure the Backend**:
   - IP + port or URL of your actual service (set on your application)

Otoroshi intercepts incoming requests, applies your rules (security, rate limiting, etc.), and forwards them to the backend.

**Use Cases:**
- Proxy HTTP/HTTPS requests to web applications
- Forward TCP connections to databases or custom services
- Route gRPC calls to microservices

### Frontend vs Backend

**Frontend**: The public entry point that clients use to access your service. This is the URL your users will call.

**Backend**: The actual internal address of your application/service that processes requests. Otoroshi proxies requests to this address after filtering through WAF and other plugins.

{{< callout type="info" >}}
Your DNS must point the frontend domain to Otoroshi, not to your backend application. The backend URL is used internally by Otoroshi to forward filtered traffic.
{{< /callout >}}

---

## Rate Limiting & Custom Quotas

### Overview

Rate limiting protects your services from abuse by controlling the number of requests allowed per time period. Otoroshi provides flexible quota management based on various criteria.

### Implementation

To limit the number of requests per IP or per user:

1. Navigate to your route's configuration
2. Add the **"Custom quotas"** plugin in the "Plugins" section
3. Configure the following parameters:
   - **Quota**: Number of authorized requests
   - **Period**: Time window (per second, minute, hour, day)
   - **Criteria**: IP address, API key, user, etc.

**Common Use Cases:**
- Protect your APIs against abuse and brute force attacks
- Manage differentiated quotas for commercial tiers
- Mitigate DDoS attempts
- Implement fair usage policies (free vs paid tiers)

### Configuration Example

```json
{
  "throttling_quota": "1000",
  "throttling_period": "3600",
  "throttling_by": "ip"
}
```

This configuration allows **1000 requests per hour per IP address**.

### Additional Options

You can customize rate limiting based on:
- **IP address**: Limit per visitor
- **API key**: Different quotas per client
- **User**: Authenticated user limits
- **Custom header**: Advanced filtering

---

## Canary Deployments

Canary mode allows you to test a new version of your application on a percentage of traffic before a complete deployment. This technique reduces risk by gradually exposing new code to production users.

### Method 1: Route-Level Configuration with Plugin (Recommended)

This method provides more granular control and is easier to configure for single routes.

#### Configuration Steps

1. **Create a new route**
2. **Select the "Canary Mode" plugin**
3. **Configure the following parameters**:
    - **Frontend**: Public URL (set on Otoroshi addon)
    - **Canary mode**:
        - **Traffic**: 0.2 for 20% redirection to canary (or 0.5 for 50%)
        - **Targets**:
            - Hostname: `app-canary.cleverapps.io`
            - Port: `443`
            - Weight: `1`
    - **Backend**: Stable application URL (e.g., `app-stable.cleverapps.io`)

#### Complete Test Script

```sh
#!/bin/bash

echo "=== Otoroshi Canary Mode Test ==="
echo "Date: $(date)"
echo ""

STABLE=0
CANARY=0
UNKNOWN=0

# Replace with your actual Otoroshi frontend URL
FRONTEND_URL="http://myapp.mydomain.com"

for i in {1..100}; do
  RESPONSE=$(curl -L -s "$FRONTEND_URL")

  if echo "$RESPONSE" | grep -q "STABLE"; then
    ((STABLE++))
  elif echo "$RESPONSE" | grep -q "CANARY"; then
    ((CANARY++))
  else
    ((UNKNOWN++))
  fi

  echo -n "."
done

echo ""
echo ""
echo "Results over 100 requests:"
echo "  → Stable: $STABLE"
echo "  → Canary: $CANARY"
echo "  → Unknown: $UNKNOWN"
echo ""

PERCENT_CANARY=$((CANARY))
echo "Canary rate: ${PERCENT_CANARY}%"
```

#### Expected Results

- Traffic at **0.2** (20%): ~20% to CANARY, ~80% to STABLE
- Traffic at **0.5** (50%): ~50% to CANARY, ~50% to STABLE

{{< callout type="warning" >}}
Always monitor error rates and latency when testing canary deployments. Start with a low percentage (5-10%) and gradually increase if metrics remain healthy.
{{< /callout >}}

---

### Method 2: Service-Level Configuration

This method is useful for managing multiple routes with the same canary configuration.

#### Configuration Steps

1. **Create a new Service**:
    ```
    Name: "My Service"
    Description: "Service with Canary"
    ```

2. **Service Exposition Settings**:
    ```
    Exposed domain: myapp.mydomain.com
    Legacy domain: true
    Strip path: true
    ```

3. **Service Targets**:
    ```
    Load balancing: WeightBestResponseTime
    Weight ratio: 0.2

    Target 1: app-stable.cleverapps.io (STABLE)
    Target 2: app-canary.cleverapps.io (CANARY)
    ```

4. **URL Patterns**:
    ```
    Public patterns: "/.*"
    ```

#### Testing

```sh
# Replace with your actual frontend URL
out=$(for i in {1..200}; do curl -s https://myapp.mydomain.com | grep Version; done); 
echo "CANARY: $(echo "$out" | grep -c CANARY)"
echo "STABLE: $(echo "$out" | grep -c STABLE)"
```

Expected Result: ~40 requests to CANARY, ~160 to STABLE (20/80 ratio)
{{< callout type=“info” >}}
Traffic Flow: Client → your-domain.com → Otoroshi → { stable / canary }
{{< /callout >}}

### Load Balancing Strategies

When using canary deployments, you can choose from several load balancing algorithms:
- WeightBestResponseTime: Routes traffic based on response time and weights
- RoundRobin: Distributes requests evenly across targets
- Random: Randomly selects a target for each request
- IpAddressHash: Routes based on client IP (sticky sessions)

---
## Resources

- Official Otoroshi Documentation : https://maif.github.io/otoroshi/
- Clever Cloud Documentation : https://www.clever.cloud/developers/doc/
- OWASP ModSecurity Core Rule Set : https://owasp.org/www-project-modsecurity-core-rule-set/
- Coraza WAF Documentation : https://coraza.io/
- API Gateway Patterns : https://microservices.io/patterns/apigateway.html

