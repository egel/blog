# The Egel's Blog
Made with Pelican static generator.


## Setup
Download main repository

```bash
cd ~/workspace
git clone --recursive git@github.com:egel/blog.git
```

Download plugins
```bash
git clone --recursive https://github.com/getpelican/pelican-plugins ~/.pelican-plugins
ln -s $HOME/.pelican-plugins $HOME/workspace/blog/plugins
```


Before next move we need to fix python [InsecurePlatformWarning issue][issue-InsecurePlatformWarning]

```shell
sudo apt-get install libffi-dev libssl-dev # Debian
sudo pacman -S libffi # Arch
```

[Install `virtualenvwrapper`](http://virtualenvwrapper.readthedocs.io/en/latest/install.html)

```shell
# Debian/Ubuntu
sudo apt-get install virtualenvwrapper

# Arch
sudo pacman -S python-pip python-setuptools python-virtualenv python-virtualenvwrapper
sudo pacman -S python2-pip python2-setuptools python2-virtualenv python-virtualenvwrapper

# OSX
brew install python python3
pip install virtualenvwrapper
```


Set the environment

```shell
mkvirtualenv --python=$(which python3) pelicanblog
workon pelicanblog
(pelicanblog) pip install --upgrade pip
(pelicanblog) pip install setuptools
(pelicanblog) pip install requests[security]
(pelicanblog) pip install -r requirements.txt
(pelicanblog) deactivate
```

Then run server to test (it works in background)

```shell
workon pelicanblog
(pelicanblog) ./develop_server.py start
```

or run tmux session

```shell
./tmux.sh
```

## Publishing
Update content of `publishconf.py` to suite your needs and then:

> This process can be automated, but for now I prefer manual approach.

```shell
make publish  # that will clone output submodule, switch to master and generate output
cd output
git add .
git commit -m "Update"
git push
cd ..
git add output
git commit -m "Upgrade: output submodule to latest version"
```


## Development

*   date
    +   [strftime](http://strftime.org/)


### Configuration for nginx

```nginx
server {
  server_name www.blog.loc;
  return 301 $scheme://blog.loc$request_uri;
}

server {
  server_name blog.loc;

  listen  80;
  listen  [::]:80;

  access_log /var/log/nginx/blog.loc-access.log;
  error_log /var/log/nginx/blog.loc-error.log;

  root /home/maciej/workspace/blog/output/;

  index index.html;
  autoindex off;

  # Setting Compression
  gzip on;
  gzip_disable "msie6";
  gzip_min_length 1100;
  gzip_vary on;
  gzip_proxied any;
  gzip_comp_level 6;
  gzip_buffers 16 8k;
  gzip_http_version 1.1;
  gzip_types text/plain text/css application/json application/x-javascript text/xml application/xml application/xml+rss text/javascript;

  # Define 404 pages URL
  location / {
   try_files $uri $uri/ =404;
  }

  # Disable favicon.ico logging
  location = /favicon.ico {
  	log_not_found off;
  	access_log off;
  }

  # Allow robots and disable logging
  location = /robots.txt {
  	allow all;
  	log_not_found off;
  	access_log off;
  }

  # Disable static content logging and set cache time to max
  location ~* .(js|css|png|jpg|jpeg|gif|ico)$ {
  	expires 1d;
  	log_not_found off;
  }

  # Deny access to htaccess and htpasswd files
  location ~ /.ht {
  	deny  all;
  }

}
```


## License
GPLv3 2015 Maciej Sypień


[issue-InsecurePlatformWarning]: http://stackoverflow.com/questions/29134512/insecureplatformwarning-a-true-sslcontext-object-is-not-available-this-prevent
