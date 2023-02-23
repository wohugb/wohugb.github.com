# Builtin modules[#](#builtin-modules)

[Core modules](modules.html#core-modules) provide named exports of their public API. A default export is also provided which is the value of the CommonJS exports. The default export can be used for, among other things, modifying the named exports. Named exports of builtin modules are updated only by calling [`module.syncBuiltinESMExports()`](module.html#modulesyncbuiltinesmexports).

```js
import EventEmitter from "node:events";
const e = new EventEmitter();

import { readFile } from "node:fs";
readFile("./foo.txt", (err, source) => {
  if (err) {
    console.error(err);
  } else {
    console.log(source);
  }
});

import fs, { readFileSync } from "node:fs";
import { syncBuiltinESMExports } from "node:module";
import { Buffer } from "node:buffer";

fs.readFileSync = () => Buffer.from("Hello, ESM");
syncBuiltinESMExports();

fs.readFileSync === readFileSync;
```
