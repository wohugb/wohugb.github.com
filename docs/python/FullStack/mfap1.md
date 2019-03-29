# 使用 Python，Flask 和 Angular 构建现代 Web 应用程序 - 第 1 部分

> https://auth0.com/blog/using-python-flask-and-angular-to-build-modern-apps-part-1/

> 在本系列中，您将学习如何使用 Python，Flask 和 Angular 创建现代 Web 应用程序。

在本系列中，您将学习如何使用 Python，Flask 和 Angular 创建现代 Web 应用程序。
您将使用此堆栈构建 SPA 和后端 API 以公开考试和问题，以便用户可以测试他们对不同技术的知识。在这个 GitHub 存储库中，您可以找到在本系列的第一部分中创建的最终代码。

到目前为止，这个系列包含三个部分:

- 第 1 部分包括引导 Flask 应用程序，使用 SQLAlchemy ORM 管理实体以及引导 Angular 应用程序等主题。
- 第 2 部分包括保护 Flask 应用程序，处理 Angular 表单和保护 Angular Apps 等主题。
- 第 3 部分包括配置 Angular Material，处理授权和使用 Alembic 迁移数据库等主题。

## 你将要建立什么

在本系列中，您将使用 Python，Flask 和 Angular 构建基于现代架构的 Web 应用程序。
使用 Angular，您将构建一个 SPA（单页应用程序），允许用户浏览考试和问题。
这些用户在通过身份验证后，将能够通过选择问题所揭示的多个选项之一来测试他们关于特定主题的知识。
然后，当您的用户提交他们的答案时，您的后端将检查他们是对还是错，记录结果，并将此结果发回给用户。

当您期待构建现代 Web 应用程序时，您将使用 Auth0 作为应用程序的身份管理系统。
您还将在数据库中保留所有考试，问题，替代方案和结果。

## 为何选择 Python，Flask 和 Angular

正如 StackOverflow 最近分析的那样，Python 是增长最快的编程语言之一，在平台上提出的问题数量上甚至超过了 Java。
除此之外，该语言也在 GitHub 上大量采用。
在这个平台上，Python 在 2017 年开放的拉动请求数量上占据第二的位置。

在使用 Python 开发 Web 应用程序时，您必须在两个流行的框架之间进行选择：Django 或 Flask。
Django 比 Flask 更成熟，更受欢迎。
然而，Flask 也有其优势。
从一开始，Flask 就是可扩展的，并且易于入门。
与 Django 相比，使用 Flask 构建的应用程序明显更轻。
因此，Python 开发人员通常将 Flask 称为微框架。

对于前端应用程序，您将使用 Angular，因为这是最流行的框架之一。
要了解此框架的优点，您可以在 Rangle.io 上查看这个漂亮的页面。
如本页所述，Angular 为开发人员提供了构建和构建大型 JavaScript 应用程序所需的工具。
除此之外，Angular 比一些替代品有一些很大的优势。
例如，Angular 由 Google 工程师构建和支持。
除了这些工程师之外，还有一个庞大的社区随时准备帮助您解决问题。

正如您所看到的，通过选择 Python，Flask 和 Angular 来构建 Web 应用程序，您可以放心，您将始终能够依靠优秀且蓬勃发展的社区来为您提供支持。

## 依赖

既然您已经了解了为什么 Python，Flask 和 Angular 构建了一个很好的堆栈来构建现代 Web 应用程序，那么您就可以安装本地依赖项了。
本节分为两个小节，以突出显示后端和前端视图中的环境依赖性。

### 后端依赖

首先，您需要一个最新版本的 Python 3。
如果您的开发计算机上没有可用的 Python 3，请浏览 Python 下载页面并进行安装。

安装 Python 后，您必须安装 pipenv 工具。
该工具旨在为 Python 开发人员带来最好的打包世界（bundler，composer，npm 等）。
此外，该工具是 Windows 上的一流公民。
因此，如果您仍然停留在此操作系统上，请不要担心，您将受到保护。

要安装 pipenv，只需打开终端并键入以下命令：

```sh
# depending on the environment, you will have to use
# pip3 instead of pip (just once)
pip install pipenv
```

Python 和 pipenv 一起就足以开始开发 Flask 应用程序了。
但是，由于您希望保留事务数据，因此仍需要选择和配置数据库引擎。
为了让您的生活更轻松，您将使用 SQLAlchemy 来持久化并从所选引擎中检索数据。
如果您没有 SQLAlchemy 的经验，请查看关于该主题的这篇精彩的介绍性文章。
在那里，您将了解到通过使用 SQLAlchemy ORM（对象关系映射）扩展，您将能够轻松连接和使用任何主要的 SQL 数据库引擎（例如，

如果您的计算机上没有可用的数据库，一个很好的方法是使用 Docker 创建一个新数据库:

```sh
docker run --name online-exam-db \
 -p 5432:5432 \
 -e POSTGRES_DB=online-exam \
 -e POSTGRES_PASSWORD=0NLIN3-ex4m \
 -d postgres
```

当然，要运行上面的命令，您需要在本地安装 Docker。

### 前端依赖

当您打算使用 Angular 创建前端应用程序时，您需要在计算机上安装 Node.js 和 NPM。
您可以通过从 Node.js 下载页面下载并执行安装程序（根据您的操作系统选择一个）来同时安装这两个工具。
另一种方法是使用 NVM 之类的工具来管理多个主动节点版本。
在开发机器上，这可能是最好的选择。

无论您选择哪种安装方法，请确保使用的是最新版本的 Node.js（即> = 8）。

正确安装 Node.js 和 NPM 后，可以使用 npm 命令安装 Angular CLI 工具。
您将使用此 CLI（命令行界面）来引导前端应用程序，启动开发服务器以及创建 Angular 组件，服务等。

使用以下命令安装 Angular CLI:

```sh
nstall -g @angular/cli
```

## 自举 Python 应用程序

现在您已经处理了环境依赖关系，您可以专注于开发应用程序。
对于初学者，您可以创建一个目录来保存应用程序的所有前端和后端源代码。
此外，您可能希望将所有内容提交到 Git 存储库以保证您的进度得以保存。
因此，请使用以下命令开始构建应用程序:

```sh
# create the project root directory
mkdir online-exam
# move into it
cd online-exam
# initialize it as a Git repository
git init
```

之后，您将需要专门为 Flask 后端应用程序创建的目录:

```sh
# create directory to hold backend source code
mkdir backend
# move into it
cd backend
```

然后，您将需要使用 pipenv 来创建虚拟环境。
如果您不知道为什么需要虚拟环境，请查看 pipenv 作者撰写的这篇精彩文章。

```sh
# initialize the virtual environment
pipenv --three
```

当您使用 Git 备份代码时，您可能希望忽略某些文件。
为此，请在项目根目录中创建名为.gitignore 的文件，并将此 URL 中的规则复制到其中。

## 使用 SQLAlchemy ORM 管理实体

在设置虚拟环境后，您可以开始开发应用程序的功能。
一个好的起点是定义实体并配置 SQLAlchemy 以持久化并检索这些实体的实例。
因此，您将使用 pipenv 安装 sqlalchemy 软件包和驱动程序以连接到您的数据库。
如果您使用的是 PostgreSQL，则可以将 SQLycopg2-binary 驱动程序与 SQLAlchemy 一起使用。
如果您正在使用其他数据库引擎，请检查此页面以选择一个好的驱动程序。

以下命令显示如何使用 pipenv 安装 sqlalchemy 和 psycopg2-binary 驱动程序:

```sh
# install sqlalchemy and psycopg2 on the venv
pipenv install sqlalchemy psycopg2-binary
```

安装 SQLAlchemy 和驱动程序以连接到数据库后，您可以开始创建实体.
为此，请使用以下命令在另一个名为 src 的模块中创建名为 entities 的模块:

```sh
# create directories
mkdir -p src/entities
# create file to mark src as a module
touch src/**init**.py
# create file to mark entities as a module
touch src/entities/**init**.py
# create file to hold some boilerplate code
touch src/entities/entity.py
```

上面的前两个`touch`命令只是创建空的`** init **.py`文件，将两个目录标记为 Python 模块。
最后一个 `touch` 命令创建将保存名为 `Entity` 的类的文件。
您将使用此类作为所有实体的超类。
这将有助于避免重复某些样板代码连接到数据库并定义一些常见属性（例如 id 和 created_at）：

```python
# coding=utf-8
from datetime import datetime
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_url = 'localhost:5432'
db_name = 'online-exam'
db_user = 'postgres'
db_password = '0NLIN3-ex4m'
engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_url}/{db_name}')
Session = sessionmaker(bind=engine)

Base = declarative_base()

class Entity():
id = Column(Integer, primary_key=True)
created_at = Column(DateTime)
updated_at = Column(DateTime)
last_updated_by = Column(String)

    def __init__(self, created_by):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.last_updated_by = created_by
```

然后，在定义 Entity 类之后，您可以创建一个名为 exam.py 的文件来表示您的第一个实体:

```sh
touch src/entities/exam.py
```

On this file, insert the following code:

```python
# coding=utf-8
from sqlalchemy import Column, String
from .entity import Entity, Base
class Exam(Entity, Base):
**tablename** = 'exams'

    title = Column(String)
    description = Column(String)

    def __init__(self, title, description, created_by):
        Entity.__init__(self, created_by)
        self.title = title
        self.description = description
```

Here, you are defining a class called Exam that inherits from Entity and from Base.
This entity contains, besides the properties defined by its superclasses, two properties: title and description.
Besides that, this class also defines that instances of it must be persisted to and retrieved from a table called exams.

Having the Exam and Entity classes properly defined, you can create a script called main.py in the src directory to test if they are really connecting to the database:

```sh
touch src/main.py
```

Inside this script, you can add the following code:

```python
# coding=utf-8
from .entities.entity import Session, engine, Base
from .entities.exam import Exam
# generate database schema
Base.metadata.create_all(engine)
# start session
session = Session()
# check for existing data
exams = session.query(Exam).all()
if len(exams) == 0: # create and persist dummy exam
python_exam = Exam("SQLAlchemy Exam", "Test your knowledge about SQLAlchemy.", "script")
session.add(python_exam)
session.commit()
session.close()
    # reload exams
    exams = session.query(Exam).all()
# show existing exams
print('### Exams:')
for exam in exams:
print(f'({exam.id}) {exam.title} - {exam.description}')
```

As you can see, the code in this script is quite simple.
Here is a list that summarizes what it does:

It starts by importing Session, engine, and Base from the .entities.entity module.
Then, it imports the Exam class from the .entities.exam module.
Then, it generates (if needed) the database schema.
After generating the schema, it queries all instances of Exam.
Then, if there are no exams on the database, it creates a new one and queries all instances of the Exam class again.
Lastly, it prints the exams retrieved from the database.
To run this script, you will have to activate the virtual environment (created by pipenv) then use python to trigger the src.main module:

```sh
# activate virtual environment
pipenv shell
# run main module
python -m src.main
```

If everything works as expected, your module will create an instance of Exam, persist to the database, and print its details on the terminal.

SQLAlchemy ORM querying a PostgreSQL database

By the way, this might be a good time to save your progress:

```sh
git add . && git commit -m "adding SQLAlchemy and some entities"
```

## 使用 Flask 管理 HTTP 请求

Now that your app is connected to a database, it's time to transform it into a Flask web application.
To do so, the first thing you will need is to install Flask.
Besides Flask, you will also need to install marshmallow to handle serialization and deserialization of JSON objects.
To install both dependencies, issue the following command in the backend directory:

pipenv install flask marshmallow
After that, you will need to update the ./src/entities/exam.py file as follows:

```python
# coding=utf-8
from marshmallow import Schema, fields
# ...
other import statements ...
# ...
```

Exam class definition ...

```python
class ExamSchema(Schema):
id = fields.Number()
title = fields.Str()
description = fields.Str()
created_at = fields.DateTime()
updated_at = fields.DateTime()
last_updated_by = fields.Str()
```

In the new version of this file, you are using the Schema class of marshmallow to define a new class called ExamSchema.
You will use this class to transform instances of Exam into JSON objects.

After defining ExamSchema, you can refactor the ./src/main.py file to expose two endpoints:

```python
# coding=utf-8
from flask import Flask, jsonify, request
from .entities.entity import Session, engine, Base
from .entities.exam import Exam, ExamSchema
# creating the Flask application
app = Flask(**name**)
# if needed, generate database schema
Base.metadata.create_all(engine)
@app.route('/exams')
def get_exams(): # fetching from the database
session = Session()
exam_objects = session.query(Exam).all()

    # transforming into JSON-serializable objects
    schema = ExamSchema(many=True)
    exams = schema.dump(exam_objects)

    # serializing as JSON
    session.close()
    return jsonify(exams.data)

@app.route('/exams', methods=['POST'])
def add_exam(): # mount exam object
posted_exam = ExamSchema(only=('title', 'description'))\
 .load(request.get_json())

    exam = Exam(**posted_exam.data, created_by="HTTP post request")

    # persist exam
    session = Session()
    session.add(exam)
    session.commit()

    # return created exam
    new_exam = ExamSchema().dump(exam).data
    session.close()
    return jsonify(new_exam), 201
```

This file now creates a Flask application, based on SQLAlchemy and PostgreSQL, that is capable of accepting POST requests to create new instances of exam and capable of accepting GET requests to serialize these instances as a JSON array.

Now, to facilitate running this application, you can create a script called bootstrap.sh in the backend directory with the following code:

```sh
#!/bin/bash
export FLASK_APP=./src/main.py
source \$(pipenv --venv)/bin/activate
flask run -h 0.0.0.0
```

This script does three things:

it sets ./src/main.py as the value of the FLASK_APP environment variable (this is needed by the last command);
it activates the virtual environment;
and it runs flask listening on all interfaces (-h 0.0.0.0).
Then, to test everything, you can use the following commands:

```sh
# make script executable
chmod u+x bootstrap.sh
# execute script in the background
./bootstrap.sh &
# create a new exam
curl -X POST -H 'Content-Type: application/json' -d '{
"title": "TypeScript Advanced Exam",
"description": "Tricky questions about TypeScript."
}' http://0.0.0.0:5000/exams
# retrieve exams
curl http://0.0.0.0:5000/exams
```

The first command on the snippet above transforms the bootstrap.sh script into an executable file.
After that, it runs this script in the backend so you can keep using the same terminal.
When the Flask application is up and running, you can use the two curl commands to interact with it.
The first one issues POST requests to create new exams and the second one lists all exams persisted on the database.

Flask application and SQLAlchemy ORM integrated.

Besides using curl, you can also fetch exams by browsing to http://0.0.0.0:5000/exams.

You have made some good progress.
So, it's better to save everything:

```sh
git add . && git commit -m "integrating Flask RESTful endpoints and SQLAlchemy"
```

## 在 Flask 应用程序上处理 CORS

As your Flask app will receive requests from a SPA, you will need to allow CORS on it.
If you don't do so, most browsers will block requests to your API because the backend does not explicitly allow Cross-Origin Resource Sharing (CORS).

Luckily, there is a Flask module called flask-cors that is easy to configure.
So, to install this module, issue the following command in your backend directory:

```sh
pipenv install flask-cors
```

Then, update the main.py file to take advantage of this module:

```python
# coding=utf-8
from flask_cors import CORS
# ...
other import statements ...
# creating the Flask application
app = Flask(**name**)
CORS(app)
# ...
create_all(engine) and endpoint definitions ...
```

Without any further configuration, flask-cors allows CORS for all domains on all routes.
During the development process, this configuration will be enough.
However, in the future, you will probably want to be more restrictive.
When the day comes, check the official documentation of the flask-cors module to learn how to tweak these settings.

Now, before switching to Angular, you can save your progress and leave your Flask application up and running:

```sh
# commit your progress
git add . && git commit -m "enabling CORS"
# run the Flask app in the background
./bootstrap.sh &
```

## 引导 Angular 应用程序

To create your Angular application, you will use the ng tool that Angular CLI made available.
So, move back to the project root directory and issue ng new frontend.
This will create the basic structure of an Angular app.
The following snippet summarizes the commands to create your app and to commit it untouched to your Git repository:

```sh
# change working directory to project root
cd ..
# run @angular/cli to bootstrap the Angular app
ng new frontend
# move working directory to your frontend app
cd frontend
# commit template Angular project
git add . && git commit -m "bootstrapping an Angular project"
```

## 使用 Angular 消耗 Flask Endpoints

After creating your Angular app, the next thing you will need is to create a file called env.ts inside the ./frontend/src/app directory with the following code:

```sh
export const API_URL = 'http://localhost:5000';
```

For now, this TypeScript module simply exports a single constant (API_URL) that references your Flask backend application running locally.
In the third part of this series, you will enhance this module to define different API_URL values depending on the environment.

Now, you can create a new directory called exams inside ./frontend/src/app to hold files related to this entity.
In this directory, you will create two files: exam.model.ts and exams-api.service.ts.
The first file (exam.model.ts) will have a TypeScript class to represent exams:

```js
export class Exam {
constructor(
public title: string,
public description: string,
public \_id?: number,
public updatedAt?: Date,
public createdAt?: Date,
public lastUpdatedBy?: string,
) { }
}
```

The second file, exams-api.service.ts, will create a service that uses HttpClient to fetch exams from your Flask backend application:

```js
import {Injectable} from '@angular/core';
import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import {Observable} from 'rxjs/Observable';
import 'rxjs/add/operator/catch';
import {API_URL} from '../env';
import {Exam} from './exam.model';

@Injectable()
export class ExamsApiService {

constructor(private http: HttpClient) {
}

private static \_handleError(err: HttpErrorResponse | any) {
return Observable.throw(err.message || 'Error: Unable to complete request.');
}

// GET list of public, future events
getExams(): Observable<Exam[]> {
return this.http
.get(`${API_URL}/exams`)
.catch(ExamsApiService.\_handleError);
}
}
```

As this service depends on HttpClient, you will need to import HttpClientModule from Angular in your AppModule declaration.
Besides that, you will have to register ExamsApiService as a provider.
So, open the ./frontend/src/app/app.module.ts file and replace its contents with this:

```js
import { BrowserModule } from "@angular/platform-browser";
import { NgModule } from "@angular/core";
import { HttpClientModule } from "@angular/common/http";

import { AppComponent } from "./app.component";
import { ExamsApiService } from "./exams/exams-api.service";

@NgModule({
  declarations: [AppComponent],
  imports: [BrowserModule, HttpClientModule],
  providers: [ExamsApiService],
  bootstrap: [AppComponent]
})
export class AppModule {}
```

Now, you will have to update the ./frontend/src/app/app.component.ts file to use your new service to fetch data from your Flask app:

```js
import {Component, OnInit, OnDestroy} from '@angular/core';
import {Subscription} from 'rxjs/Subscription';
import {ExamsApiService} from './exams/exams-api.service';
import {Exam} from './exams/exam.model';

@Component({
selector: 'app-root',
templateUrl: './app.component.html',
styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit, OnDestroy {
title = 'app';
examsListSubs: Subscription;
examsList: Exam[];

constructor(private examsApi: ExamsApiService) {
}

ngOnInit() {
this.examsListSubs = this.examsApi
.getExams()
.subscribe(res => {
this.examsList = res;
},
console.error
);
}

ngOnDestroy() {
this.examsListSubs.unsubscribe();
}
}
```

Lastly, you will have to update its template (app.component.html) to show the exams fetched:

```html
<div style="text-align:center">
  <h1>Exams</h1>
</div>
<h2>Here are the exams created so far:</h2>
<ul>
  <li *ngFor="let exam of examsList">
    {{exam.title}}
  </li>
</ul>
```

With all these changes in place, you can run your Angular application (run ng serve on the frontend directory) to check if everything is working as expected.
After Angular finishes compiling your app, you can browse to http://localhost:4200.
On this URL, you will see a page similar to this:

使用 Angular 从 Flask 应用程序中获取数据

这包含了系列的第一部分。
因此，在继续下一部分之前，不要忘记保存进度:

```sh
git add .
git commit -m "integrating Flask and Angular"
```

"使用 Angular 和 Flask 开发 Web 应用程序非常简单！"

## 结论和后续步骤

在本系列的第一部分中，您使用 pipenv 来引导 Flask 后端 API。
之后，您使用 SQLAlchemy ORM 将 Flask 应用程序与数据库集成。
然后，您安装并运行了 Angular CLI 以创建新的 Angular SPA。
最后，您从后端进行了 SPA 提取检查以向访问者显示。
这些功能共同为创建依赖于 Flask 和 Angular 的应用程序铺平了道路，以提供现代用户体验。

在下一篇文章中，您将了解现代 Web 应用程序如何管理身份，您将增强后端和前端应用程序以包含更多功能。
敬请关注！
