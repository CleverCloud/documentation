## Main concepts

Warp 10 is a time series database, it uses the notion of `class`, `labels`, `longitude`, `latitude`, `altitude` and `value`. `labels` is a kind of dictionary. That's called a **map** under the warp10 terminology.

A GeoTime Serie (GTS) is defined by a `class` and some `labels`. They're indexed and used to quickly retrieved the data. A GTS may contain some values which have the following model: `[ timestamp longitude latitude altitude value ]`

Warp 10 uses Warp Script. It's a stack based language using reverse polish notation.

* [Warp 1O documentation](https://www.warp10.io/doc/reference)
* [Warp Script documentation](https://www.warp10.io/content/03_Documentation/04_WarpScript)
