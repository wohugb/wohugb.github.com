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

## 实际处理

The `site.process` call is responsible for doing all the work necessary to turn the files in the site's source into a site. In `lib/jekyll/site.rb`:

```ruby
def initialize(config)
  self.config = config.clone

  # Lots of configuration...

  self.reset
  self.setup
end

def process
  self.reset
  self.read
  self.generate
  self.render
  self.cleanup
  self.write
end
```

`reset` and `setup` are called during initialization of the site to reset its internal data structures and to load libraries, plugins, generators and converters, respectively. `process` delegates the work to these 6 methods:

+ reset: initialize the layouts, categories and tags hashes and the posts, pages and static_files arrays.
+ read: get site data from the filesystem and store it in internal data structures. Generators and converters are loaded.
+ generate: call each of the generators' `generate` method.
+ render: call the `render` method for each post and page.
+ cleanup: All pages, posts and static_files are stored in a `Set` and everything else (unused files, empty directories) is deleted.
+ write: call the `write` method of each post, page and static_file, copying them to the destination folder.

This makes it easy to see that a plugin is hooked into Jekyll in the `generate` and `render` stages. As seen in the [[Plugins]] page, you only need to implement the correct methods and all is well.

This page was based on [this blog post](http://onox.com.br/2012/10/02/how-jekyll-works.html).
