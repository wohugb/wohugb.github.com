# 星际文件系统（InterPlanetary File System，缩写IPFS）

[ipfs](https://github.com/ipfs/ipfs) ![GitHub stars](https://img.shields.io/github/stars/ipfs/ipfs.svg?style=social)

是一个旨在创建持久且分布式存储和共享文件的网络传输协议。[1]它是一种内容可寻址的对等超媒体分发协议。在IPFS网络中的节点将构成一个分布式文件系统。它是一个开放源代码项目，自2014年开始由Protocol Labs在开源社区的帮助下发展。[2]其最初由Juan Benet设计。[3]


## 历史

在2014年，IPFS协议利用比特币区块链协议和网络基础设施的优势来存储不可更改的数据，移除网络上的重复文件，以及获取存储节点的地址信息——用以搜索网络中的文件。[4]

目前的实现采用Go[5]和JavaScript[6]，并有Python的实现正在发展。[7]Go实现被认为是开发正式规范时的“参考实现”[8][9]。

## 描述

IPFS是一个对等的分布式文件系统，它尝试为所有计算设备连接同一个文件系统。在某些方面，IPFS类似于万维网，但它也可以被视作一个独立的BitTorrent群、在同一个Git仓库中交换对象。换种说法，IPFS提供了一个高吞吐量、按内容寻址的块存储模型，及与内容相关超链接。[10]这形成了一个广义的Merkle有向无环图（DAG）。IPFS结合了分布式散列表、鼓励块交换和一个自我认证的命名空间。IPFS没有单点故障，并且节点不需要相互信任。[11]分布式内容传递可以节约带宽，和防止HTTP方案可能遇到的DDoS攻击。

该文件系统可以通过多种方式访问，包括FUSE与HTTP。将本地文件添加到IPFS文件系统可使其面向全世界可用。文件表示基于其哈希，因此有利于缓存。文件的分发采用一个基于BitTorrent的协议。其他查看内容的用户也有助于将内容提供给网络上的其他人。IPFS有一个称为IPNS的名称服务，它是一个基于PKI的全局命名空间，用于构筑信任链，这与其他NS兼容，并可以映射DNS、.onion、.bit等到IPNS。[12]

## Merkle数据格式

每个Merkle都是一个有向无环图 ，因为每个节点都通过其名称访问。每个Merkle分支都是其本地内容的哈希，它们的子节点使用它们的哈希而非完整内容来命名。因此，在创建后将不能编辑节点。这可以防止循环（假设没有哈希碰撞），因为无法将第一个创建的节点链接到最后一个节点从而创建最后一个引用。

对任何Merkle来说，要创建一个新的分支或验证现有分支，通常需要在本地内容的某些组合体（例如列表的子哈希和其他字节）上使用一种哈希算法。IPFS中有多种散列算法可用。

输入到散列算法中的数据的描述见 https://github.com/ipfs/go-ipfs/tree/master/merkledag。

## 参见

- ZeroNet
- 合作存储云
- 分布式文件系统
- 分布式散列表
- 自我认证文件系统
- 珊瑚内容分发网络
- Kademlia
- Akasha项目
- OpenBazaar

## 参考资料

1. Finley, Kurt. The Inventors of the Internet Are Trying to Build a Truly Permanent Web. Wired. June 20, 2016.
1. The IPFS Project. [11 September 2015].
1. IPFS README - Who designed it?. [11 September 2015].
1. https://cointelegraph.com/news/ipfs-protocol-selects-ethereum-over-bitcoin-prefers-ethereum-dev-community
1. ipfs/go-ipfs. GitHub. [2017-02-13] （英语）.
1. ipfs/js-ipfs. GitHub. [2017-02-13] （英语）.
1. ipfs/py-ipfs. GitHub. [2017-02-13] （英语）.
1. IPFS Docs. ipfs.io. [2017-02-13] （英语）.
1. ipfs/specs. GitHub. [2017-02-13] （英语）.
1. http://www.ibtimes.co.uk/juan-benet-ipfs-talks-about-filecoin-1586122, International Business Times, accessed 26 December 2016
1. The IPFS Project - How it works. [11 September 2015].
1. IPFS README. [11 September 2015].

## 外部链接

- IPFS介绍视频（英文）
- IPFS网站（英文）
- HTTP is obsolete. It's time for the distributed, permanent web（英文）
- Protocol Labs（英文）
- OpenBazaar Integrating InterPlanetary File System to Help Keep Stores Open Longer（英文）
- [星际文件存储IPFS是如何颠覆云存储的？](http://blog.csdn.net/owndiandian/article/details/54340508)（简体中文）
- [详解基于IPFS存储模式的区块链医疗保健解决方案](https://www.okcoin.cn/t-2505691.html)（简体中文）