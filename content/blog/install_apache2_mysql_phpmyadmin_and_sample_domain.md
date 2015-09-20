Title: Setup LAMP server with sample domain
Date: 2014-04-06
Modified: 2015-06-27
Status: published
Category: How to
Tags: apache, mysql, php, domains

### Table of content

- [Apache 2](#apache-2)

Dobry polski [artykuł](http://www.ubuntu-pomoc.org/instalacja-apache-php5-mysql/) oraz [angieslki][article_about_apache2_url].


Let' begin from updating our system:

```shell
sudo apt-get update
```

### Apache 2.4
Installation Apache with its useful depedencies

```shell
sudo apt-get install apache2 apache2-doc apache2-utils apache2-mpm-worker
```

And restat of the service

```shell
sudo /etc/init.d/apache2 restart
```

or
```shell
sudo service apache2 restart
```

Now we take a peek on our server's version

```console
apache2 -v
```

Start some of your webbrowser to check if "it works" 

```console
firefox http://localhost/
```

Powinno ukazać się "It Works". Jest to plik index.html znajdujący sie w katalogu `/var/www/`, ale o szczegółach później.

#### Dodanie do www-data
Aby sprawdzić czy nasz user jest w tej grupie sprawdzamy:

```shell
groups maciek
```



Dodaj istniejącego już użytkownika do grupy `www-data` group:

```shell
sudo usermod -a -G maciek www-data
```

#### Dodanie nazwy dla serwera
To wszystko aby nie powstawał komunikat o treści podobnej do:

```
 * Restarting web server apache2
AH00558: apache2: Could not reliably determine the server's fully qualified domain name, using 127.0.1.1. Set the 'ServerName' directive globally to suppress this message
 ...done.
```

stad wykonujemy komendę:

```shell
echo "ServerName localhost" | sudo tee /etc/apache2/conf-available/servername.conf
```

i uaktywniamy naszą konfigurację:

```shell
sudo a2enconf servername
```

Jeszcze tylko testowy restart servera:

```shell
sudo service apache2 restart
 * Restarting web server apache2
  ...done.
```

...i pełny zaciesz z naszej strony :)

### MySQL

  Instalacja bazy danych MySQL. Podczas instalacji program zapyta o hasło dla użytkownika root, więc podajemy hasło i **zapamiętujemy**.

```shell
sudo apt-get install mysql-server
```


### PHP

#### Instalacja interpretera PHP

```shell
$ sudo apt-get install php5 php5-cli php5-common php5-gd libapache2-mod-php5 php5-mysql libapache2-mod-auth-mysql apache2-mpm-prefork libapache2-mod-php5 php5-mcrypt
$ sudo a2enmod php5
$ sudo a2enmod rewrite
$ sudo php5enmod mcrypt   # required by phpMyAdmin
```

#### Pliki konfiguracyjne

W poniższym pliku konfiguracynjnym warto rozważyć zmianę pozycji:


```shell
sudo vim /etc/php5/apache2/php.ini
```

na

```ini
upload_max_filesize = 50M
post_max_size = 50M
display_errors = On
display_startup_errors = On
track_errors = On
```


#### Pozostałe pliki konfiguracyjne
- `/etc/apache2/sites-available/default`
- `/home/[user-name]/apache/conf/httpd.conf`



### PhpMyAdmin

```shell
sudo apt-get install phpmyadmin
```

  1. Podczas instalacji program zapyta jaki serwer www wybrać. Wybieramy (spacją) `apache2`.
  2. Następne okienko to konfiguracja pakietu phpmyadmin i integracja z obecną bazą, - wybieramy `TAK`.

> Czasem trzeba przekonfigurować i używamy do tego `sudo dpkg-reconfigure
> phpmyadmin`

### Katalog public_html w apache 2.4
Są 2 różne podejścia do tej sprawy:

  - Pierwszy zakłada że katalog użytkownika to katalog użytkownika i własności plików (permissions) powinny należeć do użytkownika
  - Drugie podejście powinno być odmienne. wszystkie pliki w katalogach powinny być własnością `www-data`. Jest to lepsze o tyle że późniejsza migracja na inne Apache nie powoduje kolizji w właściciela pliku `permissions`

```shell
sudo vim /etc/apache2/mods-enabled/php5.conf
```

i w tym pliku zakomentować `##` wpisy:

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

Teraz ustawimy serwer tak, abyśmy mogli wrzucać pliki do katalogu `public_html` w naszym katalogu domowym. Niezbęde może się okazać nadanie odpowiednich praw dla katalogu wiec i to uwzględnimy.

```shell
mkdir ~/public_html
chmod 775 ~/public_html
```

```
sudo a2enmod userdir
```
Teraz tylko restart Apache:

```shell
sudo /etc/init.d/apache2 restart
```

Od tego momentu możemy spokojnie używać `public_html` w katalogach użytkowników jako katalogu serwerowego.


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
  Ponowna konfiguracja `phpMyAdmin` w razie problemów:
```
sudo dpkg-reconfigure phpmyadmin
```

### Problem #4
**Pliki** powinny mieć prawa **664**, natomiast **katalogi 755**.

> Wyjątkiem są oczywiście pliki wykonywalne.

Przykład zmiany ustawień dla obu katalogów (rekurencyjnie)

```
$ find ~/public_html -type d -exec chmod 755 {} \;
$ find ~/public_html -type f -exec chmod 644 {} \;
```

### Problem #5
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



