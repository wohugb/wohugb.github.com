## 安装

```sh
$ mkdir myapp
$ cd myapp
$ npm init
$ entry point: (index.js)
$ npm install express --save
```

## 使用

```js
var express = require('express');
var app = express();

app.get('/', function (req, res) {
  res.send('Hello World!');
});

app.listen(3000, function () {
  console.log('Example app listening on port 3000!');
});
```

```sh
$ node app.js
```