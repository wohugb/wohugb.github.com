# Angular

## 第一步: 配置开发环境

```sh
npm install -g @angular/cli
```

## 第二步: 创建新项目

```sh
ng new my-app
```

## 第三步: 启动应用

```sh
cd my-app
ng serve --open
```

## 第四步: 编辑第一个组件

!!! note "src/app/app.component.ts"
    ```js
    export class AppComponent {
      title = 'My First Angular App';
    }
    ```

!!! note "src/app/app.component.css"
    ```css
    h1 {
      color: #369;
      font-family: Arial, Helvetica, sans-serif;
      font-size: 250%;
    }
    ```