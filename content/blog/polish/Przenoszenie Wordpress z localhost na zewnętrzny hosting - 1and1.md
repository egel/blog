Title:      Przenoszenie Wordpress z localhost na zewnętrzny hosting - 1and1
Date:       2014-08-17 15:30:03
Modified:   2014-08-17 13:30:03
Status:     inherit
Category:   
Tags:       
Summary: 



<div style="float: left;">
  <a href="http://blog.egel.pl/przenoszenie-wordpress-z-localhost-na-zewnetrzny-hosting-1and1/wordpress_logo/" rel="attachment wp-att-1342"><img src="http://blog.egel.pl/media/wordpress_logo-150x150.png" alt="Wordpress Logo" width="150" height="150" class="alignnone size-thumbnail wp-image-1342" /></a>
</div>

Ostatnio szybko potrzebowałem przenieść swój blog Wordpress'a w wersji **3\.9** (to ważne, ponieważ niektóre wcześniejsze wersje mogą się od siebie nieco różnić) z mojego lokalnego hosta na zewnętrzny serwer, w tym wypadku jest to serwer [1and1][1].  
Nie marnując czasu na szukaniu dedykowanych ku temu narzędzi zabrałem się do pracy. Cały proces był wyjątkowo prosty.

<!--more-->

<p style="clear:both">
</p>

Poniżej wyszczególnione kolejne kroki:

1.  Tworzymy kopię zapasową plików oraz bazy danych.

2.  Zbieramy wszystkie potrzebne dane na temat zewnętrznego serwera:
    
    *   nazwa hosta: `nazwa_hosta`
    *   nazwa bazy danych: `nazwa_bazy_danych`
    *   nazwa użytkownika bazy: `nazwa_uzytkownika_bazy_danych`
    *   hasło użytkownika bazy danych: `haslo_uzytkownika_bazy_danych`

3.  Przenosimy wszystkie pliki **Wordpress** z naszego **localhost** do wskazanego na serwerze folderu przez klienta **FTP** (np: [FileZilla][2]) lub poprzez termial. Jak komu wygodniej.
    
    Wygodną opcją jest spakowanie całości folderu do pliku `.zip` i wysłanie na serwer, ponieważ szybciej nastąpi przesyłanie 1 spakowanego pliku na serwer niż całego niespakowanego katalogu wraz z plikami.
    
    Spakowanie folderu można wykonać z pomocą prostej komendy:
    
        zip -r name_of_file.zip your_folder_with_wordpress/
        
    
    Natomiast rozpakować paczkę `.zip` za pomocą komendy:
    
        unzip name_of_file.zip
        

4.  Eksportujemy bazę danych do pliku (najlepiej przez **phpMyAdmin** i funkcje eksport lub **sqldump**) oraz **dopisujemy na samym początku** wygenerowanego pliku:
    
        USE nazwa_naszej_bazy_danych;
        
    
    > To ważne ponieważ przy wykonaniu zapytania serwer MySQL może nie załapać o którą bazę danych nam chodzi i zapytanie się nie powiedzie.

5.  Po imporcie bazy na zewnętrzny serwer wchodzimy w tabele `wp_options` i podmieniamy wartości 2 rekordów (`siteurl` i `home`) na adres do naszej strony. W razie problemów można przeczytać obszerny [tutorial][3].
    
        UPDATE wp_options
        SET option_value = REPLACE(option_value, 'http://localhost/~maciej/wordpress/theegelblog/', 'http://blog.egel.pl/')
        WHERE option_name='siteurl'
        
        UPDATE wp_options
        SET option_value = REPLACE(option_value, 'http://localhost/~maciej/wordpress/theegelblog/', 'http://blog.egel.pl/')
        WHERE option_name='home'
        

6.  Logując się przez klienta FTP (lub terminal i ssh) do naszego katalogu z stroną wordpress edytujemy plik `wp_config.php` znajdujący się w głównym katalogu. Podmieniamy wartości, które tam znajdziemy z informacjami zebranymi od serwera zewnętrznego (patrz punkt 2).

7.  Istnieje również problem z zdjęciami w naszych postach, ponieważ po przeniesieniu trzeba zmienić również adresy URL do obrazków.
    
    Na początek **tylko** wyświetlimy artykuły w których znajdują się zdjęcia z starą ścieżką (dla informacji):
    
        SELECT * FROM wp_posts WHERE (post_content LIKE '%http://localhost/~maciej/wordpress/theegelblog/%');
        
    
    > Jeśli ustaliliśmy, że nasza formuła jest OK, tzn. wyszukuje właściwe posty. Należy się upewnić czy właściwy fragment chcemy zamienić oraz czy wszystkie obrazki posiadają jednakowy początek adresu URL.
    
    Podmienimy wszystkie adresy URL znajdujące się w artykułach na właściwy początek adresu URL:
    
        UPDATE wp_posts SET post_content = REPLACE (  post_content,  'http://localhost/~maciej/wordpress/theegelblog/',  'http://blog.egel.pl/');
        
    
    Taki zabieg pozwolił nam na w miarę komfortowe zaktualizowanie wszystkich adresów URL znajdujących się w postach.

8.  Zapisujemy plik. W tym momencie  wszystko powinno już sprawnie działać.  
    Aby się upewnić sprawdzamy odpalając Wordpress pod nowym adresem.

Jest również wiele innych sposobów przeniesienia Wordpress'a, lecz jak już wspominałem dla mnie ten wydał mi się najbardziej przystępny przy braku informacji oraz czasu o innych lepszych i wydajniejszych sposobach.

Możemy posiłkować się [tą stroną][4] opublikowaną na wordpress.org poświęconej specjalnie temu zagadnieniu.

 [1]: https://www.1and1.pl/
 [2]: https://filezilla-project.org/
 [3]: http://coolestguidesontheplanet.com/find-and-replace-across-whole-wordpress-site/
 [4]: http://codex.wordpress.org/Moving_WordPress
