# Enabling[#](#enabling)

Node.js has two module systems: [CommonJS](modules.html) modules and ECMAScript modules.

Authors can tell Node.js to use the ECMAScript modules loader via the `.mjs` file extension, the `package.json` [`"type"`](packages.html#type) field, or the [`--input-type`](cli.html#--input-typetype) flag. Outside of those cases, Node.js will use the CommonJS module loader. See [Determining module system](packages.html#determining-module-system) for more details.
