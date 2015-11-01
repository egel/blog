Title:      Import ustawień Git z Windows do Cygwin (Linux)
Date:       2014-07-24 02:46:54
Modified:   2014-07-24 00:46:54
Status:     inherit
Category:   
Tags:       
Summary:  


<div style="float: left;">
  <a href="http://blog.egel.pl/import-ustawien-git-z-windows-do-cygwin/git_logo-mini/" rel="attachment wp-att-1325"><img src="http://blog.egel.pl/media/git_logo-mini.png" alt="git_logo-mini" width="200" height="83" class="aligncenter size-full wp-image-1325" /></a>
</div>

Ostatnia zabawa Linuksem zachęciła mnie do posiadania i korzystania z terminala w stylu "pingwinka". Z pomocą oczywiście pośpieszył *Cygwin*. Ustawienia Git'a obecne w `cmd`, trudno szukać w terminalu Cygwin'a, lecz zbytnio mnie nie zdziwiło.  
Wygląda na to że instalacja *Cygwin* na *Windows* jest zupełnie odrębną rzeczą. Brak opcji integracji obydwu terminali ze sobą (np. wspólnych aliasów).

Nie chciałem przepisywać wszystkich przydatnych aliasów oraz personalnych ustawień z *Git* pod *Windows*, więc postanowiłem poszukać trochę informacji o przechowywaniu konfiguracji `.gitconfig` w systemie.

Poniżej drobny tip, jak tego szybko dokonać dla oszczędności czasu.

<!--more-->

### Windows

Plik z ustawieniami `.gitconfig` pod *Windows* znajduje się w ścieżce: `C:\Users\<nazwa usera>`.  
Dla przykładu: `C:\Users\Maciek`

### Linux (Cygwin)

Plik z ustawieniami `.gitconfig` pod *Cygwin'em* znajduje się w głównym katalogu użytkownika.  
Dla przykładu:

    /home/Maciek
    

lub

    ~/
    

### Komenda

A oto komenda, którą należy wpisać w terminal *Cygwin'a*, aby skopiować *domyślne* istniejące ustawienia *Git'a* z *Windows'a* do *Cygwin'a*

    cp /cygdrive/c/Users/Maciek/.gitconfig /home/Maciek/.gitconfig
