Title:      How to improve nginx setup on Mac OSX
Date:       2016-02-16
Status:     published
Category:   How to
Tags:       osx, nginx
Authors:    Maciej Sypień

<!--
<div class="intro-article-image-sm" markdown="1">
  ![Logo of Sublime Text 3]({filename}/images/nginx_logo.png)
</div>
-->

If you store all your configurations for nginx servers on your Mac into single
file... you probably can do it better.

Take a look how to improve your server instances by separating it into folders,
just like Apache handle with it by `sites-enables` and `sites-available`.

Default nginx installation did not provide this but in few quick steps we can
achieve this.

Some example code snippets comes from [this gist][1].

### Create desired directories

```bash
mkdir -p /usr/local/etc/nginx/sites-{enabled,available}
cd /usr/local/etc/nginx/sites-enabled
ln -s ../sites-available/default.conf
ln -s ../sites-available/default-ssl.conf
```

Now some info about important file locations:

 - *nginx.conf* to `/usr/local/etc/nginx/`
 - *default.conf* and *default-ssl.conf* to `/usr/local/etc/nginx/sites-available`
 - homebrew.mxcl.nginx.plist to `/Library/LaunchDaemons/`

For log files you can use `/usr/local/var/log/nginx` directory. For example if you have frontend configuration for your static blog configuration `blog.loc.conf`.

### Improve nginx.conf file
If you use Linux most the time you will feel more familiar with below configuration, just because it try to be very same as Linux's version of nginx implement that.

Probably the most important part of this snippet is last two `include` methods.

Those are enables `sites-enabled/` directory to observe every file into it. So
now you can put separate configurations for your server configurations.

> Note: You may have to create log directory if doesn't exist yet. To do so
type: `sudo mkdir -p /Library/Logs/nginx`

```nginx
user www-data staff;
worker_processes 1;

error_log /Library/Logs/nginx/error.log;

events {
  worker_connections  1024;
}

http {
  include mime.types;
  default_type application/octet-stream;
  log_format main   '$remote_addr - $remote_user [$time_local] "$request" '
                    '$status $body_bytes_sent "$http_referer" '
                    '"$http_user_agent" "$http_x_forwarded_for"';
  access_log /Library/Logs/nginx/access.log  main;
  sendfile on;
  keepalive_timeout 65;
  index index.html index.php;

  upstream www-upstream-pool{
      server unix:/tmp/php-fpm.sock;
  }

  include /etc/nginx/conf.d/*.conf;
  include /usr/local/etc/nginx/sites-enabled/*.conf;
}
```

 [1]: https://gist.github.com/jimothyGator/5436538
