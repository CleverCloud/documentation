## Available Java versions

Simply set the environment variable **CC_JAVA_VERSION** to the version you want.

{{< callout type="info" >}}
We are using Java version 11 by default.
New applications will have the `CC_JAVA_VERSION` environment variable set to **21**.
{{< /callout >}}

Accepted values are `7`, `8`, `11`, `17`, `21` or `graalvm-ce` (for GraalVM 21.0.0.2, based on OpenJDK 11.0).

We follow the official Java [roadmap](https://www.oracle.com/java/technologies/java-se-support-roadmap.html) by supporting both LTS and latest non-LTS versions.

We are using OpenJDK distribution for mentionned Java versions.

{{< callout type="warning" >}}
Every non-LTS versions where _Premier support_ ends will be removed without warning as you should be able to switch to the next available non-LTS version without any trouble.
{{< /callout >}}
