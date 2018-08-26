# Node-RSA

Node.js RSA库

基于Tom Wu的jsbn库 http://www-cs-students.stanford.edu/~tjw/jsbn/

* 纯JavaScript
* 不需要OpenSSL
* 生成密钥
* 支持加密/解密的长消息
* 签署和验证

## 例

```javascript
const NodeRSA = require('node-rsa');
const key = new NodeRSA({b: 512});

const text = 'Hello RSA!';
const encrypted = key.encrypt(text, 'base64');
console.log('encrypted: ', encrypted);
const decrypted = key.decrypt(encrypted, 'utf8');
console.log('decrypted: ', decrypted);
```

## 安装

```shell
npm install node-rsa
```

> <sub>Requires nodejs >= 8.11.1</sub>

### 测试

```shell
npm test
```

## 工作环境

该库主要为Node.js开发并测试了， 但它仍然可以在浏览器中使用[browserify](http://browserify.org/).

## 用法

### 创建实例

```javascript
const NodeRSA = require('node-rsa');

const key = new NodeRSA([keyData, [format]], [options]);
```

* keyData — `{string|buffer|object}` — 以支持的格式之一生成密钥或密钥的参数。
* format — `{string}` — 导入密钥格式。 在[导出/导入](#importexport-keys)部分查看有关格式的更多详细信息。
* options — `{object}` — 其他设置.

#### 选项

您可以通过第二个/第三个构造函数参数或`key.setOptions()`方法指定一些选项。

* environment — 工作环境（默认自动检测）:
  * `'browser'` — 将运行RSA算法的纯js实现.
  * `'node'` 对于`nodejs> = 0.10.x或io.js> = 1.x` — 提供一些本地方法，如签名/验证和加密/解密.
* encryptionScheme — 用于加密/解密的填充方案. 可以是`'pkcs1_oaep'` 或 `'pkcs1'`. 默认 `'pkcs1_oaep'`.
* signingScheme — 用于签名和验证的方案。 可以使`'pkcs1'` 或 `'pss'` 或 'scheme-hash' 格式字符串 (例如 `'pss-sha1'`). 默认 `'pkcs1-sha256'`, 或者, 如果选择pss: `'pss-sha1'`.

> *注意:* 这个lib支持下一个哈希算法: `'md5'`, `'ripemd160'`, `'sha1'`, `'sha256'`, `'sha512'` in browser and node environment and additional `'md4'`, `'sha'`, `'sha224'`, `'sha384'` in node only.

#### 高级选项

您也可以为这样的一些方案指定高级选项:

```javascript
options = {
  encryptionScheme: {
    scheme: 'pkcs1_oaep', //scheme
    hash: 'md5', //hash using for scheme
    mgf: function(...) {...} //mask generation function
  },
  signingScheme: {
    scheme: 'pss', //scheme
    hash: 'sha1', //hash using for scheme
    saltLength: 20 //salt length for pss sign
  }
}
```

```javascript
options = {
  encryptionScheme: {
    scheme:'pkcs1',
    padding: constants.RSA_NO_PADDING
  }
}
```

> *NOTICE:* encryptionScheme.hash, encryptionScheme.mfg and signingScheme.saltLength don't work in `node` environment

#### 创建 "空" 键

```javascript
const key = new NodeRSA();
```

#### 生成新的512位长度密钥

```javascript
const key = new NodeRSA({b: 512});
```

你也可以使用下一个方法:

```javascript
key.generateKeyPair([bits], [exp]);
```

* bits — `{int}` — 密钥大小以位为单位。 2048默认。
* exp — `{int}` — 公开指数。 默认情况下为65537。

#### 从PEM字符串加载密钥

```javascript
const key = new NodeRSA('-----BEGIN RSA PRIVATE KEY-----\n'+
                      'MIIBOQIBAAJAVY6quuzCwyOWzymJ7C4zXjeV/232wt2ZgJZ1kHzjI73wnhQ3WQcL\n'+
                      'DFCSoi2lPUW8/zspk0qWvPdtp6Jg5Lu7hwIDAQABAkBEws9mQahZ6r1mq2zEm3D/\n'+
                      'VM9BpV//xtd6p/G+eRCYBT2qshGx42ucdgZCYJptFoW+HEx/jtzWe74yK6jGIkWJ\n'+
                      'AiEAoNAMsPqwWwTyjDZCo9iKvfIQvd3MWnmtFmjiHoPtjx0CIQCIMypAEEkZuQUi\n'+
                      'pMoreJrOlLJWdc0bfhzNAJjxsTv/8wIgQG0ZqI3GubBxu9rBOAM5EoA4VNjXVigJ\n'+
                      'QEEk1jTkp8ECIQCHhsoq90mWM/p9L5cQzLDWkTYoPI49Ji+Iemi2T5MRqwIgQl07\n'+
                      'Es+KCn25OKXR/FJ5fu6A6A+MptABL3r8SEjlpLc=\n'+
                      '-----END RSA PRIVATE KEY-----');
```

### 导入/导出密钥

```javascript
key.importKey(keyData, [format]);
key.exportKey([format]);
```

* keyData — `{string|buffer}` — may be:
    * key in PEM string
    * Buffer containing PEM string
    * Buffer containing DER encoded data
    * Object contains key components
* format  — `{string}` — format id for export/import.

#### 格式字符串语法

格式化字符串由几部分组成: `scheme-[key_type]-[output_type]`

Scheme — NodeRSA支持导入/导出密钥的多种格式方案:

* `'pkcs1'` — 公钥从 `'-----BEGIN RSA PUBLIC KEY-----'` 头 和 私钥从 `'-----BEGIN RSA PRIVATE KEY-----'` 头
* `'pkcs8'` — 公钥从 `'-----BEGIN PUBLIC KEY-----'` 头 和 私钥从 `'-----BEGIN PRIVATE KEY-----'` 头
* `'components'` — 将它用于从/到原始组件的导入/导出密钥（请参见下面的示例）. 对于私钥， 导入数据应该包含所有私钥组件， 为公钥: only public exponent (`e`) and modulus (`n`). All components (except `e`) should be Buffer, `e` could be Buffer or just normal Number.

Key type — can be `'private'` or `'public'`. Default `'private'`
Output type — can be:

* `'pem'` — Base64 encoded string with header and footer. Used by default.
* `'der'` — Binary encoded key data.

> *注意:* For import, if *keyData* is PEM string or buffer containing string, you can do not specify format, but if you provide *keyData* as DER you must specify it in format string.

**快捷键和例子**

* `'private'` or `'pkcs1'` or `'pkcs1-private'` == `'pkcs1-private-pem'` — private key encoded in pcks1 scheme as pem string.
* `'public'` or `'pkcs8-public'` == `'pkcs8-public-pem'` — public key encoded in pcks8 scheme as pem string.
* `'pkcs8'` or `'pkcs8-private'` == `'pkcs8-private-pem'` — private key encoded in pcks8 scheme as pem string.
* `'pkcs1-der'` == `'pkcs1-private-der'` — private key encoded in pcks1 scheme as binary buffer.
* `'pkcs8-public-der'` — public key encoded in pcks8 scheme as binary buffer.

**代码示例**

```javascript
const keyData = '-----BEGIN PUBLIC KEY----- ... -----END PUBLIC KEY-----';
key.importKey(keyData, 'pkcs8');
const publicDer = key.exportKey('pkcs8-public-der');
const privateDer = key.exportKey('pkcs1-der');
```

```javascript
key.importKey({
    n: Buffer.from('0086fa9ba066685845fc03833a9699c8baefb53cfbf19052a7f10f1eaa30488cec1ceb752bdff2df9fad6c64b3498956e7dbab4035b4823c99a44cc57088a23783', 'hex'),
    e: 65537,
    d: Buffer.from('5d2f0dd982596ef781affb1cab73a77c46985c6da2aafc252cea3f4546e80f40c0e247d7d9467750ea1321cc5aa638871b3ed96d19dcc124916b0bcb296f35e1', 'hex'),
    p: Buffer.from('00c59419db615e56b9805cc45673a32d278917534804171edcf925ab1df203927f', 'hex'),
    q: Buffer.from('00aee3f86b66087abc069b8b1736e38ad6af624f7ea80e70b95f4ff2bf77cd90fd', 'hex'),
    dmp1: Buffer.from('008112f5a969fcb56f4e3a4c51a60dcdebec157ee4a7376b843487b53844e8ac85', 'hex'),
    dmq1: Buffer.from('1a7370470e0f8a4095df40922a430fe498720e03e1f70d257c3ce34202249d21', 'hex'),
    coeff: Buffer.from('00b399675e5e81506b729a777cc03026f0b2119853dfc5eb124610c0ab82999e45', 'hex')
}, 'components');
const publicComponents = key.exportKey('components-public');
console.log(publicComponents);

/*
{ n: <Buffer 00 86 fa 9b a0 66 68 58 45 fc 03 83 3a 96 99 c8 ba ef b5 3c fb f1 90 52 a7 f1 0f 1e aa 30 48 8c ec 1c eb 75 2b df f2 df 9f ad 6c 64 b3 49 89 56 e7 db ... >,
  e: 65537
}
*/
```

如果你只想输入公共密钥``components-public'`作为选项:

```javascript
key.importKey({
    n: Buffer.from('0086fa9ba066685845fc03833a9699c8baefb53cfbf19052a7f10f1eaa30488cec1ceb752bdff2df9fad6c64b3498956e7dbab4035b4823c99a44cc57088a23783', 'hex'),
    e: 65537,
}, 'components-public');
```

### 属性

#### 键测试

```javascript
key.isPrivate();
key.isPublic([strict]);
```

strict — `{boolean}` — if true method will return false if key pair have private exponent. Default `false`.

```javascript
key.isEmpty();
```

如果密钥对没有任何数据，则返回“true”。

#### 键信息

```javascript
key.getKeySize();
```

Return key size in bits.

```javascript
key.getMaxMessageSize();
```

Return max data size for encrypt in bytes.

### 加密/解密

```javascript
key.encrypt(buffer, [encoding], [source_encoding]);
key.encryptPrivate(buffer, [encoding], [source_encoding]); // use private key for encryption
```

Return encrypted data.

* buffer — `{buffer}` —  data for encrypting, may be string, Buffer, or any object/array. Arrays and objects will encoded to JSON string first.
* encoding — `{string}` — encoding for output result, may be `'buffer'`, `'binary'`, `'hex'` or `'base64'`. Default `'buffer'`.
* source_encoding — `{string}` —  source encoding, works only with string buffer. Can take standard Node.js Buffer encodings (hex, utf8, base64, etc). `'utf8'` by default.

```javascript
key.decrypt(buffer, [encoding]);
key.decryptPublic(buffer, [encoding]); // use public key for decryption
```

Return decrypted data.

* buffer — `{buffer}` — data for decrypting. Takes Buffer object or base64 encoded string.
* encoding — `{string}` — encoding for result string. Can also take `'buffer'` for raw Buffer object, or `'json'` for automatic JSON.parse result. Default `'buffer'`.

> *Notice:* `encryptPrivate` and `decryptPublic` using only pkcs1 padding type 1 (not random)

### 签名/验证

```javascript
key.sign(buffer, [encoding], [source_encoding]);
```

Return signature for buffer. All the arguments are the same as for `encrypt` method.

```javascript
key.verify(buffer, signature, [source_encoding], [signature_encoding])
```

Return result of check, `true` or `false`.

* buffer — `{buffer}` — data for check, same as `encrypt` method.
* signature — `{string}` — signature for check, result of `sign` method.
* source_encoding — `{string}` — same as for `encrypt` method.
* signature_encoding — `{string}` — encoding of given signature. May be `'buffer'`, `'binary'`, `'hex'` or `'base64'`. Default `'buffer'`.

## 特约

Questions, comments, bug reports, and pull requests are all welcome.

## 更新日志

### 1.0.0

* Using semver now 🎉
* **Breaking change**: Drop support nodejs < 8.11.1
* **Possible breaking change**: `new Buffer()` call as deprecated was replaced by `Buffer.from` & `Buffer.alloc`.
* **Possible breaking change**: Drop support for hash scheme `sha` (was removed in node ~10). `sha1`, `sha256` and others still works.
* **Possible breaking change**: Little change in environment detect algorithm.

### 0.4.2

* `no padding` scheme will padded data with zeros on all environments.

### 0.4.1

* `PKCS1 no padding` scheme support.

### 0.4.0

* License changed from BSD to MIT.
* Some changes in internal api.

### 0.3.3

* Fixed PSS encode/verify methods with max salt length.

### 0.3.2

* Fixed environment detection in web worker.

### 0.3.0

* Added import/export from/to raw key components.
* Removed lodash from dependencies.

### 0.2.30

* Fixed a issue when the key was generated by 1 bit smaller than specified. It may slow down the generation of large keys.

### 0.2.24

* Now used old hash APIs for webpack compatible.

### 0.2.22

* `encryptPrivate` and `decryptPublic` now using only pkcs1 (type 1) padding.

### 0.2.20

* Added `.encryptPrivate()` and `.decryptPublic()` methods.
* Encrypt/decrypt methods in nodejs 0.12.x and io.js using native implementation (> 40x speed boost).
* Fixed some regex issue causing catastrophic backtracking.

### 0.2.10

* **Methods `.exportPrivate()` and `.exportPublic()` was replaced by `.exportKey([format])`.**
  * By default `.exportKey()` returns private key as `.exportPrivate()`, if you need public key from `.exportPublic()` you must specify format as `'public'` or `'pkcs8-public-pem'`.
* Method `.importKey(key, [format])` now has second argument.

### 0.2.0

* **`.getPublicPEM()` method was renamed to `.exportPublic()`**
* **`.getPrivatePEM()` method was renamed to `.exportPrivate()`**
* **`.loadFromPEM()` method was renamed to `.importKey()`**
* Added PKCS1_OAEP encrypting/decrypting support.
  * **PKCS1_OAEP now default scheme, you need to specify 'encryptingScheme' option to 'pkcs1' for compatibility with 0.1.x version of NodeRSA.**
* Added PSS signing/verifying support.
* Signing now supports `'md5'`, `'ripemd160'`, `'sha1'`, `'sha256'`, `'sha512'` hash algorithms in both environments
and additional `'md4'`, `'sha'`, `'sha224'`, `'sha384'` for nodejs env.
* **`options.signingAlgorithm` was renamed to `options.signingScheme`**
* Added `encryptingScheme` option.
* Property `key.options` now mark as private. Added `key.setOptions(options)` method.

### 0.1.54

* Added support for loading PEM key from Buffer (`fs.readFileSync()` output).
* Added `isEmpty()` method.

### 0.1.52

* Improve work with not properly trimming PEM strings.

### 0.1.50

* Implemented native js signing and verifying for browsers.
* `options.signingAlgorithm` now takes only hash-algorithm name.
* Added `.getKeySize()` and `.getMaxMessageSize()` methods.
* `.loadFromPublicPEM` and `.loadFromPrivatePEM` methods marked as private.

### 0.1.40

* Added signing/verifying.

### 0.1.30

* Added long message support.

## 许可

Copyright (c) 2014  rzcoder

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## 用于rsa.js和jsbn.js中代码的许可

Copyright (c) 2003-2005  Tom Wu

All Rights Reserved.

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS-IS" AND WITHOUT WARRANTY OF ANY KIND,
EXPRESS, IMPLIED OR OTHERWISE, INCLUDING WITHOUT LIMITATION, ANY
WARRANTY OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE.

IN NO EVENT SHALL TOM WU BE LIABLE FOR ANY SPECIAL, INCIDENTAL,
INDIRECT OR CONSEQUENTIAL DAMAGES OF ANY KIND, OR ANY DAMAGES WHATSOEVER
RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER OR NOT ADVISED OF
THE POSSIBILITY OF DAMAGE, AND ON ANY THEORY OF LIABILITY, ARISING OUT
OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

In addition, the following condition applies:

All redistributions must retain an intact copy of this copyright notice
and disclaimer.

[![Build Status](https://travis-ci.org/rzcoder/node-rsa.svg?branch=master)](https://travis-ci.org/rzcoder/node-rsa)