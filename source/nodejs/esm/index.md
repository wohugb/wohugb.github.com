# 模块: ECMAScript 模块

## 目录

- [介绍](./introduction.md)
- [启用](./enabling.md)
- [软件包](./packages.md)
- [`import` 指定器](./import-specifiers.md)
- [进口断言](./import-assertions.md)
- [内置模块](./builtin-modules.md)
- [`import()` 表达](./import-expressions.md)
- [`import.meta`](./importmeta.md)
- [与 commonjs 的互操作性](./interoperability-with-commonjs.md)
- [JSON 模块](./json-modules.md)
- [Wasm 模块](./wasm-modules.md)
- [顶层 `await`](./top-level-await.md)
- [HTTPS 和 HTTP imports](./https-and-http-imports.md)
- [装载机](./loaders.md)
- [分辨率算法](./resolution-algorithm.md)

## 历史

Version

Changes

v18.6.0, v16.17.0

Add support for chaining loaders.

v17.1.0, v16.14.0

Add support for import assertions.

v17.0.0, v16.12.0

Consolidate loader hooks, removed `getFormat`, `getSource`, `transformSource`, and `getGlobalPreloadCode` hooks added `load` and `globalPreload` hooks allowed returning `format` from either `resolve` or `load` hooks.

v14.8.0

Unflag Top-Level Await.

v15.3.0, v14.17.0, v12.22.0

Stabilize modules implementation.

v14.13.0, v12.20.0

Support for detection of CommonJS named exports.

v14.0.0, v13.14.0, v12.20.0

Remove experimental modules warning.

v13.2.0, v12.17.0

Loading ECMAScript modules no longer requires a command-line flag.

v12.0.0

Add support for ES modules using `.js` file extension via `package.json` `"type"` field.

v8.5.0

Added in: v8.5.0
