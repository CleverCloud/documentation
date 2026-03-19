## Environment injection

Clever Cloud exposes [environment variables defined for your application](#setting-up-environment-variables-on-clever-cloud) alongside those provided by linked add-ons. Read a standard variable such as `MY_VARIABLE` from the process environment with:

```java
String value = System.getenv("MY_VARIABLE");
```

### Java system properties

By default, Clever Cloud also passes variables to the generated launch command as Java system properties using `-D` options. When this command runs your application in the same JVM, retrieve a property with `System.getProperty("MY_VARIABLE")`.

Variable names containing a dot (`.`) are not exported to the process environment. The generated launch command only receives them as Java system properties. For example, if you define `my.app.config=production` for your application, Clever Cloud adds `-Dmy.app.config=production` to the generated launch command.

A Maven or Gradle deployment goal can start the application in another JVM. In this case, forwarding system properties depends on the plugin or task configuration. When the property reaches the application JVM, retrieve its value with:

```java
String value = System.getProperty("my.app.config"); // returns "production"
```

This mechanism can configure frameworks such as Spring Boot or Quarkus without modifying configuration files. Prefer standard environment variable names for portable application configuration.

Setting [`CC_RUN_COMMAND`](#custom-run-command) replaces the generated launch command, so Clever Cloud no longer adds these `-D` options automatically. With a custom run command, use standard environment variable names and map them in your application configuration.
