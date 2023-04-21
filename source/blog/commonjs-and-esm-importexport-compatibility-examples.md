---
title: "CommonJS (cjs) and Modules (esm): Import compatibility"
ref_url: https://adamcoster.com/blog/commonjs-and-esm-importexport-compatibility-examples
---

# CommonJS (cjs) and Modules (esm): 导入兼容性

Node's CommonJS (cjs) vs. ECMAScript (ESM) divide is probably the source of most of my quality of life frustrations as a fullstack Typescript/Node/Javascript programmer.

I can often go for weeks at a time before running into new incompatibility problems, so then each time I have to remind myself how interoperability works between them. Well, this time I made a tiny, simple demo so that next time I can just refer to it. And now you can, too!

## CommonJS (cjs) vs. Modules (ESM)

简要概述了这两种管理 JavaScript 代码之间的差异:

- CONCORJS 使用 require（'./ file.js'）语法用于导入其他模块和模块。exports=语法用于导出来自模块的内容
- ESM 从'./file.js'语法中使用导入{supp}用于导入和导出的导出语法。
- CONCORJS 文件可以使用.cjs 扩展名告诉节点它们在 concomjs 中
- ESM 文件可以使用.mjs 扩展名告诉节点它们在 ESM 中
- commonjs 进口是同步的
- ESM 导入是异步的（也允许顶级等待）
- commonjs 在节点中起作用，但在浏览器中不起作用
- ESM 受所有现代浏览器和最新版本的支持，但在 12 岁以下的节点版本中根本不起作用
- 在节点中开发了大量的核心 JavaScript 生态系统工具，而 Node 直到最近才开始支持 ESM，因此很大一部分现有节点项目都在 COMPORJS 中
- 这就是我们的情况。现在，要解决眼前的问题：如果您使用的是 ESM，您可以导入 commonjs 吗？相反的方式呢？

简而言之，是的！但是有考虑。

## 样本导出模块

Let's start with some importable modules. One in CommonJS, the other in ESM:

```js title="exporter.mjs"
/**
 * @file `exporter.mjs`
 * (An ESM module exporting a default and named entity.)
 */

export function namedMjsExport() {}

export default function defaultMjsExport() {}
```

```js
/**
 * @file `exporter.cjs`
 * (A CommonJS module exporting a default and named entity.)
 */

module.exports = function defaultCjsExport() {};

module.exports.namedCjsExport = function namedCjsExport() {};
```

## 如何将 commonj（CJ）导入 ESM

如果您要导入 ESM 模块，无论您是导入 CONCORJS 还是 ESM 模块，它看起来都相同：您将使用'./file.js'语法使用 import defaultStuff，{nequ stuff}异步。

```js
/**
 * @file `importer.mjs`
 *
 * An ESM module that imports stuff
 */

import defaultCjsExport, { namedCjsExport } from "./exporter.cjs";
import defaultMjsExport, { namedMjsExport } from "./exporter.mjs";

console.log({
  title: "Importing into an ESM module.",
  defaultCjsExport,
  namedCjsExport,
  defaultMjsExport,
  namedMjsExport,
});
```

And after we run that script via node importer.mjs (Node v16):

```json
{
  title: 'Importing into an ESM module.',
  defaultCjsExport: [Function: defaultCjsExport] {
    namedCjsExport: [Function: namedCjsExport]
  },
  namedCjsExport: [Function: namedCjsExport],
  defaultMjsExport: [Function: defaultMjsExport],
  namedMjsExport: [Function: namedMjsExport]
}
```

完美的！如果我们使用 ESM，我们基本上可以像 ESM 一样对待所有代码。（有一些细微差别，但我们通常可以忽略它们。）

## 将 ESM 导入 concomjs（CJS）

由于 require（）是同步的，因此您不能使用它来导入 ESM 模块。
相反，要将 ESM 导入 commonjs，您将使用异步导入（）函数。
返回的承诺解答为具有默认字段的对象（指向默认导出值），以及每个命名导出的字段。

让我们来看看：

```js
/**
 * @file `importer.cjs`
 *
 * From a require-style Node script, import cjs and mjs modules.
 */

/**
 * Import a module by `require()`ing it. If that results in
 * an error, return the error code.
 */
function requireModule(modulePath, exportName) {
  try {
    const imported = require(modulePath);
    return exportName ? imported[exportName] : imported;
  } catch (err) {
    return err.code;
  }
}

/**
 * CommonJS does not have top-level `await`, so we can wrap
 * everything in an `async` IIFE to make our lives a little easier.
 */
(async function () {
  console.log({
    title: "Importing into a CommonJS module",

    // CJS<-CJS and MJS<-CJS are equivalent
    defaultCjsExport: requireModule("./exporter.cjs"),
    namedCjsExport: requireModule("./exporter.cjs", "namedCjsExport"),

    // Cannot `require` an ESM module
    defaultMjsExportUsingRequire: requireModule("./exporter.mjs"),
    namedMjsExportUsingRequire: requireModule("./exporter.mjs", "namedMjsExport"),

    defaultMjsExport: (await import("./exporter.mjs")).default,
    namedMjsExport: (await import("./exporter.mjs")).namedMjsExport,
  });
})();
```

和节点进口商的输出：cjs：

```json
{
  title: 'Importing into a CommonJS module',
  defaultCjsExport: [Function: defaultCjsExport] {
    namedCjsExport: [Function: namedCjsExport]
  },
  namedCjsExport: [Function: namedCjsExport],
  defaultMjsExportUsingRequire: 'ERR_REQUIRE_ESM',
  namedMjsExportUsingRequire: 'ERR_REQUIRE_ESM',
  defaultMjsExport: [Function: defaultMjsExport],
  namedMjsExport: [Function: namedMjsExport]
}
```

哦，哇，看看我们需要多少代码以及我们需要多么小心！

## 建议

我已经在 ESM 上呆了一段时间了。
这是一种更好的开发人员体验，显然是我们将来会使用的。
但这会带来头痛，因为很多节点生态系统仍在 concomjs 中，您应该在全力以赴之前仔细考虑。

- 不要忘记文件扩展名！现代节点可以处理.mjs 和.cjs 扩展名，因此，如果您需要在一个地方使用一个模块类型，而另一个地方则可以随意混合！这也可在.mts 和.cts 扩展程序的打字稿（v4.5+）中起作用。
- (但也请注意，有些工具不知道这些扩展。)
- 在 concomjs 中编写的工具（即大多数基于节点的工具）通常处理 ESM。甚至非常受欢迎的项目。如果您想保证可以使用代码的工具，则可能需要坚持使用 COMPORJS。
- 如果您主要将其他软件包导入您的项目（与将其导入其他软件包），ESM 将不必担心您要导入哪种模块。
  ESM 规格要求导入路径是有效的路径，这意味着您需要文件扩展名和所有内容（commonjs 不需要）。节点可以选择对 ESM 模块的要求，如果要保留旧院：Node -ES-Module-Specifier-resolution-resolution-node = node your-dope-module.mjs
- 如果您确实决定在节点上全面介绍 ESM，请准备好进行很多非常烦人的故障排除！
