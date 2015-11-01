Title:      Setup LAMP server with sample domain
Date:       2014-04-06
Modified:   2015-06-27
Status:     published
Category:   How to
Tags:       apache, mysql, php, domains
Summary:    We will install standard and secure Linux - Apache - MySQL - PHP
            configuration with PHPMyAdmin for easy database management and Apache's
            VirtualHost. Shall we begin? :)


Every young IT person will at last faced with the challenge of creating his own
website.  It could be a simple static site, managed by some static site
generator (like [Jekkly](http://jekyllrb.com/),
[Octopress](http://octopress.org/), [Pelican](http://docs.getpelican.com) or
[some others examples](https://www.staticgen.com/)). But few proud, claim that
it's to easy and they would like to try something more complex like basic PHP
CMS similar to [Joomla](https://www.joomla.com/),
[Wordpress](https://wordpress.org) or even use a professional, enterprise class
frameworks like Laravel, Symfony or Zend.

Whatever they choose, they will need some tools to deal with showing to the
whole world their new website project.

In this simple article I'll show you how to build your own simple (and standard
in these days) server configuration based on (Ubuntu 14.04 LTS) LAMP, but those
tools can be easily replaced with others technologies. For example if you're
interested in Django you could replace PHP language with more mature Python (of
course some setting will vary a bit from content presented in this article, but
in the end setup will be made).

I think this is good, start example to play with :) Enjoy.


### Table of content
- [Apache 2](#apache-2)
  * [Add user to www-data group](#add-user-to-www-data-group)
- [MySQL](#mysql)
- [PHP](#php)
- [PHPMyAdmin](#phpmyadmin)
- [Common problems](#common-problems)


Dobry polski [artykuł](http://www.ubuntu-pomoc.org/instalacja-apache-php5-mysql/) oraz [angieslki][article_about_apache2_url].


Let's begin from updating our Debian based system (Ubuntu):

```shell
sudo apt-get update
```

### Apache
Installation Apache 2.4 with its useful dependencies:

```shell
sudo apt-get install apache2 apache2-doc apache2-utils apache2-mpm-worker
```

and restart the service with

```shell
sudo service apache2 restart
```
Or also you can use good, oldshool [daemon][wikipedia-daemon] `sudo /etc/init.d/apache2 restart`.

Now we take a peek on our server's version by writing `apache2 -v` in your
console.

Now, if all went well, you could start your web browser with `http://localhost/`
to check if "It works!" appears to you :)

> "It works!" page is actually simple `index.html` file stored in
> `/var/www/html/` directory, but details comes later :)


#### Add user to www-data group
Now we'd like to add your current user (`$USER`)  to `www-data` group used by
apache server. We will do this to prevent you from some error-access failures
like user owner.

To check if your current user belongs to `www-data` group simply do:

```shell
groups $USER
```

Now add existing user to `www-data` group.

```shell
sudo usermod -a -G $USER www-data
```

#### Add a name to the server
Basic apache configuration does not impose add the server name, but I really
don't like to see some text like this below, when I reloading the server.

```
 * Restarting web server apache2
AH00558: apache2: Could not reliably determine the server's fully qualified domain name, using 127.0.1.1. Set the 'ServerName' directive globally to suppress this message
 ...done.
```

That's why we will name it :)

```shell
echo "MyOwnServerName localhost" | sudo tee /etc/apache2/conf-available/servername.conf
```

then we're enable its name in for apache config by

```shell
sudo a2enconf servername
```
Just restart the server to make sure that all is done correctly.

```shell
sudo service apache2 restart
 * Restarting web server apache2
  ...done.
```

...and now full smile should appear on your face :)


### MySQL
MySQL is one of the most popular databases on the website market. So we will
install it along.

During the installation process program ask you for the root password, so we
write it and **remeber it** for later use.

```shell
sudo apt-get install mysql-server
```
That's it for the database server :)


### PHP
Instalation of the PHP interperter isn't hard. One important thing is to install
all modules related to our new setup, enable it, and configure to suite your
needs. I'll show you most commony used setup to save your precious time
searching it through Internet.

####  Installation of PHP interpreter
Below we will install all useful modules, and enable them Apache server and PHP.

```shell
$ sudo apt-get install php5 php5-cli php5-common php5-gd libapache2-mod-php5 php5-mysql libapache2-mod-auth-mysql apache2-mpm-prefork libapache2-mod-php5 php5-mcrypt
$ sudo a2enmod php5
$ sudo a2enmod rewrite
$ sudo php5enmod mcrypt   # required by phpMyAdmin
```

#### Configuration files
Into below Apache's PHP configuration file stored at
`/etc/php5/apache2/php.ini`, it worth to change default parameters according to
those presented below. There are most commonly changed variables for PHP.

```ini
upload_max_filesize = 50M
post_max_size = 50M
display_errors = On
display_startup_errors = On
track_errors = On
```


#### Other useful configuration files

- `/etc/apache2/sites-available/default`
<!--- `/home/$USER/apache/conf/httpd.conf`-->



### PHPMyAdmin

Installation of PHPMyAdmin is trivial.

```shell
sudo apt-get install phpmyadmin
```
During installion, wizard ask you for:

1.  Which WWW Server would you like to choose. We mark (with space key)
    `apache2`.
2.  Next window is the configuration of phpmyadmin package and integration with
    current database. We mark `Yes`.

> Sometimes we made mistake during this installion process, so command to reopen
> this configuration wizard is `sudo dpkg-reconfigure phpmyadmin`.

### Creating public_html directory for the user
Some people not agree with it (mainly by security issues it can cause) but
apache also support the old user catalog usually stored at `~/public_html`,
and it can be working like `/var/www/html`.

There are 2 different approaches for creating this directory.

1.  First one assumes that User's catalog (~/public_html) should be owned by
    [hir][wikipedia-hir] and hir alone, also with files permissions.
2.  The second one, presuppose that all files should be owned by `www-data`
    user. This solution is a bit better because other files migration not cause
    the access collisions.

> Personally, I prefer the second approach.

To enable this magical directory we need to edit
`/etc/apache2/mods-enabled/php5.conf` (it may require `sudo` privileges to save
it).

Into this file we need to comment some lines (`##`) like in below snippet.


```apache
<FilesMatch ".+\.ph(p[345]?|t|tml)$">
    SetHandler application/x-httpd-php
</FilesMatch>
<FilesMatch ".+\.phps$">
    SetHandler application/x-httpd-php-source
    # Deny access to raw php sources by default
    # To re-enable it's recommended to enable access to the files
    # only in specific virtual host or directory
    Order Deny,Allow
    Deny from all
</FilesMatch>
# Deny access to files without filename (e.g. '.php')
<FilesMatch "^\.ph(p[345]?|t|tml|ps)$">
    Order Deny,Allow
    Deny from all
</FilesMatch>

# Running PHP scripts in user directories is disabled by default
#
# To re-enable PHP in user directories comment the following lines
# (from <IfModule ...> to </IfModule>.) Do NOT set it to On as it
# prevents .htaccess files from disabling it.
##<IfModule mod_userdir.c>
##    <Directory /home/*/public_html>
##        php_admin_flag engine Off
##    </Directory>
##</IfModule>
```
Now we set server, so that we can throw files into the `~/public_html`
directory. It maybe necessary to give the appropriate rights for the directory
so we need to take this under consideration as well.

```shell
mkdir ~/public_html
chmod 775 ~/public_html
sudo a2enmod userdir
```
Now restart the apache and since this moment we can easly use `~/public_html` in
all user's catalogs like the server's one.

```shell
sudo /etc/init.d/apache2 restart
```


##### Ustawienie httpd.conf

Lokalizujemy nasz plik `httpd.conf`.

**Dla różnych systemów różnie sie nazywa**, dla przykładu dla Ubuntu 14.04 64-bit to 'apache2.conf'

Pobieramy ścieżkę uruchomionego apacha2

```shell
$ ps -ef | grep apache
apache   12846 14590  0 Oct20 ?        00:00:00 /usr/sbin/apache2
```

Teraz dodajemy flagę -V

```shell
$ /usr/sbin/apache2 -V | grep SERVER_CONFIG_FILE
-D SERVER_CONFIG_FILE="/etc/apache2/apache2.conf"
```

Teraz otwieramy plik i możemy dodać naszą ścieżkę `public_html` do pliku:

```apache
<Directory /home/maciej/public_html/>
    Options Indexes FollowSymLinks
    AllowOverride All
    Require all granted
</Directory>
```

restart i jesteśmy w domu

##### Może pojawic sie problem z "index.php not found"

    Not Found

    The requested URL /index.php was not found on this server.

Prawdopodobnym podwodem jest przepisywanie url w np: Joomla (`Konfiguracja globalna` > `Zastosuj przepisywanie URL` na **OFF**)

### Problem #1

  Once you install the module, the module will be available in the `/etc/apache2/mods-available` directory. You can use the `a2enmod` command to enable a module. You can use the `a2dismod` command to disable a module. Once you enable the module, the module will be available in the the `/etc/apache2/mods-enabled` directory.

  Example: `sudo a2enmod rewrite`

### Problem #2
  [Apache2 on ubuntu - PHP downloading files insteed of run](http://stackoverflow.com/questions/6245895/apache2-on-ubuntu-php-files-downloading)


### Problem #3
**Pliki** powinny mieć prawa **664**, natomiast **katalogi 755**.

> Wyjątkiem są oczywiście pliki wykonywalne.

Przykład zmiany ustawień dla obu katalogów (rekurencyjnie)

```
$ find ~/public_html -type d -exec chmod 755 {} \;
$ find ~/public_html -type f -exec chmod 644 {} \;
```

### Problem #4
Aktualizacja wszystkich folderów i plików na `www-data` w katalogu `public_html`

```
#!/bin/bash

sudo adduser $USER www-data
sudo chown -R www-data:www-data /home/$USER/public_html
sudo chmod -R 775 /home/$USER/public_html
```

Save it inside /home/$USER/bin and make it executable using:

```
sudo chmod +x /home/$USER/bin/public_html_fix.sh
```


 [jdownloader_shell_installer]: http://installer.jdownloader.org/jd_unix_0_9.sh

 [xmind_homepage]: http://www.xmind.net/

 [poedit_download_page]: https://launchpad.net/~schaumkeks/+archive/ppa/+sourcepub/2991913/+listing-archive-extra

 [sublime_home_page]: http://www.sublimetext.com/
 [sublime_blog_page_url]: http://dbader.org/blog/setting-up-sublime-text-for-python-development
 [sublime_package_control_installation_page]: https://sublime.wbond.net/installation
 [sublime_github_livereload_page]: https://github.com/dz0ny/LiveReload-sublimetext2
 [sublime_soda_theme_page]: http://buymeasoda.github.io/soda-theme/
 [sublime_tomorrow_theme]: https://github.com/theymaybecoders/sublime-tomorrow-theme

 [article_about_apache2_url]: https://library.linode.com/web-servers/apache/installation/ubuntu-12.04-precise-pangolin
 [textmaker_download_page_url]: http://www.xm1math.net/texmaker/download.html#linux
 [google_chrome_download_page_url]: http://www.google.pl/intl/pl/chrome/
 [dashboard_icon_link]: http://askubuntu.com/questions/68612/how-to-change-the-dash-icon-in-the-unity-launcher

 [wikipedia-daemon]: https://en.wikipedia.org/wiki/Daemon_%28computing%29
 [wikipedia-hir]: https://en.wikipedia.org/wiki/Hir_%28disambiguation%29



