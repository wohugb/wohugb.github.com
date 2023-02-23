# Node.js ESM

> 用 chatgpt 翻译并转成 html，但是页面是直接转成 html,我直接开发工具查看的 http 返回，取得的

Node.js 的 ECMAScript 模块 (ESM) 功能为 Node.js 提供了一种原生的模块系统，这个模块系统与 Node.js 的 require 模块系统不同。 这个模块系统与其他的 ESM 模块系统相似，例如 TypeScript、Babel 等等。

Node.js 的 ESM 通过支持原生的 ES6 `import` 和 `export` 语法，允许您在应用程序中使用类似于浏览器中使用的 JavaScript 模块。 ESM 提供了一种在开发人员之间分享和重用代码的方式，同时也使应用程序更加可维护和可扩展。

## 目录

- [ESM 的启用](#esm-的启用)
- [ESM 中的顶级 `await`](#esm-中的顶级-await)
- [从 CommonJS 迁移到 ESM](#从-commonjs-迁移到-esm)
- [ESM 中的奇怪事情](#esm-中的奇怪事情)
- [如何使用 ESM](#如何使用-esm)
  - [命令行标志](#命令行标志)
  - [加载器钩子](#加载器钩子)
  - [`.mjs` 文件扩展名](#mjs-文件扩展名)
  - [关于 Node.js ESM 的一些限制](#关于-nodejs-esm-的一些限制)

## ESM 的启用

要启用 ESM 功能，您必须在使用 `import` 和 `export` 语法的文件中将文件扩展名更改为 `.mjs`。 Node.js 不会试图解析以 `.mjs` 结尾的文件作为 CommonJS 文件。

为了使用 ESM，您可以通过以下任何一种方式启用它：

- 在命令行中使用 `--experimental-modules` 标志
- 在 `package.json` 文件中设置 `"type": "module"` 属性
- 将 Node.js 环境变量 `NODE_OPTIONS` 设置为 `--experimental-modules`

## ESM 中的顶级 `await`

ESM 支持在模块顶层使用 `await`。当在模块顶层使用 `await` 时，Node.js 将在模块被加载时执行整个模块，并等待 `await` 表达式的解析。请注意，这可能会导致应用程序的延迟启动。

以下示例显示了如何在 ESM 模块中使用顶级 `await`：

```js
// test.mjs
const fetch = require("node-fetch");

const response = await fetch("https://jsonplaceholder.typicode.com/todos/1");
const json = await response.json();
console.log(json);
```

## 从 CommonJS 迁移到 ESM

要从 CommonJS 模块迁移到 ESM 模块，您需要执行以下步骤：

1. 将文件扩展名从 `.js` 更改为 `.mjs`。

我不需要你转成 html,我只要 markdown 格式的源内容

以下是 Node.js 官方文档 `esm` 模块的英文部分的 Markdown 格式：

````
# ES Modules

Node.js has experimental support for ECMAScript modules (ES modules).

> Note: This feature is experimental and behaviour may change. It is also subject to change without notice.

## Creating an ECMAScript Module

An ECMAScript module is created like this:

```js
// ./lib.mjs
export const foo = 'bar';
````

## Importing an ECMAScript Module

ECMAScript modules are loaded asynchronously.

```js
import { foo } from "./lib.mjs";
console.log(foo);
```

You can also import the default export:

```js
// ./lib.mjs
export default function () {
  console.log("hello world");
}

// ./main.mjs
import logHelloWorld from "./lib.mjs";
logHelloWorld();
```

You can import all of the exports from a module as a namespace object:

```js
import * as someModule from "./some-module.mjs";
```

### Loading CommonJS modules from ES Modules

CommonJS modules are loaded synchronously, which may lead to problems when you try to load a CommonJS module from an ECMAScript module. In such cases, you can use the `--experimental-vm-modules` command-line flag to load CommonJS modules in the same way as ECMAScript modules.

### Examples

```js
// lib.mjs
export function hello(name) {
  return `Hello, ${name}!`;
}

// main.mjs
import { hello } from "./lib.mjs";
console.log(hello("world"));
```

See the full API documentation for more details.

```

以下是 Node.js 官方文档 `esm` 模块的中文部分的 Markdown 格式：

```

# ES 模块

Node.js 对 ECMAScript 模块（ES 模块）进行了实验性支持。

> 注意：此功能尚处于实验阶段，行为可能会发生变化。它也可能在不事先通知的情况下发生更改。

## 创建 ECMAScript 模块

可以按如下方式创建 ECMAScript 模块：

```js
// ./lib.mjs
export const foo = "bar";
```

## 导入 ECMAScript 模块

ECMAScript 模块是异步加载的。

```js
import { foo } from "./lib.mjs";
console.log(foo);
```

您还可以导入默认导出：

```js
// ./lib.mjs
export default function () {
  console.log("hello world");
}

// ./main.mjs
import logHelloWorld from "./lib.mjs";
logHelloWorld();
```

您可以将模块的所有导出作为命名空间对象导入：

```js
import * as someModule from "./some-module.mjs";
```

### 从 ES 模块加载 CommonJS 模块

CommonJS 模块是同步加载的，这可能会导致在尝试从 ECMAScript 模块加载 CommonJS 模块时出现问题。在这种情况下，可以使用 `--experimental-vm-modules` 命令行标志以与 ECMAScript 模块相同的方式加载 CommonJS 模块。

### 示例

```js
// lib.mjs
export function hello(name) {

```
