Title:      Aktualizacja gcc oraz g++ na Ubuntu
Date:       2014-07-24 02:14:45
Modified:   2014-07-24 00:14:45
Status:     Draft
Category:   
Tags:       
Summary: 


<div style="float: left;">
  <a href="http://blog.egel.pl/aktualizacja-kompilatora-gcc-oraz-g-na-ubuntu/ubuntu-logo/" rel="attachment wp-att-1309"><img src="http://blog.egel.pl/media/ubuntu-logo-150x150.png" alt="Logo Linux Ubuntu" width="150" height="150" class="aligncenter size-thumbnail wp-image-1309" /></a>
</div>

Ostatnio potrzebowałem zaktualizować mój kompilator w Ubuntu 12.04. Zmusił mnie do tego projekt na zajęcia. Miałem do napisania klasę macierzy i chciałem posłużyć się w niej biblioteką `regex`. Niestety, domyślny kompilator gcc/g++ zainstalowany w Ubuntu 12.04 był w wersji 4.6 i nie obsługuje nowego standardu [`c++0x`][1].

Wersja gcc/g++ na dzień dzisiejszy to [4\.8.2][2]

Tak więc, aby zapewnić sobie maksimum bezpieczeństwa posłużę się programem `update-alternatives` pomagającym w zarządzaniu wersjami (w tym domyślną) programów, tak aby nie stracić możliwości przełączenia się miedzy wersją 4.6, a 4.8 ;)

Do dzieła! :)

<!--more-->

### Upewniamy się czy mamy przydatne pakiety

    sudo apt-get install build-essential
    

### Sprawdzimy wersję kompilatorów

    gcc --version
    g++ --version
    

W moim wypadku zaowocowało to wynikiem:

    gcc (Ubuntu/Linaro 4.6.4-1ubuntu1~12.04) 4.6.4
    g++ (Ubuntu/Linaro 4.6.4-1ubuntu1~12.04) 4.6.4
    

### Dodanie repozytorium

Skorzystamy z wygodnego repo do aktualizacji naszych kompilatorów oraz zaktualizujemy nasza listę pakietów.

    sudo add-apt-repository ppa:ubuntu-toolchain-r/test
    sudo apt-get update
    

### Instalacja

Instalujemy dodatkowe 2 kompilatory.

    sudo apt-get install gcc-4.8 g++-4.8
    

W tym momencie posiadamy 4 kompilatory.

> Po co nam aż tyle? - zapytacie

2 kompilatory pozostały z domyślnej instalacji, natomiast 2 kolejne to nasz nowy doinstalowany nabytek. Wszystkie 4 kompilatory przydadza nam się do sprawnego przełączania miedzy różnymi wersjami kompilatorów.

### Dodanie nowych wersji kompilatorów

    sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.6 60 --slave /usr/bin/g++ g++ /usr/bin/g++-4.6
    sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.8 40 --slave /usr/bin/g++ g++ /usr/bin/g++-4.8
    

Po dodaniu powyższych linijek definiujących nam wersję kompilatorów, możemy bardzo wygodnie przełączyć się miedzy wersjami prostym poleceniem:

    sudo update-alternatives --config gcc

 [1]: http://www.stroustrup.com/C++11FAQ.html
 [2]: http://gcc.gnu.org/
