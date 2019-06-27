[![CircleCI](https://circleci.com/gh/angular/universal/tree/master.svg?style=shield)](https://circleci.com/gh/angular/universal/tree/master)
[![Join the chat at https://gitter.im/angular/universal](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/angular/universal?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

# 通用角度

![Angular Universal](https://angular.io/generated/images/marketing/concept-icons/universal.png)

## 目录

- [通用角度](#%E9%80%9A%E7%94%A8%E8%A7%92%E5%BA%A6)
  - [目录](#%E7%9B%AE%E5%BD%95)
  - [介绍](#%E4%BB%8B%E7%BB%8D)
  - [入门](#%E5%85%A5%E9%97%A8)
  - [包](#%E5%8C%85)
  - [通用“陷阱”](#%E9%80%9A%E7%94%A8%E9%99%B7%E9%98%B1)
    - [路线图](#%E8%B7%AF%E7%BA%BF%E5%9B%BE)
      - [已完成](#%E5%B7%B2%E5%AE%8C%E6%88%90)
      - [进行中](#%E8%BF%9B%E8%A1%8C%E4%B8%AD)
      - [规划](#%E8%A7%84%E5%88%92)
    - [从 Angular2-Universal 升级](#%E4%BB%8E-angular2-universal-%E5%8D%87%E7%BA%A7)
    - [预启动](#%E9%A2%84%E5%90%AF%E5%8A%A8)
    - [什么名字？](#%E4%BB%80%E4%B9%88%E5%90%8D%E5%AD%97)
    - [环球团队](#%E7%8E%AF%E7%90%83%E5%9B%A2%E9%98%9F)
    - [执照](#%E6%89%A7%E7%85%A7)

---

## 介绍

Angular Universal 项目是一个社区驱动的项目，旨在扩展 Angular(平台服务器)的核心 API，使开发人员能够在各种场景中对 Angular 应用程序进行服务器端渲染。

该存储库将托管各种工具，如引擎，以与各种后端(NodeJS，ASP.NET 等)集成，还有额外的模块和示例，以帮助您开始使用服务器端渲染。

环球项目由社区贡献推动。请将您的 Pull 请求发送给我们！

## 入门

[\* **NodeJS** :: Example repo](https://github.com/angular/universal-starter)

- 最小的通用例子

[\* ASP.NET Core :: Universal Starter repo](https://github.com/MarkPieszak/aspnetcore-angular2-universal)

- **Installation**: 克隆上面的回购，`npm i && dotnet restore` _(VStudio 将在打开项目时自动运行)_
- 启动包含 VSCode 和 VStudio 的文件以自动运行/调试(按 F5)。

## 包

来自此 repo 的软件包在[@nguniversal](https://www.npmjs.com/search?q=%40nguniversal)下发布为作用域软件包

- [@nguniversal/common](/modules/common/README.md)
- [@nguniversal/express-engine](/modules/express-engine/README.md)
- [@nguniversal/aspnetcore-engine](/modules/aspnetcore-engine/README.md)
- [@nguniversal/hapi-engine](/modules/hapi-engine/README.md)
- [@nguniversal/module-map-ngfactory-loader](/modules/module-map-ngfactory-loader)
- [@nguniversal/socket-engine](/modules/socket-engine)

## 通用“陷阱”

移至[/docs/gotchas.md](/docs/gotchas.md)

### 路线图

#### 已完成

- 将平台 API 集成到核心中
- 支持服务器上的标题和元服务
- 开发 Express，ASP.NET Core，Hapi 引擎
- 对 Universal 的 Angular CLI 支持
- 在服务器上提供 DOM 实现
- `renderModule *` 中的钩子在渲染到字符串之前做东西
- 平台中的通用状态转移 API
- Http Transfer State Module 使用 HTTP 拦截器和状态转移 API
- 材料 2 适用于 Universal
- 编写核心 API 的文档
- 支持[AppShell](https://developers.google.com/web/updates/2015/11/app-shell)用例

#### 进行中

- 更好的内部性能和压力测试
- 为 Universal 组件编写单元测试更容易
- 更容易支持其他第三方库，如 jQuery / d3，这些库不具备通用性
- Node.js 桥接协议与不同语言后端通信 - Django，Go，PHP 等。

#### 规划

- 完全客户端补液策略，重用在服务器上呈现的 DOM 元素/ CSS

### 从 Angular2-Universal 升级

如果你来自最初的 `angular2-universal`(2.x), 这里有一些有用的步骤，可以将你的应用程序移植到 Angular 4 和 platform-server。

[去这里找指南](/docs/angular2-universal-migration.md)

### 预启动

在客户端 Web 应用程序加载到客户端应用程序之前控制服务器呈现的页面和传输状态。 [回购](https://github.com/angular/preboot)

### 什么名字？

我们认为，当引用在比浏览器更多的环境中运行的 JavaScript 应用程序时，使用“通用”一词是正确的。 (受[Universal JavaScript]启发(https://medium.com/@mjackson/universal-javascript-4761051b7ae9))

### 环球团队

- [Adam Plumer](https://github.com/CaerusKaru) 和 [Fabian Wiles](https://github.com/Toxicable) - 目前的维护者
- [PatrickJS](https://twitter.com/gdi2290) 和 [Jeff Whelpley](https://twitter.com/jeffwhelpley) - Founders of the Angular Universal project. (通用渲染也称为[PatrickJS-ing](https://twitter.com/jeffbcross/status/846512930971516928))
- [Mark Pieszak](https://twitter.com/MarkPieszak) - 贡献者和传播者，ASP.NET 核心引擎
- [Jason Jean](https://github.com/FrozenPandaz) - CLI 的 Express 引擎和 Universal 支持
- [Wassim Chegham](https://twitter.com/manekinekko) - Hapi 引擎开发人员和传播者。
  - [Angular for the rest of us](https://medium.com/google-developer-experts/angular-universal-for-the-rest-of-us-922ca8bac84)
  - [Angular outside the browser](http://slides.com/wassimchegham/angular2-universal#/)
- [Jeff Cross](https://twitter.com/jeffbcross) - 福音传道者和表演顾问
- [Vikram Subramanian](https://twitter.com/vikerman) 和 [Alex Rickabaugh](https://github.com/alxhub) - Angular 核心 API

### 执照

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)](/LICENSE)
