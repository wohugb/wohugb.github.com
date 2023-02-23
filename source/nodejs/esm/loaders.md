# Loaders[#](#loaders)

History

Version

Changes

v18.6.0, v16.17.0

Add support for chaining loaders.

v16.12.0

Removed `getFormat`, `getSource`, `transformSource`, and `globalPreload`; added `load` hook and `getGlobalPreload` hook.

v8.8.0

Added in: v8.8.0

[Stability: 1](documentation.html#stability-index) - Experimental

> This API is currently being redesigned and will still change.

To customize the default module resolution, loader hooks can optionally be provided via a `--experimental-loader ./loader-name.mjs` argument to Node.js.

When hooks are used they apply to each subsequent loader, the entry point, and all `import` calls. They won't apply to `require` calls; those still follow [CommonJS](modules.html) rules.

Loaders follow the pattern of `--require`:

    node \
      --experimental-loader unpkg \
      --experimental-loader http-to-https \
      --experimental-loader cache-buster

These are called in the following sequence: `cache-buster` calls `http-to-https` which calls `unpkg`.

## Hooks[#](#hooks)

Hooks are part of a chain, even if that chain consists of only one custom (user-provided) hook and the default hook, which is always present. Hook functions nest: each one must always return a plain object, and chaining happens as a result of each function calling `next<hookName>()`, which is a reference to the subsequent loader's hook.

A hook that returns a value lacking a required property triggers an exception. A hook that returns without calling `next<hookName>()` _and_ without returning `shortCircuit: true` also triggers an exception. These errors are to help prevent unintentional breaks in the chain.

### `resolve(specifier, context, nextResolve)`[#](#resolvespecifier-context-nextresolve)

History

Version

Changes

v18.6.0, v16.17.0

Add support for chaining resolve hooks. Each hook must either call `nextResolve()` or include a `shortCircuit` property set to `true` in its return.

v17.1.0, v16.14.0

Add support for import assertions.

> The loaders API is being redesigned. This hook may disappear or its signature may change. Do not rely on the API described below.

- `specifier` [<string>](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type)
- `context` [<Object>](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)
  - `conditions` [<string\[\]>](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) Export conditions of the relevant `package.json`
  - `importAssertions` [<Object>](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)
  - `parentURL` [<string>](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) | [<undefined>](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Undefined_type) The module importing this one, or undefined if this is the Node.js entry point
- `nextResolve` [<Function>](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function) The subsequent `resolve` hook in the chain, or the Node.js default `resolve` hook after the last user-supplied `resolve` hook
  - `specifier` [<string>](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type)
  - `context` [<Object>](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)
- Returns: [<Object>](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)
  - `format` [<string>](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) | [<null>](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Null_type) | [<undefined>](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Undefined_type) A hint to the load hook (it might be ignored) `'builtin' | 'commonjs' | 'json' | 'module' | 'wasm'`
  - `shortCircuit` [<undefined>](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Undefined_type) | [<boolean>](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type) A signal that this hook intends to terminate the chain of `resolve` hooks. **Default:** `false`
  - `url` [<string>](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) The absolute URL to which this input resolves

The `resolve` hook chain is responsible for resolving file URL for a given module specifier and parent URL, and optionally its format (such as `'module'`) as a hint to the `load` hook. If a format is specified, the `load` hook is ultimately responsible for providing the final `format` value (and it is free to ignore the hint provided by `resolve`); if `resolve` provides a `format`, a custom `load` hook is required even if only to pass the value to the Node.js default `load` hook.

The module specifier is the string in an `import` statement or `import()` expression.

The parent URL is the URL of the module that imported this one, or `undefined` if this is the main entry point for the application.

The `conditions` property in `context` is an array of conditions for [package exports conditions](packages.html#conditional-exports) that apply to this resolution request. They can be used for looking up conditional mappings elsewhere or to modify the list when calling the default resolution logic.

The current [package exports conditions](packages.html#conditional-exports) are always in the `context.conditions` array passed into the hook. To guarantee _default Node.js module specifier resolution behavior_ when calling `defaultResolve`, the `context.conditions` array passed to it _must_ include _all_ elements of the `context.conditions` array originally passed into the `resolve` hook.

    export async function resolve(specifier, context, nextResolve) {
      const { parentURL = null } = context;

      if (Math.random() > 0.5) { // Some condition.
        // For some or all specifiers, do some custom logic for resolving.
        // Always return an object of the form {url: <string>}.
        return {
          shortCircuit: true,
          url: parentURL ?
            new URL(specifier, parentURL).href :
            new URL(specifier).href,
        };
      }

      if (Math.random() < 0.5) { // Another condition.
        // When calling `defaultResolve`, the arguments can be modified. In this
        // case it's adding another value for matching conditional exports.
        return nextResolve(specifier, {
          ...context,
          conditions: [...context.conditions, 'another-condition'],
        });
      }

      // Defer to the next hook in the chain, which would be the
      // Node.js default resolve if this is the last user-specified loader.
      return nextResolve(specifier);
    }

### `load(url, context, nextLoad)`[#](#loadurl-context-nextload)

History

Version

Changes

v18.6.0, v16.17.0

Add support for chaining load hooks. Each hook must either call `nextLoad()` or include a `shortCircuit` property set to `true` in its return.

> The loaders API is being redesigned. This hook may disappear or its signature may change. Do not rely on the API described below.

> In a previous version of this API, this was split across 3 separate, now deprecated, hooks (`getFormat`, `getSource`, and `transformSource`).

- `url` [<string>](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) The URL returned by the `resolve` chain
- `context` [<Object>](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)
  - `conditions` [<string\[\]>](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) Export conditions of the relevant `package.json`
  - `format` [<string>](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) | [<null>](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Null_type) | [<undefined>](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Undefined_type) The format optionally supplied by the `resolve` hook chain
  - `importAssertions` [<Object>](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)
- `nextLoad` [<Function>](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function) The subsequent `load` hook in the chain, or the Node.js default `load` hook after the last user-supplied `load` hook
  - `specifier` [<string>](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type)
  - `context` [<Object>](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)
- Returns: [<Object>](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)
  - `format` [<string>](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type)
  - `shortCircuit` [<undefined>](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Undefined_type) | [<boolean>](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type) A signal that this hook intends to terminate the chain of `resolve` hooks. **Default:** `false`
  - `source` [<string>](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) | [<ArrayBuffer>](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer) | [<TypedArray>](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray) The source for Node.js to evaluate

The `load` hook provides a way to define a custom method of determining how a URL should be interpreted, retrieved, and parsed. It is also in charge of validating the import assertion.

The final value of `format` must be one of the following:

`format`

Description

Acceptable types for `source` returned by `load`

`'builtin'`

Load a Node.js builtin module

Not applicable

`'commonjs'`

Load a Node.js CommonJS module

Not applicable

`'json'`

Load a JSON file

{ [`string`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String), [`ArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer), [`TypedArray`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray) }

`'module'`

Load an ES module

{ [`string`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String), [`ArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer), [`TypedArray`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray) }

`'wasm'`

Load a WebAssembly module

{ [`ArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer), [`TypedArray`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray) }

The value of `source` is ignored for type `'builtin'` because currently it is not possible to replace the value of a Node.js builtin (core) module. The value of `source` is ignored for type `'commonjs'` because the CommonJS module loader does not provide a mechanism for the ES module loader to override the [CommonJS module return value](#commonjs-namespaces). This limitation might be overcome in the future.

> **Caveat**: The ESM `load` hook and namespaced exports from CommonJS modules are incompatible. Attempting to use them together will result in an empty object from the import. This may be addressed in the future.

> These types all correspond to classes defined in ECMAScript.

- The specific [`ArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer) object is a [`SharedArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SharedArrayBuffer).
- The specific [`TypedArray`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray) object is a [`Uint8Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array).

If the source value of a text-based format (i.e., `'json'`, `'module'`) is not a string, it is converted to a string using [`util.TextDecoder`](util.html#class-utiltextdecoder).

The `load` hook provides a way to define a custom method for retrieving the source code of an ES module specifier. This would allow a loader to potentially avoid reading files from disk. It could also be used to map an unrecognized format to a supported one, for example `yaml` to `module`.

    export async function load(url, context, nextLoad) {
      const { format } = context;

      if (Math.random() > 0.5) { // Some condition
        /*
          For some or all URLs, do some custom logic for retrieving the source.
          Always return an object of the form {
            format: <string>,
            source: <string|buffer>,
          }.
        */
        return {
          format,
          shortCircuit: true,
          source: '...',
        };
      }

      // Defer to the next hook in the chain.
      return nextLoad(url);
    }

In a more advanced scenario, this can also be used to transform an unsupported source to a supported one (see [Examples](#examples) below).

### `globalPreload()`[#](#globalpreload)

History

Version

Changes

v18.6.0, v16.17.0

Add support for chaining globalPreload hooks.

> The loaders API is being redesigned. This hook may disappear or its signature may change. Do not rely on the API described below.

> In a previous version of this API, this hook was named `getGlobalPreloadCode`.

- `context` [<Object>](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object) Information to assist the preload code
  - `port` [<MessagePort>](worker_threads.html#class-messageport)
- Returns: [<string>](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type) Code to run before application startup

Sometimes it might be necessary to run some code inside of the same global scope that the application runs in. This hook allows the return of a string that is run as a sloppy-mode script on startup.

Similar to how CommonJS wrappers work, the code runs in an implicit function scope. The only argument is a `require`\-like function that can be used to load builtins like "fs": `getBuiltin(request: string)`.

If the code needs more advanced `require` features, it has to construct its own `require` using `module.createRequire()`.

    export function globalPreload(context) {
      return `\
    globalThis.someInjectedProperty = 42;
    console.log('I just set some globals!');

    const { createRequire } = getBuiltin('module');
    const { cwd } = getBuiltin('process');

    const require = createRequire(cwd() + '/<preload>');
    // [...]
    `;
    }

In order to allow communication between the application and the loader, another argument is provided to the preload code: `port`. This is available as a parameter to the loader hook and inside of the source text returned by the hook. Some care must be taken in order to properly call [`port.ref()`](https://nodejs.org/dist/latest-v17.x/docs/api/worker_threads.html#portref) and [`port.unref()`](https://nodejs.org/dist/latest-v17.x/docs/api/worker_threads.html#portunref) to prevent a process from being in a state where it won't close normally.

    /**
     * This example has the application context send a message to the loader
     * and sends the message back to the application context
     */
    export function globalPreload({ port }) {
      port.onmessage = (evt) => {
        port.postMessage(evt.data);
      };
      return `\
        port.postMessage('console.log("I went to the Loader and back");');
        port.onmessage = (evt) => {
          eval(evt.data);
        };
      `;
    }

## Examples[#](#examples)

The various loader hooks can be used together to accomplish wide-ranging customizations of the Node.js code loading and evaluation behaviors.

### HTTPS loader[#](#https-loader)

In current Node.js, specifiers starting with `https://` are experimental (see [HTTPS and HTTP imports](#https-and-http-imports)).

The loader below registers hooks to enable rudimentary support for such specifiers. While this may seem like a significant improvement to Node.js core functionality, there are substantial downsides to actually using this loader: performance is much slower than loading files from disk, there is no caching, and there is no security.

    // https-loader.mjs
    import { get } from 'node:https';

    export function resolve(specifier, context, nextResolve) {
      const { parentURL = null } = context;

      // Normally Node.js would error on specifiers starting with 'https://', so
      // this hook intercepts them and converts them into absolute URLs to be
      // passed along to the later hooks below.
      if (specifier.startsWith('https://')) {
        return {
          shortCircuit: true,
          url: specifier,
        };
      } else if (parentURL && parentURL.startsWith('https://')) {
        return {
          shortCircuit: true,
          url: new URL(specifier, parentURL).href,
        };
      }

      // Let Node.js handle all other specifiers.
      return nextResolve(specifier);
    }

    export function load(url, context, nextLoad) {
      // For JavaScript to be loaded over the network, we need to fetch and
      // return it.
      if (url.startsWith('https://')) {
        return new Promise((resolve, reject) => {
          get(url, (res) => {
            let data = '';
            res.on('data', (chunk) => data += chunk);
            res.on('end', () => resolve({
              // This example assumes all network-provided JavaScript is ES module
              // code.
              format: 'module',
              shortCircuit: true,
              source: data,
            }));
          }).on('error', (err) => reject(err));
        });
      }

      // Let Node.js handle all other URLs.
      return nextLoad(url);
    }

    // main.mjs
    import { VERSION } from 'https://coffeescript.org/browser-compiler-modern/coffeescript.js';

    console.log(VERSION);

With the preceding loader, running `node --experimental-loader ./https-loader.mjs ./main.mjs` prints the current version of CoffeeScript per the module at the URL in `main.mjs`.

### Transpiler loader[#](#transpiler-loader)

Sources that are in formats Node.js doesn't understand can be converted into JavaScript using the [`load` hook](#loadurl-context-nextload). Before that hook gets called, however, a [`resolve` hook](#resolvespecifier-context-nextresolve) needs to tell Node.js not to throw an error on unknown file types.

This is less performant than transpiling source files before running Node.js; a transpiler loader should only be used for development and testing purposes.

    // coffeescript-loader.mjs
    import { readFile } from 'node:fs/promises';
    import { dirname, extname, resolve as resolvePath } from 'node:path';
    import { cwd } from 'node:process';
    import { fileURLToPath, pathToFileURL } from 'node:url';
    import CoffeeScript from 'coffeescript';

    const baseURL = pathToFileURL(`${cwd()}/`).href;

    // CoffeeScript files end in .coffee, .litcoffee, or .coffee.md.
    const extensionsRegex = /\.coffee$|\.litcoffee$|\.coffee\.md$/;

    export async function resolve(specifier, context, nextResolve) {
      if (extensionsRegex.test(specifier)) {
        const { parentURL = baseURL } = context;

        // Node.js normally errors on unknown file extensions, so return a URL for
        // specifiers ending in the CoffeeScript file extensions.
        return {
          shortCircuit: true,
          url: new URL(specifier, parentURL).href,
        };
      }

      // Let Node.js handle all other specifiers.
      return nextResolve(specifier);
    }

    export async function load(url, context, nextLoad) {
      if (extensionsRegex.test(url)) {
        // Now that we patched resolve to let CoffeeScript URLs through, we need to
        // tell Node.js what format such URLs should be interpreted as. Because
        // CoffeeScript transpiles into JavaScript, it should be one of the two
        // JavaScript formats: 'commonjs' or 'module'.

        // CoffeeScript files can be either CommonJS or ES modules, so we want any
        // CoffeeScript file to be treated by Node.js the same as a .js file at the
        // same location. To determine how Node.js would interpret an arbitrary .js
        // file, search up the file system for the nearest parent package.json file
        // and read its "type" field.
        const format = await getPackageType(url);
        // When a hook returns a format of 'commonjs', `source` is be ignored.
        // To handle CommonJS files, a handler needs to be registered with
        // `require.extensions` in order to process the files with the CommonJS
        // loader. Avoiding the need for a separate CommonJS handler is a future
        // enhancement planned for ES module loaders.
        if (format === 'commonjs') {
          return {
            format,
            shortCircuit: true,
          };
        }

        const { source: rawSource } = await nextLoad(url, { ...context, format });
        // This hook converts CoffeeScript source code into JavaScript source code
        // for all imported CoffeeScript files.
        const transformedSource = coffeeCompile(rawSource.toString(), url);

        return {
          format,
          shortCircuit: true,
          source: transformedSource,
        };
      }

      // Let Node.js handle all other URLs.
      return nextLoad(url);
    }

    async function getPackageType(url) {
      // `url` is only a file path during the first iteration when passed the
      // resolved url from the load() hook
      // an actual file path from load() will contain a file extension as it's
      // required by the spec
      // this simple truthy check for whether `url` contains a file extension will
      // work for most projects but does not cover some edge-cases (such as
      // extensionless files or a url ending in a trailing space)
      const isFilePath = !!extname(url);
      // If it is a file path, get the directory it's in
      const dir = isFilePath ?
        dirname(fileURLToPath(url)) :
        url;
      // Compose a file path to a package.json in the same directory,
      // which may or may not exist
      const packagePath = resolvePath(dir, 'package.json');
      // Try to read the possibly nonexistent package.json
      const type = await readFile(packagePath, { encoding: 'utf8' })
        .then((filestring) => JSON.parse(filestring).type)
        .catch((err) => {
          if (err?.code !== 'ENOENT') console.error(err);
        });
      // Ff package.json existed and contained a `type` field with a value, voila
      if (type) return type;
      // Otherwise, (if not at the root) continue checking the next directory up
      // If at the root, stop and return false
      return dir.length > 1 && getPackageType(resolvePath(dir, '..'));
    }

    # main.coffee
    import { scream } from './scream.coffee'
    console.log scream 'hello, world'

    import { version } from 'node:process'
    console.log "Brought to you by Node.js version #{version}"

    # scream.coffee
    export scream = (str) -> str.toUpperCase()

With the preceding loader, running `node --experimental-loader ./coffeescript-loader.mjs main.coffee` causes `main.coffee` to be turned into JavaScript after its source code is loaded from disk but before Node.js executes it; and so on for any `.coffee`, `.litcoffee` or `.coffee.md` files referenced via `import` statements of any loaded file.
