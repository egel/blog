Title:      Polskie znaki w Texmaker na Ubuntu
Date:       2015-03-13 10:05:27
Modified:   2015-03-13 09:05:27
Status:     inherit
Category:   
Tags:       
Summary:


<div style="float: left;">
  <a href="http://blog.egel.pl/?attachment_id=1154" rel="attachment wp-att-1154"><img src="http://blog.egel.pl/media/texmaker128.png" alt="texmaker128" width="128" height="128" class="alignright size-full wp-image-1154" /></a>
</div>

Ostatnio napotkałem pewien problem z instalacją **Texmaker** na **Ubuntu 13.04**. Problem polegał na tym, że chcąc skompilować dokument PDF w programie, wywaliło błąd: `missing polish.sty` Jak się okazało po prostu brakowało zainstalowanego polskiego pakietu.

<!--more-->

<br style="clear: both" />

Proste lekarstwo na tą przypadłość, to 2 komendy w terminalu:

    sudo apt-cache search texlive polish
    sudo apt-get install texlive-lang-polish
    

> **Notka:** Warto jednak zainstalować pełny pakiet bibliotek TeX'a. Dzięki temu zabiegowi zniknie problem brakujących bibliotek, które momentami dość ciężko wykryć (zdebugować). Można tego dokonać poleceniem: `sudo apt-get install texlive-full`. Całość zajmuje ~1,5GB.

A wtedy poniższy krótki skrypcik LaTeXa wykorzystujący literki typowe dla polskiego alfabetu, powinien zadziałać już bezproblemowo :)

    \documentclass[10pt, oneside, a4paper]{book}
    \usepackage[OT4,plmath]{polski} % definicja użycia platex
    \usepackage[utf8]{inputenc}
    \usepackage[OT4]{fontenc}
    \usepackage{url}
    
    \title{\huge Protokoły routingu}
    \author{Maciej Sypień}
    \date{\today}
    
    \begin{document}
    \maketitle
    \section{Podsumowanie}
    
    Protokoły routingu stanu łącza, zwane także protokołami wyboru najkrótszej ścieżki, opierają się na algorytmie SPF \emph{Edsgera Dijkstry}. Istnieją dwa protokoły routingu stanu łącza dla sieci IP: \emph{OSPF (Open Shortest Path First)} i~\mbox{\emph{IS-IS (Intermediate System-to-Inter-mediate System)}}.
    \end{document}
    

Działający gotowy przykład możesz odnaleźć tutaj: <a class="btn btn-primary" href="http://bit.ly/1BBnnm6">Przykład online</a>
