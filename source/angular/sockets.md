# 使用TypeScript的实时应用程序：集成Web套接字，Node和Angular

作者: [Luis Aviles](https://medium.com/dailyjs/real-time-apps-with-typescript-integrating-web-sockets-node-angular-e2b57cbd1ec1)

使用TypeScript从头开始构建实时聊天应用程序

前段时间我只使用TypeScript语言实现了一个简单的聊天应用程序。 主要目标是写一个演示来解释如何在客户端和服务器上使用这种编程语言。 客户端应用程序正在使用最新的Angular功能。

在这篇文章中，我将向您展示我是如何从头开始实施该应用的。

演示：TypeScript聊天应用程序

## 什么是实时应用程序？

根据维基百科的定义，实时应用程序允许信息一发布即可收到，而不需要定期检查信息来源以获取更新。
因此，这种应用程序应该给用户感觉事件和行为立即发生。

## WebSockets

WebSockets是一种提供双向通信信道的协议。
这意味着浏览器和Web服务器可以维护实时通信，并在连接打开时来回发送消息。

Websockets通信

## 应用结构

我们将分离服务器相关的代码和客户端代码。
我将详细解释最重要的文件。
目前，这是我们应用程序的预期结构：

    server/
      |- src/
      |- package.json
      |- tsconfig.json
      |- gulpfile.js
    client/
      |- src/
      |- package.json
      |- tsconfig.json
      |- .angular-cli.json

## 服务器代码

由于WebSockets是一个规范，我们可以找到它的几个实现。
我们可以选择TypeScript或任何其他编程语言。

在这种情况下，我们将使用Socket.IO，它是最快和最可靠的实时引擎之一。

### 为什么在服务器端代码上使用TypeScript？

TypeScript带有非常酷的功能，并且经常更新。
它可以防止大约15％的错误。
你需要更多的理由吗？ 😄

### 初始化服务器应用

创建一个package.json文件，然后安装以下依赖项:

```bash
  npm install --save express socket.io @types/express @types/socket.io
```

我们需要安装一些devDependencies以允许集成gulp和typescript，以便我们可以稍后使用这些工具轻松定义构建任务:

```bash
npm install --save-dev typescript gulp gulp-typescript
```

### TypeScript编译器

使用以下内容创建一个tsconfig.json文件:

```json
{
  "files": [
    "src/*.ts",
    "src/model/*.ts"
  ],
  "compilerOptions": {
    "target": "es5"
  }
}
```

### 定义的数据模型

利用静态类型，我们定义一个小数据模型如下:

```ts
export class User {
    constructor(private name: string) {}
}

export class Message {
    constructor(private from: User, private content: string) {}
}

export class ChatMessage extends Message{
    constructor(from: User, content: string) {
        super(from, content);
    }
}
```

..让我们看看更多的细节到我们的server/src目录:

    server/
      |- src/
        |- model/
            |- message.model.ts
            |- user.model.ts
        |- index.ts
        |- server.ts
      |- package.json
      |- tsconfig.json
      |- gulpfile.js

### 聊天服务器实现

服务器目录中的主要文件是index.ts和chat-server.ts。
第一个允许我们创建和导出我们的ChatServer应用程序，而最后一个包含express和socket.IO配置：

index.ts

```ts
import { ChatServer } from './chat-server';

let app = new ChatServer().getApp();
export { app };
```

chat-server.ts

```ts
import { createServer, Server } from 'http';
import * as express from 'express';
import * as socketIo from 'socket.io';

import { Message } from './model';

export class ChatServer {
    public static readonly PORT:number = 8080;
    private app: express.Application;
    private server: Server;
    private io: SocketIO.Server;
    private port: string | number;

    constructor() {
        this.createApp();
        this.config();
        this.createServer();
        this.sockets();
        this.listen();
    }

    private createApp(): void {
        this.app = express();
    }

    private createServer(): void {
        this.server = createServer(this.app);
    }

    private config(): void {
        this.port = process.env.PORT || ChatServer.PORT;
    }

    private sockets(): void {
        this.io = socketIo(this.server);
    }

    private listen(): void {
        this.server.listen(this.port, () => {
            console.log('Running server on port %s', this.port);
        });

        this.io.on('connect', (socket: any) => {
            console.log('Connected client on port %s.', this.port);
            socket.on('message', (m: Message) => {
                console.log('[server](message): %s', JSON.stringify(m));
                this.io.emit('message', m);
            });

            socket.on('disconnect', () => {
                console.log('Client disconnected');
            });
        });
    }

    public getApp(): express.Application {
        return this.app;
    }
}
```

### 服务器类

前面的代码将给出以下类和关系的结果：

![服务器类图](https://cdn-images-1.medium.com/max/2000/1*-FNkJxTH5kDiBPdJx4tVIg.png)

### 构建并运行服务器

为了获得Node.js的V8引擎所需的JavaScript文件，我们可以将一个构建任务添加到我们的gulpfile.js文件中：

gulpfile.js

```js
var gulp = require("gulp");
var ts = require("gulp-typescript");
var tsProject = ts.createProject("tsconfig.json");

gulp.task("build", function () {
    return tsProject.src()
        .pipe(tsProject())
        .js.pipe(gulp.dest("./dist"));
});
```

如您所见，构建过程（JavaScript文件）的输出将位于indist目录中。
要执行此操作，您需要运行：

```bash
gulp build
```

现在我们可以运行`node dist/index.js`命令让服务器运行。

## 客户代码

让我们使用最新的Angular CLI版本生成客户端目录：

```bash
ng new typescript-chat-client --routing --prefix tcc --skip-install
```

然后安装运行`npm install`的依赖项（我更喜欢使用`Yarn`来执行此步骤）：

```bash
cd typescript-chat-client
yarn install
```

### 添加角度材质

查找并按照最新指南在Angular CLI项目中安装Angular Material。

作为我们项目结构中使用最佳实践的一部分，我们可以创建共享和物料模块：

    client/
      |- src/
        |- app/
            |- chat/
            |- shared/
              |- material/
                  |- material.module.ts
              |- shared.module.ts
            |-app.module.ts

我们可以从命令行界面执行此操作：

```sh
ng generate module shared --module app
ng generate module shared/material --module shared
```

检查`app.module.ts`和`shared.module.ts`中的更改以查看这些模块之间创建的关系。

### 添加express和socket.IO

我们需要将express和socket.io模块添加到我们的客户端应用程序中：

```bash
npm install express socket.io --save
```

### 聊天模块和组件

在开始为聊天应用程序创建组件之前，先创建一个新模块：

```sh
ng generate module chat --module app
```

现在将一个组件添加到最新的模块中：

```sh
ng generate component chat --module chat
```

为了使用网络套接字和自定义模型，我们创建另一个共享文件夹。
这段时间内聊天目录中：

```sh
ng generate service chat/shared/services/socket --module chat
ng generate class chat/shared/model/user
ng generate class chat/shared/model/message
```

我们将以类似于以下的结构结束：

    client/
      |- src/
        |- app/
            |- chat/
              |- shared/
                |- model/
                    |- user.ts
                    |- message.ts
                |- services/
                    |- socket.service.ts
            |- shared/
            |-app.module.ts

### Observables和Web套接字

由于我们的Angular应用程序带有RxJS，因此我们可以使用Observables来捕获Socket.IO事件：

socket.service.ts

```ts
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs/Observable';
import { Observer } from 'rxjs/Observer';
import { Message } from '../model/message';
import { Event } from '../model/event';

import * as socketIo from 'socket.io-client';

const SERVER_URL = 'http://localhost:8080';

@Injectable()
export class SocketService {
    private socket;

    public initSocket(): void {
        this.socket = socketIo(SERVER_URL);
    }

    public send(message: Message): void {
        this.socket.emit('message', message);
    }

    public onMessage(): Observable<Message> {
        return new Observable<Message>(observer => {
            this.socket.on('message', (data: Message) => observer.next(data));
        });
    }

    public onEvent(event: Event): Observable<any> {
        return new Observable<Event>(observer => {
            this.socket.on(event, () => observer.next());
        });
    }
}
```

我们需要定义一些枚举来管理应用中的操作和事件：

```ts
// Actions you can take on the App
export enum Action {
    JOINED,
    LEFT,
    RENAME
}

// Socket.io events
export enum Event {
    CONNECT = 'connect',
    DISCONNECT = 'disconnect'
}
```

现在我们准备好收听来自服务器的消息：

```ts
import { Component, OnInit } from '@angular/core';

import { Action } from './shared/model/action';
import { Event } from './shared/model/event';
import { Message } from './shared/model/message';
import { User } from './shared/model/user';
import { SocketService } from './shared/services/socket.service';

@Component({
  selector: 'tcc-chat',
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.css']
})
export class ChatComponent implements OnInit {
  action = Action;
  user: User;
  messages: Message[] = [];
  messageContent: string;
  ioConnection: any;

  constructor(private socketService: SocketService) { }

  ngOnInit(): void {
    this.initIoConnection();
  }

  private initIoConnection(): void {
    this.socketService.initSocket();

    this.ioConnection = this.socketService.onMessage()
      .subscribe((message: Message) => {
        this.messages.push(message);
      });

    this.socketService.onEvent(Event.CONNECT)
      .subscribe(() => {
        console.log('connected');
      });

    this.socketService.onEvent(Event.DISCONNECT)
      .subscribe(() => {
        console.log('disconnected');
      });
  }

  public sendMessage(message: string): void {
    if (!message) {
      return;
    }

    this.socketService.send({
      from: this.user,
      content: message
    });
    this.messageContent = null;
  }

  public sendNotification(params: any, action: Action): void {
    let message: Message;

    if (action === Action.JOINED) {
      message = {
        from: this.user,
        action: action
      }
    } else if (action === Action.RENAME) {
      message = {
        action: action,
        content: {
          username: this.user.name,
          previousUsername: params.previousUsername
        }
      };
    }

    this.socketService.send(message);
  }
}
```

材料代码和UI事件在此文件中被省略

一旦ChatComponent被初始化，组件将订阅SocketService observables以开始接收连接事件或传入消息。

sendMessage和sendNotification函数将通过相同的服务发送相应的内容。
此时发送的通知是重命名用户和用户加入。

### 聊天应用功能

Angular CLI

Angular 5

Angular Material

Validation Forms

## 源代码

在这个GitHub仓库中找到完整的项目：

> [github.com/luixaviles/socket-io-typescript-chat](https://github.com/luixaviles/socket-io-typescript-chat)

## 现场演示

打开[typescript-chat.firebaseapp.com](https://typescript-chat.firebaseapp.com/)并在您喜爱的浏览器中打开两个或更多标签并开始对话。

如果你喜欢这篇文章，一定要分享给你的朋友，或给它拍手。👏

您可以在[Twitter](https://twitter.com/luixaviles)和[GitHub](https://github.com/luixaviles)上关注我，以了解更多关于我的工作的信息。

感谢您的阅读！ — 路易斯阿维莱斯