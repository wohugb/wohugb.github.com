## 安装
```sh
$ npm install pm2 -g
```
### 升级
```
# 安装最新版本
$ npm install pm2@latest -g
# 更新所有进程
$ pm2 update
```

## 配置

```yml
apps:
  - script   : app.js
    instances: 4
    exec_mode: cluster
  - script : worker.js
    watch  : true
    env    :
      NODE_ENV: development
    env_production:
      NODE_ENV: production
```

## 使用

```sh
# 启动应用
$ pm2 start app.json
# 重新加载应用
$ pm2 reload app
```

## 日志

```sh
# 查看日志
$ pm2 logs app
# 错误日志
$ pm2 logs app --err --lines 1000
# 清空日志
$ pm2 flush
```