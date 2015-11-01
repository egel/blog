Title:      Przyspieszenie pracy dzięki aliasom w Linux
Date:       2014-07-24 03:36:24
Modified:   2014-07-24 01:36:24
Status:     inherit
Category:   
Tags:       
Summary:  



<div style="float: left">
  <a href="http://blog.egel.pl/wydajniejsza-praca-dzieki-aliasom/terminal_icon/" rel="attachment wp-att-1345"><img src="http://blog.egel.pl/media/terminal_icon-150x150.png" alt="Konsola terminala" width="150" height="150" class="alignnone size-thumbnail wp-image-1345" /></a>
</div>

Nie od dziś wiadomo, że *aliasy* to użyteczna rzecz :)  
Oszczędności czasu, przyspieszenie pracy, zastąpienie szeregu żmudnych działań do wykonania poprzez skrócenie ich do jednej komendy - tak, to jest to!

*Ale jak z tego skorzystać?*

Odpowiedź jak zwykle jest bardzo prosta.

<!--more-->

<p style="clear: both">
</p>

Otwieramy terminal i wpisujemy:

    sudo gedit ~/bash_aliases 
    

Do otworzonego edytora wpisujemy nasze komendy.  
Poniżej kilka użytecznych przykładów, które moim zdaniem z pewnością przydadzą się podczas codziennej pracy z konsolą.

    alias aktualizuj='sudo apt-get clean && sudo apt-get autoclean && sudo apt-get autoremove && sudo apt-get update && sudo apt-get dist-upgrade'  
    
    alias nara='sudo shutdown -h now' 
    
    alias reset='sudo reboot' 
    
    alias instaluj='sudo apt-get install' 
    
    alias ..='cd ..' 
    

Zapisujemy plik i uruchamiamy ponownie terminal. Enjoy :)
