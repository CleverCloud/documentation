## Available Java versions

Simply set the environment variable **CC_JAVA_VERSION** to the version you want.

{{< alert "info" "Default version" >}}
    <p>We are using Java version 11 by default.</p>
    <p>New applications will have the <strong>CC_JAVA_VERSION</strong> environment variable set to 11.</p>
{{< /alert >}}

Accepted values are `7`, `8`, `11`, `17` or `graalvm-ce` (for GraalVM 21.0.0.2, based on OpenJDK 11.0).

We follow the official Java [roadmap](https://www.oracle.com/java/technologies/java-se-support-roadmap.html) by supporting both LTS and latest non-LTS versions.

We are using OpenJDK distribution for mentionned Java versions. 

{{< alert "warning" "non-LTS versions" >}}
    <p>Every non-LTS versions where <i>Premier support</i> ends will be removed without warning as you should be able to switch to the next available non-LTS version without any trouble.</p>
{{< /alert >}}
