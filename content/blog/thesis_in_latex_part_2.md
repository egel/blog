Title:      Thesis in LaTeX - part 2
Date:       2014-10-19 12:21:49
Modified:   2014-10-19 10:21:49
Lang:       en
Status:     published
Category:   Self improvement
Tags:       latex, university


<div class="intro-article-image-md" markdown="1">
  ![LaTeX logo]({filename}/images/LaTeX_logo.png)
</div>
I assume that at the moment of reading this second part of writing thesis in
LaTeX you have red
[Thesis&nbsp;in&nbsp;LaTeX&nbsp;part&nbsp;1]({filename}thesis_in_latex_part_1.md)
and install required software. If you do, then perfect carry on, but if not you
should catch up.

I this part I will try to make some very basic introduction how to use LaTeX in
practice. But it is hard. Not by writing, because paper can take everything. The
real thing hides into a simple question how condense this knowledge in
acceptable for average person. You can not read this article for 5 days, because
you can read few book, far more detailed then my article in this time.

My main goal for this series is to assure and show you that creating thesis in
LaTeX is the best you can get in reasonable time. By the way "LaTeX is the de
facto standard for the communication and publication of scientific
documents."[ref]Get from official LaTeX webpage
<https://www.latex-project.org/>[/ref]

LaTeX can scare with its complex examples, but those examples are usually very
rare. In this part I will only guide you though the basics and point best
practices which I discovered during few years of writing. But it will be a very
good starting point.

## Creating basic document
TeX is a compiling type of text processor. In plain words that means its
generate from source files final product (whatever it is) and during this
process it creating some helping content/files to achieve final result.
So, do not panic if among your source files another will arise - that is norm
for LaTeX.

I recommend to start by creating new folder with some obvious name for you (and
you after a while). I would use `firstname_lastname_thesis`. This folder should
lay in location easy get, because you will we regularly use it. As a programmer
I usually use `~/workspace` as a container of my git projects, but `~/Desktop`
is also fine if you like mess on your desk ;)

So we have got folder location for your thesis


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
