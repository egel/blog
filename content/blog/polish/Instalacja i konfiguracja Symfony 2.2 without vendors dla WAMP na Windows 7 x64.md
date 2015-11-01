Title:      Instalacja i konfiguracja Symfony 2.2 without vendors dla WAMP na Windows 7 x64
Date:       2014-05-24 00:06:53
Modified:   2014-05-23 22:06:53
Status:     inherit
Category:   
Tags:       
Summary: 


<div style="float: left;">
  <a href="http://blog.egel.pl/?attachment_id=1147" rel="attachment wp-att-1147"><img src="http://blog.egel.pl/media/wamp-apache-mysql-php-windows-300x300.png" alt="wamp-apache-mysql-php-windows" width="300" height="300" class="alignleft size-medium wp-image-1147" /></a>
</div>

*Windows*, *Apache*, *MySQL*  i *PHP*.

Standardowe i prawdopodobnie jedno z najpopularniejszych wraz z *XAMPP* środowisko dla developerów stron www. Zapewnia większość, jak nie wszystko w jednej wygodnej paczce instalacyjnej, chodź przy konfiguracji może momentami wydać się trudny.  
Udostępniony wraz z instalacją manager pomaga w codziennym odnajdywaniu ważniejszych plików i folderów, włączaniu/wyłączaniu rozszerzeń oraz podobnych temu działań.

<!--more-->

### Niezbędne przed instalacją:

1.  Zainstalowany WAMP ze [strony][1].  
    Moja wersja to: [Wampserver (64 bits & PHP 5.4) 2.2E][2]
2.  Zainstalowany [Composer][3]
3.  *Opcjonalnie*: zainstalowany [Git][4] do późniejszej "pielęgnacji" kodu.

## Proces instalacji i konfiguracji:

1.  Tworzymy w domyślnym folderze (domyślnie **C:\wamp\www**) ścieżkę: `symfony2/test/`

2.  Pobieramy [Symfony 2][5] w wersji "without vendors" i rozpakowujemy do naszego folderu *test*. Wybór wersji `without vendors` daję większą kontrolę nad instalacją poszczególnych dodatków. Jest to zalecane developerom.

3.  Teraz doinstalujemy nasze *vendors* i w konsoli (przechodzimy do naszego katalogu *test*) wklepujemy, w zależności od rodzaju instalacji Composer'a:
    
        composer install
        
    
    lub
    
        php composer.phar install
        

4.  Po pomyślnym zainstalowaniu czas sprawdzić czego nam brak wiec nie zmieniając ścieżki wpisujemy:
    
        php app/check.php
        

5.  W moim przypadku ujawniono kilka braków i ostrzeżeń:
    
    *   **date.datetime**  
        Trzeba zmienić w 2 różnych plikach php.ini (taka specyfika WAMP'a - bedzie się ona powtarzać prawie za każdym razem, gdy będziemy zmieniać coś w **php.ini**)
    
    *   **intl extension**  
        Sytuacja identyczna j.w. W obu plikach php.ini odszukujemy i komentujemy dodając na początku średnik do: `extension=php_intl.dll`
    
    *   **xdebug.max_nesting_level**  
        Tu wyjątek dodajemy lub zmieniamy **tylko** w pliku `php.ini` w katalogu Apache `xdebug.max_nesting_level = 250`
    
    *   **PHP accelerator**  
        Na chwilę pisania owego artykułu, brak rozwiązania problemu (zasłyszana, lecz nie skorygowana prze mnie przyczyna - obecny na tą chwilę brak kompatybilności kompilacji kodu z Visual Studio 2008 dla PHP 5.4. Niektórzy użytkownicy twierdzą ze rozszerzenie działa na PHP 5.2, lecz paradoksalnie przewodnik Symfony 2.2 zaleca już używanie PHP 5.3.8 i wyżej, a kompilacji dla tej wersji nie odnalazłem). Rozszerzenie to nie jest niezbędne do pracy i może zostać na dobrą sprawę pominięte, chodź zalecane przez twórców jest jego posiadanie.

6.  Otwieramy przeglądarkę i w URL wpisując poniższy adres powinna wyświetlić się nasza "domyślna" strona Symfony 2.
    
        http://localhost/symfony2/test/web/app_dev.php 
        

7.  Prawdopodobnie w tym momencie odniosłeś **niebywały** sukces w przedwstępnej walce wraz z Symfony 2.   
    Gratuluje! :)

 [1]: http://www.wampserver.com/en/#download-wrapper
 [2]: http://www.wampserver.com/en/#wampserver-64-bits
 [3]: http://getcomposer.org/download/
 [4]: http://git-scm.com/
 [5]: http://symfony.com/download
