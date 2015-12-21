Title:      Thesis in LaTeX - part 3
Date:       2015-04-06
Status:     published
Category:   Self improvement
Tags:       latex, university
Summary:    Making a title page of your thesis and talk about how to properly write with LaTeX syntax to dunch wrong code.


<div class="intro-article-image-md" markdown="1">
  ![LaTeX logo]({filename}/images/LaTeX_logo.png)
</div>

W tej części artykułu zajmiemy się przede wszystkim utworzeniem strony tytułowej dla naszej pracy dyplomowej. Powiemy także jak poprawnie pisać i formatować treść pracy korzystając z domyślnych (wbudowanych) komend oraz jak korzystać z innych, poprzez dołączanie nowych pakietów.

Zakładam, że na ten moment użytkownik ukończył lub chociaż zapoznał się z obiema poprzednimi częściami artykułu ([część 1][1] oraz [cześć 2][2]), a także posiada przygotowane środowisko pracy.

<!--more-->

<p style="clear: both;">
</p>

Czytelniku przeszedłeś już jedną z najtrudniejszych możliwych dróg jaką trzeba pokonać, aby stać się **LaTeX Ninja** - zainteresowałeś się nim oraz poświęciłeś swój czas, aby zrozumieć go lepiej. Tak więc i on (LaTeX) nie pozostanie Ci obojętny w tym wypadku, ponieważ dzięki temu okresowi czasu jaki mu poświeciłeś, on pozwoli Ci (odpowiednio do ilości poświęconego czasu) na bajecznie wygodną realizację nawet bardzo obszernych i skomplikowanych dokumentów.

Ale wracając do głównego założenia niniejszej części artykułu - utworzymy teraz stronę tytułową dla naszej pracy. Co prawda będzie to zajęcie ogromnie łatwe, tym bardziej jeśli tworzy się szablon od zupełnego zera, jednak po przeczytaniu i analizie treści zamieszczonych w tym artykule z powodzeniem będziesz mógł tworzyć nowe szablony lub dostosowywać istniejące do własnych potrzeb.

## Tworzenie strony tytułowej

Tworzenie strony tytułowej dla naszej pracy dyplomowej zaczniemy od zdefiniowania własnej klasy dokumentu. W poniższym przykładzie klasę tą ochrzciłem nazwą `uekthesis` z racji tego, że uczęszczam na Uniwersytet Ekonomiczny w Krakowie, stąd decyzja o wyborze implementacji była oczywista ;)

> Co prawda klasa którą będziemy wspólnie tworzyć jest domyślnie przygotowywana na wzór dla prac dyplomowych Uniwersytetu Ekonomicznego w Krakowie (w pełni zgodna z wymogami prac dyplomowych), jednak wszystko przygotowałem na tyle sprytnie, że zmiana domyślnych treści dla szablonu będzie wyjątkowo prosta.

Zacznijmy więc od budowy naszego pliku `uekthesis.cls` będącego sercem naszego dokumentu.

Plik ten jest dość obszerny, tak wiec umieszczanie wszystkich jego fragmentów bezpośrednio do artykułu jest bezcelowe (jednak nie ukrywam, że chciałbym omówić każą jego ważniejszą część). Aczkolwiek budowałem plik `uekthesis.cls` w taki sposób, aby był możliwie najprostszy do odczytania i zrozumienia przez innych użytkowników (nawet nie będących programistami). Dodatkowo każdy fragment jest skrupulatnie komentowany, wiec jest nikła szansa, że zgubisz się w nim drogi Czytelniku :)

Przejdźmy jednak do ważniejszych fragmentów pliku klasy `ukethesis.cls` i o dziwo, nie będę tu mówić bezpośrednio o kodzie, który wykonuje najważniejsze partie kodu w klasie, gdyż nie zamierzam obrażać Twojej inteligencji ;) - prostą analizę gotowego pliku możesz przeprowadzić samodzielnie (wystarczy jedynie trochę chęci).

Powiem jednak nieco o konfiguracji wspomnianej wyżej klasy, gdyż tyle wystarczy do bezproblemowego i wygodnego jej użytkowania, czy nawet dostosowania do wymogów prac na innych uczelniach i wydziałach.

Najważniejszymi rzeczami jakie należy wiedzieć na temat klasy `uekthesis.cls` to zmienne globalne jakich używam w dokumencie oraz specjalnie ustawienia opcji dla klasy.

> Tak wiem, wiem,...zmienne globalne to generalnie we współczesnym programowaniu praktycznie samo zło. LaTeX nie do języków typowo obiektowych (są oczywiście klasy, funkcje, zmienne - jednak filozofia ich programowania zupełnie odbiega od OOP) stąd uprosiciłem omawianą klasę na tyle na ile było to możliwe tak, aby nie spędzić zbyt dużo czasu na budowaniu samego pliku klasy, a także by zachować maksymalną czytelność dla użytkownika klasy. Zachęcam więc gorąco do współpracy nad tworzoną klasą [uekthesis][3] lub kompletnym przykładem gotowego dokumentu w moim repozytorium na Github [latex-thesis-example][4] :)

### Klasa uekthesis

Klasa uekthesis zawiera zestaw kilku opcji konfiguracyjnych pozwalających dostosować poszczególne partię dokumentu dla uzyskania pożądanego wyglądu.

Opcję należy wpisywać w głównym pliku dla naszego dokumentu. W naszym przypadku będzie to plik `main.tex`, natomiast linijka konfiguracji to oczywiście:

    \documentclass[nazwy_opcji_odzielone_przecinkami]{uekthesis}


czyli przykładowo:

    \documentclass[male, authorStatement, indexNumber, fileVersion, ]{uekthesis}


#### Opcje konfiguracji klasy uekthesis

*   `male` lub `female` - opcja ta ustawia konfigurację płci dla autora dokumentu i jest wykorzystywana w innych opcjach jeśli zachodzi w nich potrzeba personalizacji płci (np: `authorStatement`).
    Jeśli żadna z opcji nie jest sprecyzowana, domyślnie ustawia: `male`.

*   `twoside` - opcja ta ustawia konfigurację układu pracy na dwustronny. *Nie chodzi tu bynajmniej o wydruk dwustronny*, gdyż wydruk pracy, a jej układ to dwie zupełnie odrębne sprawy.
    Jeśli żadna z opcji nie jest podana, domyślnie ustawia: `oneside`.

*   `indexNumber` - opcja ta ustawia numer indeksu studenta. Wyświetlana jest na 1 stronie (stronie tytułowej), aby informować użytkownika z wersją dokumentu ma obecnie doczynienia (szczególnie pomocne dla autora oraz promotora). Opcja ta jest też bardzo pomocna, jeśli pracujesz nad pracą z jakimś systemem kontroli wersji (np: [Git][5]). W finalnej wersji pracy opcja ta powinna oczywiście zostać usunięta.
    Jeśli opcja nie została ustawiona, domyślnie jest wyłączona (Off).

*   `fileVersion` - opcja ta ustawia numer wersji dokumentu. Wyświetlana jest na 1 stronie (stronie tytułowej) zaraz obok numeru studenta, aby informować użytkownika nad z wersją dokumentu obecnie ma doczynienia (szczególnie pomocne dla pisarza, a także promotora).Dla finalnej wersji pracy oczywiście opcja ta powinna zostać usunięta.
    Jeśli opcja nie została ustawionia, domyślnie pozostaje wyłączona (Off).

*   `authorStatement` - opcja ta ustawia standardowe oświadczenie autora o samodzielnym wykonaniu pracy (często opcja ta wymagana jest przez uczelnie bezpośrednio w dokumencie pracy).
    Jeśli opcja nie została ustawiona, domyślnie pozostaje wyłączona (Off).

To by było na tyle z opcji konfiguracji wyglądu i zachowania klasy. Teraz zajmiemy się wspomnianymi wcześniej zmiennymi globalnymi pełniącymi funkcję bezpośredniej personalizacji klasy dla naszego dokumentu.

#### Zmienne globalne klasy uekthesis

Wiemy już, że zmienne globalne udostępnione w klasie `uekthesis` to forma personalizacji klasy naszego dokumentu. Dzięki tym zmiennym zdefiniujemy podstawowe informacje tj.: imię i nazwisko autora, uniwersytet, wydział, imię i nazwisko promotora, numer indeksu studenta oraz wiele, wiele innych danych.

Zacznijmy wiec od kompletnego kodu zamieszczonego w naszym pliku `main.tex` gdyż przejdziemy od ogółu do szczegółu. Same zmienne zostały dość intuicyjnie nazwane przeze mnie, wiec nie będzie większego problemu z odszyfrowaniem do czego służą, natomiast jeśli to by nie wystarczyło każda z nich okupiona jest komentarzem informacyjnym. Ważniejsze fragmenty omówię nieco niżej.

    %##############################################################################
    % Global variables !!!
    %
    % To zmiennne do modyfikacji przez użytkownika (nie trzeba ruszać klasy "uekthesis.cls")
    \globalFullAuthor{Maciej Sypień}    % Pełna nazwa autora pracy
    \globalShortAuthor{M. Sypień}       % Autor - zwięzła forma wydruku
    \globalFullTitle{Projekt i implementacja autorskiego systemu zarządzania treścią}  % Pełny tytuł pracy
    \globalShortTitle{Projekt i implementacja autorskiego CMS}  % Krótki, zwięzły tytuł pracy
    \globalFullUniversity{Uniwersytet Ekonomiczny w Krakowie} % Pełna nazwa uniwersytetu
    \globalShortUniversity{UEK}                           % Skrócona nazwa uniwersytetu
    \globalDepartment{Wydział Zarządzania}                % Wydział
    \globalDegreeprogramme{Informatyka Stosowana}         % Kierunek studiów
    \globalThesisType{Praca dyplomowa}                    % Typ pracy dyplomowej
    \globalSupervisor{prof. n. dr hab. Jana Iksińskiego}  % Promotor
    \globalAcknowledgements{Dla moich rodziców oraz najbliższych przyjaciół za niezłomną wiarę w~moje zwycięstwo.}   % Podziękowania
    \globalFileVersion{0.1.0}   % wersja pliku (przy włączonej opcji "fileVersion")
    \globalIndexNumber{123456}  % numer indeksu (przy włączonej opcji "indexNumber")
    \globalCity{Kraków}         % miasto
    \globalYear{2014}           % rok powstania pracy


Zacznijmy od tego, że definiujemy tu wszystkie zmienne, nawet te których nie wywołujemy w opcjach klasy. Taka praktyka jest wymagana przez notację LaTeXa. Jednak mimo, iż definiujemy je wszystkie, nie to oznacza, że będziemy ich wszystkich używać (założyłem, że nie każdy będzie miał ochotę użyć opcji np: `fileVersion`). Od tego co pokazujemy lub ukrywamy w pracy służą nam [opcje konfiguracji klasy uekthesis][6] :)

Wszystkie zmienne zostały wykorzystują notację `lowerCamelCase` oraz zostały wzbogacone przeze mnie przedrostkiem "global" przypominającym o jej zasięgu względem całej pracy. Przedrostek ten jest moim rozwiązaniem dla ujednolicenia notacji zmiennych i bynajmniej nie stanowi domyślnej notacji LaTeXa.

Większość ze zmiennych zawiera również ich skrócone odpowiedniki. Skrótowce te wykorzystywane są w miejscach gdzie nie można posłużyć się pełną nazwą (głównie ze względów typograficznych), wiec również należy pamiętać o ich zmienieniu/uzupełnieniu.

To by było na tyle z na tyle z konfiguracji klasy uekthesis - ...i nie było to takie trudne, prawda? Tyle opcji w zupełności wystarcza do pełnej personalizacji klasy, bez zbędnego zagnieżdżania się w strukturę kodu.

Osoby chętne do ulepszania projektu klasy, zachęcam gorąco do forkowania i współdzielenia mojego kompletnego [przykładu klasy uekthesis na Github][4] :)

## Praca z zewnętrznymi pakietami

LaTeX posiada szeroką game opcji konfiguracji tworzonych dokumentów. Od drobnych listów, przez krótkie dokumenty, po ogromnie i złożone prace lub książki.

Na popularnym pakiecie `graphicx` zademonstruje jak dołączyć ten lub dowolny inny pakiet do dokumentu, a także gdzie szukać i jak wykorzystać jego funkcjonalności.

Jednak aby móc zacząć korzystać z jakiegokolwiek pakietu (w tym przykładowego pakietu `graphicx`) należy na początku dołączyć deklarację jego użycia w *preabule dokumentu*. Stąd przechodzimy do naszego pliku `main.tex` i deklarujemy chęć jego użycia komendą `usepackage{}`. Fragment ten ilustruje poniższy kod:

    \documentclass[male, indexNumber, fileVersion, twoside, ]{uekthesis}
    \usepackage[utf8]{inputenc}
    ...
    \usepackage{graphicx}
    ...
    \begin{document}


Od tego momentu możemy używać w naszym dokumencie komend charakterystycznych dla pakietu `graphicx`. Jak widać jest to trywialnie proste :)

> Należy pamiętać, że aby móc dołączać nowe pakiety bezpośrednio w pliku `.tex`, muszą one być zainstalowane (oczywiście jednorazowo). System Windows posiada manager pakietów LaTeXa o nazwie *MikTeX*, który w aktualnych wersjach automatycznie dociąga potrzebne pakiety podczas kompilacji pliku. W systemie Linux Debian/Ubuntu można doinstalować wszystkie pakiety jedną wygodną komendą: `sudo apt-get install texlive-full`. Wspominałem o tym w [pierwszej części][1] artykułu.

### graphicx

To pakiet do wygodnego manipulowania grafiką w dokumencie. Posiada prostą konstrukcję budowy i nie powinien stanowić dużego wyzwania intelektualnego przy budowaniu komend z udziałem jego interfejsu.

#### Przykład 1.1

    \includegraphics[scale=0.5]{images/lion_1.jpg}


Ta krótka linijka dołącza do dokumentu obraz, a także skaluje go do 50% jego domyślnej wielkości, natomiast samo źródło obrazka pobiera ze ścieżki: `images/lion_1.jpg`.

#### Przykład 1.2

    \includegraphics[width=12cm]{images/lion_2.jpg}


Ta krótka linijka dołącza do dokumentu obraz o żądanej szerokości, w tym wypadku 12cm. Jest to bardzo przydatna opcja w szczególności, gdy chcemy uzyskać zawsze ten sam rozmiar zdjęcia bez względu na wielkość obrazu wejściowego.

> Oczywiście im większy obraz, tym lepsza jego jakość końcowa (gdyż zdjęcie ma określone wymiary), jednak zwiększenie jakości okupione będzie zwiększeniem wagi pliku wynikowego pracy.

Możliwe też są inne bardzo przydatne opcje zamiast przykładowych "12cm" umieścić szerokość strony poleceniem:

    \includegraphics[width=\textwidth]{images/lion_2.jpg}


Dzięku temu szerokość zdjęcia będzie zawsze równa 100% szerokości strony. Tutaj również trzeba uważać, ponieważ jeśli zdjęcie nie zostanie poprawnie przycięte może zasłonić całą stronę spychając tekst na margines.

#### Więcej przykładów

Po więcej przykładów zachęcam do zagłębienia się w artykuł na wikibooks na temat [dołączania grafiki do dokumentów LaTeXa][7]

Chodź wiki nie zawsze jest wiarygodnym i aktualnym źródłem informacji to w tym wypadku artykuł ten jest całkiem przyjemnie zbudowany.

## Dobre praktyki

Ten rozdział jest w rzeczywistości bardzo rozległym tematem, którego nie można zamknąć w kilku wąskich poradach (może kiedyś rozbuduje go na tyle by utworzyć z niego osobny, pełnoprawny artykuł).

Poniżej znajdziesz kilka dobrych praktyk przy tworzeniu rozległych dokumentów takich jak praca dyplomowa:

#### Dziel rozdziały na mniejsze pliki

Każdy z rozdziałów powinien mieć swój odrębny plik. Dzięki temu możesz w łatwy sposób manipulować ich kolejnością z pliku głównego (u nas był to `main.tex`), a także skrócić kompilację, jeśli jakiś ukończony rozdział zawiera rozbudowaną logikę (np: dynamiczne tworzenie modeli graficznych dla związków chemicznych).

#### Tworzenie akapitów - treść zasadnicza

Tworzenie nowego akapitu zaczynaj zawsze od nowej linii, natomiast dla kontynuowania myśli z poprzedniego akapitu stosuj dodatkowo komendę `\noindent` usuwającą domyślnie tworzone wcięcie w tekście (Za to odpowiedzialny jest pakiet `indentfirst`). Takie praktyki zapewnią lepsze układanie i dostosowanie treści do całej zawartości dokumenty (w tym tabel, obrazków, wzorów matematycznych ect.)

Przykład poniżej:

    Oto bardzo długi akapit zwierający jedną określoną myśl autora \dots

    A o to kolejny, również szalenie długi akapit zawierający inną, kolejną myśl autora.

    \noindent Natomiast to również jest kolejny akapit, jednak ten dzięki zastosowaniu komendy \texttt{\noindent} nie zawiera domyślnie tworzonego wcięcia. Symbolizuje kontynuacje myśli z poprzedniego akapitu.


#### Używaj wcięć dla lepszego zobrazowania zawartości

To zasada którą tyczy się bardziej programowania aniżeli zwyczajnego pisania. Jednak LaTeX nie należy do *zwykłych* systemów pisania.

Wcięcia mają pomóc Ci w orientacji w Twoim dokumencie, gdyż w swojej notacji LaTeX wykorzystuje wiele znaków specjalnych, a między innymi są znaki `{}` czy `[]`. Znaki te grupują treści i niektóre ich kombinacje warto oddzielać do siebie, inne zaś mogą być pisane jednym ciągiem.

Przykład dla lepszego zobrazowania sytuacji:

    To jest zwykły tekst który zwieraz \textbf{pogrubioną czcionkę}, ale również tą pisaną \textit{kursywą}. Natomiast ten tekst będzie {\large adekwatnie większy}, a ten {\small odpowiednio mniejszy}.

    Poniżej pojawi się drobna tabela:

    \begin{table}[t]
        \begin{tabular}{l|c}
        Imię    & Nazwisko          \\ \hline \hline
        Stefan  & Batory            \\ \hline
        Juliusz & Słowacki          \\ \hline
        Maria   & Skłodowska-Curie  \\ \hline
        \end{tabular}
    \caption{Podpis dla mojej prostej tabelki.}
    \label{moja-prosta-tabelka}
    \end{table}


#### Zamieniaj tabulatory na spacje

Praktyka ta pozwala na wygodną edycję tekstu w zarówno w Twoim edytorze tekstu (broń Boże nie mówię tu o Microsoft Word!) jak i na innych prostych edytorach tekstu. Każdy edytor posiada inną domyślną interpretację tabulatorów na spacje - dla jednych to 2, 4 lub nawet 8 spacji. Stąd ładnie wyglądający tekst w Twoim edytorze może u promotora wyglądać jak "Koszmar z ulicy wiązów" ;) (tym bardziej jeśli promotor ma dodatkowo zacięcie programistyczne i wie jak powinien wyglądać dobry kod).

* * *

Myślę, że jak na początkujący poziom trudności artykułu, tyle powinno wystarczyć. Ze swojej strony dziękuje za uwagę i pozostanie ze mną do samego końca.

Pełny przykład dla niniejszego artykułu odnajdziesz w linku poniżej. Zawiera kompletny, działający kod.

<a href="https://www.sharelatex.com/project/543abd9e69870b1d3e39c3f8" title="Pełny przykład online" class="btn btn-primary">Pełny przykład online</a>

* * *

W tym miejscu zapraszam Cię na kolejną i prawdopodobnie już ostatnią, 4 część tworzenia dokumentu pracy dyplomowej, a w nim:

*   omówienie istniejących systemów bibliograficznych stosowanych dla języka polskiego;
*   dokonamy pełnej implementacji systemu bibliograficznego `biblatex` + `biber` dla naszego dokumentu;
*   a także dołączymy na końcu dokumentu listy: pozycji bibliograficznych, rysunków oraz tabel.

Będzie to jeden z najciekawszych artykułów w całej serii, gdyż prac z gotowymi przykładami implementacji połączenia `biblatex` i `biber` jest jak na lekarstwo (w szczególności polskich prac). Na dzień publikacji niniejszego artykułu, powyższe połączenie wydaje się najskuteczniejszym rozwiązaniem do przechowywania i formatowania bibliografii - tak, więc już teraz gorąco zapraszam :)

 [1]: http://blog.egel.pl/praca-dyplomowa-w-latex-cz1/
 [2]: http://blog.egel.pl/praca-dyplomowa-w-latex-cz2/
 [3]: https://github.com/egel/uek-latex-thesis-class
 [4]: https://github.com/egel/latex-thesis-example
 [5]: http://git-scm.com/
 [6]: #opcje-konfiguracji-klasy-uekthesis
 [7]: http://en.wikibooks.org/wiki/LaTeX/Importing_Graphics
