Title:      Instalacja Composer wraz WAMP na systemie Windows
Date:       2013-10-15 19:20:32
Modified:   2013-10-15 17:20:32
Status:     inherit
Category:   
Tags:       
Summary: 


Przy pracy z dużymi projektami PHP, [Composer][1] jest błogosławieństwem. Informacja ta zapewne nie dziwi i jest doskonale znana wszystkim programistom zajmującym się przykładowo takimi framework'ami jak *Symfony* czy *Zend*.

Ale do rzeczy... Przy rozpoczynaniu swojej pracy z *Composer* i WAMP napotkałem wiele trudności (wcześniej korzystałem z XAMPP). Miedzy innymi była w nim kłopotliwa instalacja *Composera* w domyślnej konfiguracji WAMP.

<!--more-->

Podczas instalacji Composer'a wyskoczył błąd:

    openssl extension is missing 
    

Wyczytałem w jednym z artykułów, że WAMP używa 2 zupełnie różnych plików `php.ini` do działania (osobno dla Apache i osobno dla CLI).  
Tak więc aktywacja modułu `php_openssl` w zakładce PHP w WAMP Manager, a następnie restart programu, nie powinien przynieść ze sobą żadnych zmian. Niezbędna jest również aktywacja modułu `php_opensll` dla CLI w domyślnej ścieżce (gdzie X,Y,X to wersja PHP):

    C:\wamp\bin\php\php-X.Y.Z\php.ini   
    

Po tych zabiegach problem instalacji powinien zniknąć :)

Polecam również artykuły  

*   [Setting Up Composer PHP Dependencies Manager in Windows][2] 
*   [Composer-Setup Warning][3]

 [1]: http://getcomposer.org/
 [2]: http://diywebdev.com/setting-up-composer-php-dependencies-manager-in-windows/
 [3]: https://github.com/composer/composer/issues/1440
