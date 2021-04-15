# JavaScript中的RSA和ECC

jsbn库是纯JavaScript中的大数学运算的快速，便携式实现，可在桌面和移动浏览器上启用公钥密码和其他应用程序。

## 演示

* RSA Encryption Demo - 使用公钥对字符串进行简单的RSA加密
* RSA Cryptography Demo - 更完整的RSA加密，解密和密钥生成演示
* ECDH Key Agreement Demo - 使用椭圆曲线的Diffie-Hellman密钥协议

## 源代码

jsbn库的API与Jav​​a中的java.math.BigInteger类非常相似。 例如：

```sh
  x = new BigInteger("abcd1234", 16);
  y = new BigInteger("beef", 16);
  z = x.mod(y);
  alert(z.toString(16));
```

将打印b60c。

### 核心代码库

* jsbn.js - 基本的BigInteger实现，刚好足够用于RSA加密，而不是更多。
* jsbn2.js - 包括大多数公共BigInteger方法在内的其他库。

### RSA

* rsa.js - 实施RSA加密，不需要jsbn2.js。
* rsa2.js - 其余的RSA算法，包括解密和keygen。

### ECC

* ec.js - 椭圆曲线数学，取决于jsbn.js和jsbn2.js
* sec.js - 标准椭圆曲线参数

### 公用事业

* rng.js - 基本熵收集器和RNG接口，需要PRNG后端来定义prng_newstate()。
* prng4.js - rng.js基于ARC4的PRNG后端，非常小巧。
* base64.js - Base64编码和解码例程。
* sha1.js - SHA-1散列函数，仅用于IBE演示。

## 互通性

该演示使用PKCS＃1加密样式填充（类型2）直接加密字符串，这是目前唯一支持的格式。
要显示与可解密字符串的潜在基于OpenSSL的后端的互操作性，请在任何安装了OpenSSL命令行工具的系统上尝试以下操作：

1. 生成一个新的公钥/私钥对:

    ```sh
    $ openssl genrsa -out key.pem
    Generating RSA private key, 512 bit long modulus
    ..++++++++++++
    ..............++++++++++++
    e is 65537 (0x10001)
    $
    ```

1. 从您的密钥中提取模数:

    ```sh
    $ openssl rsa -in key.pem -noout -modulus
    Modulus=DA3BB4C40E3C7E76F7DBDD8BF3DF0714CA39D3A0F7F9D7C2E4FEDF8C7B28C2875F7EB98950B22AE82D539C1ABC1AB550BA0B2D52E3EF7BDFB78A5E817D74BBDB
    $
    ```

1. 转到RSA Encryption演示，并将模数值粘贴到底部的“Modulus（十六进制）”字段中。
1. 确保“公开指数”字段中的值是“10001”，或公钥使用的任何值。
1. 在“Plaintext（字符串）”字段中输入一个短字符串（例如测试）并点击“加密”。 结果应显示在“密文”字段中。
1. 复制密文的base64版本并将其粘贴为以下命令的输入：

    ```sh
    $ openssl base64 -d | openssl rsautl -inkey key.pem -decrypt
    1JW24UMKntVhmmDilAYC1AjLxgiWHBzTzZsCVAejLjVri92abLHkSyLisVyAdYVr
    fiS7FchtI9vupe9JF/m3Kg==
    Hit ctrl-D or whatever your OS uses for end-of-file. Your original plaintext should appear:
    testing$
    ```

## 性能

速度表包含jsbn执行公共密钥操作（如RSA，ECC和IBE）的详细时间信息。

## 使用jsbn的项目

* Forge - 一个纯SSL / TLS的JavaScript实现，包括他们对BigInteger库选择的讨论
* Dojo Toolkit在其dojox.math.BigInteger类中使用jsbn。
* 没有更多明文密码 - 由于性能原因，此项目从另一个JavaScript BigInteger库中切换
* Google的V8基准测试套件，版本6
* JavaScript加密工具包
* RSA-Sign JavaScript库
* JavaScript RSA

## 历史

1. Version 1.4 (7/1/2013):

    修复sha1.js和base64.js之间的变量名称冲突。
    在可用的情况下从window.crypto.getRandomValues获取熵。
    增加了ECCurveFp.encodePointHex。
    修复了在jsbn.js中使用DV不一致的问题。

1. Version 1.3 (7/3/2012):

    修正了比较不同字长的负整数时的错误。

1. Version 1.2 (3/29/2011):

    增加了方法来提高ECC性能。
    在isProbablePrime中使用随机基

1. Version 1.1 (9/15/2009):

    PKCS1编码和解码JavaScript字符串时，增加了对非ASCII字符的utf-8编码的支持。
    修正了以非2的幂次方式创建新的BigInteger（“0”）时的错误。

## 许可

jsbn在BSD许可下发布。 详情请参阅许可证。

----------

Tom Wu 上次修改时间：9月15日星期二23:30:00 PST 2009