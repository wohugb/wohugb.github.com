# iOS 资源下载

​
开发工具包（SDK）

使用微信分享、登录、收藏、支付等功能需要的库以及文件。通过 CocoaPods 集成（详情查看接入流程接入流程）或点击下载以下开发工具包：

iOS 开发工具包 iOS 开发工具包（1.8.3 版本，包含支付功能）。
iOS 开发工具包 iOS 开发工具包（1.8.3 版本，不包含支付功能）。
使用微信语音识别接口、语音合成接口。点击下载 语音 SDK+Demo+开发文档语音 SDK+Demo+开发文档

使用微信图像识别接口。点击下载 图像 SDK+Demo+开发文档图像 SDK+Demo+开发文档

使用微信卡券功能接口。点击下载 卡券 SDK+开发文档卡券 SDK+开发文档

范例代码

包含了一个完整的范例工程，该范例的使用可以参阅 iOS 平台上手指南。点击下载 范例代码

范例代码
包含了一个完整的范例工程，该范例的使用可以参阅 iOS 平台上手指南。点击下载 范例代码

各版本信息

SDK1.8.3

1.SDK 增加调起微信刷卡支付接口

2.SDK 增加小程序订阅消息接口

3.修复小程序订阅消息接口没有 resp 的问题

SDK1.8.2
1.SDK 增加开发票授权 WXInvoiceAuthInsert
2.SDK 增加非税接口 WXNontaxPay
3.SDK 增加医保接口 WXPayInsurance 4.更换 MTA 库

SDK1.8.1
1.SDK 打开小程序支持指定版本（体验，开发，正式版）
2.SDK 分享小程序支持指定版本（体验，开发，正式版）
3.SDK 支持输出 log 日志

SDK1.8.0
1.SDK 支持打开小程序
2.SDK 分享小程序支持 shareTicket

SDK1.7.9
1.SDK 订阅一次性消息

SDK1.7.8
1.SDK 分享小程序支持大图

SDK1.7.7 1.增加 SDK 分享小程序 2.增加选择发票接口

SDK1.7.6 1.提高稳定性 1)修复 mta 崩溃 2)新增接口支持开发者关闭 mta 数据统计上报

SDK1.7.5 1.提高稳定性 2.加快 registerApp 接口启动速度

SDK1.7.4 1.更新支持 iOS 启用 ATS(App Transport Security) 2.需要在工程中链接 CFNetwork.framework 3.在工程配置中的”Other Linker Flags”中加入”-Objc -all_load”

SDK1.7.3 1.增强稳定性，适配 iOS10 2.修复小于 32K 的 jpg 格式缩略图设置失败的问题

SDK1.7.2 1.修复因 CTTeleponyNetworkInfo 引起的崩溃问题

SDK1.7.1 1.支持兼容 ipv6(提升稳定性)
2.xCode Version 7.3.1 (7D1014) 编译

SDK1.7

支持兼容 ipv6
修复若干问题增强稳定性
SDK1.6.3
1.xCode7.2 构建的 sdk 包 2.请使用 xCode7.2 进行编译 3.需要在 Build Phases 中 Link Security.framework 4.修复若干小问题

SDK1.6.2
1.xCode7.1 构建的 sdk 包 2.请使用 xCode7.1 进行编译

SDK1.6.1 1.修复 armv7s 下,bitcode 可能编译不过 2.解决 warning

SDK1.6
1.iOS 9 系统策略更新，限制了 http 协议的访问，此外应用需要在“Info.plist”中将要使用的 URL Schemes 列为白名单，才可正常检查其他应用是否安装。
受此影响，当你的应用在 iOS 9 中需要使用微信 SDK 的相关能力（分享、收藏、支付、登录等）时，需要在“Info.plist”里增加如下代码：

<key>LSApplicationQueriesSchemes</key>
<array>
<string>weixin</string>
</array>
<key>NSAppTransportSecurity</key>
<dict>
<key>NSAllowsArbitraryLoads</key>
<true/>
</dict> 2.开发者需要在工程中链接上 CoreTelephony.framework 3.解决 bitcode 编译不过问题

SDK1.5 1.废弃 safeSendReq:接口，使用 sendReq:即可 2.新增+(BOOL) sendAuthReq:(SendAuthReq) req viewController : (UIViewController) viewController delegate:(id) delegate;
支持未安装微信情况下 Auth,具体见 WXApi.h 接口描述 3.微信开放平台新增了微信模块用户统计功能，便于开发者统计微信功能模块的用户使用和活跃情况。开发者需要在工程中链接上:SystemConfiguration.framework,libz.dylib,libsqlite3.0.dylib。
