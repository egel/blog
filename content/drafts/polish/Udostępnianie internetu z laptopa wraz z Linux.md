Title:      Udostępnianie internetu z laptopa wraz z Linux
Date:       2014-06-15 13:58:26
Modified:   2014-06-15 11:58:26
Status:     inherit
Category:   
Tags:       
Summary: 


<div style="float: left;">
  <a href="http://blog.egel.pl/?attachment_id=1143" rel="attachment wp-att-1143"><img src="http://blog.egel.pl/media/0-lan-300x167.png" alt="Udostępnianie internetu przez Wi-Fi z laptopa do komputera stacjonarnego" width="300" height="167" class="alignleft size-medium wp-image-1143" /></a>
</div>

Szybki i prosty sposób na połączenie laptopa udostępniającego internet przez Wi-Fi (Linux Ubuntu 12.04) dla komputera stacjonarnego PC (Windows 7) poprzez kabel krosowy.

<!--more-->

Istnieje w sieci wiele poradników co i jak połączyć, aby internet "magicznie" zadziałał, lecz moim zdaniem prawie zawsze czegoś w każdym z tych opisów brakuje.  
Często niezbędne jest przeczytanie kilku poradników tak, by z każdego coś wyłuskać i ulepić w jedną "własną" całość. Pytanie po co tak się męczyć, jeśli jest to wyjątkowo proste.  
Z resztą przekonajcie się sami :)

Na początek pewne założenia. Zakładam, że osoby korzystające z domowego routera wykorzystują wbudowany w urządzenie protokół DHCP do zarządzania przydzielaniem komputerów w domowej sieci.

## Laptop (udostępnia internet, Linux Ubuntu 12.04)

Uruchamiamy terminal (domyślnie: *Ctrl*+*Alt*+*T*) i sprawdzamy dostępność naszych interfejsów poleceniem:

    ifconfig
    

Następnie otwieramy plik interfejsów sieci w ulubionym edytorze. Wybrałem **gedit** - jako że jest to domyślny edytor w Ubuntu.

    sudo gedit /etc/network/interfaces 
    

Teraz niezbędne jest wstawienie odpowiedniego wpisu o przekazywaniu połączenia przez interfejs **eth0**. Przypisujemy interfejsowi *eth0* statyczny adres oraz odpowiednią maskę - w tym wypadku 24 bitową, ponieważ adres 192.168.0.1 jest adresem klasy C. Powyższy adres jest bardzo popularnym i prostym do zapamiętania adresem stąd pozwoliłem sobie na jego użycie.

Dodajemy poniższy wpis do naszego pliku *interfaces*

    auto eth0
    iface eth0 inet static
         address 192.168.0.1
         netmask 255.255.255.0  
    

Całość mojego pliku **interfaces **jest widoczna na obrazku poniżej.

<a href="http://blog.egel.pl/udostepnianie-internetu-z-laptopa-wraz-z-linux-ubuntu/interfaces-2/" rel="attachment wp-att-1153"><img src="http://blog.egel.pl/media/interfaces-300x214.png" alt="interfaces" width="300" height="214" class="alignright size-medium wp-image-1153" /></a>

Teraz niezbędne jest zainstalowanie programu **Firestarter**, który rzeczywiście będzie udostępniał nasze połączenie z **wlan0** do **eth0**.  W terminalu wpisujemy:

    sudo apt-get install firestarter
    

Po uruchomieniu programu pojawia się menu konfiguratora - wybieramy jako nasze połączenie udostępniające wlan0 i zaznaczamy obie poniższe opcje. Następnie wybieramy eth0 jako interfejs wyjściowy, przez który ma wychodzić nasze połączenie i zakańczamy konfiguracje.

Pozostaje teraz uruchomić ponownie komputer tak, aby uwzględnił naszą ciężką prace! :)

## Komputer stacjonarny (odbiera internet)

Pierwszą czynnością jaką wykonamy to połączenie skonfigurowanego laptopa z stacjonarką *kablem krosowanym*.  
Kolejno przechodzimy w `Panel sterowania` -> `Sieć i internet` -> `Połączenia sieciowe` -> `Właściwości`.  
Klikamy na protokół TCP/IPv4 i następnie ponownie wybieramy `Właściwości` w nowym okienku i wpisujemy w odpowiednie pola:

<a href="http://blog.egel.pl/udostepnianie-internetu-z-laptopa-wraz-z-linux-ubuntu/untitled-1-2/" rel="attachment wp-att-1152"><img src="http://blog.egel.pl/media/Untitled-1-268x300.png" alt="internet-protocol-ipv4-1" width="268" height="300" class="alignright size-medium wp-image-1152" /></a>

    **Adres IP:** 192.168.0.2 
    **Maska:** 255.255.255.0 
    **Brama:** 192.168.0.1 
    **DNS preferowany:** 208.67.222.222 
    **DNS alternatywny:** 208.67.220.220
    

Upewniamy się że wszystkie ustawienia są z godne z powyższym wpisem, akceptujemy powyższe zmiany, a po chwili komputery wymienią miedzy sobą niezbędne pakiety i połączenie powinno zostać ustanowione samoczynnie. To wszystko:) I przyznacie wcale nie było to, aż takie ciężkie ;)

**Notka:** Czasem istotne może być **włączenie lub zresetowanie usługi DHCP** (reset routera).
