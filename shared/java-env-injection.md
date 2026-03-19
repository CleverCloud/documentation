### Environment injection

Clever Cloud injects environment variables defined in the Console and by linked add-ons into your application. For JVM-based applications, all environment variables are passed as system properties using `-D` flags, making them accessible through `System.getProperty()`.

To access a standard environment variable such as `MY_VARIABLE`, use `System.getProperty("MY_VARIABLE")` or `System.getenv("MY_VARIABLE")`.

#### Variables with dots as JVM system properties

Environment variable names containing a dot (`.`) are handled differently. Since most shells do not support dots in variable names, these variables are passed exclusively as JVM system properties via `-D` flags, and are not set in the shell environment.

For example, if you define `my.app.config=production` in the Clever Cloud Console, the JVM receives `-Dmy.app.config=production` at startup. You can then retrieve it with:

```java
String value = System.getProperty("my.app.config"); // returns "production"
```

This is useful for setting framework-specific properties directly from the Console without modifying configuration files (e.g. Spring Boot properties, Quarkus settings, or any custom `-D` parameter your application expects).
