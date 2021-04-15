## Angular CLI

### 基于[ember-cli](http://www.ember-cli.com/)项目的Angular应用程序的CLI

<!-- Badges section here. -->
[![Build Status](https://img.shields.io/travis/angular/angular-cli/master.svg?label=travis)][travis-badge-url]
[![CircleCI branch](https://img.shields.io/circleci/project/github/angular/angular-cli/master.svg?label=circleci)](https://circleci.com/gh/angular/angular-cli)
[![Dependency Status][david-badge]][david-badge-url]
[![devDependency Status][david-dev-badge]][david-dev-badge-url]

[![npm](https://img.shields.io/npm/v/%40angular/cli.svg)][npm-badge-url]
[![npm](https://img.shields.io/npm/v/%40angular/cli/next.svg)][npm-badge-url]
[![npm](https://img.shields.io/npm/l/@angular/cli.svg)][npm-badge-url]
[![npm](https://img.shields.io/npm/dm/@angular/cli.svg)][npm-badge-url]

[![Join the chat at https://gitter.im/angular/angular-cli](https://img.shields.io/gitter/room/nwjs/nw.js.svg)](https://gitter.im/angular/angular-cli?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Caretaker](https://img.shields.io/badge/caretaker-filipesilva-blue.svg)](https://github.com/filipesilva)

[![GitHub forks](https://img.shields.io/github/forks/angular/angular-cli.svg?style=social&label=Fork)](https://github.com/angular/angular-cli/fork)
[![GitHub stars](https://img.shields.io/github/stars/angular/angular-cli.svg?style=social&label=Star)](https://github.com/angular/angular-cli)

## 注意

如果您正在从测试版或RC版进行更新，请查看我们的[1.0更新指南](https://github.com/angular/angular-cli/wiki/stories-1.0-update).

如果您希望合作，请查看[我们的问题列表](https://github.com/angular/angular-cli/issues).

在提交新问题之前，请查看[使用`type：faq`标签标记的问题](https://github.com/angular/angular-cli/issues?utf8=%E2%9C%93&q=is%3Aissue%20label%3A%22type%3A%20faq%22%20).

## 先决条件

CLI和生成的项目都有相关性，需要Node 6.9.0或更高版本以及NPM 3或更高版本。

## 目录

* [安装](#installation)
* [用法](#usage)
* [生成一个新项目](#generating-and-serving-an-angular-project-via-a-development-server)
* [生成组件，指令，管道和服务](#generating-components-directives-pipes-and-services)
* [更新Angular CLI](#updating-angular-cli)
* [开发Angular CLI的开发提示](#development-hints-for-working-on-angular-cli)
* [文档](#documentation)
* [文档](#license)

## 安装

**在您安装之前:** 请阅读[先决条件](#prerequisites)

```bash
npm install -g @angular/cli
```

## 用法

```bash
ng help
```

### 通过开发服务器生成并提供Angular项目

```bash
ng new PROJECT-NAME
cd PROJECT-NAME
ng serve
```

导航`http://localhost:4200/`.
如果您更改任何源文件，该应用程序将自动重新加载。

您可以使用两个命令行选项来配置开发服务器使用的默认HTTP主机和端口：

```bash
ng serve --host 0.0.0.0 --port 4201
```

### 生成组件，指令，管道和服务

你可以使用`ng generate`（或者`ng g`）命令来生成Angular组件：

```bash
ng generate component my-new-component
ng g component my-new-component # 使用别名

# 如果在目录src/app/feature /中运行，组件支持相对路径生成
ng g component new-cmp
# 你的组件将在src/app/feature/new-cmp中生成，但是如果你要运行的话
ng g component ./newer-cmp
# 你的组件将在src/app/newer-cmp中生成，如果你还可以在src/app目录下运行的话
ng g component feature/new-cmp
# 并且您的组件将在src/app/feature/new-cmp中生成
```

您可以在下表中找到所有可能的蓝图：

脚手架  | 用法
---       | ---
[Component](https://github.com/angular/angular-cli/wiki/generate-component) | `ng g component my-new-component`
[Directive](https://github.com/angular/angular-cli/wiki/generate-directive) | `ng g directive my-new-directive`
[Pipe](https://github.com/angular/angular-cli/wiki/generate-pipe)           | `ng g pipe my-new-pipe`
[Service](https://github.com/angular/angular-cli/wiki/generate-service)     | `ng g service my-new-service`
[Class](https://github.com/angular/angular-cli/wiki/generate-class)         | `ng g class my-new-class`
[Guard](https://github.com/angular/angular-cli/wiki/generate-guard)         | `ng g guard my-new-guard`
[Interface](https://github.com/angular/angular-cli/wiki/generate-interface) | `ng g interface my-new-interface`
[Enum](https://github.com/angular/angular-cli/wiki/generate-enum)           | `ng g enum my-new-enum`
[Module](https://github.com/angular/angular-cli/wiki/generate-module)       | `ng g module my-module`

angular-cli会自动在`app.module.ts`中添加对`components`，`directives`和`pipes`的引用。
如果您需要将此引用添加到另一个自定义模块，请按照下列步骤操作：

 1. `ng g module new-module`创建一个新的模块
 2. 调用 `ng g component new-module/new-component`

这应该将新的`component`，`directive`或`pipe`引用添加到您创建的`new-module`。

### 更新Angular CLI

如果您使用Angular CLI`1.0.0-beta.28`或更低版本，则需要卸载`angular-cli`软件包。
应该这样做，因为将包的名称和范围从`angular-cli`改为`@ angular/cli`：

```bash
npm uninstall -g angular-cli
npm uninstall --save-dev angular-cli
```

要将Angular CLI更新为新版本，您必须更新全局包和您的项目的本地包。

全局包:

```bash
npm uninstall -g @angular/cli
npm cache verify
# if npm version is < 5 then use `npm cache clean`
npm install -g @angular/cli@latest
```

本地项目包:

```bash
rm -rf node_modules dist # use rmdir /S/Q node_modules dist in Windows Command Prompt; use rm -r -fo node_modules,dist in Windows PowerShell
npm install --save-dev @angular/cli@latest
npm install
```

如果您从测试版或RC版升级到1.0，请查看我们的[1.0更新指南](https://github.com/angular/angular-cli/wiki/stories-1.0-update).

您可以在GitHub上的“[版本](https://github.com/angular/angular-cli/releases)”选项卡中找到有关版本之间更改的更多详细信息.

## 开发Angular CLI的开发提示

### 与主人一起工作

```bash
git clone https://github.com/angular/angular-cli.git
cd angular-cli
npm link
```

`npm link`与`npm install -g`非常相似，不同之处在于不是从repo下载软件包，而是将刚刚克隆的`angular-cli /`文件夹变成全局软件包。
另外，这个存储库发布了几个包，我们使用特殊的逻辑在开发设置中加载它们。

对`angular-cli /`文件夹中的文件所做的任何更改都会立即影响全局的`@ angular/cli`软件包，允许您快速测试您对cli项目所做的任何更改。

现在你可以通过命令行使用`@ angular/cli`：

```bash
ng new foo
cd foo
npm link @angular/cli
ng serve
```

`npm link @ angular/cli`是必需的，因为默认情况下，全局安装的`@ angular/cli`只是从npm远程获取的项目加载本地`@角度/ cli`。
`npm link @ angular/cli`将全局`@ angular/cli`软件包符号链接到本地​​`@ angular/cli`软件包。
现在你以前克隆过的`angular-cli`有三个地方：
您将其克隆到的文件夹，npm的存储全局程序包的文件夹以及刚刚创建的Angular CLI项目。

您还可以使用`ng foo --link-cli`来自动链接`@ angular/cli`软件包。

请阅读官方的[npm-link文档](https://docs.npmjs.com/cli/link)和[npm-link作弊表](http://browsenpm.org/help#linkinganynpmpackagelocally)以获取更多信息。

要运行Angular CLI测试套件，请使用`node tests/run_e2e.js`命令。
它也可以接收一个文件名，只运行该测试（例如`node tests/run_e2e.js tests/e2e/tests/build/dev-build.ts`）。

作为测试程序的一部分，所有软件包将被构建并链接。
测试完成后，您需要重新运行`npm link`重新连接开发的Angular CLI环境。

## 文档

Angular CLI的文档位于此repo的[wiki](https://github.com/angular/angular-cli/wiki)中.

## 执照

MIT

[travis-badge]: https://travis-ci.org/angular/angular-cli.svg?branch=master
[travis-badge-url]: https://travis-ci.org/angular/angular-cli
[david-badge]: https://david-dm.org/angular/angular-cli.svg
[david-badge-url]: https://david-dm.org/angular/angular-cli
[david-dev-badge]: https://david-dm.org/angular/angular-cli/dev-status.svg
[david-dev-badge-url]: https://david-dm.org/angular/angular-cli?type=dev
[npm-badge]: https://img.shields.io/npm/v/@angular/cli.svg
[npm-badge-url]: https://www.npmjs.com/package/@angular/cli