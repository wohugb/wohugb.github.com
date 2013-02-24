---
layout: post
category : 手册
title:  Jekyll是如何工作的
tagline: 翻译中
tags : [Jekyll,手册]
---

##  可执行的Jekyll

The command-line parameters, the defaults and the `_config.yml` (through `Jekyll::configuration` method) are used to create an `options` hash and then a new site is instantiated:
        
```ruby

