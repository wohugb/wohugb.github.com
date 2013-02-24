## The Jekyll executable  

The command-line parameters, the defaults and the `_config.yml` (through `Jekyll::configuration` method) are used to create an `options` hash and then a new site is instantiated:
        
```ruby

# Create the Site

site = Jekyll::Site.new(options)


