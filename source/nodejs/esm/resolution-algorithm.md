# Resolution algorithm[#](#resolution-algorithm)

## Features[#](#features)

The resolver has the following properties:

- FileURL-based resolution as is used by ES modules
- Support for builtin module loading
- Relative and absolute URL resolution
- No default extensions
- No folder mains
- Bare specifier package resolution lookup through node_modules

## Resolver algorithm[#](#resolver-algorithm)

The algorithm to load an ES module specifier is given through the **ESM_RESOLVE** method below. It returns the resolved URL for a module specifier relative to a parentURL.

The algorithm to determine the module format of a resolved URL is provided by **ESM_FORMAT**, which returns the unique module format for any file. The _"module"_ format is returned for an ECMAScript Module, while the _"commonjs"_ format is used to indicate loading through the legacy CommonJS loader. Additional formats such as _"addon"_ can be extended in future updates.

In the following algorithms, all subroutine errors are propagated as errors of these top-level routines unless stated otherwise.

_defaultConditions_ is the conditional environment name array, `["node", "import"]`.

The resolver can throw the following errors:

- _Invalid Module Specifier_: Module specifier is an invalid URL, package name or package subpath specifier.
- _Invalid Package Configuration_: package.json configuration is invalid or contains an invalid configuration.
- _Invalid Package Target_: Package exports or imports define a target module for the package that is an invalid type or string target.
- _Package Path Not Exported_: Package exports do not define or permit a target subpath in the package for the given module.
- _Package Import Not Defined_: Package imports do not define the specifier.
- _Module Not Found_: The package or module requested does not exist.
- _Unsupported Directory Import_: The resolved path corresponds to a directory, which is not a supported target for module imports.

## Resolver Algorithm Specification[#](#resolver-algorithm-specification)

**ESM_RESOLVE**(_specifier_, _parentURL_)

> 1.  Let _resolved_ be **undefined**.
> 2.  If _specifier_ is a valid URL, then
>     1.  Set _resolved_ to the result of parsing and reserializing _specifier_ as a URL.
> 3.  Otherwise, if _specifier_ starts with _"/"_, _"./"_, or _"../"_, then
>     1.  Set _resolved_ to the URL resolution of _specifier_ relative to _parentURL_.
> 4.  Otherwise, if _specifier_ starts with _"#"_, then
>     1.  Set _resolved_ to the result of **PACKAGE_IMPORTS_RESOLVE**(_specifier_, _parentURL_, _defaultConditions_).
> 5.  Otherwise,
>     1.  Note: _specifier_ is now a bare specifier.
>     2.  Set _resolved_ the result of **PACKAGE_RESOLVE**(_specifier_, _parentURL_).
> 6.  Let _format_ be **undefined**.
> 7.  If _resolved_ is a _"file:"_ URL, then
>     1.  If _resolved_ contains any percent encodings of _"/"_ or _"\\"_ (_"%2F"_ and _"%5C"_ respectively), then
>         1.  Throw an _Invalid Module Specifier_ error.
>     2.  If the file at _resolved_ is a directory, then
>         1.  Throw an _Unsupported Directory Import_ error.
>     3.  If the file at _resolved_ does not exist, then
>         1.  Throw a _Module Not Found_ error.
>     4.  Set _resolved_ to the real path of _resolved_, maintaining the same URL querystring and fragment components.
>     5.  Set _format_ to the result of **ESM_FILE_FORMAT**(_resolved_).
> 8.  Otherwise,
>     1.  Set _format_ the module format of the content type associated with the URL _resolved_.
> 9.  Load _resolved_ as module format, _format_.

**PACKAGE_RESOLVE**(_packageSpecifier_, _parentURL_)

> 1.  Let _packageName_ be **undefined**.
> 2.  If _packageSpecifier_ is an empty string, then
>     1.  Throw an _Invalid Module Specifier_ error.
> 3.  If _packageSpecifier_ is a Node.js builtin module name, then
>     1.  Return the string _"node:"_ concatenated with _packageSpecifier_.
> 4.  If _packageSpecifier_ does not start with _"@"_, then
>     1.  Set _packageName_ to the substring of _packageSpecifier_ until the first _"/"_ separator or the end of the string.
> 5.  Otherwise,
>     1.  If _packageSpecifier_ does not contain a _"/"_ separator, then
>         1.  Throw an _Invalid Module Specifier_ error.
>     2.  Set _packageName_ to the substring of _packageSpecifier_ until the second _"/"_ separator or the end of the string.
> 6.  If _packageName_ starts with _"."_ or contains _"\\"_ or _"%"_, then
>     1.  Throw an _Invalid Module Specifier_ error.
> 7.  Let _packageSubpath_ be _"."_ concatenated with the substring of _packageSpecifier_ from the position at the length of _packageName_.
> 8.  If _packageSubpath_ ends in _"/"_, then
>     1.  Throw an _Invalid Module Specifier_ error.
> 9.  Let _selfUrl_ be the result of **PACKAGE_SELF_RESOLVE**(_packageName_, _packageSubpath_, _parentURL_).
> 10. If _selfUrl_ is not **undefined**, return _selfUrl_.
> 11. While _parentURL_ is not the file system root,
> 12. Let _packageURL_ be the URL resolution of _"node_modules/"_ concatenated with _packageSpecifier_, relative to _parentURL_.
> 13. Set _parentURL_ to the parent folder URL of _parentURL_.
> 14. If the folder at _packageURL_ does not exist, then
>     1.  Continue the next loop iteration.
> 15. Let _pjson_ be the result of **READ_PACKAGE_JSON**(_packageURL_).
> 16. If _pjson_ is not **null** and _pjson_._exports_ is not **null** or **undefined**, then
>     1.  Return the result of **PACKAGE_EXPORTS_RESOLVE**(_packageURL_, _packageSubpath_, _pjson.exports_, _defaultConditions_).
> 17. Otherwise, if _packageSubpath_ is equal to _"."_, then
>     1.  If _pjson.main_ is a string, then
>         1.  Return the URL resolution of _main_ in _packageURL_.
> 18. Otherwise,
>     1.  Return the URL resolution of _packageSubpath_ in _packageURL_.
> 19. Throw a _Module Not Found_ error.

**PACKAGE_SELF_RESOLVE**(_packageName_, _packageSubpath_, _parentURL_)

> 1.  Let _packageURL_ be the result of **LOOKUP_PACKAGE_SCOPE**(_parentURL_).
> 2.  If _packageURL_ is **null**, then
>     1.  Return **undefined**.
> 3.  Let _pjson_ be the result of **READ_PACKAGE_JSON**(_packageURL_).
> 4.  If _pjson_ is **null** or if _pjson_._exports_ is **null** or **undefined**, then
>     1.  Return **undefined**.
> 5.  If _pjson.name_ is equal to _packageName_, then
>     1.  Return the result of **PACKAGE_EXPORTS_RESOLVE**(_packageURL_, _packageSubpath_, _pjson.exports_, _defaultConditions_).
> 6.  Otherwise, return **undefined**.

**PACKAGE_EXPORTS_RESOLVE**(_packageURL_, _subpath_, _exports_, _conditions_)

> 1.  If _exports_ is an Object with both a key starting with _"."_ and a key not starting with _"."_, throw an _Invalid Package Configuration_ error.
> 2.  If _subpath_ is equal to _"."_, then
>     1.  Let _mainExport_ be **undefined**.
>     2.  If _exports_ is a String or Array, or an Object containing no keys starting with _"."_, then
>         1.  Set _mainExport_ to _exports_.
>     3.  Otherwise if _exports_ is an Object containing a _"."_ property, then
>         1.  Set _mainExport_ to _exports_\[_"."_\].
>     4.  If _mainExport_ is not **undefined**, then
>         1.  Let _resolved_ be the result of **PACKAGE_TARGET_RESOLVE**( _packageURL_, _mainExport_, **null**, **false**, _conditions_).
>         2.  If _resolved_ is not **null** or **undefined**, return _resolved_.
> 3.  Otherwise, if _exports_ is an Object and all keys of _exports_ start with _"."_, then
>     1.  Let _matchKey_ be the string _"./"_ concatenated with _subpath_.
>     2.  Let _resolved_ be the result of **PACKAGE_IMPORTS_EXPORTS_RESOLVE**( _matchKey_, _exports_, _packageURL_, **false**, _conditions_).
>     3.  If _resolved_ is not **null** or **undefined**, return _resolved_.
> 4.  Throw a _Package Path Not Exported_ error.

**PACKAGE_IMPORTS_RESOLVE**(_specifier_, _parentURL_, _conditions_)

> 1.  Assert: _specifier_ begins with _"#"_.
> 2.  If _specifier_ is exactly equal to _"#"_ or starts with _"#/"_, then
>     1.  Throw an _Invalid Module Specifier_ error.
> 3.  Let _packageURL_ be the result of **LOOKUP_PACKAGE_SCOPE**(_parentURL_).
> 4.  If _packageURL_ is not **null**, then
>     1.  Let _pjson_ be the result of **READ_PACKAGE_JSON**(_packageURL_).
>     2.  If _pjson.imports_ is a non-null Object, then
>         1.  Let _resolved_ be the result of **PACKAGE_IMPORTS_EXPORTS_RESOLVE**( _specifier_, _pjson.imports_, _packageURL_, **true**, _conditions_).
>         2.  If _resolved_ is not **null** or **undefined**, return _resolved_.
> 5.  Throw a _Package Import Not Defined_ error.

**PACKAGE_IMPORTS_EXPORTS_RESOLVE**(_matchKey_, _matchObj_, _packageURL_, _isImports_, _conditions_)

> 1.  If _matchKey_ is a key of _matchObj_ and does not contain _"\*"_, then
>     1.  Let _target_ be the value of _matchObj_\[_matchKey_\].
>     2.  Return the result of **PACKAGE_TARGET_RESOLVE**(_packageURL_, _target_, **null**, _isImports_, _conditions_).
> 2.  Let _expansionKeys_ be the list of keys of _matchObj_ containing only a single _"\*"_, sorted by the sorting function **PATTERN_KEY_COMPARE** which orders in descending order of specificity.
> 3.  For each key _expansionKey_ in _expansionKeys_, do
>     1.  Let _patternBase_ be the substring of _expansionKey_ up to but excluding the first _"\*"_ character.
>     2.  If _matchKey_ starts with but is not equal to _patternBase_, then
>         1.  Let _patternTrailer_ be the substring of _expansionKey_ from the index after the first _"\*"_ character.
>         2.  If _patternTrailer_ has zero length, or if _matchKey_ ends with _patternTrailer_ and the length of _matchKey_ is greater than or equal to the length of _expansionKey_, then
>             1.  Let _target_ be the value of _matchObj_\[_expansionKey_\].
>             2.  Let _patternMatch_ be the substring of _matchKey_ starting at the index of the length of _patternBase_ up to the length of _matchKey_ minus the length of _patternTrailer_.
>             3.  Return the result of **PACKAGE_TARGET_RESOLVE**(_packageURL_, _target_, _patternMatch_, _isImports_, _conditions_).
> 4.  Return **null**.

**PATTERN_KEY_COMPARE**(_keyA_, _keyB_)

> 1.  Assert: _keyA_ ends with _"/"_ or contains only a single _"\*"_.
> 2.  Assert: _keyB_ ends with _"/"_ or contains only a single _"\*"_.
> 3.  Let _baseLengthA_ be the index of _"\*"_ in _keyA_ plus one, if _keyA_ contains _"\*"_, or the length of _keyA_ otherwise.
> 4.  Let _baseLengthB_ be the index of _"\*"_ in _keyB_ plus one, if _keyB_ contains _"\*"_, or the length of _keyB_ otherwise.
> 5.  If _baseLengthA_ is greater than _baseLengthB_, return -1.
> 6.  If _baseLengthB_ is greater than _baseLengthA_, return 1.
> 7.  If _keyA_ does not contain _"\*"_, return 1.
> 8.  If _keyB_ does not contain _"\*"_, return -1.
> 9.  If the length of _keyA_ is greater than the length of _keyB_, return -1.
> 10. If the length of _keyB_ is greater than the length of _keyA_, return 1.
> 11. Return 0.

**PACKAGE_TARGET_RESOLVE**(_packageURL_, _target_, _patternMatch_, _isImports_, _conditions_)

> 1.  If _target_ is a String, then
>     1.  If _target_ does not start with _"./"_, then
>         1.  If _isImports_ is **false**, or if _target_ starts with _"../"_ or _"/"_, or if _target_ is a valid URL, then
>             1.  Throw an _Invalid Package Target_ error.
>         2.  If _patternMatch_ is a String, then
>             1.  Return **PACKAGE_RESOLVE**(_target_ with every instance of _"\*"_ replaced by _patternMatch_, _packageURL_ + _"/"_).
>         3.  Return **PACKAGE_RESOLVE**(_target_, _packageURL_ + _"/"_).
>     2.  If _target_ split on _"/"_ or _"\\"_ contains any _""_, _"."_, _".."_, or _"node_modules"_ segments after the first _"."_ segment, case insensitive and including percent encoded variants, throw an _Invalid Package Target_ error.
>     3.  Let _resolvedTarget_ be the URL resolution of the concatenation of _packageURL_ and _target_.
>     4.  Assert: _resolvedTarget_ is contained in _packageURL_.
>     5.  If _patternMatch_ is **null**, then
>         1.  Return _resolvedTarget_.
>     6.  If _patternMatch_ split on _"/"_ or _"\\"_ contains any _""_, _"."_, _".."_, or _"node_modules"_ segments, case insensitive and including percent encoded variants, throw an _Invalid Module Specifier_ error.
>     7.  Return the URL resolution of _resolvedTarget_ with every instance of _"\*"_ replaced with _patternMatch_.
> 2.  Otherwise, if _target_ is a non-null Object, then
>     1.  If _exports_ contains any index property keys, as defined in ECMA-262 [6.1.7 Array Index](https://tc39.es/ecma262/#integer-index), throw an _Invalid Package Configuration_ error.
>     2.  For each property _p_ of _target_, in object insertion order as,
>         1.  If _p_ equals _"default"_ or _conditions_ contains an entry for _p_, then
>             1.  Let _targetValue_ be the value of the _p_ property in _target_.
>             2.  Let _resolved_ be the result of **PACKAGE_TARGET_RESOLVE**( _packageURL_, _targetValue_, _patternMatch_, _isImports_, _conditions_).
>             3.  If _resolved_ is equal to **undefined**, continue the loop.
>             4.  Return _resolved_.
>     3.  Return **undefined**.
> 3.  Otherwise, if _target_ is an Array, then
>     1.  If \_target.length is zero, return **null**.
>     2.  For each item _targetValue_ in _target_, do
>         1.  Let _resolved_ be the result of **PACKAGE_TARGET_RESOLVE**( _packageURL_, _targetValue_, _patternMatch_, _isImports_, _conditions_), continuing the loop on any _Invalid Package Target_ error.
>         2.  If _resolved_ is **undefined**, continue the loop.
>         3.  Return _resolved_.
>     3.  Return or throw the last fallback resolution **null** return or error.
> 4.  Otherwise, if _target_ is _null_, return **null**.
> 5.  Otherwise throw an _Invalid Package Target_ error.

**ESM_FILE_FORMAT**(_url_)

> 1.  Assert: _url_ corresponds to an existing file.
> 2.  If _url_ ends in _".mjs"_, then
>     1.  Return _"module"_.
> 3.  If _url_ ends in _".cjs"_, then
>     1.  Return _"commonjs"_.
> 4.  If _url_ ends in _".json"_, then
>     1.  Return _"json"_.
> 5.  Let _packageURL_ be the result of **LOOKUP_PACKAGE_SCOPE**(_url_).
> 6.  Let _pjson_ be the result of **READ_PACKAGE_JSON**(_packageURL_).
> 7.  If _pjson?.type_ exists and is _"module"_, then
>     1.  If _url_ ends in _".js"_, then
>         1.  Return _"module"_.
>     2.  Throw an _Unsupported File Extension_ error.
> 8.  Otherwise,
>     1.  Throw an _Unsupported File Extension_ error.

**LOOKUP_PACKAGE_SCOPE**(_url_)

> 1.  Let _scopeURL_ be _url_.
> 2.  While _scopeURL_ is not the file system root,
>     1.  Set _scopeURL_ to the parent URL of _scopeURL_.
>     2.  If _scopeURL_ ends in a _"node_modules"_ path segment, return **null**.
>     3.  Let _pjsonURL_ be the resolution of _"package.json"_ within _scopeURL_.
>     4.  if the file at _pjsonURL_ exists, then
>         1.  Return _scopeURL_.
> 3.  Return **null**.

**READ_PACKAGE_JSON**(_packageURL_)

> 1.  Let _pjsonURL_ be the resolution of _"package.json"_ within _packageURL_.
> 2.  If the file at _pjsonURL_ does not exist, then
>     1.  Return **null**.
> 3.  If the file at _packageURL_ does not parse as valid JSON, then
>     1.  Throw an _Invalid Package Configuration_ error.
> 4.  Return the parsed JSON source of the file at _pjsonURL_.

## Customizing ESM specifier resolution algorithm[#](#customizing-esm-specifier-resolution-algorithm)

The [Loaders API](#loaders) provides a mechanism for customizing the ESM specifier resolution algorithm. An example loader that provides CommonJS-style resolution for ESM specifiers is [commonjs-extension-resolution-loader](https://github.com/nodejs/loaders-test/tree/main/commonjs-extension-resolution-loader).
