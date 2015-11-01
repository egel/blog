Title:      Konfiguracja NetBeans 7.4
Date:       2014-07-24 01:53:12
Modified:   2014-07-23 23:53:12
Status:     inherit
Category:   
Tags:       
Summary:  


<div style="float: left;">
  <a href="http://blog.egel.pl/konfiguracja-netbeans-7-4/netbeans74-logo/" rel="attachment wp-att-1278"><img src="http://blog.egel.pl/media/netbeans74-logo-150x150.png" alt="Logo programu NetBeans 7" width="150" height="150" class="alignright size-thumbnail wp-image-1278" /></a>
</div>

Jeśli chodzi o komponowanie kodu to NetBeans bez cienia wątpliwości jest do tego doskonałym narzędziem. Szerokie zastosowanie i potężna, jednolita konfiguracja dla różnego rodzaju języków przezeń wspieranych, oddaje w ręce użytkownika potocznie nazywany "kombajn" do tworzenia doskonałego oprogramowania.

To kwestia gustu co prawda, lecz w subiektywnym odczuciu NetBeans wydaje się nieco bardziej przyjazny użytkownikowi (względem interfejsu, konfiguracji, czy instalacji dodatków) od jego zagorzałego rywala, edytora Eclipse.

Jednak nie przekomarzanie się o tym "który lepszy" jest tematem tego artykułu, a zatem przejdźmy do zasadniczego punktu - konfiguracji środowiska NetBeans:

<!--more-->

Co będzie zawarte w niniejszej prostej konfiguracji programu Netbeans?

*   [Instalacja programu][1]
*   [Instalacja ciemnej skórki][2]
*   [Styl pisania kodu][3]
*   [Pokazanie ukrytych plików `.*`][4]

### <a name="instalacja-programu"></a>Instalacja programu

Dla systemu Linux sprawa jest miodnie prosta :)

    $ cd ~/Pobrane && wget http://download.netbeans.org/netbeans/7.4/final/bundles/netbeans-7.4-linux.sh && chmod +x netbeans-7.4-linux.sh && ./netbeans-7.4-linux.sh
    

Tyle wystarczy, aby terminal sam pobrał i uruchomił nasz instalator oraz zainicjował proces instalacji.

Po instalacji ewentualnie można posprzątać po sobie usuwając skrypt instalacyjny:

    $ rm ~/Pobrane/netbeans-7.4-linux.sh
    

### <a name="instalacja-ciemnej-skorki"></a>Instalacja ciemnej skórki

Z racji tego, że przyjemniejszym dla mego oka są ciemne skórki, zmienimy więc delikatnie domyślny wygląd programu.

Pierw zainstalujemy ciemny motyw interfejsu użytkownika.

Tools > Plugins

i szukamy `Dark Theme` lub coś podobnego (możliwe że nazwa się zmieni), a następnie instalujemy i restart IDE.

Na stronie <http://netbeansthemes.com/> odnajdziesz paczki z różnymi, bardzo ciekawymi skórkami do NetBeans.

Mi osobiście do gustu przypadła skórka `Monokai Sublime`. Tak więc na jej przykładzie zobrazuje całą instalację (tyczy się to również wszystkich innych skórek z tej strony)

1.  Uruchamiamy program
2.  Pobieramy skórkę na komputer
3.  Tools > Options > import (lewy dolny róg okienka)
4.  Wyszukujemy nasz plik `.zip` i otwieramy, pozwalając instalatorowi zrobić resztę
5.  Restart IDE
6.  Jeszcze tylko drobna zmiana kolorów z konfiguracji domyślnej i jesteśmy w domu:

Tools > Options > Fonts & Colors > Syntax tab-> Language (wybierz PHP, C, C++, C/C++ Headers [oraz te w których pracujesz]) -> Mark Occurences -> Foreground = zmienić na [black]

### <a name="styl-pisania-kodu"></a>Styl pisania kodu

Z racji tego że dużo czasu spędzam przy komputerze (Laptop z rozdzielczością 1920*1080) i stosunkowo małym ekranie 16,4" cala, preferuje delikatnie odmienne ustawienia od przeciętnego monitora z tą samą rozdzielczością, stąd w ustawieniach:

Tools > Options > Formating

*   Style: Apache (Jak dla mnie styl idealny)
*   Font: 16
*   Tab size: 4

### <a name="pokazanie-ukrytych-plikow"></a>Pokazanie ukrytych plików

1.  Tools > Options > Miscellaneous > Files
2.  Zamieniamy:
    
        ^(CVS|SCCS|vssver.?.scc|#.*#|%.*%|_svn)$|~$|^.(?!htaccess$).*$
        
    
    na
    
        ^(CVS|SCCS|vssver.?.scc|#.*#|%.*%|_svn)$|~$|^.(?!htaccess$)$ 
        
    
    pozbywając się `.*` z końca wiersza.

3.  Zapis i gotowe.

 [1]: #instalacja-programu
 [2]: #instalacja-ciemnej-skorki
 [3]: #styl-pisania-kodu
 [4]: #pokazanie-ukrytych-plikow
