Title:      Git log - bardziej wyrafinowany styl wyglądu grafów
Date:       2014-07-24 02:56:04
Modified:   2014-07-24 00:56:04
Status:     inherit
Category:   
Tags:       
Summary: 


<div style="float: left">
  <a href="http://blog.egel.pl/import-ustawien-git-z-windows-do-cygwin/git_logo-mini/" rel="attachment wp-att-1325"><img src="http://blog.egel.pl/media/git_logo-mini.png" alt="Logo programu Git" width="200" height="83" class="alignnone size-full wp-image-1325" /></a>
</div>

Bardzo ważną rzeczą w skutecznym rozwijaniu projektu jest jego dokumentacja. Im jest lepsza tym lepiej możemy zrozumieć projekt. Tak przynajmniej jest w teorii.

Oto kilka bardzo fajnych aliasów dla *Git'a* do wyświetlania "pięknego" loga z commit'ami ;)

<!--more-->

<p style="clear:both">
</p>

### Komenda 1

    git log --graph --date-order -C -M --pretty=format:"<%h> %ad [%an] %Cgreen%d%Creset %s" --all --date=short 
    

### Przykłady Aliasów

    [alias] 
    lg1 = log --graph --all --format=format:'%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(bold white)— %an%C(reset)%C(bold yellow)%d%C(reset)' --abbrev-commit --date=relative 
    
    lg2 = log --graph --all --format=format:'%C(bold blue)%h%C(reset) - %C(bold cyan)%aD%C(reset) %C(bold green)(%ar)%C(reset)%C(bold yellow)%d%C(reset)%n'' %C(white)%s%C(reset) %C(bold white)— %an%C(reset)' --abbrev-commit 
    
    lg = !"git lg1"
    

> Ale jak zapisać to na stałe w konfiguracji Git'a?

Powyższy kod można bezpośrednio wkleić w `.gitconfig` zaraz pod [alias] i zadziała bez większego problemu lub skorzystać z wbudowanej komendy `Git'a`.  
Żeby to osiągnąć najprościej trzeba otworzyć konsole i wklepać:

    git config --global alias.lg "log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr)%Creset' --abbrev-commit --date=relative"
