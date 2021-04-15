# 大鼻子文档分享主页

- 使用 MkDocs: <http://jekyllbootstrap.com>
- 以及 Material for MkDocs: <https://squidfunk.github.io/mkdocs-material/>

## 安装 mkdocs-material

### Manually Upgrade mkdocs-material Version with pip

```sh
pip install --upgrade mkdocs-material
pip show mkdocs-material
```

### Includemkdocs-material Python package in a pip requirements.txt file

创建 `requirements.txt` 输入

```txt
mkdocs-material
```

安装

```sh
pip install -r requirements.txt
```

### back

```yml
# nav:
#   - Ð巴别塔: index.md
#   - GitHub: github/collections.md
#   - 赞表: awesome/awesome.md
#   - 器:
#       - 利器: tools/index.md
#       - vscode:
#           - 简介: tools/vscode/index.md
#           - Prettier: tools/vscode/prettier.md
#   - 智能:
#       - AI: ai/index.md
#       - 自然语言处理: ai/nlp.md
#       - 机器学习: ai/deeplearning.md
#       - 赞表: ai/awesome.md
#       - 2018: ai/2018.md
#       - 2017: ai/2017.md
#       - 机器人:
#           - BOT: bot/index.md
#           - 开发框架: bot/framework.md
#           - ROS: bot/ros.md
#           - Arduino: bot/arduino.md
#       - IOT:
#           - 物联网: iot/InternetOfThings.md
#   - 无心:
#       - 概述: blockchain/index.md
#       - 技术树: blockchain/tree.md
#       - 术语: blockchain/term.md
#       - 赞表: blockchain/awesome.md
#       - 比特币: blockchain/bitcoin/index.md
#       - 山寨币: blockchain/altcoins.md
#       - IPFS: ipfs/index.md
#       - 以太坊:
#           - Serpent指南: blockchain/ethereum/serpent.md
#           - 开发计划: blockchain/ethereum/development.md
#           - 术语表: blockchain/ethereum/term.md
#           - 白皮书: blockchain/ethereum/whitepaper.md
#           - FAQ: blockchain/ethereum/ProofOfStake.md
#           - 网络状态: blockchain/ethereum/network-status.md
#       - twister:
#           - 概述: blockchain/twister/index.md
#           - UNIX: blockchain/twister/build-unix.md
#           - UBUNTU: blockchain/twister/building-on-ubuntu-debian.md
#           - OSX: blockchain/twister/build-osx.md
#           - Windows: blockchain/twister/compiling-for-windows.md

#   - Py:
#       - Python: python/python.md
#       - 赞表: python/awesome.md
#       - PIP:
#           - 概述: python/pip/index.md
#       - Django:
#           - 概述: python/django/index.md
#           - 赞表: python/django/awesome.md
#       - Flask:
#           - 概述: python/flask/index.md
#           - 赞表: python/flask/awesome.md
#       - Anaconda:
#           - 入门使用指南: python/Anaconda/QuickStart.md
#       - Framework:
#           - TOP11: python/framework.md
#       - FullStack:
#           - mfap0: python/FullStack/mfap0.md
#           - mfap1: python/FullStack/mfap1.md
#           - mfap2: python/FullStack/mfap2.md
#           - mfap3: python/FullStack/mfap3.md
#   - Node:
#       - NodeJs: nodejs/nodejs.md
#       - awesome: nodejs/awesome.md
#       - Express: nodejs/express.md
#       - KOA: nodejs/koa.md
#       - Mongoose: nodejs/mongoose.md
#       - PM2: nodejs/pm2.md
#       - 组件:
#           - QrCode:
#               - 概述: nodejs/node_modules/qrcode/readme.md
#               - API: nodejs/node_modules/qrcode/api.md
#           - GM: nodejs/node_modules/gm.md
#           - RSA:
#               - 概述: nodejs/node_modules/node-rsa/readme.md
#               - JSBN: nodejs/node_modules/node-rsa/jsbn.md
#   - Ng:
#       - 概述: angular/index.md
#       - cli: angular/cli.md
#       - 赞表: angular/awesome.md
#       - starter: angular/starter.md
#       - 升级: angular/migrate.md
#       - 升级6: angular/migrate6.md
#       - IO: angular/sockets.md
#       - MarkDown: angular/ngx-markdown.md
#   - 阿里:
#       - 阿里云: aliyun/index.md
#       - ECS: aliyun/ECS.md
#       - MonogoDb: aliyun/MonogoDb.md
#       - LBS: aliyun/LBS.md
#       - DDOS: aliyun/DDOS.md
#       - 云客服: aliyun/ykf.md
#       - 视频: aliyun/video.md
#   - 微信:
#       - 微信: wechat/index.md
#       - 公号: wechat/oa.md
#       - 第三方:
#           - 移动应用: wechat/app/index.md
#           - 网站应用: wechat/site/index.md
#           - 公众帐号: wechat/mp/index.md
#           - 第三方平台: wechat/d3f/index.md
#           - 返回码说明: wechat/code/index.md
#           - 资源下载:
#               - iOS资源下载: wechat/open/download/ios.md
#               - Android资源下载: wechat/open/download/android.md
#               - WP8资源下载: wechat/open/download/wp8.md
#               - 设计资源下载: wechat/open/download/design.md
#       - 企业微信: wechat/work.md
#       - 小程序: wechat/weapp-awesome.md
#   - 拼团:
#       - 佣金团: pin/group.md
#       - 阶梯团: pin/ladder.md
#       - 聚力团: pin/cohesion.md
#       - 生鲜:
#           - 平台: fresh/platform.md
#           - 教育: fresh/education.md
#           - 知识库: fresh/repository.md
#   - 教育:
#       - 幼儿园: education/kindergarten.md
#       - 小学: education/primary-school.md
#       - 初中: education/junior-middle-school.md
#       - 高中: education/senior-middle-school.md
#   - 寓所:
#       - 概述: apartment/index.md
#       - 泊寓: apartment/inboyu.md
#       - 邦舍公寓: apartment/boonself.md
#       - 自如寓: apartment/ziroom.md
#       - 蛋壳公寓: apartment/danke.md
#       - 冠寓: apartment/guanyu.md
#       - 相寓: apartment/1zu.md
#       - 悠然客公寓: apartment/youranke.md
#   - 行:
#       - 🚙: running/card.md
#       - 🚲: running/bicycle.md
#       - 🚶🏻: running/walk.md
```
