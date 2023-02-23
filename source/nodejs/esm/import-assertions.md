# Import assertions[#](#import-assertions)

Added in: v17.1.0, v16.14.0

[Stability: 1](documentation.html#stability-index) - Experimental

The [Import Assertions proposal](https://github.com/tc39/proposal-import-assertions) adds an inline syntax for module import statements to pass on more information alongside the module specifier.

```mjs
import fooData from "./foo.json" assert { type: "json" };

const { default: barData } = await import("./bar.json", { assert: { type: "json" } });
```

Node.js supports the following `type` values, for which the assertion is mandatory:

Assertion `type`

Needed for

`'json'`

[JSON modules](#json-modules)
