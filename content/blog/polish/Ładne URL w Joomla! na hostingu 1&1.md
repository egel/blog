Title:      Ładne URL w Joomla! na hostingu 1&1
Date:       2014-07-24 03:13:37
Modified:   2014-07-24 01:13:37
Status:     Draft
Category:   
Tags:       
Summary: 


<div style="float: left;">
  <a href="http://blog.egel.pl/ukrywanie-obrazka-w-zawartosci-artykulu-thumb-class/joomla_logo_mini/" rel="attachment wp-att-1337"><img src="http://blog.egel.pl/media/joomla_logo_mini-150x150.png" alt="Joomla Logo" width="150" height="150" class="alignnone size-thumbnail wp-image-1337" /></a>
</div>

Kolejny problem jaki spotkałem w trakcie prac z *Joomla!* na polskim hostingu [1&1][1].  
Instalacja Joomla! na wspomnianym hostingu przebiega bez żanych problemów.  
Chcąc uzyskać ładne sformatowane adresy w URL, włączenie `mod_rewrite` w konfiguracji Joomla! wyświetla komunikat na stronie:

`INTERNAL SERVER ERROR`

<!--more-->

<p style="clear:both">
</p>

Rozwiązaniem problemu okazało się od komentowanie poniższej linijki z domyślnej konfiguracji pliku `.htaccess`.

    RewriteEngine On RewriteBase /

 [1]: http://1and1.pl
