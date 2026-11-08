## Clever Cloud KV Explorer

Access and edit your Key-Value databases with the **KV Explorer** tool, it's part of Clever Cloud's all included experience.

### Supported data types

The KV Explorer supports the hash, list, set, and string types. For Materia KV, its editor handles string values only: keys of other types stay listed, but selecting one shows an unsupported type message. Use the terminal to work with them.

### An intuitive, useful interface

The interface lets you filter keys by type and perform wildcard searches (for example: `*value_to_search*`). Value fields are multi-line for convenience, and you can copy/paste values directly from the interface. Special attention has been paid to accessibility and keyboard navigation with shortcuts to optimize your experience.

### KV Explorer Terminal

At the bottom of the page, you'll find an integrated terminal that works like a traditional CLI client. Type your commands and press Enter to execute them. All commands are supported, including `FLUSHDB` and `FLUSHALL`. Be careful with these as they erase data!

- [Share your feedback on KV Explorer](https://github.com/CleverCloud/Community/discussions/categories/kv-explorer)

![KV Explorer](/images/kv-explorer.webp "The KV Explorer tool in the Console")
