## Available Java versions

Simply set the environment variable **CC_JAVA_VERSION** to the version you want.


⚠️ Clever Cloud uses Java version 11 by default. New applications have the `CC_JAVA_VERSION` environment variable set to **21**.

Accepted values are `7`, `8`, `11`, `17`, `21`, `22` or `graalvm-ce` (for GraalVM 21.0.0.2, based on OpenJDK 11.0).

We follow the official Java [roadmap](https://www.oracle.com/java/technologies/java-se-support-roadmap.html) by supporting both LTS and latest non-LTS versions.

We are using OpenJDK distribution for mentioned Java versions.

Every non-LTS versions where _Premier support_ ends will be removed without warning as you should be able to switch to the next available non-LTS version without any trouble.
