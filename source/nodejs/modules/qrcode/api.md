## API

Browser:

- [create()](#createtext-options)
- [toCanvas()](#tocanvascanvaselement-text-options-cberror)
- [toDataURL()](#todataurltext-options-cberror-url)
- [toString()](#tostringtext-options-cberror-string)

Server:

- [create()](#createtext-options)
- [toCanvas()](#tocanvascanvas-text-options-cberror)
- [toDataURL()](todataurltext-options-cberror-url-1)
- [toString()](#tostringtext-options-cberror-string-1)
- [toFile()](#tofilepath-text-options-cberror)
- [toFileStream()](#tofilestreamstream-text-options)

### 浏览器

??? info "`create(text, [options])`"

    Creates QR Code symbol and returns a qrcode object.

    `text`

    类型: `String|Array`

    Text to encode or a list of objects describing segments.

    `options`

    See [QR Code options](#qr-code-options).

    `returns`

    类型: `Object`

    ```javascript
    // QRCode object
    {
      modules,              // Bitmatrix class with modules data
      version,              // Calculated QR Code version
      errorCorrectionLevel, // Error Correction Level
      maskPattern,          // Calculated Mask pattern
      segments              // Generated segments
    }
    ```

??? info "`toCanvas(canvasElement, text, [options], [cb(error)])`"

??? info "`toCanvas(text, [options], [cb(error, canvas)])`"

    Draws qr code symbol to canvas.
    If `canvasElement` is omitted a new canvas is returned.

    `canvasElement`

    类型: `DOMElement`

    Canvas where to draw QR Code.

    `text`

    类型: `String|Array`

    Text to encode or a list of objects describing segments.

    `options`

    See [Options](#options).

    `cb`

    类型: `Function`

    Callback function called on finish.

    ***Example***

    ```javascript
      QRCode.toCanvas('text', { errorCorrectionLevel: 'H' }, function (err, canvas) {
        if (err) throw err

        var container = document.getElementById('container')
        container.appendChild(canvas)
      })
    ```

??? info "`toDataURL(text, [options], [cb(error, url)])`"

??? info "`toDataURL(canvasElement, text, [options], [cb(error, url)])`"
    Returns a Data URI containing a representation of the QR Code image.
    If provided, `canvasElement` will be used as canvas to generate the data URI.

    `canvasElement`

    类型: `DOMElement`

    Canvas where to draw QR Code.

    `text`

    类型: `String|Array`

    Text to encode or a list of objects describing segments.

    `options`
    - `type`

      类型: `String`
      默认:  `image/png`

      Data URI format.
      Possible values are: `image/png`, `image/jpeg`, `image/webp`.
      **Note: `image/webp` only works in Chrome browser.**

    - `rendererOpts.quality`

      类型: `Number`
      默认:  `0.92`

      A Number between `0` and `1` indicating image quality if the requested type is `image/jpeg` or `image/webp`.

    See [Options](#options) for other settings.

    `cb`

    类型: `Function`

    Callback function called on finish.

    ***Example***

    ```javascript
    var opts = {
      errorCorrectionLevel: 'H',
      类型: 'image/jpeg',
      rendererOpts: {
        quality: 0.3
      }
    }

    QRCode.toDataURL('text', opts, function (err, url) {
      if (err) throw err

      var img = document.getElementById('image')
      img.src = url
    })
    ```

??? info "`toString(text, [options], [cb(error, string)])`"

    Returns a string representation of the QR Code.
    Currently only works for SVG.

    `text`

    类型: `String|Array`

    Text to encode or a list of objects describing segments.

    `options`

    - `type`

      类型: `String`
      默认:  `svg`

      Output format.
      Possible values are: `svg`.

    See [Options](#options) for other settings.

    `cb`

    类型: `Function`

    Callback function called on finish.

    ***Example***

    ```javascript
    QRCode.toString('http://www.google.com', function (err, string) {
      if (err) throw err
      console.log(string)
    })
    ```

### 服务器

??? info "`create(text, [options])`"

    See [create](#createtext-options).

??? info "`toCanvas(canvas, text, [options], [cb(error)])`"

    Draws qr code symbol to [node canvas](https://github.com/Automattic/node-canvas).

    `text`

    类型: `String|Array`

    Text to encode or a list of objects describing segments.

    `options`

    See [Options](#options).

    `cb`

    类型: `Function`

    Callback function called on finish.

??? info "`toDataURL(text, [options], [cb(error, url)])`"

    Returns a Data URI containing a representation of the QR Code image.
    Only works with `image/png` type for now.

    `text`

    类型: `String|Array`

    Text to encode or a list of objects describing segments.

    `options`

    See [Options](#options) for other settings.

    `cb`

    类型: `Function`

    Callback function called on finish.

??? info "`toString(text, [options], [cb(error, string)])`"

    Returns a string representation of the QR Code.
    If choosen output format is `svg` it will returns a string containing xml code.

    `text`

    类型: `String|Array`

    Text to encode or a list of objects describing segments.

    `options`

    - `type`

      类型: `String`
      默认:  `utf8`

      Output format.
      Possible values are: `utf8`, `svg`, `terminal`.

    See [Options](#options) for other settings.

    `cb`

    类型: `Function`

    Callback function called on finish.

    ***Example***

    ```javascript
    QRCode.toString('http://www.google.com', function (err, string) {
      if (err) throw err
      console.log(string)
    })
    ```

??? info "`toFile(path, text, [options], [cb(error)])`"

    Saves QR Code to image file.
    If `options.type` is not specified, the format will be guessed from file extension.
    Recognized extensions are `png`, `svg`, `txt`.

    `path`

    类型: `String`

    文件保存路径.

    `text`

    类型: `String|Array`

    Text to encode or a list of objects describing segments.

    `options`

      - `type`

        类型: `String`

        默认:  `png`

        Output format.

        Possible values are: `png`, `svg`, `utf8`.

      - `rendererOpts.deflateLevel` **(png only)**

        类型: `Number`

        默认:  `9`

        Compression level for deflate.

      - `rendererOpts.deflateStrategy` **(png only)**

        类型: `Number`

        默认:  `3`

        Compression strategy for deflate.

    查询 [选项](#选项) 的其它设置.

    `cb`

    类型: `Function`

    结束回调函数.

    ***Example***

    ```javascript
    QRCode.toFile('path/to/filename.png', 'Some text', {
      color: {
        dark: '#00F',  // Blue dots
        light: '#0000' // Transparent background
      }
    }, function (err) {
      if (err) throw err
      console.log('done')
    })
    ```

??? info "`toFileStream(stream, text, [options])`"
    Writes QR Code image to stream. Only works with `png` format for now.

    `stream`

    类型: `stream.Writable`

    Node stream.

    `text`

    类型: `String|Array`

    Text to encode or a list of objects describing segments.

    `options`

    查询 [选项](#选项).

### 选项

??? info "QR Code 选项"

    `version`

      类型: `Number`

      QR Code version. If not specified the more suitable value will be calculated.

    `errorCorrectionLevel`

      类型: `String`

      默认:  `M`

      Error correction level.
      Possible values are `low, medium, quartile, high` or `L, M, Q, H`.

    `maskPattern`

      类型: `Number`

      Mask pattern used to mask the symbol.
      Possible values are `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`.
      If not specified the more suitable value will be calculated.

    `toSJISFunc`

      类型: `Function`

      Helper function used internally to convert a kanji to its Shift JIS value.
      Provide this function if you need support for Kanji mode.

??? info "渲染器选项"

    `margin`

      类型: `Number`

      默认:  `4`

      Define how much wide the quiet zone should be.

    `scale`

      类型: `Number`

      默认:  `4`

      Scale factor. A value of `1` means 1px per modules (black dots).

    `width`

      类型: `Number`

      Forces a specific width for the output image.
      If width is too small to contain the qr symbol, this option will be ignored.
      Takes precedence over `scale`.

    `color.dark`

    类型: `String`

    默认:  `#000000ff`

    Color of dark module. Value must be in hex format (RGBA).

    Note: dark color should always be darker than `color.light`.

    `color.light`

    类型: `String`

    默认:  `#ffffffff`

    Color of light module. Value must be in hex format (RGBA).