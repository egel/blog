Title:      Obsługa przydatnych komend w Git
Date:       2014-07-24 03:08:23
Modified:   2014-07-24 01:08:23
Status:     inherit
Category:   
Tags:       
Summary:  


<div style="float: left;">
  <a href="http://blog.egel.pl/import-ustawien-git-z-windows-do-cygwin/git_logo-mini/" rel="attachment wp-att-1325"><img src="http://blog.egel.pl/media/git_logo-mini.png" alt="Logo programu Git" width="200" height="83" class="alignnone size-full wp-image-1325" /></a>
</div>

Bardzo przydatne komendy przy pracy z systemem kontroli wersji Git.

<!--more-->

<p style="clear:both">
</p>

### Poprawka do ostatniej rewizji

    git commit -m 'initial commit'
    git add forgotten_file
    git commit --amend
    

### Zmiana rewizji

    git checkout 983dc23s
    git checkout dev
    

### Usuwanie nieśledzonych plików z aktualnie rozwijanej rewizji

    git clean -f
    

### Dodatkowo usuwa katalogi

    git clean -f -d
    

### Usuwa ingnowane pliki

    git clean -f -X
    

### Usuwa pliki ignorowane oraz nie ignorowane

    git clean -f -x
    

### Przenieś/Zmień nazwę gałęzi nawet jeśli aktualna gałąź już istnieje.

Zmień nazwę gałęzi i wskazywania gałęzi na daną rewizje. Przykładowo jeśli przez przypadek stworzyłeś dwie gałęzie `dev` i `DEV`.   
Poniższe polecenie zmieni nazwę na `dev` i zniknie wskaźnik gałęzi `DEV`

    git branch -M dev
