Title:      Udostępnianie internetu z laptopa z Windows 7
Date:       2014-05-24 00:03:20
Modified:   2014-05-23 22:03:20
Status:     inherit
Category:   
Tags:       
Summary: 


<div style="float:left;">
  <a href="http://blog.egel.pl/?attachment_id=1143" rel="attachment wp-att-1143"><img src="http://blog.egel.pl/media/0-lan-300x167.png" alt="Udostępnianie internetu przez Wi-Fi z laptopa do komputera stacjonarnego" width="300" height="167" class="alignleft size-medium wp-image-1143" /></a>
</div>

Szybki i prosty sposób na połączenie laptopa udostępniającego internet przez Wi-Fi dla komputera stacjonarnego PC poprzez kabel krosowy, a oba komputery wyposażone są w system Windows 7.

<!--more-->

## Laptop (udostępnia internet)

<a href="http://blog.egel.pl/?attachment_id=1142" rel="attachment wp-att-1142"><img src="http://blog.egel.pl/media/1-lan-282x300.png" alt="1-lan" width="282" height="300" class="alignleft size-medium wp-image-1142" /></a>

Wchodzimy w `Panel sterowania` -> `Sieć i internet` -> `Połączenia sieciowe` -> `Właściwości`.  
Klikamy na protokół TCP/IPv4 i następnie ponownie wybieramy *Właściwości -* wpisując poniższe ustawienia w okienko:

    IP: 192.168.137.1
    MASKA: 255.255.255.0
    Brama DNS: puste
    

<a href="http://blog.egel.pl/?attachment_id=1141" rel="attachment wp-att-1141"><img src="http://blog.egel.pl/media/2-lan-300x280.png" alt="2-lan" width="300" height="280" class="alignleft size-medium wp-image-1141" /></a>

Następnie ponownie wchodzimy w `Panel sterowania` -> `Sieć i internet` -> `Połączenia sieciowe` (domyślenie to: *Połączenie sieci bezprzewodowej*) z którego laptop łączy się z siecią internet i wybieramy `Właściwości`.  
W nowym okienku wybieramy zakładkę *Udostępnianie* i zaznaczamy *Zezwalaj innym użytkownikom sieci na łączenie się poprzez połączenie internetowe tego komputera*, a następnie wpisujemy lub wybieramy połączenie którym będziemy rozgłaszać sieć. Tyle jeśli chodzi o laptopa. Teraz przechodzimy do komputera stacjonarnego.</p> 

## Komputer stacjonarny (odbiera internet)

<a href="http://blog.egel.pl/?attachment_id=1140" rel="attachment wp-att-1140"><img src="http://blog.egel.pl/media/3-lan-273x300.png" alt="3-lan" width="273" height="300" class="alignleft size-medium wp-image-1140" /></a>

Pierwszą czynnością jaką wykonamy to połączenie skonfigurowanego laptopa z stacjonarką *kablem krosowanym*.  
Kolejno przechodzimy jak wyżej w `Panel sterowania` -> `Sieć i internet` -> `Połączenia sieciowe` -> `Właściwości`.  
Klikamy na protokół *TCP/IPv4* i następnie ponownie wybieramy `Właściwości` w nowym okienku:

Upewniamy się że wszystkie ustawienia pozostawione na konfigurację automatyczną (IP, maska, brama oraz DNS)

Po chwili komputery powinny wymienić miedzy sobą pakiety i połączenie powinno zostać ustanowione samoczynnie. Gotowe :)

### Notka:

Czasem istotne może być **włączenie lub zresetowanie usługi DHCP** (reset routera).
