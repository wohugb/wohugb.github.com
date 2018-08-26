# Arduino


Arduino是一家制作开源计算机硬件和软件的公司，同时兼有项目和用户社区，他负责设计和制造单板微控制器和微控制器包，用于构建数字设备和交互式对象，以便在物理和数字世界中感知和控制对象。该项目的产品是按照GNU宽通用公共许可证（LGPL）或GNU通用公共许可证（GPL）[1] 许可的开源硬件和软件分发的，Arduino允许任何人制造Arduino板和软件分发。 Arduino板可以以预装的形式商业销售，也可以作为自己动手（DIY）包购买。

Arduino电路板设计使用各种微处理器和控制器。这些电路板配有一组数字和模拟输入/输出（I/O）引脚，可以连接各种扩展板或面包板（屏蔽板）和其他电路。这些电路板具有串行通信接口，包括某些型号上的通用串行总线（USB），也用于从个人计算机加载程序。微控制器通常使用C/C++编程语言。除了使用传统的编译工具链之外，Arduino项目还提供了一个基于Processing语言项目的集成开发环境（IDE）。

Arduino项目始于2003年，作为意大利伊夫雷亚地区交互设计研究所Ivrea的学生项目，目的是为新手和专业人员提供一种低成本且简单的方法，以创建使用传感器与环境相互作用的设备执行器。适用于初学者爱好者的此类设备的常见示例包括简单机器人，恒温器和运动检测器。

Arduino这个名字来自意大利伊夫雷亚的一家酒吧，该项目的一些创始人过去常常会去这家酒吧。 酒吧以伊夫雷亚的Arduin命名，他是1002年至1014年期间伊夫雷亚三国和意大利国王的统治者。[2]


## 关于

它使用 Atmel AVR 单片机，采用开放源代码的软硬件平台，构建于开放源代码 simple I/O 接口板，并具有使用类似 Java，C 语言的 Processing/Wiring 开发环境。

## 开发沿革

Arduino的核心开发团队成员包括：马西莫·班齐（Massimo Banzi）、大卫·奎提耶斯（David Cuartielles）、汤姆·伊果（Tom Igor）、赞布罗塔·马提诺（Gianluca Martino）、大卫·梅利斯（David Mellis）和尼可拉斯·兰比提（Nicholas Zambetti）。

据说马西莫·班齐之前是意大利Ivrea一家高科技设计学校的老师。他的学生们经常抱怨找不到便宜好用的微控制器。2005年冬天，马西莫·班齐跟大卫·奎提耶斯讨论了这个问题。大卫·奎提耶斯是一个西班牙籍芯片工程师，当时在这所学校做访问学者。两人决定设计自己的电路板，并引入了马西莫·班齐的学生大卫·梅利斯为电路板设计编程语言。两天以后，大卫·梅利斯就写出了代码。又过了三天，电路板就完工了。这块电路板被命名为Arduino。几乎任何人，即使不懂计算机编程，也能用Arduino做出很酷的东西，比如对感测器作出回应，闪烁灯光，还能控制马达。随后马西莫·班齐、大卫·奎提耶斯和大卫·梅利斯把设计图放到了网上。保持设计的开放源代码理念，因为版权法可以监管开源软件，却很难用在硬件上，他们决定采用共享创意许可。[3]共享创意是为保护开放版权行为而出现的类似GPL的一种许可（license）。在共享创意许可下，任何人都被允许生产印刷电路板的复制品，还能重新设计，甚至销售原设计的复制品。你不需要付版税，甚至不用获取Arduino团队的许可。然而，如果你重新发布了引用设计，你必须说明原始Arduino团队的贡献。如果你调整或改动了电路板，你的最新设计必须使用相同或类似的共享创意许可，以保证新版本的Arduino电路板也会一样的自由和开放。唯一被保留的只有Arduino这个名字。它被注册成了商标。如果有人想用这个名字卖电路板，那他们可能必须付一点商标费用给Arduino的核心开发团队成员。

赞布罗塔·马提诺创立的Arduino Srl被2009年创立的Arduino LLC控告侵犯了他们的著作权，这第二家被控侵权的Arduino（也就是Arduino Srl），原先叫做Smart Projects Srl，以前是在意大利负责生产制造Arduino控制板的公司。而第一家Arduino（也就是我们较熟悉的Arduino LLC）则负责开发控制板，并管理周边的开放源代码专题与社区。在之前，原本双方是合作的关系；2014年马提诺与另外四位共同创办人，对于Arduino品牌的发展方向意见不合，导致马提诺另外请费德里科·穆斯托担任Smart Projects的新首席执行官，并把公司名称改为Arduino Srl。[4]

## 特色

基于知识共享开放源代码的电路图设计。
免费下载，也可依需求自己修改，但需遵照姓名标示。您必须按照作者或授权人所指定的方式，表彰其姓名。
依相同方式分享，若您改变或转变著作，当散布该派生著作时，您需采用与本著作相同或类似的授权条款。
Arduino可使用ICSP线上烧入器，将Bootloader烧入新的IC芯片。[5]
可依据Arduino官方网站，获取硬件的设计档，加以调整电路板及组件，以匹配自己实际设计的需求。[6]
可简单地与感测器，各式各样的电子组件连接，如红外线、超音波、热敏电阻、光敏电阻、伺服马达…等。
支持多样的交互程序，如Adobe Flash, Max/MSP, VVVV, Pure Data, C, Processing…等。
使用低价格的微处理控制器（Atmel AVR）（ATMEGA 8,168,328等）。
USB接口，不需外接电源。另外有提供直流（DC）电源输入。

## 硬件

### 官方硬件

更多信息：en:List of Arduino boards and compatible systems
原始的Arduino硬件是从一间意大利公司Smart Projects制造。[7]有些Arduino硬件则是被官方授权由美国公司SparkFun Electronics和Adafruit Industries设计。[8]

Arduino硬件示例

Arduino Diecimila in Stoicheia



Arduino Duemilanove (rev 2009b)



Arduino UNO



Arduino Leonardo



Arduino Mega



Arduino MEGA 2560 R3（正面）[a]


Arduino MEGA 2560 R3（背面）[a]



Arduino Nano



Arduino Due
（ARM Cortex-M3核心）



LilyPad Arduino (rev 2007)



Arduino Yun

### Shields

"Shields"扩展版能够被插入Arduino和Arduino兼容硬件。用途是增加Arduino硬件上没有的功能，如马达控制, GPS, 有线网络，液晶显示器，或者是面包板。用户也可以自己动手做Shields扩展版。[10][11][12]

Arduino shields扩展版示例

多重的Shield可以被堆栈起来。在这张图里，最上层的Shield扩展版上含有面包板。



翅膀形状的螺丝端子Shield扩展版。



Adafruit马达Shield扩展版和用于连接马达的螺丝端子Shield扩展版。



HackARobot结构Shield，专为了Arduino Nano硬件设计以推动马达和感测器如：陀螺仪和GPS，以及其他的扩展版如：Wifi、蓝牙、无线射频等。

## 软件

Arduino Software IDE

编写于Arduino IDE上简单的入门程序“Blink”的显示屏截图
编写于Arduino IDE上简单的入门程序“Blink”的显示屏截图
开发者	Arduino Software
稳定版本
1.8.5 （2017年9月29日，​10个月前[13] ）
编程语言	Java, C and C++
操作系统	Windows, macOS, Linux
类型	集成开发环境
许可协议	LGPL或GPL授权
网站	arduino.cc
源代码库	github.com/arduino/Arduino
在Arduino上运行的程序可以使用任何能够被编译成Arduino机器码的编程语言编写。
而Atmel也提供了数个可以开发Atmel微处理机程序的集成开发环境，AVR Studio[14]和更新的Atmel Studio[15][16]
目前微软在其Visual Studio 也有提共Arduino 的SDK 可以使用 在编译运行更方便


### IDE

而Arduino计划也提供了Arduino Software IDE，一套以Java编写的跨平台应用软件。Arduino Software IDE源自于Processing编程语言以及Wiring计划的集成开发环境。它是被设计于介绍程序编写给艺术家和不熟悉程序设计的人们，且包含了一个拥有语法突显、括号匹配、自动缩进和一键编译并将可执行文件烧写入Arduino硬件中的编辑器。

Arduino Software IDE使用与C语言和C++相仿的编程语言，并且提供了包含常见的输入/输出函数的Wiring软件库。在使用GNU toolchain编译和链接后，Arduino Software IDE提供了一个程序“avrdude”用来转换可执行档成为能够烧写入Arduino硬件的固件。

### Sketch

使用Arduino Software IDE编写的程序被称为“sketch”。[17]一个典型的Arduino C/C++ sketch程序会包含两个函数，它们会在编译后合成为main()函数：

setup()：在程序运行开始时会运行一次，用于初始化设置。
loop()：直到Arduino硬件关闭前会重复运行函数放的代码。

## Arduino语言

```c
int LED_PIN=13;

void setup () {                    // 初始化副程式，程式起始時僅執行一次
    pinMode (LED_PIN, OUTPUT);     // 以數位輸出方式啟用Pin13
}

void loop () {                     // loop副程式，重複不斷執
    digitalWrite (LED_PIN, HIGH);  // 打開LED（發光二極管）
    delay (1000);                  // 等待一秒，delay內含數值1000，代表延遲1000毫秒，即一秒。
    digitalWrite (LED_PIN, LOW);   // 關閉LED
    delay (1000);                  // 等待一秒
}                                  // loop副程式結束
```

这是Arduino的Blink示例程序。

Arduino 程序可由五个部分组成 :

//1. 导入库与定义 (可有可无)

```c
#include <SoftEasyTranfer.h>

#define LEDPIN 13;

//2. 宣告常量与全域变量 (可有可无)

const float PI=3.14159;

int r;

//3. 设置函数 (必要)

void setup() {}

//4. 无限循环  (必要)

void loop() {}

//5. 自定义函数 (可有可无)

float area(float r) {

  float a=PI*r*r;

  return a;

  }
```

其中 setup() 与 loop() 是一定要有的函数 (均无参数无传回值), 其他则视需要而定. Arduino 语言采用 C/C++ 语法,

加上以 Wiring 为基础的电子设计核心库组合而成, 包括 Digital I/O, Analog I/O 等库. 内置的库可直接调用,

但若有使用第三方库(例如驱动感测器模块所需的库), 则必须使用 include 前置指令引入. 此外, 也可以用前置指令 define 定义一个常量或宏 (表达式).

前置指令乃 C 编译器指令, 不属于 C 语言本身, 其用途有三 :

引入头文件 : 例如 #include <myLibrary.h> 或 "myLibrary.h"
  定义常量 : 例如 #define PI 3.14159
  定义宏 : 例如 #define AREA(r) PI*r*r
所以前置指令的功能一言以蔽之就是替换, include 就是在标头处以指定之文件内容替换; 而 define 就是在程序中用到所定义之常量与宏名称时, 以其内容替换.

宏的功能事实上与函数类似, 不同之处是函数调用使用堆栈, 而宏则是直接放在源代码中, 运行效率较快 (但若很多地方都要用到时, 编译后就会比较大).

头文件可用角括号 < > 或双引号 "", 差别是用双引号时, 前置处理器会先从源文件所在位置开始去搜索头文件; 而用角括号则会先从 libraries 目录开始找.

## 相关设备名称

自由软件主题

icon	电子学主题
BASIC Stamp
OOPic
PICAXE
Parallax Propeller
ARM express
Fritzing
Gumstix
ioBridge
Make Controller Kit
Minibloq
树莓派 - 单板机计算机
Simplecortex