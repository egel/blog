Title:      Zmiana mac karty w Ubuntu
Date:       2013-10-20 
Modified:   
Status:     Draft
Category:   
Tags:       Vim, text-editor
Summary:


Mała poprawka: - żeby zmienić MAC należy najpierw wyłączyć interfejs, zmienić MAC, włączyć interfejs, tj.: sudo ifconfig ethX down sudo ifconfig ethX hw ether adres_MAC_karty_sieciowej sudo ifconfig ethX up

*   ponowne uruchomienie komputera przywraca oryginalny MAC karty.

*   do zmiany MAC'a polecam macchanger (jest w repozytoriach),

*   ja osobiście zrobiłem sobie skrypcik do zmiany MAC'a, bo macchanger przyjmuje MAC w postaci z dwukropkami, a nie zawsze mam tak adresy (często bez) a ifconfig bierze to i to :) tu http://wklej.org/id/111365/ wrzuciłem skrypcik :) miłego korzystania ;]
