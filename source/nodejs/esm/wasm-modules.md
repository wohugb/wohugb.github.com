# Wasm modules[#](#wasm-modules)

[Stability: 1](documentation.html#stability-index) - Experimental

Importing WebAssembly modules is supported under the `--experimental-wasm-modules` flag, allowing any `.wasm` files to be imported as normal modules while also supporting their module imports.

This integration is in line with the [ES Module Integration Proposal for WebAssembly](https://github.com/webassembly/esm-integration).

For example, an `index.mjs` containing:

    import * as M from './module.wasm';
    console.log(M);

executed under:

    node --experimental-wasm-modules index.mjs

would provide the exports interface for the instantiation of `module.wasm`.
