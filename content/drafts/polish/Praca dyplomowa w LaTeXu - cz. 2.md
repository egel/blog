Title:      Praca dyplomowa w LaTeXu - cz. 2
Date:       2014-10-19 12:21:49
Modified:   2014-10-19 10:21:49
Status:     inherit
Category:   
Tags:       
Summary: 


<div style="float: left;">
  <img class="alignleft size-medium wp-image-626" alt="LaTeX_logo" src="http://blog.egel.pl/wp-content/uploads/2013/05/LaTeX_logo-300x124.png" width="300" height="124" />
</div>

Zakładam, że w tym momencie użytkownik ukończył lub chociaż zapoznał się z [1 częścią artykułu][1], a także pobrał i zainstalował niezbędne oprogramowanie (tj. TexLive lub MikTeX oraz edytor tekstu).

<!--more-->

<p style="clear: both;">
</p>

## Tworzenie dokumentu

Tworzymy w dowolnym miejscu (dla przykładu na pulpicie) folder o nazwie *magisterka*, *praca dyplomowa* lub cokolwiek innego sensownego. W tym nowo utworzonym folderze będziemy umieszczać wszystkie pliki związane z pracą. W głównej mierze te z rozszerzeniem `.tex`, lecz również pojawią się inne (tj. `.bib`, `.cls`, `.sty`) ale nie zaprzątajmy sobie tym głowy w tej chwili.

> Pliki umieszczamy w osobnym folderze z tego względu, że podczas kompilacji do pliku wynikowego będą tworzyły się dodatkowe pliki pomocnicze do uzyskania ostatecznej formy np: PDF.

Warto zapamiętać plik z rozszerzeniem `.tex`, ponieważ jest on o tyle istotny, iż stanowi podstawę (w głównej mierze treść) naszego dokumentu. To w nim lub plikach z tym samym rozszerzeniem będziemy pisać kolejne rozdziały naszej pracy.

Przykładowo główny plik naszego dokumentu będzie się nazywać `dokument.tex`, natomiast ze względu na przyszłe rozrastanie się tego pliku kolejne rozdziały umieścimy w nowych plikach z tym samym rozszerzeniem tj. `chap_rozdzial_1.tex`, `chap_rozdzial_2.tex`, `chap_rozdzial_3.tex`... i tak dalej - zasada jest prosta :)

W nazwach plików dobrze jest utworzyć na początku nazwy "wskaźnik" do tego czym jest zawartość pliku (np: **chap_**, od ang. *chapter*) - pomaga to w późniejszej orientacji w posiadanych plikach oraz bezpośrednio w imporcie konkretnych rozdziałów już w pracy.

> Podczas kompilacji (czasem kilkukrotnej w przypadku posiadania dodatkowo bibliografii) nasz program będzie tworzyć inne niezbędne pliki służące generowaniu pliku wynikowego (np.: PDF), a przy wielu różnych plikach których nie znamy, bądź nie rozumiemy do czego służą, łatwo się pogubić, stąd ważna jest pewna ustalona struktura pracy.

### Preambuła i treść właściwa

Każdy nowy dokument czy to artykuł (ang. *article*), czy raport (ang. *report*), czy może książka (ang. *book*) - jest kilka różnych gotowych schematów - składa się standardowo z tak zwanej *preambuły* oraz *treści właściwej*.

**Preambuła**
:   to zestaw reguł z którymi program musi się zapoznać zanim zacznie tworzyć nasz dokument.

**Treść właściwa**
:   to miejsce w którym korzystając z odpowiednich poleceń układamy treść w dokumencie.

Standardowa, prosta preambuła (niekoniecznie dla prac dyplomowych) wygląda podobnie jak poniżej:

    \documentclass[12pt, oneside, a4paper]{report}
    \usepackage[OT4, plmath]{polski}                % definicja użycia platex
    \usepackage[utf8]{inputenc}                     % kodowanie na UTF-8
    \usepackage[OT4]{fontenc}
    \usepackage{url}
    \title{Projekt i implementacja autorskiego systemu zarządzania treścią}
    \author{Maciej Sypień}
    \date{\today}
    

Najczęściej preambułę wstawia się w głównym pliku naszej pracy, czyli w naszym przypadku będzie to plik `main.tex`.  
Rozdziały będą zawierać jedynie treść właściwą (bez preambuły), ponieważ będą włączane bezpośrednio do głównego dokumentu.

Warto wspomnieć coś o klasach. Klasa to w dużym skrócie zestaw reguł definiujących jak będzie w dużej mierze wyglądał nasz dokument końcowy. LaTeX zawiera już wstępnie zdefiniowane klasy przykładowo kilka z nich to wspomniane wcześniej:

*   book
*   report
*   article
*   letter

Dość dobrze obrazuje to linijka `\documentclass[12pt, oneside, a4paper]{report}` w której wyraźnie napisana jest definicja klasy `report` oraz jej opcjonalne argumenty jak czcionka, rodzaj druku, czy rozmiar papieru wynikowego papieru.

To tylko niewielka część z szerokiej gamy dostępnych opcji, ponieważ każda z tych klas (book, report, etc.) może zawierać te same opcjonalne argumenty ale również i inne (nowe) nie zdefiniowane w żadnej z klas podstawowych. Bynajmniej te słowa nie są po to, aby przestraszyć czytelnika, lecz ku przestrodze, że warto czasem zapoznać się z dokumentacją używanej klasy. Natomiast jeszcze inną rzeczą jest fakt, że często nowo tworzone klasy bywają bardzo kiepsko udokumentowane i zwykle ze względu na brak czasu twórcy (style potrzebne do jednego lub kilku dokumentów i na tym koniec).

Druga część dokumentu to treść właściwa. Z punktu pisarza jest ona najważniejsza, gdyż zawiera treść widoczną później w pliku wynikowym. Owa cześć pliku jest jedną z najprostszych do definiowania ponieważ wygląda jak przykładzie poniżej:

    \begin{document}
    \maketitle
    
    \begin{abstract}
    Dokument ten prezentuje kilka zasad składu tekstu w~systemie \LaTeX. 
    \end{abstract}
    
    
    \chapter{Nasz pierwszy rozdział}
    % pierwsza sekcja
    \section{Tekst}\label{sec:tekst}
    \LaTeX\ ułatwia autorowi tekstu zarządzanie numerowaniem sekcji, wypunktowaniami oraz odwołaniami do tabel, rysunków i~innych elementów. W~łatwy sposób możemy się odwołać do wzoru \ref{eqn:wzor1}.
    
    % sekcja
    \section{Matematyka}\label{sec:matematyka}
    Poniższy wzór prezentuje możliwości \LaTeX\ w~zakresie składu formuł matematycznych. Wzory są numerowane automatycznie, podobnie jak inne elementy o~których mowa w~sekcji~\ref{sec:tekst}.
    
    \begin{equation}
        E = mc^2,
        \label{eqn:wzor1}
    \end{equation}
    
    gdzie
    
    \begin{equation}
        m = \frac{m_0}{\sqrt{1-\frac{v^2}{c^2}}}.
    \end{equation}
    
    % --------------------------------------
    
    \chapter{Nasz drugi rozdział}
    Bardzo długa treść rozdziału drugiego.
    
    \section{Sekcja rozdziału drugiego}
    \label{sec:sekcjaRozdzialuDrugiego}
    Bardzo długa treść sekcji rozdziału drugiego.
    
    \subsection{Podsekcja sekcji rozdziału drugiego}
    \label{subsec:podsekcjaRozdzialuDrugiego}
    Bardzo długa treść podsekcji rozdziału drugiego.
    
    % --------------------------------------
    
    \chapter{Nasz trzeci rozdział}
    Bardzo długa treść rozdziału trzeciego.
    
    \section{Sekcja rozdziału trzeciego}
    \label{sec:sekcjaRozdzialuTrzeciego}
    Bardzo długa treść sekcji rozdziału trzeciego.
    
    \subsection{Podsekcja sekcji rozdziału trzeciego}
    \label{subsec:podsekcjaRozdzialuTrzeciego}
    Bardzo długa treść podsekcji rozdziału trzeciego.
    
    \end{document}
    

Powyższy fragment stanowi *treść właściwą* dokumentu i jak z pewnością czytelnik już zauważył, treść właściwa rozpoczyna fraza `\begin{document}` i kończy `\end{document}`. Jednak jeden duży plik może być trudny do edycji przy dużej ilości zawartego w nim tekstu. Przejdźmy więc do podziału jednego spójnego pliku tekstowego na mniejsze, osobne fragmenty. Natomiast znaczenie poszczególnych znaków oraz fraz zostaną omówione już w kolejnej 3 części :)

### Podział na osobne pliki

Jak wspomniałem wyżej, domyślnie interesuje nas podział dokumentu na konkretne rozdziały tak, aby każdy rozdział znajdował się w osobnym pliku.

Plik `dokument.tex` powinien wyglądać wtedy następująco:

    \documentclass[12pt, oneside, a4paper]{report}
    \usepackage[OT4, plmath]{polski}                % definicja użycia platex
    \usepackage[utf8]{inputenc}                     % kodowanie na UTF-8
    \usepackage[OT4]{fontenc}
    \usepackage{url}
    \title{Projekt i implementacja autorskiego systemu zarządzania treścią}
    \author{Maciej Sypień}
    \date{\today}
    
    \begin{document}
    \maketitle
    
    \begin{abstract}
    Dokument ten kilka podstawowych zasad składu tekstu w~systemie \LaTeX. 
    \end{abstract}
    
    \tableofcontents
    \clearpage
    
    \include{chap_wstep}
    \include{chap_rozdzial_1}
    \include{chap_rozdzial_2}
    \include{chap_rozdzial_3}
    
    \end{document}
    

Jak widać główny plik naszej przyszłej pracy jest prosty, przejrzysty i czytelny. Każdy z rozdziałów jest dołączany poprzez komendę `include{}`, jak zapewne zauważyłeś drogi czytelniku w przykładzie brak pełnej nazwy pliku (tj. rozszerzenia `.tex`), LaTeX dzięki swojej "magii" nie potrzebuje podawania rozszerzenia przy dołączaniu kolejnych plików z treścią. Jest to dość wygodne bo minimalnie skraca nazwę naszych rozdziałów.

Wracając do naszych rozdziałów. Każdy z nich rozpoczyna się zupełnie zwyczajnie, tak jakbyśmy dalej pisali w tym samym dokumencie (przed rozdzieleniem na osobne pliki). Dla przykładu poniżej podaje kody źródłowe dla lepszego zobrazowania tej sytuacji :)

Prolog, **chap_prolog.tex**:

    \chapter{Wstęp}
    Tu będzie się znajdować wstęp do naszej bardzo obszernej pracy ;)
    

Plik pierwszy, **chap_rozdzial_1.tex**:

    \chapter{Nasz pierwszy rozdział}
    % pierwsza sekcja
    \section{Tekst}\label{sec:tekst}
    \LaTeX\ ułatwia autorowi tekstu zarządzanie numerowaniem sekcji, wypunktowaniami oraz odwołaniami do tabel, rysunków i~innych elementów. W~łatwy sposób możemy się odwołać do wzoru \ref{eqn:wzor1}.
    
    % sekcja
    \section{Matematyka}\label{sec:matematyka}
    Poniższy wzór prezentuje możliwości \LaTeX\ w~zakresie składu formuł matematycznych. Wzory są numerowane automatycznie, podobnie jak inne elementy o~których mowa w~sekcji~\ref{sec:tekst}.
    
    \begin{equation}
        E = mc^2,
        \label{eqn:wzor1}
    \end{equation}
    
    gdzie
    
    \begin{equation}
        m = \frac{m_0}{\sqrt{1-\frac{v^2}{c^2}}}.
    \end{equation}
    

Plik drugi, **chap_rozdzial_2.tex**

    \chapter{Nasz drugi rozdział}
    Bardzo długa treść rozdziału drugiego.
    
    \section{Sekcja rozdziału drugiego}
    \label{sec:sekcjaRozdzialuDrugiego}
    Bardzo długa treść sekcji rozdziału drugiego.
    
    \subsection{Podsekcja sekcji rozdziału drugiego}
    \label{subsec:podsekcjaRozdzialuDrugiego}
    Bardzo długa treść podsekcji rozdziału drugiego.
    

Plik trzeci, **chap_rozdzial_3.tex**

    \chapter{Nasz trzeci rozdział}
    Bardzo długa treść rozdziału trzeciego.
    
    \section{Sekcja rozdziału trzeciego}
    \label{sec:sekcjaRozdzialuTrzeciego}
    Bardzo długa treść sekcji rozdziału trzeciego.
    
    \subsection{Podsekcja sekcji rozdziału trzeciego}
    \label{subsec:podsekcjaRozdzialuTrzeciego}
    Bardzo długa treść podsekcji rozdziału trzeciego.
    

Jak widać podział naszego jednego pliku nie przyniósł, aż tak epickiego rezultatu jaki mogliśmy się spodziewać, lecz to z tego względu, że samej treści było w nim niewiele. Jednak podział jednego dużego pliku na mniejsze jest szalenie pomocny w przypadku opracowywania długich prac. Pozwala na usystematyzowanie pracy oraz lepszą organizację podczas pisania np: gdy chcemy odłączyć jakiś rozdział wystarczy że w naszym głównym pliki zakomentujemy linijkę (`\include{}`) dołączającą określony fragment i gotowe.

<a href="https://www.sharelatex.com/project/543aad2f69870b1d3e39c26b" title="Pełny przykład online" class="btn btn-primary">Pełny przykład online</a>

Myślę że to na tyle w tej części i dziękuje Wam za uwagę.

* * *

Ale, ale... Drogi Czytelniku, jeśli nie zraziłeś się jeszcze do LaTeXa i masz ochotę poznać go nieco dokładniej zapraszam Cię już teraz do kolejnej 3 odsłony pisania pracy dyplomowej z LaTeX (która ukaże się już niebawem), a pojawi się w niej między innymi:

*   omówienie poszczególnych znaczników i fraz wraz z przykładami; 
*   dodawanie oraz stosowanie nowych pakietów;
*   podstawowe **dobre praktyki** tworzenia dokumentów w LaTeX;
*   a także stworzymy stronę tytułową dla naszej pracy.

...tak więc będzie dużo dobrej zabawy ;)

 [1]: http://blog.egel.pl/praca-dyplomowa-w-latex-cz1/
