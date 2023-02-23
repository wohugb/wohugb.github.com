# Introduction

ECMAScript modules are [the official standard format](https://tc39.github.io/ecma262/#sec-modules) to package JavaScript code for reuse. Modules are defined using a variety of [`import`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import) and [`export`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export) statements.

The following example of an ES module exports a function:

    // addTwo.mjs
    function addTwo(num) {
      return num + 2;
    }

    export { addTwo };

The following example of an ES module imports the function from `addTwo.mjs`:

    // app.mjs
    import { addTwo } from './addTwo.mjs';

    // Prints: 6
    console.log(addTwo(4));

Node.js fully supports ECMAScript modules as they are currently specified and provides interoperability between them and its original module format, [CommonJS](modules.html).
