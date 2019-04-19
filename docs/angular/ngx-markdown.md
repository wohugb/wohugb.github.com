# ngx-markdown

ngx-markdown 是一个[Angular](https://angular.io/)库，它使用[标记](https://github.com/chjj/marked)来解析 html 与[Prism.js](http://prismjs.com/)的结合用于语法高亮。

- 可用演示 @ [https://jfcere.github.io/ngx-markdown](https://jfcere.github.io/ngx-markdown)
- 可用 Plunker @ [https://plnkr.co/edit/y5LPj7?p=preview](https://plnkr.co/edit/y5LPj7?p=preview)
- 可用 StackBlitz @ [https://stackblitz.com/edit/ngx-markdown](https://stackblitz.com/edit/ngx-markdown)

## 安装

### ngx-markdown

要将 ngx-markdown 库添加到`package.json`，请使用以下命令。

```bash
npm install ngx-markdown --save
```

由于库使用[标记](https://github.com/chjj/marked)解析器，您需要将`node_modules/marked/lib/marked.js`添加到您的应用程序中。

如果您使用的是[Angular CLI](https://cli.angular.io/)，可以按照下面的`angular.json`示例进行操作...

```diff
"scripts": [
+ "node_modules/marked/lib/marked.js"
]
```

### 语法高亮

> :bell: 语法高亮是**可选**，如果您不打算使用它，请跳过此步骤

要激活[Prism.js](http://prismjs.com/)语法高亮显示，您需要包含...

- prism.js 核心库 - `node_modules/prismjs/prism.js` 文件
- 一个突出的CSS主题 - 来自 `node_modules/prismjs/themes` 目录
- 所需的代码语言语法文件 - 来自 `node_modules/prismjs/components` 目录

_通过浏览网页可以找到其他主题，如[Prism-Themes](https://github.com/PrismJS/prism-themes)或[Mokokai](https://github.com/Ahrengot/Monokai-theme- for-Prism.js)例如。_

如果您使用的是[Angular CLI](https://cli.angular.io/)，可以按照下面的`angular.json`示例进行操作...

```diff
"styles": [
  "styles.css",
+ "node_modules/prismjs/themes/prism-okaidia.css"
],
"scripts": [
+ "node_modules/prismjs/prism.js",
+ "node_modules/prismjs/components/prism-csharp.min.js", # c-sharp language syntax
+ "node_modules/prismjs/components/prism-css.min.js" # css language syntax
]
```

#### 行号插件

要使用显示代码块中行号的[行号插件](http://prismjs.com/plugins/line-numbers/),除 Prism.js 配置文件外，还需要包含以下文件： `prismjs/plugins/line-numbers`目录到你的应用程序：

- css为行号设计样式 - `prism-line-numbers.css`
- 行号插件脚本 - `prism-line-numbers.js`

如果您使用的是[Angular CLI](https://cli.angular.io/)，可以按照下面的`angular.json`示例进行操作...

```diff
"styles": [
  "src/styles.css",
  "node_modules/prismjs/themes/prism-okaidia.css",
+ "node_modules/prismjs/plugins/line-numbers/prism-line-numbers.css"
],
"scripts": [
  "node_modules/prismjs/prism.js",
  "node_modules/prismjs/components/prism-csharp.min.js",
  "node_modules/prismjs/components/prism-css.min.js",
+ "node_modules/prismjs/plugins/line-numbers/prism-line-numbers.js"
]
```

使用`markdown`组件和/或指令，您将能够使用`lineNumbers`属性来激活插件。
该属性可以与用于变量绑定的`data`，用于远程内容的`src`或用于静态markdown的transclusion组合使用。


此外，您可以使用`start` input属性指定第一个显示行的偏移号。

```html
<markdown [src]="path/to/file.js" lineNumbers [start]="5"></markdown>
```

#### 线条突出显示插件

要使用突出显示代码块中特定行和/或行范围的[行高亮插件](http://prismjs.com/plugins/line-highlight/)，除Prism.js配置文件外，您还需要将`prismjs/plugins/line-highlight`目录中的以下文件包含在您的应用程序中:

- css造型为线条突出显示 - `prism-line-highlight.css`
- 行突出显示插件脚本 - `prism-line-highlight.js`

如果您使用的是[Angular CLI](https://cli.angular.io/)，可以按照下面的`angular.json`示例进行操作...

```diff
"styles": [
  "src/styles.css",
  "node_modules/prismjs/themes/prism-okaidia.css",
+ "node_modules/prismjs/plugins/line-highlight/prism-line-highlight.css"
],
"scripts": [
  "node_modules/prismjs/prism.js",
  "node_modules/prismjs/components/prism-csharp.min.js",
  "node_modules/prismjs/components/prism-css.min.js",
+ "node_modules/prismjs/plugins/line-highlight/prism-line-highlight.js"
]
```

使用`markdown`组件和/或指令，您将能够使用`lineHighlight`属性来激活插件。
该属性可以与用于变量绑定的`data`，用于远程内容的`src`或用于静态markdown的transclusion组合使用。

使用`line`输入属性指定要突出显示的行，并可选择使用`lineOffset`属性来指定代码段所代表的起始行代码。

```html
<markdown
  [src]="path/to/file.js"
  lineHighlight
  [line]="'6, 10-16'"
  [lineOffset]="5"
></markdown>
```

## 配置

### 主要应用模块

您必须使用`forRoot`在主应用程序模块(通常名为AppModule)中导入`MarkdownModule`才能使用`markdown`组件和/或指令。

```diff
import { NgModule } from '@angular/core';
+ import { MarkdownModule } from 'ngx-markdown';

import { AppComponent } from './app.component';

@NgModule({
  imports: [
+   MarkdownModule.forRoot(),
  ],
  declarations: [AppComponent],
  bootstrap: [AppComponent],
})
export class AppModule { }
```

您必须使用`forRoot`在主应用程序模块(通常称为AppModule)中导入`MarkdownModule`以使用`markdown`组件和/或指令。:

```diff
imports: [
+  HttpClientModule,
+  MarkdownModule.forRoot({ loader: HttpClient }),
],
```

#### MarkedOptions

Optionaly，可以通过将[MarkedOptions](https://marked.js.org/#/USING_ADVANCED.md#options)传递给`MarkdownModule`的`forRoot`方法来配置markdown解析。

Imports:

```typescript
import { MarkdownModule, MarkedOptions } from "ngx-markdown";
```

Default options:

```typescript
// using default options
MarkdownModule.forRoot(),
```

自定义选项并传递`HttpClient`以使用`[src]`属性:

```typescript
// using specific options with ValueProvider and passing HttpClient
MarkdownModule.forRoot({
  loader: HttpClient, // optional, only if you use [src] attribute
  markedOptions: {
    provide: MarkedOptions,
    useValue: {
      gfm: true,
      tables: true,
      breaks: false,
      pedantic: false,
      sanitize: false,
      smartLists: true,
      smartypants: false,
    },
  },
}),
```

#### MarkedOptions.renderer

`MarkedOptions`还公开了`renderer`属性，它允许你覆盖整个应用程序的标记渲染。

下面的示例通过在使用Bootstrap CSS时添加用于自定义样式的CSS类来覆盖默认的blockquote标记呈现：

```typescript
import { MarkedOptions, MarkedRenderer } from 'ngx-markdown';

// function that returns `MarkedOptions` with renderer override
export function markedOptionsFactory(): MarkedOptions {
  const renderer = new MarkedRenderer();

  renderer.blockquote = (text: string) => {
    return '<blockquote class="blockquote"><p>' + text + '</p></blockquote>';
  };

  return {
    renderer: renderer,
    gfm: true,
    tables: true,
    breaks: false,
    pedantic: false,
    sanitize: false,
    smartLists: true,
    smartypants: false,
  };
}

// using specific option with FactoryProvider
MarkdownModule.forRoot({
  loader: HttpClient,
  markedOptions: {
    provide: MarkedOptions,
    useFactory: markedOptionsFactory,
  },
}),
```

### 其他应用模块

将`MarkdownModule`导入其他应用程序模块时使用`forChild`，以允许您在应用程序中使用相同的解析器配置。

```diff
import { NgModule } from '@angular/core';
+ import { MarkdownModule } from 'ngx-markdown';

import { HomeComponent } from './home.component';

@NgModule({
  imports: [
+   MarkdownModule.forChild(),
  ],
  declarations: [HomeComponent],
})
export class HomeModule { }
```

## 用法

`ngx-markdown`提供了不同的方法来帮助您根据需要解析应用程序的降价。

> :bulb: 从Angular 6开始，模板编译器默认情况下会删除空格。使用`ngPreserveWhitespaces`指令来保留空格，例如换行符，以便按照预期呈现降价格式的内容。
> https://angular.io/api/core/Component#preserveWhitespaces

### 组件

你可以使用`markdown`组件直接从你的html标记解析静态markdown，使用`src`属性从远程url加载内容，或者使用`data`属性将变量绑定到你的组件。
您可以使用`load`输出事件属性或使用`error`输出事件属性加载错误来获取加载完成时的挂钩。

```html
<!-- static markdown -->
<markdown ngPreserveWhitespaces>
  # Markdown
</markdown>

<!-- loaded from remote url -->
<markdown
  [src]="'path/to/file.md'"
  (load)="onLoad($event)"
  (error)="onError($event)"
></markdown>

<!-- variable binding -->
<markdown [data]="markdown"></markdown>
```

### Directive

组件的工作方式相同，您可以使用`markdown`指令来完成相同的操作。

```html
<!-- static markdown -->
<div markdown ngPreserveWhitespaces>
  # Markdown
</div>

<!-- loaded from remote url -->
<div
  markdown
  [src]="'path/to/file.md'"
  (load)="onLoad($event)"
  (error)="onError($event)"
></div>

<!-- variable binding -->
<div markdown [data]="markdown"></div>
```

### Pipe

使用`markdown`管道将markdown转换为HTML允许您链接管道转换，并在值更改时更新DOM。

```html
<!-- chain `language` pipe with `markdown` pipe to convert typescriptMarkdown variable content -->
<div
  [innerHTML]="typescriptMarkdown | language : 'typescript' | markdown"
></div>
```

### Service

您可以使用`MarkdownService`访问markdown解析器和语法高亮方法。

```typescript
import { Component, OnInit } from '@angular/core';
import { MarkdownService } from 'ngx-markdown';

@Component({ ...
})
export class ExampleComponent implements OnInit() {
  constructor(private markdownService: MarkdownService) { }

  ngOnInit() {
    // outputs: <p>I am using <strong>markdown</strong>.</p>
    console.log(this.markdownService.compile('I am using __markdown__.'));
  }
}
```

## Renderer

标记可以通过自定义方式呈现...

- 在将`MarkdownModule.forRoot()`导入主应用程序模块时，将`renderer`属性与`MarkedOptions`一起提供(参见[Configuration](＃markedoptionsrenderer)部分)
- 使用`MarkdownService`暴露`renderer`

这是一个通过添加嵌入式锚标记来覆盖默认标题标记呈现的示例，通过添加嵌入式锚标记，如GitHub:

```typescript
import { Component, OnInit } from "@angular/core";
import { MarkdownService } from "ngx-markdown";

@Component({
  selector: "app-example",
  template: "<markdown># Heading</markdown>"
})
export class ExampleComponent implements OnInit() {
  constructor(private markdownService: MarkdownService) {}

  ngOnInit() {
    this.markdownService.renderer.heading = (text: string, level: number) => {
      const escapedText = text.toLowerCase().replace(/[^\w]+/g, "-");
      return (
        "<h" +
        level +
        ">" +
        '<a name="' +
        escapedText +
        '" class="anchor" href="#' +
        escapedText +
        '">' +
        '<span class="header-link"></span>' +
        "</a>" +
        text +
        "</h" +
        level +
        ">"
      );
    };
  }
}
```

此代码将输出以下HTML:

```html
<h1>
  <a name="heading" class="anchor" href="#heading">
    <span class="header-link"></span>
  </a>
  Heading
</h1>
```

> :blue_book: 按照官方[marked.renderer](https://github.com/chjj/marked#block-level-renderer-methods)文档获取可以覆盖的令牌列表。

## 语法高亮

使用静态markdown时，您有责任使用相关语言提供代码块。

````diff
<markdown ngPreserveWhitespaces>
+  ```typescript
    const myProp: string = 'value';
+  ```
</markdown>
````

使用远程url时，ngx-markdown将使用文件扩展名自动解析代码语言。

```html
<!-- will use html highlights -->
<markdown [src]="'path/to/file.html'"></markdown>

<!-- will use php highlights -->
<markdown [src]="'path/to/file.php'"></markdown>
```

使用变量绑定时，您可以选择使用`language`管道来指定变量内容的语言(默认值为不使用管道时的降价)。

```html
<markdown [data]="markdown | language : 'typescript'"></markdown>
```

## 演示应用程序

@ [https://jfcere.github.io/ngx-markdown](https://jfcere.github.io/ngx-markdown)提供了一个演示，它的源代码可以在`demo`目录中找到。

以下命令将克隆存储库，安装npm依赖项并提供应用程序@ [http：// localhost：4200](http：// localhost：4200)

```bash
git clone https://github.com/jfcere/ngx-markdown.git
npm install
ng serve
```

## AoT 编译

使用AoT构建是CI的一部分，每次提交时都会对其进行测试，因此您根本不必担心。

## 路线图

以下是在不久的将来将在此库上完成的任务列表 ...

- ~~添加CircleCI集成~~
- ~~在github页面上发布演示~~
- ~~添加变量绑定功能~~
- ~~将库变换为Javascript~~
- ~~使棱镜高亮显示可选~~
- 支持Prism.js自定义选项(行号，行高，...)

## 贡献

我们始终欢迎您的贡献，只需确保 ...

- 您的代码样式与项目的其余部分匹配
- 单元测试通过
- Linter传球

## 执照

根据[麻省理工](https://opensource.org/licenses/MIT)获得许可.
