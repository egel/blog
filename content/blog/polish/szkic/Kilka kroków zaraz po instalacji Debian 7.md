Title:      Kilka kroków zaraz po instalacji Debian 7
Date:       2013-10-24 
Modified:   
Status:     Draft
Category:   
Tags:       Linux, Debian
Summary: 



Prosty poradnik - niekoniecznie poprawny - co powinno się zrobić zaraz po instalacji Debian 7 Wheezy.

### Dodanie użytkownika do grupy sudo. <small>Nie jest to koniecznie</small>

Niektórzy nie zalecają tej operacji ze względów bezpieczeństwa, ale uważam, że jeśli ktoś jest świadomym użytkownikiem i wie co robi, to jest to tylko dodatkową pomocą w pracy z systemem.

Użytkownik: maciek  
Grupa: sudo

    su root
    useradd -g sudo maciek
    

### Aktualizacja repozytoriów.

Kluczowa rzecz którą należy zrobić po zaraz po instalacji jest aktualizacja repozytoriów.

    sudo gedit /etc/apt/sources.list
    

Podstawowe pakiety w dla wersji stabilnej Debian 7 Wheezy

    #~~~~~~Wheezy~~~~~~#
    deb http://ftp.pl.debian.org/debian/ wheezy main non-free contrib
    deb-src http://ftp.pl.debian.org/debian/ wheezy main non-free contrib
    deb http://security.debian.org/ wheezy/updates main contrib non-free
    deb-src http://security.debian.org/ wheezy/updates main contrib non-free
    deb http://ftp.pl.debian.org/debian/ wheezy-updates main non-free contrib
    deb-src http://ftp.pl.debian.org/debian/ wheezy-updates main non-free contrib
    

Dodatkowe pakiety

    #~~~~~~Deb-multimedia~~~~~~#
    deb http://www.deb-multimedia.org/ stable main non-free
    deb-src http://www.deb-multimedia.org/ stable main non-free
