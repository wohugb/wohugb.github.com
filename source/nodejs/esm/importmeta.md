# `import.meta`

- [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)

The `import.meta` meta property is an `Object` that contains the following properties.

## `import.meta.url`

- [<string>](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) The absolute `file:` URL of the module.

This is defined exactly the same as it is in browsers providing the URL of the current module file.

This enables useful patterns such as relative file loading:

```mjs
import { readFileSync } from "node:fs";
const buffer = readFileSync(new URL("./data.proto", import.meta.url));
```

## `import.meta.resolve(specifier[, parent])`

[Stability: 1](documentation.html#stability-index) - Experimental

This feature is only available with the `--experimental-import-meta-resolve` command flag enabled.

- `specifier` [<string>](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) The module specifier to resolve relative to `parent`.
- `parent` [<string>](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) | [<URL>](url.html#the-whatwg-url-api) The absolute parent module URL to resolve from. If none is specified, the value of `import.meta.url` is used as the default.
- Returns: [<Promise>](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)

Provides a module-relative resolution function scoped to each module, returning the URL string.

```mjs
const dependencyAsset = await import.meta.resolve("component-lib/asset.css");
```

`import.meta.resolve` also accepts a second argument which is the parent module from which to resolve from:

```mjs
await import.meta.resolve("./dep", import.meta.url);
```

This function is asynchronous because the ES module resolver in Node.js is allowed to be asynchronous.
