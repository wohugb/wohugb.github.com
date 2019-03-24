# ngx-markdown

![Ngx-Markdown Logo](https://github.com/jfcere/ngx-markdown/raw/master/demo/src/assets/ngx-markdown.png)

[![CircleCI Status](https://circleci.com/gh/jfcere/ngx-markdown/tree/master.svg?style=shield)](https://circleci.com/gh/jfcere/ngx-markdown)
[![Coverage Status](https://coveralls.io/repos/github/jfcere/ngx-markdown/badge.svg?branch=master)](https://coveralls.io/github/jfcere/ngx-markdown?branch=master)
[![NPM Version](https://img.shields.io/npm/v/ngx-markdown.svg?style=flat)](https://www.npmjs.com/package/ngx-markdown)
[![License](https://img.shields.io/npm/l/ngx-markdown.svg)](https://opensource.org/licenses/MIT)
[![Monthly Downloads](https://img.shields.io/npm/dm/ngx-markdown.svg)](https://www.npmjs.com/package/ngx-markdown)
[![Dependencies Status](https://david-dm.org/jfcere/ngx-markdown/status.svg?path=lib)](https://david-dm.org/jfcere/ngx-markdown?path=lib)
[![PeerDependencies Status](https://david-dm.org/jfcere/ngx-markdown/peer-status.svg?path=lib)](https://david-dm.org/jfcere/ngx-markdown?path=lib&type=peer)

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

- prism.js core library - `node_modules/prismjs/prism.js` file
- a highlight css theme - from `node_modules/prismjs/themes` directory
- desired code language syntax files - from `node_modules/prismjs/components` directory

_Additional themes can be found by browsing the web such as [Prism-Themes](https://github.com/PrismJS/prism-themes) or [Mokokai](https://github.com/Ahrengot/Monokai-theme-for-Prism.js) for example._

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

- css styling for line numbers - `prism-line-numbers.css`
- line numbers plugin script - `prism-line-numbers.js`

If you are using [Angular CLI](https://cli.angular.io/) you can follow the `angular.json` example below...

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

Using `markdown` component and/or directive, you will be able to use the `lineNumbers` property to activate the plugin. The property can be use in combinaison with either `data` for variable binding, `src` for remote content or using transclusion for static markdown.

Additionaly, you can use `start` input property to specify the offset number for the first display line.

```html
<markdown [src]="path/to/file.js" lineNumbers [start]="5"></markdown>
```

#### 线条突出显示插件

To use the [line highlight plugin](http://prismjs.com/plugins/line-highlight/) that highlights specific lines and/or line ranges in code blocks, in addition to Prism.js configuration files, you will need to include the following files from `prismjs/plugins/line-highlight` directory to your application:

- css styling for line highlight - `prism-line-highlight.css`
- line highlight plugin script - `prism-line-highlight.js`

If you are using [Angular CLI](https://cli.angular.io/) you can follow the `angular.json` example below...

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

Using `markdown` component and/or directive, you will be able to use the `lineHighlight` property to activate the plugin. The property can be use in combinaison with either `data` for variable binding, `src` for remote content or using transclusion for static markdown.

Use `line` input property to specify the line(s) to highlight and optionally there is a `lineOffset` property to specify the starting line of code your snippet represents.

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

You must import `MarkdownModule` inside your main application module (usually named AppModule) with `forRoot` to be able to use `markdown` component and/or directive.

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

If you want to use the `[src]` attribute to directly load a remote file, in order to keep only one instance of `HttpClient` and avoid issues with interceptors, you also have to provide `HttpClient`:

```diff
imports: [
+  HttpClientModule,
+  MarkdownModule.forRoot({ loader: HttpClient }),
],
```

#### MarkedOptions

Optionaly, markdown parsing can be configured by passing [MarkedOptions](https://marked.js.org/#/USING_ADVANCED.md#options) to the `forRoot` method of `MarkdownModule`.

Imports:

```typescript
import { MarkdownModule, MarkedOptions } from "ngx-markdown";
```

Default options:

```typescript
// using default options
MarkdownModule.forRoot(),
```

Custom options and passing `HttpClient` to use `[src]` attribute:

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

`MarkedOptions` also exposes the `renderer` property which allows you to override token rendering for your whole application.

The example below overrides the default blockquote token rendering by adding a CSS class for custom styling when using Bootstrap CSS:

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

Use `forChild` when importing `MarkdownModule` into other application modules to allow you to use the same parser configuration accross your application.

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

`ngx-markdown` provides different approaches to help you parse markdown to your application depending of your needs.

> :bulb: As of Angular 6, the template compiler strips whitespace by default. Use `ngPreserveWhitespaces` directive to preserve whitespaces such as newlines in order for the markdown-formatted content to render as intended.
> https://angular.io/api/core/Component#preserveWhitespaces

### 组件

You can use `markdown` component to either parse static markdown directly from your html markup, load the content from a remote url using `src` property or bind a variable to your component using `data` property. You can get a hook on load complete using `load` output event property or on loading error using `error` output event property.

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

The same way the component works, you can use `markdown` directive to accomplish the same thing.

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

Using `markdown` pipe to transform markdown to HTML allow you to chain pipe transformations and will update the DOM when value changes.

```html
<!-- chain `language` pipe with `markdown` pipe to convert typescriptMarkdown variable content -->
<div
  [innerHTML]="typescriptMarkdown | language : 'typescript' | markdown"
></div>
```

### Service

You can use `MarkdownService` to have access to markdown parser and syntax highlight methods.

```typescript
import { Component, OnInit } from '@angular/core';
import { MarkdownService } from 'ngx-markdown';

@Component({ ... })
export class ExampleComponent implements OnInit() {
  constructor(private markdownService: MarkdownService) { }

  ngOnInit() {
    // outputs: <p>I am using <strong>markdown</strong>.</p>
    console.log(this.markdownService.compile('I am using __markdown__.'));
  }
}
```

## Renderer

Tokens can be render in a custom manner by either...

- providing the `renderer` property with the `MarkedOptions` when importing `MarkdownModule.forRoot()` into your main application module (see [Configuration](#markedoptionsrenderer) section)
- using `MarkdownService` exposed `renderer`

Here is an example of overriding the default heading token rendering through `MarkdownService` by adding an embedded anchor tag like on GitHub:

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

This code will output the following HTML:

```html
<h1>
  <a name="heading" class="anchor" href="#heading">
    <span class="header-link"></span>
  </a>
  Heading
</h1>
```

> :blue_book: Follow official [marked.renderer](https://github.com/chjj/marked#block-level-renderer-methods) documentation for the list of tokens that can be overriden.

## 语法高亮

When using static markdown you are responsible to provide the code block with related language.

````diff
<markdown ngPreserveWhitespaces>
+  ```typescript
    const myProp: string = 'value';
+  ```
</markdown>
````

When using remote url ngx-markdown will use file extension to automatically resolve the code language.

```html
<!-- will use html highlights -->
<markdown [src]="'path/to/file.html'"></markdown>

<!-- will use php highlights -->
<markdown [src]="'path/to/file.php'"></markdown>
```

When using variable binding you can optionally use `language` pipe to specify the language of the variable content (default value is markdown when pipe is not used).

```html
<markdown [data]="markdown | language : 'typescript'"></markdown>
```

## 演示应用程序

A demo is available @ [https://jfcere.github.io/ngx-markdown](https://jfcere.github.io/ngx-markdown) and it source code can be found inside the `demo` directory.

The following commands will clone the repository, install npm dependencies and serve the application @ [http://localhost:4200](http://localhost:4200)

```bash
git clone https://github.com/jfcere/ngx-markdown.git
npm install
ng serve
```

## AoT 编译

Building with AoT is part of the CI and is tested every time a commit occurs so you don't have to worry at all.

## 路线图

Here is the list of tasks that will be done on this library in a near future ...

- ~~Add CircleCI integration~~
- ~~Publish demo on github pages~~
- ~~Add variable binding feature~~
- ~~Transpile library to Javascript~~
- ~~Make Prism highlight optional~~
- Support Prism.js customizing options (line-numbers, line-height, ...)

## 贡献

Contributions are always welcome, just make sure that ...

- Your code style matches with the rest of the project
- Unit tests pass
- Linter passes

## 执照

Licensed under [MIT](https://opensource.org/licenses/MIT).
