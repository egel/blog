Title:      Komendy dla cmd do Symfony 2
Date:       2013-10-15 20:35:03
Modified:   2013-10-15 18:35:03
Status:     inherit
Category:   
Tags:       
Summary: 


Poniżej umieszczam zestawienie komend, które znacznie uprościły moją prace z [Symfony][1] z poziomu `cmd`, a w natłoku różnych innych spraw po prostu zapomina się o nich.  
Oczywiście wszystkie są dostępne  po wpisaniu `php app/console`, lecz niektórych nie ma jawnie wypisanych, a są zlepkiem przemyślanych działań ;)

Liczę, że przydadzą się nie tylko mnie, ale posłużą również Wam. Dodatkowe propozycje mile widziane w komentarzach.

<!--more-->

### Inicjalizacja Bundle

    php app/console generate:bundle --namespace=<nazwa projektu>/<nazwa modułu>Bundle --format=yml
    

przykład:

    php app/console generate:bundle --namespace=Egel/GameBundle --format=yml
    

### Czyszczenie środowiska produkcyjnego

    php app/console cache:clear  --env=prod --no-debug
    

### Zmiana uprawnień dla katalogów cache i log <small>based on linux</small>

    chmod 777 -R app/cache</code> <code>chmod 777 -R app/log
    

### Debugowanie ścieżek (Routes)

    php app/console router:debug
    

### Kopiowanie public bundle do katalogu public web

    php app/console assets:install web
    

### Generowanie getterów i setterów <small>po ustawieniu prawidłowo Doctrine @ORM dla klasy</small>

    php app/console doctrine:generate:entities <nazwa naszego projektu>
    

przykład:

    php app/console doctrine:generate:entities Egel
    

### Generowanie wpisów pól do bazy z przygotowanych klas** <small>oraz wcześniej wygenerowanych getterów i setterów</small>

NIE UŻYWAĆ W PRODUKCYJNYM ŚRODOWISKU

    php app/console doctrine:schema:entities <nazwa naszego projektu>
    

przykład:

    php app/console doctrine:schema:entities Egel
    

### Generowanie nowej bazy danych poprzez doctrine

    php app/console doctrine:database:create

 [1]: http://symfony.com/
