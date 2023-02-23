# 与 CommonJS 的互操作性

## `import` 语句

`import`语句可以引用 ES 模块或 CommonJS 模块。
仅在 ES 模块中允许`import` 语句, 但是 CommonJS 中支持动态[`import()`](#import-expressions)表达式来加载 ES 模块。

当导入[CommonJS 模块](#commonjs-namespaces)时，`module.exports`对象被作为默认导出提供。
可以使用静态分析提供的命名导出，以方便更好的生态系统兼容性。

## `require`

CommonJS 模块`require`总是将它引用的文件视为 CommonJS。

不支持使用`require`加载 ES 模块，因为 ES 模块具有异步执行。
相反，使用[`import()`](#import-expressions)从 CommonJS 模块加载 ES 模块。

## CommonJS 名称空间

CommonJS 模块由一个模块组成。导出对象，该对象可以是任何类型。

当导入 CommonJS 模块时，可以使用 ES 模块默认导入或对应的 sugar 语法可靠地导入:

```mjs
import { default as cjs } from "cjs";

// The following import statement is "syntax sugar" (equivalent but sweeter)
// for `{ default as cjsSugar }` in the above import statement:
import cjsSugar from "cjs";

console.log(cjs);
console.log(cjs === cjsSugar);
// Prints:
//   <module.exports>
//   true
```

CommonJS 模块的 ECMAScript 模块命名空间表示形式始终是一个带有`default`导出键的命名空间，该导出键指向 CommonJS 的`module.exports`值。

当使用`import * as m from 'cjs'`或动态导入时，可以直接观察到这个模块命名空间外来对象:

```mjs
import * as m from "cjs";
console.log(m);
console.log(m === (await import("cjs")));
// Prints:
//   [Module] { default: <module.exports> }
//   true
```

为了更好地兼容 JS 生态系统中的现有使用，Node.js 还试图确定每个导入的 CommonJS 模块的 CommonJS 命名导出，并使用静态分析过程将它们作为单独的 ES 模块导出提供。

例如，考虑这样一个 CommonJS 模块:

```cjs
// cjs.cjs
exports.name = "exported";
```

例如，考虑一个 CommonJS 模块:前面的模块支持 ES 模块中的命名导入:

```mjs
import { name } from "./cjs.cjs";
console.log(name);
// Prints: 'exported'

import cjs from "./cjs.cjs";
console.log(cjs);
// Prints: { name: 'exported' }

import * as m from "./cjs.cjs";
console.log(m);
// Prints: [Module] { default: { name: 'exported' }, name: 'exported' }
```

从上一个记录模块名称空间外来对象的示例中可以看出，导入模块时，`name`导出是从`module.exports`对象中复制出来的，并直接在 ES 模块名称空间上设置。

对于这些已命名的导出，不会检测到添加到`module.exports`中的实时绑定更新或新导出。

命名导出的检测基于通用语法模式，但并不总是正确地检测命名导出。
在这些情况下，使用上面描述的默认导入表单可能是更好的选择。

Named exports detection covers many common export patterns, reexport patterns and build tool and transpiler outputs.
See [cjs-module-lexer](https://github.com/nodejs/cjs-module-lexer/tree/1.2.2) for the exact semantics implemented.

命名导出检测包括许多常见的导出模式、再导出模式以及构建工具和转译器输出。
具体实现的语义请参见[cjs-module-lexer](https://github.com/nodejs/cjs-module-lexer/tree/1.2.2)。

## ES 模块和 CommonJS 的区别

### No `require`, `exports`, or `module.exports`

在大多数情况下，ES 模块`import`可以用来加载 CommonJS 模块。

如果需要，可以使用[`module.createRequire()`](module.html#modulecreaterequirefilename)在 ES 模块中构造`require`函数

### No `__filename` or `__dirname`

这些 CommonJS 变量在 ES 模块中不可用。

`__filename` 和 `__dirname` 用例可以通过[`import.meta.url`](#importmetaurl)复制

### 无加载插件

ES 模块导入目前不支持[Addons](../addons.md)。

它们可以用[`module.createRequire()`](module.html#modulecreaterequirefilename)或[`process.dlopen`](process.html#processdlopenmodule-filename-flags)来加载。

### No `require.resolve`

相对解析可以通过`new URL('./local', import.meta.url)`来处理。

对于一个完整的`require.resolve`替换，有一个标记的实验[`import.meta.resolve`](#importmetaresolvespecifier-parent) API。

也可以使用`module.createRequire()`。

### No `NODE_PATH`

`NODE_PATH`不是解析`import`说明符的一部分。
如果需要这种行为，请使用符号链接。

### No `require.extensions`

`require.extensions`不会被`import`使用。
我们期望将来加载器钩子可以提供这个工作流。

### No `require.cache`

`require.cache`不会被`import`使用，因为 ES 模块加载器有自己单独的缓存。
