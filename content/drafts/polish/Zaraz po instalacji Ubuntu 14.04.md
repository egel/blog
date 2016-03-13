Title:      Zaraz po instalacji Ubuntu 14.04
Date:       2015-01-30 12:11:20
Modified:   2015-01-30 11:11:20
Status:     inherit
Category:   
Tags:       
Summary:  


<div style="float:left">
  <a href="http://blog.egel.pl/aktualizacja-kompilatora-gcc-oraz-g-na-ubuntu/ubuntu-logo/" rel="attachment wp-att-1309"><img src="http://blog.egel.pl/media/ubuntu-logo-150x150.png" alt="Logo Linux Ubuntu" width="150" height="150" class="alignnone size-thumbnail wp-image-1309" /></a>
</div>

17 kwietnia 2014 roku ukazała się kolejna seria Ubuntu LTS charakteryzująca się długoterminowym wsparciem (5 lat).

Przestawię Wam kilka kroków, które zwykle przydają się zaraz po instalacji Ubuntu 14.04, aby wzbogacić oprogramowanie domyślnie dostarczone z [głównej strony Ubuntu][1].

Generalną przeznaczeniem tego artykułu jest zbiór najefektywniejszego zestawu oprogramowania (w moim subiektywnym odczuciu) i zebranie go w jednym miejscu. Odnajdziesz tu konfigurację oprogramowania dla zwykłych użytkowników Ubuntu, oraz dla developerów, jak również kilka prostych kroków do upiększenia systemu.

Każdy podpunkt instalacji jest niezależny od innych, tak więc, jeśli nie masz ochoty instalować jakiegoś programu po prostu możesz go pominąć i przejść dalej.

Z czasem artykuł ten będę uzupełniać o nowe, dodatkowe programy, a także ich konfiguracje odwołujące się do moich innych artykułów.

<!--more-->

<p style="clear:both">
</p>

#### Instalacja i aktualizacja podstawowych programów:

*   [Podstawowy niezbędnik][2]
*   [Programy archaizujące][3]
*   [Nvidia][4]
*   [Przywrócenie prywatności w Ubuntu][5]
*   [Bluetooth: domyślenie wyłączone][6]
*   [Ubuntu Tweek tool][7]
*   [TLP Battery guardian][8]
*   [Temperature sensors][9]
*   [Touchpad indicator][10]
*   [Chrome][11]
*   [Dropbox][12]
*   [VLC: Video Player][13]
*   [Banshee: Music Player][14]
*   [K3b: Nagrywarka CD/DVD][15]
*   [Pidgin: Komunikator internetowy][16]

#### Dla developerów:

*   [Java Development Kit 7][17]
*   [Git][18]
*   [Python pip][19]
*   [virtualenvwrapper][20]
*   [Nodejs + npm][21]
*   [Gimp + plugins][22]
*   [Gcolor2: Prosty color picker][23]
*   [Shutter: Tworzenie zrzutów ekranu][24]
*   [Gparted: Manager dysków][25]
*   [UNetbootin: Instalator obrazów płyt][26]
*   [Filezilla][27]
*   [Parcellite: Clipboard manager][28]
*   [Tmux: Terminal multiplexer][29]
*   [Guake: Drop-down terminal][30]
*   [Sublime Text 3][31]
*   [VirtualBox][32]

#### Niestandardowe:

*   [TeX Live][33]
*   [GNU R][34]

#### Upiększanie systemu:

*   [Conky + themes][35]
*   [Wyłączenie konta Gość][36]

* * *

### **Instalacja i aktualizacja podstawowych programów**

### <a name="podstawowy-niezbednik" class="jumptarget"></a> Podstawowy niezbędnik

*   Vim
*   Python
*   CURL
*   gcc/c++ (do kompilacji programów)
*   tree (pokazuje pliki w drzewku)
*   enca (sprawdza kodowanie plików)
*   ubuntu-restricted-extras (Ubuntu)
*   build-essential (Ubuntu)

Poniżej komenda pozwalająca na szybką instalację powyższych programów:

    $ sudo apt-get install vim python-pip python-dev python-setuptools curl gcc g++ tree enca ubuntu-restricted-extras build-essential
    

### <a name="programy-archiwizujace" class="jumptarget"></a> Programy archiwizujące

    $ sudo apt-get install unace unrar unzip p7zip-full p7zip-rar sharutils rar uudeview mpack arj cabextract file-roller
    

### <a name="nvidia" class="jumptarget"></a> Nvidia

Z instalacja trzeba uważać ponieważ różne wersje nvidii mogą różnie się zachowywać.

    $ sudo apt-get purge nvidia*
    $ sudo apt-get install nvidia-prime
    $ sudo apt-get install nvidia-331 
    $ sudo apt-get install nvidia-331-updates
    

> W razie problemów po ponownym uruchomieniu, pojawia się "czarny ekran" lub coś podobnego... przełączamy się na inny terminal `Ctrl` + `Alt` + `F1`. Logujemy się na konto z uprawnieniami admina (konto **root** lub własnego użytkownika z pozwoleniem na wykonanie `sudo`) i usuwamy wszystko co związane z nvidią tj.: `sudo apt-get purge nvidia*`, a następnie `sudo reboot`. Po ponownym uruchomieniu powinno wszystko wrócić do normy. Można popróbować z innymi wersjami nvidii. Na moim sprzęcie bez zarzutu działa wersja *nvidia-331*.

### <a name="przywrocenie-prywatnosci-w-ubuntu" class="jumptarget"></a> Przywrócenie prywatności w Ubuntu

> Więcej na temat poniższej komendy (uruchamianego skryptu), a także o nieładnej polityce prywatności firmy Canonical, odsyłam na stronę <https://fixubuntu.com/>, gdzie dokładniej omówiono całe zagadnienie prywatności w Ubutnu.

    $ wget -q -O - https://fixubuntu.com/fixubuntu.sh | bash
    

### <a name="bluetooth" class="jumptarget"></a> Bluetooth: domyślenie wyłączone

    $ sudo gedit /etc/rc.local
    

dodajemy do pliku (przed linią `exit 0`) linijkę :

    $ rfkill block bluetooth
    

i zapisujemy. Po ponownym uruchomieniu bluetooth nie zostanie domyślnie uruchomiony.

### <a name="ubuntu-tweek-tool" class="jumptarget"></a> Ubuntu Tweek tool

    $ sudo apt-get install unity-tweak-tool
    

### <a name="tlp" class="jumptarget"></a> TLP Battery guardian

    $ sudo add-apt-repository ppa:linrunner/tlp
    $ sudo apt-get update
    $ sudo apt-get install tlp tlp-rdw
    $ sudo tlp bat
    

### <a name="temperature-sensors" class="jumptarget"></a> Temperature sensors

    $ sudo apt-get install lm-sensors
    

### <a name="touchpad-indicator" class="jumptarget"></a> Touchpad indicator

    $ sudo add-apt-repository ppa:atareao/atareao
    $ sudo apt-get update
    $ sudo apt-get install touchpad-indicator
    

### <a name="chrome" class="jumptarget"></a> Chrome

Pakiet `.deb` do pobrania ze [strony producenta][37]

### <a name="dropbox" class="jumptarget"></a> Dropbox

Pakiet `.deb` do pobrania ze [strony producenta][38]

> Konieczne może być doinstalowanie wymaganego przez Dropbox pakietu: `sudo apt-get install python-gpgme`

### <a name="vlc-player" class="jumptarget"></a> VLC: Video Player

    $ sudo apt-get install vlc
    

### <a name="banshee-player" class="jumptarget"></a> Banshee: Music Player

Najbardziej niezawodny odtwarzacz muzyczny z jakim miałem do tej pory przyjemność odczynienia.

    $ sudo add-apt-repository ppa:banshee-team/ppa
    $ sudo apt-get update
    $ sudo apt-get install banshee
    

> Domyślny odtwarzacz Rhythmbox zacina się przy większych bibliotekach muzycznych (więcej niż 60GB) i jak zauważyłem ma problem z odczytaniem kodowania w niektórych plikach FLAC, mp3, ogg. Z tymi zadaniami bez kłopotu radzi sobie własnie Banshee.

### <a name="k3b-burner" class="jumptarget"></a>K3b: Nagrywarka CD/DVD

Program do nagrywania płyt

    $ sudo apt-get install k3b    
    

### <a name="pidgin" class="jumptarget"></a>Pidgin: Komunikator internetowy

Prosty chodź bardzo funkcjonalny komunikator internetowy.

    $ sudo add-apt-repository -y ppa:pidgin-developers/ppa
    $ sudo apt-get update
    $ sudo apt-get install pidgin
    

* * *

### **For Developers:**

### <a name="jdk7" class="jumptarget"></a> Java Development Kit 7

    $ sudo add-apt-repository -y ppa:webupd8team/java
    $ sudo apt-get update
    $ sudo apt-get install oracle-java7-installer -y
    $ update-alternatives --display java
    

Sprawdzić aktualną wersję Javy

    $ java -version
    

Opcjonalne: zmiana zainstalowanych wersji Javy

    $ sudo update-alternatives --config java
    

### <a name="git" class="jumptarget"></a> Git

Instalacja programu Git oraz domyślnego interfejsu graficznego:

    $ sudo add-apt-repository ppa:git-core/ppa
    $ sudo apt-get update
    $ sudo apt-get install git gitg
    

### <a name="python-pip" class="jumptarget"></a> Python pip

    $ sudo apt-get install python-dev python-pip python-setuptools
    $ sudo pip install --upgrade pip
    $ pip --version
    

> W razie kłopotów z instalacją odsyłam do [tego pytania na StackOverflow][39]

### <a name="virtualenvwrapper" class="jumptarget"></a> virtualenvwrapper

    $ sudo pip install virtualenvwrapper
    

dodać na końcu do `~/.bashrc`:

    export WORKON_HOME=$HOME/virtualenvs
    export PROJECT_HOME=$HOME/Devel
    source /usr/local/bin/virtualenvwrapper.sh
    

### <a name="install-nodejs-and-npm" class="jumptarget"></a> Install Nodejs + npm

Instalacja jest dla czystego systemu:

    # Add PPA + update system
    $ sudo apt-get install python-software-properties
    $ sudo apt-add-repository ppa:chris-lea/node.js
    $ sudo apt-get update
    
    $ sudo apt-get install nodejs
    $ node -v
    $ npm -v
    

Ewentualna aktualizacja npm'a:

    $ sudo npm update -g npm
    $ npm -V
    

> Podczas instalacji npm'a (lub aktualizacji jego podprogramów) poprzez `sudo`, występuje drobny [problem z nadpisywaniem lokalnego katalogu użytkownika][40]. Chodzi oczywiście o katalog `~/.npm`. Można ten kłopot bardzo łatwo naprawić wykonując komendę:

    $ sudo chown -R `whoami` ~/.npm
    

### <a name="gimp" class="jumptarget"></a> Gimp + plugins

    $ sudo apt-get install gimp gimp-plugin-registry
    

### <a name="gcolor2" class="jumptarget"></a> Gcolor2: Prosty color picker

Super prosty color-picker dla systemu Ubuntu.

    $ sudo apt-get install gcolor2
    

### <a name="program-shutter" class="jumptarget"></a> Shutter: Tworzenie zrzutów ekranu

Doskonały i prosty w użyciu program do tworzenia wymagających zrzutów ekranu.

    $ sudo apt-get install shutter
    

### <a name="program-gparted" class="jumptarget"></a> Gparted: Manager dysków

Genialny program do zarządzania dyskami. Świetnie nadaje się do szybkiej zmiany systemu plików np.: dla pendrive'ów.

    $ sudo apt-get install gparted
    

### <a name="unetbootin" class="jumptarget"></a> UNetbootin: Instalator obrazów płyt

Program do nagrywania obrazów płyt na dysk flash.

    $ sudo apt-get install unetbootin
    

### <a name="filezilla" class="jumptarget"></a> Filezilla

Klient FTP

    $ sudo apt-get install filezilla
    

### <a name="program-parcellite" class="jumptarget"></a> Parcellite

Menadżer kopiowania. Zapewnia historię kopiowanych elementów w schowku systemowym.

    $ sudo apt-get install parcellite
    

### <a name="program-tmux" class="jumptarget"></a> Tmux: Terminal multiplexer

    $ sudo add-apt-repository ppa:pi-rho/dev
    $ sudo apt-get update
    $ sudo apt-get install tmux
    

Więcej na temat konfiguracji tego programu można odnaleźć w moim innym artykule zatytułowanym: [Tmux – instalacja i konfiguracja][41]

### <a name="guake" class="jumptarget"></a> Guake: Drop-down terminal

Bardzo prosty i wygodny w użyciu terminal.

    $ sudo apt-get install guake
    

Dodatkowo można doinstalować wyświetlanie podręcznych opcji w górnym pasku systemowym.

    $ sudo add-apt-repository ppa:gun101/ppa
    $ sudo apt-get update
    $ sudo apt-get install guake-indicator
    

> Jeśli korzystasz z wielu monitorów jednocześnie i chcesz zmienić domyślnie pojawianie się okienka Guake skrajnym lewym ekranie to zapoznaj się z [tym pytaniem na StackOverflow][42].

### <a name="sublime-text-3" class="jumptarget"></a> Sublime Text 3

Genialny i prosty w użyciu edytorów tekstu

    $ wget http://c758482.r82.cf2.rackcdn.com/sublime-text_build-3059_amd64.deb -P /tmp && \
    sudo dpkg -i /tmp/sublime-text_build-3059_amd64.deb && \
    rm /tmp/sublime-text_build-3059_amd64.deb
    

Więcej na temat konfiguracji tego programu można odnaleźć w moim innym artykule zatytułowanym: [Sublime Text 3 – instalacja i konfiguracja][43]

### <a name="virtualbox" class="jumptarget"></a> VirtualBox

Na początek instalacja menadżera zależności pakietów aby uniknąć błędów. Następnie dodajemy klucz publiczny Oracle i dodajemy repozytorium. Na koniec odświeżenie pakietów i instalacja.

Całość prezentuje jedna zbiorcza komenda.

    $ sudo apt-get install dkms \
      && wget -q http://download.virtualbox.org/virtualbox/debian/oracle_vbox.asc -O- | sudo apt-key add - \
      && sudo sh -c 'echo "deb http://download.virtualbox.org/virtualbox/debian trusty contrib" >> /etc/apt/sources.list.d/virtualbox.list' \
      && sudo apt-get update \
      && sudo apt-get install virtualbox-4.3
    

* * *

### **Niestandardowe:**

### <a name="texlive" class="jumptarget"></a> TeX Live + biber

Ubuntu 14.04 domyślnie instaluje wersję TeX Live 2013. Natomiast `biber` w ogromnym skrócie jest zamiennikiem BibTeX dla użytkowników korzystających z biblatex. Więcej informacji na temat programu biber możesz odnaleźć [tutaj][44].

    $ sudo apt-get install texlive-full biber
    

Program `biber` powinien znajdować się w nowej aktualizacji dla TeX Live, lecz jeśli go nie ma:

    $ biber --version
    

należy go doinstalować ręcznie:

    $ sudo apt-get install biber
    

> W razie problemów [manual biber z CTAN][45]

### <a name="r" class="jumptarget"></a> R

GNU R to język programowania i środowisko do obliczeń statystycznych i wizualizacji wyników.

    $ sudo apt-get install r-base
    

> Ewentualna naprawa Javy jeśli wystąpią problemy w działaniu programu komendą: `$ sudo R CMD javareconf`

* * *

### **Upiększanie systemu:**

### <a name="conky-themes" class="jumptarget"></a>Conky + themes

> Nie wiesz co to conky? Zobacz [stronę autora][46]

    $ sudo apt-get install conky conky-all curl lm-sensors hddtemp
    

Teraz pobieramy przygotowane przeze mnie repozytorium ze skórkami:

    $ git clone --recursive https://github.com/egel/conky-themes.git ~/.conky-themes
    

doinstalowujemy dodatkowe biblioteki potrzebne dla skórek:

    $ sudo apt-get install mpd mpc hal-info vnstat lua5.2
    

oraz ręcznie instalujemy: [nbtscan][47]

Następnie dodanie conky do startu systemu na przykładzie `conky_seamod`:

    $ mkdir ~/.config/autostart/
    $ ln -s ~/.conky-themes/conky_seamod/.conkyrc ~/
    $ touch ~/.config/autostart/conky.desktop
    

oraz dodać to do nowo utworzonego pliku `conky.desktop`:

    [Desktop Entry]
    Type=Application
    Exec=conky
    Hidden=false
    NoDisplay=false
    X-GNOME-Autostart-enabled=true
    Name[pl_PL]=Conky
    Name=Conky
    Comment[pl_PL]=Program Conky
    Comment=Program Conky
    

...zapisujemy i gotowe :) Po ponownym uruchomieniu systemu conky automatycznie włączy się dla nas, ale można również uruchomić conky bezpośrednio po instalacji, wykonując w terminalu:

    $ conky & 
    

**Wyłączenie conky**

    $ killall conky
    

### <a name="wylaczenie-konta-gosc" class="jumptarget"></a>Wyłączenie konta Gość

W pliku:

    $ sudo vim /etc/lightdm/lightdm.conf
    

Dodajemy linijkę:

    allow-guest=false
    

Zapisujemy i po ponownym uruchomieniu komputera konto Gościa będzie niewidoczne.

 [1]: #http://www.ubuntu.com/download/desktop/
 [2]: #podstawowy-niezbednik
 [3]: #programy-archiwizujace
 [4]: #nvidia
 [5]: #przywrocenie-prywatnosci-w-ubuntu
 [6]: #bluetooth
 [7]: #ubuntu-tweek-tool
 [8]: #tlp
 [9]: #temperature-sensors
 [10]: #touchpad-indicator
 [11]: #chrome
 [12]: #dropbox
 [13]: #vlc-player
 [14]: #banshee-player
 [15]: #k3b-burner
 [16]: #pidgin
 [17]: #jdk7
 [18]: #git
 [19]: #python-pip
 [20]: #virtualenvwrapper
 [21]: #install-nodejs-and-npm
 [22]: #gimp
 [23]: #gcolor2
 [24]: #program-shutter
 [25]: #program-gparted
 [26]: #unetbootin
 [27]: #filezilla
 [28]: #program-parcellite
 [29]: #program-tmux
 [30]: #guake
 [31]: #sublime-text-3
 [32]: #virtualbox
 [33]: #texlive
 [34]: #r
 [35]: #conky-themes
 [36]: #wylaczenie-konta-gosc
 [37]: http://www.google.pl/intl/pl/chrome/
 [38]: https://www.dropbox.com/downloading?src=index
 [39]: http://stackoverflow.com/questions/16237490/i-screwed-up-the-system-version-of-python-pip-on-ubuntu-12-10
 [40]: http://stackoverflow.com/questions/16151018/npm-throws-error-without-sudo
 [41]: http://blog.egel.pl/tmux-instalacja-konfiguracja/
 [42]: http://askubuntu.com/a/504509/168174
 [43]: http://blog.egel.pl/sublime-text-3-instalacja-konfiguracja/
 [44]: http://biblatex-biber.sourceforge.net/
 [45]: http://www.ctan.org/pkg/biber
 [46]: http://conky.sourceforge.net/
 [47]: http://packages.ubuntu.com/lucid/amd64/nbtscan/download
