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
# 创建Site  
site = Jekyll::Site.new(options)
```

After that, it starts to watch the necessary directories if the `--auto` option was used.

```ruby
if options['auto']
  require 'directory_watcher'
  puts "Auto-regenerating enabled: #{source} -> #{destination}"
  # ...
else
  puts "Building site: #{source} -> #{destination}"
  # ...
end
```

The site is built through a call to `site.process`, the main method in the `Jekyll::Site` class. Finally, it runs the local server if `--server` was specified.


