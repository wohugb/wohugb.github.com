# `import` Specifiers[#](#import-specifiers)

## Terminology[#](#terminology)

The _specifier_ of an `import` statement is the string after the `from` keyword, e.g. `'node:path'` in `import { sep } from 'node:path'`. Specifiers are also used in `export from` statements, and as the argument to an `import()` expression.

There are three types of specifiers:

- _Relative specifiers_ like `'./startup.js'` or `'../config.mjs'`. They refer to a path relative to the location of the importing file. _The file extension is always necessary for these._
- _Bare specifiers_ like `'some-package'` or `'some-package/shuffle'`. They can refer to the main entry point of a package by the package name, or a specific feature module within a package prefixed by the package name as per the examples respectively. _Including the file extension is only necessary for packages without an [`"exports"`](packages.html#exports) field._
- _Absolute specifiers_ like `'file:///opt/nodejs/config.js'`. They refer directly and explicitly to a full path.

Bare specifier resolutions are handled by the [Node.js module resolution algorithm](#resolver-algorithm-specification). All other specifier resolutions are always only resolved with the standard relative [URL](https://url.spec.whatwg.org/) resolution semantics.

Like in CommonJS, module files within packages can be accessed by appending a path to the package name unless the package's [`package.json`](packages.html#nodejs-packagejson-field-definitions) contains an [`"exports"`](packages.html#exports) field, in which case files within packages can only be accessed via the paths defined in [`"exports"`](packages.html#exports).

For details on these package resolution rules that apply to bare specifiers in the Node.js module resolution, see the [packages documentation](packages.html).

## Mandatory file extensions[#](#mandatory-file-extensions)

A file extension must be provided when using the `import` keyword to resolve relative or absolute specifiers. Directory indexes (e.g. `'./startup/index.js'`) must also be fully specified.

This behavior matches how `import` behaves in browser environments, assuming a typically configured server.

## URLs[#](#urls)

ES modules are resolved and cached as URLs. This means that special characters must be [percent-encoded](url.html#percent-encoding-in-urls), such as `#` with `%23` and `?` with `%3F`.

`file:`, `node:`, and `data:` URL schemes are supported. A specifier like `'https://example.com/app.js'` is not supported natively in Node.js unless using a [custom HTTPS loader](#https-loader).

### `file:` URLs[#](#file-urls)

Modules are loaded multiple times if the `import` specifier used to resolve them has a different query or fragment.

    import './foo.mjs?query=1'; // loads ./foo.mjs with query of "?query=1"
    import './foo.mjs?query=2'; // loads ./foo.mjs with query of "?query=2"

The volume root may be referenced via `/`, `//`, or `file:///`. Given the differences between [URL](https://url.spec.whatwg.org/) and path resolution (such as percent encoding details), it is recommended to use [url.pathToFileURL](url.html#urlpathtofileurlpath) when importing a path.

### `data:` imports[#](#data-imports)

Added in: v12.10.0

[`data:` URLs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URIs) are supported for importing with the following MIME types:

- `text/javascript` for ES modules
- `application/json` for JSON
- `application/wasm` for Wasm

  import 'data:text/javascript,console.log("hello!");';
  import \_ from 'data:application/json,"world!"' assert { type: 'json' };

`data:` URLs only resolve [bare specifiers](#terminology) for builtin modules and [absolute specifiers](#terminology). Resolving [relative specifiers](#terminology) does not work because `data:` is not a [special scheme](https://url.spec.whatwg.org/#special-scheme). For example, attempting to load `./foo` from `data:text/javascript,import "./foo";` fails to resolve because there is no concept of relative resolution for `data:` URLs.

### `node:` imports[#](#node-imports)

History

Version

Changes

v16.0.0, v14.18.0

Added `node:` import support to `require(...)`.

v14.13.1, v12.20.0

Added in: v14.13.1, v12.20.0

`node:` URLs are supported as an alternative means to load Node.js builtin modules. This URL scheme allows for builtin modules to be referenced by valid absolute URL strings.

    import fs from 'node:fs/promises';
