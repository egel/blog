Title:      Kolorowy terminal w Ubuntu
Date:       2014-07-24 02:16:51
Modified:   2014-07-24 00:16:51
Status:     inherit
Category:   
Tags:       
Summary: 


<div style="float: left;">
  <a href="http://blog.egel.pl/aktualizacja-kompilatora-gcc-oraz-g-na-ubuntu/ubuntu-logo/" rel="attachment wp-att-1309"><img src="http://blog.egel.pl/media/ubuntu-logo-150x150.png" alt="Logo Linux Ubuntu" width="150" height="150" class="aligncenter size-thumbnail wp-image-1309" /></a>
</div>

Kolorowa składnia w terminalu Ubuntu - nic prostszego! :)

<!--more-->

<p style="clear:both">
</p>

Przechodzimy do katalogu home użytkownika (własny katalog home) i otwieramy ulubionym edytorem tekstu ukryty plik:

    gedit ~/.bashrc 
    

oraz odznaczamy za komentowaną linijkę usuwając `#` "hasz".

    force_color_prompt=yes 
    

Restart terminala i gotowe :)
