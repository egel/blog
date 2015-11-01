Title:      Instalacja spakowanego programu w Ubuntu
Date:       2014-07-24 03:36:31
Modified:   2014-07-24 01:36:31
Status:     inherit
Category:   
Tags:       
Summary:  


<div style="float: left;">
  <a href="http://blog.egel.pl/aktualizacja-kompilatora-gcc-oraz-g-na-ubuntu/ubuntu-logo/" rel="attachment wp-att-1309"><img src="http://blog.egel.pl/media/ubuntu-logo-150x150.png" alt="Logo Linux Ubuntu" width="150" height="150" class="alignnone size-thumbnail wp-image-1309" /></a>
</div>

Wydawałoby się, że instalacja programu z spakowanej paczki np .zip, .tar, tar.gz czy innych jest sprawą niezwykle skomplikowaną... otóż nic z tych rzeczy.  
W poniższym przykładzie posłużę się programem `Aptana Studio 3`, którego możliwe, że część używa pod delikatnie inną postacią jaką jest `Eclipse'a`.

<!--more-->

<p style="clear: both">
</p>

Program można pobrać ze strony producenta, którego link możecie znaleźć [tutaj][1]. Na chwilę pisania artykułu jest to wersja 3.4.1.

A teraz w kilku krokach co należy zrobić, aby nasz program był widoczny dla wyszukiwarki Ubuntu (tj. Start w Windows) oraz w terminalu pod nazwą `AptanaStudio3`.

1.  Pobieramy [spakowany program][1] (nie plugin) w wersji **standalone**.

2.  Przechodzimy do katalogu z pobranym programem
    
         cd ~/Pobrane/
        

3.  Rozpakowujemy nasz program (.zip) do przeznaczonego dla naszego programu katalogu komendą:
    
        sudo unzip Aptana_Studio_3.zip -d /opt/
        

4.  Po udanym rozpakowaniu programu do katalogu `/opt` musimy stworzyć w katalogu `/usr/share/applications/` plik np.: o nazwie `aptanastudio3.desktop` i zapisać w nim niezbędne dyrektywy.
    
        sudo gedit /usr/share/applications/aptanastudio3.desktop
        

5.  W nowo otwartym pliku w notatniku wklejamy:
    
        [Desktop Entry]
        Type=Application
        Exec=/opt/Aptana_Studio_3/AptanaStudio3
        Terminal=false
        Icon=/opt/Aptana_Studio_3/icon.xpm
        Comment=Integrated Development Environment
        NoDisplay=false
        Categories=Development;IDE
        Name=Aptana Studio 3
        Name[en]=Aptana Studio 3
        

6.  Teraz musimy utworzyć jeszcze dowiązanie do naszego pliku:
    
        cd /usr/local/bin  
        sudo ln -s /opt/Aptana_Studio_3/AptanaStudio3
        

I to już wszystko. Możemy cieszyć się nowo zainstalowanym programem w Ubuntu.

 [1]: http://www.aptana.com/products/studio3/download
