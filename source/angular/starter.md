# Angular 的 webpack 启动器

Angular Webpack Starter [![Join the chat at https://gitter.im/gdi2290/angular-starter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/gdi2290/angular-starter?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

> An Angular starter kit featuring [Angular 5](https://angular.io), [Ahead of Time Compile](https://angular.io/docs/ts/latest/cookbook/aot-compiler.html), [Router](https://angular.io/docs/ts/latest/guide/router.html), [Forms](https://angular.io/docs/ts/latest/guide/forms.html),
> [Http](https://angular.io/docs/ts/latest/guide/server-communication.html),
> [Services](https://gist.github.com/gdi2290/634101fec1671ee12b3e#_follow_@AngularClass_on_twitter),
> [Tests](https://angular.io/docs/ts/latest/guide/testing.html), [E2E](https://angular.github.io/protractor/#/faq#what-s-the-difference-between-karma-and-protractor-when-do-i-use-which-)), [Karma](https://karma-runner.github.io/), [Protractor](https://angular.github.io/protractor/), [Jasmine](https://github.com/jasmine/jasmine), [Istanbul](https://github.com/gotwarlost/istanbul), [TypeScript](http://www.typescriptlang.org/), [@types](https://www.npmjs.com/~types), [TsLint](http://palantir.github.io/tslint/), [Codelyzer](https://github.com/mgechev/codelyzer), [Hot Module Replacement](https://webpack.github.io/docs/hot-module-replacement-with-webpack.html), and [Webpack](http://webpack.github.io/) by [AngularClass](https://angularclass.com).

> If you're looking for Angular 1.x please use [NG6-starter](https://github.com/angularclass/NG6-starter)
> If you're looking to learn about Webpack and ES6 Build Tools check out [ES6-build-tools](https://github.com/AngularClass/ES6-build-tools)
> If you're looking to learn TypeScript see [TypeStrong/learn-typescript](https://github.com/TypeStrong/learn-typescript)
> If you're looking for something easier to get started with then see the angular-seed that I also maintain [AngularClass/angular-seed](https://github.com/AngularClass/angular-seed)

This seed repo serves as an Angular starter for anyone looking to get up and running with Angular and TypeScript fast. Using a [Webpack 3](https://webpack.js.org) for building our files and assisting with boilerplate. We're also using Protractor for our end-to-end story and Karma for our unit tests.

- Best practices in file and application organization for Angular.
- Ready to go build system using Webpack for working with TypeScript.
- Angular examples that are ready to go when experimenting with Angular.
- A great Angular seed repo for anyone who wants to start their project.
- Ahead of Time (AoT) compile for rapid page loads of your production builds.
- Tree shaking to automatically remove unused code from your production bundle.
- [Webpack DLLs](https://robertknight.github.io/posts/webpack-dll-plugins/) dramatically speed your development builds.
- Testing Angular code with Jasmine and Karma.
- Coverage with Istanbul and Karma
- End-to-end Angular code using Protractor.
- Type manager with @types
- Hot Module Replacement with Webpack and [@angularclass/hmr](https://github.com/angularclass/angular-hmr) and [@angularclass/hmr-loader](https://github.com/angularclass/angular-hmr-loader)
- Angular 4 support via changing package.json and any future Angular versions

#### 快速入门

**Make sure you have Node version >= 6.0 and NPM >= 3**

> Clone/Download the repo then edit `app.component.ts` inside [`/src/app/app.component.ts`](/src/app/app.component.ts)

```bash
## clone our repo
## --depth 1 removes all but one .git commit history
git clone --depth 1 https://github.com/AngularClass/angular-starter.git

## change directory to our repo
cd angular-starter

## WINDOWS only. In terminal as administrator
npm install -g node-pre-gyp

## install the repo with npm
npm install

## start the server
npm start

## use Hot Module Replacement
npm run server:dev:hmr

## if you're in China use cnpm
## https://github.com/cnpm/cnpm
```

go to [http://0.0.0.0:3000](http://0.0.0.0:3000) or [http://localhost:3000](http://localhost:3000) in your browser

## 文件结构

We use the component approach in our starter. This is the new standard for developing Angular apps and a great way to ensure maintainable code by encapsulation of our behavior logic. A component is basically a self contained app usually in a single file or a folder with each concern as a file: style, template, specs, e2e, and component class. Here's how it looks:

```
angular-starter/
 ├──config/                        * 配置文件
 |   ├──helpers.js                 * 配置文件帮助函数
 |   ├──spec-bundle.js             * ignore this magic that sets up our Angular testing environment
 |   ├──karma.conf.js              * karma 配置，为单元测试
 |   ├──protractor.conf.js         * protractor config for our end-to-end tests
 │   ├──webpack.dev.js             * webpack 开发配置
 │   ├──webpack.prod.js            * webpack 产品配置
 │   └──webpack.test.js            * webpack 测试配置
 │
 ├──src/                           * 编译成js的源原件
 |   ├──main.browser.ts            * 浏览环境的入口文件
 │   │
 |   ├──index.html                 * 用于生成主页
 │   │
 |   ├──polyfills.ts               * polyfills 文件
 │   │
 │   ├──app/                       * 应用文件夹
 │   │   ├──app.component.spec.ts  * a simple test of components in app.component.ts
 │   │   ├──app.e2e.ts             * a simple end-to-end test for /
 │   │   └──app.component.ts       * a simple version of our App component components
 │   │
 │   └──assets/                    * 静态资源
 │       ├──icon/                  * our list of icons from www.favicon-generator.org
 │       ├──service-worker.js      * ignore this. Web App service worker that's not complete yet
 │       ├──robots.txt             * for search engines to crawl your website
 │       └──humans.txt             * for humans to know who the developers are
 │
 │
 ├──tslint.json                    * typescript lint 配置
 ├──typedoc.json                   * typescript 文档成成器
 ├──tsconfig.json                  * typescript config used outside webpack
 ├──tsconfig.webpack.json          * config that webpack uses for typescript
 ├──package.json                   * what npm uses to manage its dependencies
 └──webpack.config.js              * webpack 主配置文件

```

## 入门指南

### 依赖关系

What you need to run this app:

- `node` and `npm` (`brew install node`)
- Ensure you're running the latest versions Node `v6.x.x`+ (or `v7.x.x`) and NPM `3.x.x`+

> If you have `nvm` installed, which is highly recommended (`brew install nvm`) you can do a `nvm install --lts && nvm use` in `$` to run with the latest Node LTS. You can also have this `zsh` done for you [automatically](https://github.com/creationix/nvm#calling-nvm-use-automatically-in-a-directory-with-a-nvmrc-file)

Once you have those, you should install these globals with `npm install --global`:

- `webpack` (`npm install --global webpack`)
- `webpack-dev-server` (`npm install --global webpack-dev-server`)
- `karma` (`npm install --global karma-cli`)
- `protractor` (`npm install --global protractor`)
- `typescript` (`npm install --global typescript`)

### 安装

- `fork` this repo
- `clone` your fork
- `npm install webpack-dev-server rimraf webpack -g` to install required global dependencies
- `npm install` to install all dependencies or `yarn`
- `npm run server` to start the dev server in another tab

### 运行应用

After you have installed all dependencies you can now run the app. Run `npm run server` to start a local server using `webpack-dev-server` which will watch, build (in-memory), and reload for you. The port will be displayed to you as `http://0.0.0.0:3000` (or if you prefer IPv6, if you're using `express` server, then it's `http://[::1]:3000/`).

#### 服务

```bash
## development
npm run server
## production
npm run build:prod
npm run server:prod
```

### 其它命令

??? info "构建文件"

    ```bash
    ## development
    npm run build:dev
    ## production (jit)
    npm run build:prod
    ## AoT
    npm run build:aot
    ```

??? info "热模块加载"

    ```bash
    npm run server:dev:hmr
    ```

??? info "监控并构建文件"

    ```bash
    npm run watch
    ```

??? info "运行单元测试"

    ```bash
    npm run test
    ```

??? info "监控并运行测试"

    ```bash
    npm run watch:test
    ```

??? info "运行 end-to-end 测试"

    ```bash
    ## update Webdriver (optional, done automatically by postinstall script)
    npm run webdriver:update
    ## this will start a test server and launch Protractor
    npm run e2e
    ```

??? info "持续集成 (run unit tests and e2e tests together)"

    ```bash
    ## this will test both your JIT and AoT builds
    npm run ci
    ```

??? info "run Protractor's elementExplorer (for end-to-end)"

    ```bash
    npm run e2e:live
    ```

??? info "构建 Docker"

    ```bash
    npm run build:docker
    ```

## 配置

Configuration files live in `config/` we are currently using webpack, karma, and protractor for different stages of your application

## AoT Don'ts

The following are some things that will make AoT compile fail.

- Don’t use require statements for your templates or styles, use styleUrls and templateUrls, the angular2-template-loader plugin will change it to require at build time.
- Don’t use default exports.
- Don’t use `form.controls.controlName`, use `form.get(‘controlName’)`
- Don’t use `control.errors?.someError`, use `control.hasError(‘someError’)`
- Don’t use functions in your providers, routes or declarations, export a function and then reference that function name
- @Inputs, @Outputs, View or Content Child(ren), Hostbindings, and any field you use from the template or annotate for Angular should be public

## 扩展样式

Any stylesheets (Sass or CSS) placed in the `src/styles` directory and imported into your project will automatically be compiled into an external `.css` and embedded in your production builds.

For example to use Bootstrap as an external stylesheet:

1. Create a `styles.scss` file (name doesn't matter) in the `src/styles` directory.
2. `npm install` the version of Boostrap you want.
3. In `styles.scss` add `@import 'bootstrap/scss/bootstrap.scss';`
4. In `src/app/app.module.ts` add underneath the other import statements: `import '../styles/styles.scss';`

## 贡献

You can include more examples as components but they must introduce a new concept such as `Home` component (separate folders), and Todo (services). I'll accept pretty much everything so feel free to open a Pull-Request

## TypeScript

> To take full advantage of TypeScript with autocomplete you would have to install it globally and use an editor with the correct TypeScript plugins.

### Use latest TypeScript compiler

TypeScript 2.1.x includes everything you need. Make sure to upgrade, even if you installed TypeScript previously.

```
npm install --global typescript
```

### Use a TypeScript-aware editor

We have good experience using these editors:

- [Visual Studio Code](https://code.visualstudio.com/)
- [Webstorm 10](https://www.jetbrains.com/webstorm/download/)
- [Atom](https://atom.io/) with [TypeScript plugin](https://atom.io/packages/atom-typescript)
- [Sublime Text](http://www.sublimetext.com/3) with [Typescript-Sublime-Plugin](https://github.com/Microsoft/Typescript-Sublime-plugin#installation)

#### Visual Studio Code + Debugger for Chrome

> Install [Debugger for Chrome](https://marketplace.visualstudio.com/items?itemName=msjsdiag.debugger-for-chrome) and see docs for instructions to launch Chrome

The included `.vscode` automatically connects to the webpack development server on port `3000`.

## Types

> When you include a module that doesn't include Type Definitions inside of the module you can include external Type Definitions with @types

i.e, to have youtube api support, run this command in terminal:

```shell
npm i @types/youtube @types/gapi @types/gapi.youtube
```

In some cases where your code editor doesn't support Typescript 2 yet or these types weren't listed in `tsconfig.json`, add these to **"src/custom-typings.d.ts"** to make peace with the compile check:

```es6
import "@types/gapi.youtube";
import "@types/gapi";
import "@types/youtube";
```

### 自定义类型定义

When including 3rd party modules you also need to include the type definition for the module
if they don't provide one within the module. You can try to install it with @types

```sh
> npm install @types/node
> npm install @types/lodash
```

If you can't find the type definition in the registry we can make an ambient definition in
this file for now. For example

```typescript
declare module "my-module" {
  export function doesSomething(value: string): string;
}
```

If you're prototyping and you will fix the types later you can also declare it as type any

```typescript
declare var assert: any;
declare var _: any;
declare var $: any;
```

If you're importing a module that uses Node.js modules which are CommonJS you need to import as

```typescript
import * as _ from "lodash";
```

## 常见问题

??? info "Angular 支持哪些浏览器?"

    Please view the updated list of [browser support for Angular 2](https://github.com/angularclass/awesome-angular2#current-browser-support-for-angular-2)

??? info "Why is my service, aka provider, is not injecting parameter correctly?"

    Please use `@Injectable()` for your service for typescript to correctly attach the metadata (this is a TypeScript problem)

??? info "我在哪里写测试?"

     You can write your tests next to your component files. See [`/src/app/home/home.component.spec.ts`](/src/app/home/home.component.spec.ts)

??? info "How do I start the app when I get `EACCES` and `EADDRINUSE` errors?"

     The `EADDRINUSE` error means the port `3000` is currently being used and `EACCES` is lack of permission for webpack to build files to `./dist/`

??? info "How to use `sass` for css?"

     `loaders: ['raw-loader','sass-loader']` and `@Component({ styleUrls: ['./filename.scss'] })` see Wiki page [How to include SCSS in components](https://github.com/AngularClass/angular-starter/wiki/How-to-include-SCSS-in-components), or issue [#136](https://github.com/AngularClass/angular-starter/issues/136) for more information.

??? info "如何测试服务?"

     See issue [#130](https://github.com/AngularClass/angular-starter/issues/130#issuecomment-158872648)

??? info "如何添加 `vscode-chrome-debug` 支持?"

     The VS Code chrome debug extension support can be done via `launch.json` see issue [#144](https://github.com/AngularClass/angular-starter/issues/144#issuecomment-164063790)

??? info "How do I make the repo work in a virtual machine?"

     You need to use `0.0.0.0` so revert these changes [#205](https://github.com/AngularClass/angular-starter/pull/205/files)

??? info "What are the naming conventions for Angular?"

     please see issue [#185](https://github.com/AngularClass/angular-starter/issues/185) and PR [196](https://github.com/AngularClass/angular-starter/pull/196)

??? info "如何引入 bootstrap 或者 jQuery?"

     please see issue [#215](https://github.com/AngularClass/angular-starter/issues/215) and [#214](https://github.com/AngularClass/angular-starter/issues/214#event-511768416)

??? info "如何异步加载模块?"

     see wiki [How-do-I-async-load-a-component-with-AsyncRoute](https://github.com/AngularClass/angular-starter/wiki/How-do-I-async-load-a-component-with-AsyncRoute)

??? info "Error: Cannot find module 'tapable'"

     Remove `node_modules/` and run `npm cache clean` then `npm install`

??? info "如何开启热模块加载？"

     Run `npm run server:dev:hmr`

??? info "`RangeError: Maximum call stack size exceeded`"

     This is a problem with minifying Angular and it's recent JIT templates. If you set `mangle` to `false` then you should be good.

??? info "开发环境为什么我的应用非常大?"

     We are using inline source-maps and hot module replacement which will increase the bundle size.

??? info "如果你在中国"

     check out https://github.com/cnpm/cnpm

??? info "node-pre-gyp ERR in npm install (Windows)"

     install Python x86 version between 2.5 and 3.0 on windows see issue [#626](https://github.com/AngularClass/angular-starter/issues/626)

??? info "`Error:Error: Parse tsconfig error [{"messageText":"Unknown compiler option 'lib'.","category":1,"code":5023},{"messageText":"Unknown compiler option 'strictNullChecks'.","category":1,"code":5023},{"messageText":"Unknown compiler option 'baseUrl'.","category":1,"code":5023},{"messageText":"Unknown compiler option 'paths'.","category":1,"code":5023},{"messageText":"Unknown compiler option 'types'.","category":1,"code":5023}]`"

     remove `node_modules/typescript` and run `npm install typescript@beta`. This repo now uses ts 2.0

??? info "There are multiple modules with names that only differ in casing"

     change `c:\[path to angular-starter]` to `C:\[path to angular-starter]` see [926#issuecomment-245223547](https://github.com/AngularClass/angular-starter/issues/926#issuecomment-245223547)

## 支持、问题或反馈

> Contact us anytime for anything about this repo or Angular

- [Chat: AngularClass.slack](http://angularclass.com/member-join/)
- [Twitter: @AngularClass](https://twitter.com/AngularClass)
- [Gitter: AngularClass/angular2-webpack-starter](https://gitter.im/angularclass/angular2-webpack-starter)

## 部署

### Docker

To run project you only need host machine with **operating system** with installed **git** (to clone this repo)
and [docker](https://www.docker.com/) and thats all - any other software is not needed
(other software like node.js etc. will be automatically downloaded and installed inside docker container during build step based on dockerfile).

#### 安装 docker

**MacOS:**

`brew cask install docker`

And run docker by Mac bottom menu> launchpad > docker (on first run docker will ask you about password)

**Ubuntu:**

```sh
sudo apt-get update
sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
sudo apt-add-repository 'deb https://apt.dockerproject.org/repo ubuntu-xenial main'
sudo apt-get update
apt-cache policy docker-engine
sudo apt-get install -y docker-engine
sudo systemctl status docker  ## test:  shoud be ‘active’
```

And add your user to docker group (to avoid `sudo` before using `docker` command in future):

```sh
sudo usermod -aG docker $(whoami)
```

and logout and login again.

#### 构建镜像

Because _node.js_ is big memory consumer you need 1-2GB RAM or virtual memory to build docker image
(it was successfully tested on machine with 512MB RAM + 2GB virtual memory - building process take 7min)

Go to main project folder. To build big (~280MB) image which has cached data and is able to **FAST** rebuild
(this is good for testing or staging environment) type:

`docker build -t angular-starter .`

To build **SMALL** (~20MB) image without cache (so each rebuild will take the same amount of time as first build)
(this is good for production environment) type:

`docker build --squash="true" -t angular-starter .`

The **angular-starter** name used in above commands is only example image name.
To remove intermediate images created by docker on build process, type:

`docker rmi -f $(docker images -f "dangling=true" -q)`

#### 运行镜像

To run created docker image on [localhost:8080](localhost:8080) type (parameter `-p 8080:80` is host:container port mapping)

`docker run --name angular-starter -p 8080:80 angular-starter &`

And that's all, you can open browser and go to [localhost:8080](localhost:8080).

#### Build and Run image using docker-compose

To create and run docker image on [localhost:8080](localhost:8080) as part of large project you may use **docker-compose**. Type

`docker-compose up &`

And that's all, you can open browser and go to [localhost:8080](localhost:8080).

#### Run image on sub-domain

If you want to run image as virtual-host on sub-domain you must setup [proxy](https://github.com/jwilder/nginx-proxy)
. You should install proxy and set sub-domain in this way:

```sh
docker pull jwilder/nginx-proxy:alpine
docker run -d -p 80:80 --name nginx-proxy -v /var/run/docker.sock:/tmp/docker.sock:ro jwilder/nginx-proxy:alpine
```

And in your `/etc/hosts` file (linux) add line: `127.0.0.1 angular-starter.your-domain.com` or in yor hosting add folowing DNS record (wildchar `*` is handy because when you add new sub-domain in future, you don't need to touch/add any DNS record)

```config
Type: CNAME
Hostname: *.your-domain.com
Direct to: your-domain.com
TTL(sec): 43200
```

And now you are ready to run image on subdomain by:

```sh
docker run -e VIRTUAL_HOST=angular-starter.your-domain.com --name angular-starter angular-starter &
```

#### Login into docker container

`docker exec -t -i angular-starter /bin/bash`

### Netlify

You can quickly create a free site to get started using this
starter kit in production on [Netlify](https://www.netlify.com/):

[![Deploy to Netlify](https://www.netlify.com/img/deploy/button.svg)](https://app.netlify.com/start/deploy?repository=https://github.com/AngularClass/angular-starter)

---

enjoy — [**PatrickJS**](https://twitter.com/gdi2290)

---

## 证书

[MIT](/LICENSE)
