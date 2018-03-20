# 如何从Angular4迁移到5

“Pentagonal-donut”a.k.a Angular5发布。
现在是所有`ngx-*`项目开始支持`angular5`并活在`edge`的时候了。

这个发行版在引擎盖下为我们带来了许多改进，新功能和（像往常一样）一些重大改变。

最酷的功能之一是构建优化器，默认情况下，它将应用于生产构建中。
它删除了运行时显然不需要的装饰器（保存一些字节），然后在代码中标记纯函数（这将被现有工具使用，例如树状摇动的汇总），从而在捆绑包中节省了更少的宝贵字节,。

这里列出了angular5更新日志的完整列表（包括改进，新功能和重大更改），并在此处进行了详细说明。

从Angular2开始，开发版本正在分发大量文件，当我们需要将这些文件投入生产时需要额外注意。

![ng serve output](https://cdn-images-1.medium.com/max/1600/1*eosr4_YG5n_ZTSkl58h2qw.png)

类似地，在Angular5中，构建角色cli所生成的基本应用需要5.7s的时间，并且需要7.3MB的bundle大小。

![ng serve — aot](https://cdn-images-1.medium.com/max/1600/1*q0H-sBM856EKFtwmRgSNdg.png)

另一方面，没有缩小和提供prod标记的aot构建需要约4.9s和4.1MB的bundle大小（注意：AOT编译比正常构建要快得多）

![ng serve — aot — prod](https://cdn-images-1.medium.com/max/1600/1*DbfZL2c50kPrwOs3dKnIdg.png)

使用 -  prod标志，大约需要16s才能构建，捆绑大小约为108KB

构建时间显着减少，但是需要处理的是包的大小。

```
# Basic app generated in Angular CLI version 1.5.0
╔══════════════════╦═════════════════╦═══════════════════╗
║      Mode        ║ Bundle size(MB) ║ Time to bundle(s) ║
╠══════════════════╬═════════════════╬═══════════════════╣
║ dev build        ║     7.3         ║       5.7         ║
║ with aot         ║     4.1         ║       4.9         ║
║ with aot + prod  ║     0.0108      ║      16.7         ║
╚══════════════════╩═════════════════╩═══════════════════╝
```

如果您厌倦了使用角度cli生成的应用程序的常规基准测试，并且对更多真实世界的示例感兴趣，那么我们就去。

在这个例子中，我们将拿一个示例JHipster应用程序，分享我们所做的迁移到angular 5的故事，并将看到我们面临的问题。

如果您还没有听说过JHipster，那么您一定要在这里查看。
它是一个开源项目，用于生成Web应用程序，并将所有最新和最伟大的技术捆绑在一起。
它在后端生成一个基于Java的Web应用程序，然后在后端使用Angular（1＆X）/ React。
如果您正在进行全面的堆栈开发，并且有兴趣了解如何更快更好地完成任务，那么您应该查看这里。

您可以在下面找到angular4和angular5之间的捆绑差异，

```
╔══════════════════╦═════════════════╦═══════════════════╗
║      Mode        ║ Bundle size(MB) ║ Time to bundle(s) ║
╠══════════════════╬═════════════════╬═══════════════════╣
║                        Angular 4                       ║
╠══════════════════╬═════════════════╬═══════════════════╣
║ dev build        ║     11.7        ║      33.31        ║
║ with aot + prod  ║     0.393       ║      47.47        ║
╠══════════════════╬═════════════════╬═══════════════════╣
║                        Angular 5                       ║
╠══════════════════╬═════════════════╬═══════════════════╣
║ dev build        ║     13.8        ║      21.95        ║
║ with aot + prod  ║     0.414       ║      29.52        ║
╚══════════════════╩═════════════════╩═══════════════════╝
```

仅供应商文件在开发版本中从9.9 MB增加到12 MB（注意：它还包括所有供应商库，不仅包括角度核心库）。
另一方面，生产版本增加了16KB。
但构建时间显着缩短。
所以，我们可以使用aot构建，即使在开发时也可以使用source map来进行调试。

与之前的角度迁移相比，迁移并不困难（您是否曾使用ng-upgrade并以混合模式运行），但它仍然存在瓶颈，不眠之夜和更多剂量的咖啡因。

首先，在迁移之前，你应该使用这个神奇的网站。
这整齐地列出了当我们从角度4移动到5（从任何版本到角度的任何版本）时我们需要考虑的事情。

更换 `<template>` 标签至 `<ng-template>`

用`injectToken`替换`opaqueToken`（因为这个，大多数库发布了一个新版本）

将`ngOutletContext`替换为`ngTemplateOutletContext`

用`trackByFunction`替换`trackByFn`

如果您使用2.4.2以外的打字稿版本，请升级或降级至2.4.2版本。
使用任何其他版本将导致此错误

```js
Uncaught Error: Unexpected value ‘[object Object]’ imported by the module ‘AppModule’.Please add a @NgModule annotation
```

这也适用于您导入的任何库。
那就是说，如果你的任何库都使用打字机的高级版本，他们应该降级到这个特定版本，否则你必须等到这种情况发生。

还有一个新的HttpClient模块可用，这是添加到角度通用包。

```js
import { HttpClientModule, HttpClient } from '@angular/common/http';
```

但是，如果您之前使用过`@ angular / http`，那么它不是替代Http服务的替代品

这就是说，如果您使用拦截器并入侵了http请求和响应，那么您必须确保在迁移到新版本之前必须完全删除它们。
但是很高兴我们可以使用现有的代码，我们仍然有`angular6`来完成这个。

在我们的例子中，使用自定义http拦截器。
由于以前的角色版本需要自定义http拦截器，然后使用`requestInterceptor`和`responseInterceptor`来破解请求和响应。
一旦我们开始使用httpClientModule，我们就可以摆脱这种样板。

应该明确指定您导入到模块中的服务的依赖关系。
这是最难解决的问题，并花费了大量的时间在这个特定的东西上。
在≤Angular 4中，我们只需要指定库正在导出的服务，如下所示，

```js
export class NgJhipsterModule {
    static forRoot(moduleConfig: JhiModuleConfig): ModuleWithProviders {
        return {
            ngModule: NgJhipsterModule,
            providers: [
                    ...JHI_SERVICES,
                    JhiLanguageService,
                    JhiAlertService,
                    JhiConfigService,
                    { provide: JhiModuleConfig,
                      useValue: moduleConfig }
            ]
       };
}
```

但是从Angular5中，我们需要明确地说出下面的依赖关系，

```js
export class NgJhipsterModule {
    static forRoot(moduleConfig: JhiModuleConfig):                ModuleWithProviders {
      return {
          ngModule: NgJhipsterModule,
          providers: [
                ...JHI_SERVICES,
                { provide: JhiLanguageService,
                  useClass: JhiLanguageService,
                  deps: [TranslateService, JhiConfigService] },
                { provide: JhiAlertService,
                  useClass: JhiAlertService,
                  deps: [Sanitizer, JhiConfigService,                                  TranslateService] },
                { provide: JhiModuleConfig,
                  useValue: moduleConfig },
                { provide: JhiConfigService,
                  useClass: JhiConfigService,
                  deps: [JhiModuleConfig] }
           ]
        };
}
```

否则，它会抛出一个错误无法解析您的服务的所有参数（？）

最后，我个人认为，人们对角度的兴趣水平正在下降，对于我们来说，转向未来的角度版本总是一个颠簸的过程。
希望这将在未来的版本中得到解决。
最重要的是，展望未来，捆绑包的大小如何减少。

你可以在这里查看代码的更多信息，

更新：5.1版本在上周发布，它包含修饰器包含不支持或不正确的表达式时改进的错误消息。

它还增加了“打字稿2.5.x”的支持。

Typescript 2.5，增加了可选的catch支持，为你的Javascript文件（如果有的话）和更重要的`preserveSymlinks`类型断言（防止在使用链接的npm模块时引发的错误）（请点击这里）

5.1更新还通过`angular-cli`增加了对服务工作者支持的改进。
将服务人员添加到您的网站。
增加了App-shell支持（使其更容易生成PWA）。

我们在JHipster有一个公关已经支持角5.1.0❤️