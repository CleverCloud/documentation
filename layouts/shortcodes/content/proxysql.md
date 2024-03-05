ProxySQL is a tool that acts like a proxy between your application and your MySQL add-on. Instead of connecting to your MySQL add-on, you can connect
to the local ProxySQL and it will forward all your requests to your MySQL add-on.

This allows you to let ProxySQL take care of some interesting features like connection pooling or leader / follower setup.
