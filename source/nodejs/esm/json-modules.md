# JSON modules[#](#json-modules)

[Stability: 1](documentation.html#stability-index) - Experimental

JSON files can be referenced by `import`:

    import packageConfig from './package.json' assert { type: 'json' };

The `assert { type: 'json' }` syntax is mandatory; see [Import Assertions](#import-assertions).

The imported JSON only exposes a `default` export. There is no support for named exports. A cache entry is created in the CommonJS cache to avoid duplication. The same object is returned in CommonJS if the JSON module has already been imported from the same path.
