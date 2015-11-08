Title:      Triki w LaTeXu
Date:       2013-10-22 
Modified:   
Status:     Published
Category:   
Tags:       LaTeX
Summary: 


Uwaga: ten post to nie jest kurs nauki LaTeX'a. Jeżeli szukasz kursu i/lub opracowania dotyczącego poszczególnych komend to ściągnij i przeczytaj na początek to i to.

## Jak zrobić rozdział bez numeru?

    :::latex
    \chapter*{tytuł}
    

## Jak zrobić stronę poziomą?

    :::latex
    \usepackage{lscape}
    ...
    \begin{landscape}
    \end{landscape}
    

## Jak wprowadzić ukośnik \ bez użycia trybu matematycznego?

    :::latex
    \textbackslash
    

## Czemu po kompilacji nowego źródła plik wygląda nadal tak samo (lub dalej te same błędy)?

Usuń plik AUX oraz produkt kompilacji (DVI/PDF) i spróbuj skompilować ponownie. Plik nie może być pusty (musi być jakikolwiek znak który będzie się wyświetlał po skompilowaniu, nie może być sama preambuła)

## Jak zabronić złamania słowa przez funkcję dzielenia wyrazów?

    :::latex
    \mbox{słowo}
    

## Jak uzyskać ilość stron w dokumencie (aby zrobić numer strony w formacie x/y)?

    :::latex
    \usepackage{lastpage}
    

Numer ostatniej strony zwróci \pageref{LastPage} - uwaga na wielkość znaków. Należy kompilować minimum 2x żeby złapało.

## Jak wstawić przypisy końcowe?

    :::latex
    \usepackage{endnotes}
    

Przypis definiujemy:

    :::latex
    \endnote{xxx}
    

W miejscu wstawienia przypisów:

    :::latex
    \theendnotes
    

## Jak wstawić niemiecki umlaut?

np. `\"o` Z pakietem [german]{babel} wystarczy `"o`.

## Jak wprowadzić odstęp poziomy i pionowy?

    :::latex
    \hspace{odleglosc}
    \vspace{odleglosc}
    

## Jak ustawić szerokość obrazka względnie do szerokości tekstu?

    :::latex
    \includegraphics[0.5\textwidth]{plik.eps}
    

## Darmowy konwerter do formatu EPS?

GIMP, ImageMagick (polecenie convert)

## Jak zmienić nazwy Tablica-Tabela, Rysunek-Rycina, Bibliografia - Spis literatury itd?

Np. `\renewcommand*{\figurename}{Rys.}` Zamiast `\figurename` można wpisać inne polecenia. Lista wyciagnięta z dokumentacji pakietu babel:

    :::latex
    \def\prefacename{Przedmowa}%
    \def\refname{Literatura}%
    \def\abstractname{Streszczenie}%
    \def\bibname{Bibliografia}%
    \def\chaptername{Rozdzia\l}%
    \def\appendixname{Dodatek}%
    \def\contentsname{Spistre\'sci}% spis treści
    \def\listfigurename{Spisrysunk\'ow}% spis rysunków
    \def\listtablename{Spistablic}% spis tablic
    \def\indexname{Indeks}%
    \def\figurename{Rysunek}%
    \def\tablename{Tablica}%
    \def\partname{Cz\eob{}\'s\'c}% część
    \def\enclname{Za\l\aob{}cznik}% załącznik
    \def\ccname{Kopie:}%
    \def\headtoname{Do}%
    \def\pagename{Strona}%
    \def\seename{Por\'ownaj}% porównaj
    \def\alsoname{Por\'ownajtak\.ze}% porównaj także
    \def\proofname{Dow\'od}% dowód
    \def\glossaryname{Glossary}
    

## Jak wstawić linię poziomą w tekście?

    :::latex
    \hrule
    

## Jak wznowić numerowanie z poprzedniej listy?

    :::latex
    \usepackage{enumitem}
    ...
    \begin{enumerate}[resume]
    

## Jak zmienić styl numeracji rozdziałów, list itd? Jak dodać kropkę do numeru rozdziału?

Np. `\renewcommand{\thechapter}{\arabic{chapter} }` Komendy: `\thefigure` `\thetable` `\thepage` `\thepart` `\the(subsub)section` `\theequation` `\the(sub)paragraph` Liczniki nazywają się podobnie, np chapter. Formaty liczb: arabic, roman, Roman, alph, Alph W listach numerowanych -przykład jak zrobić listę alfabetyczną:

    :::latex
    \renewcommand{\labelenumi}{\Alph{enumi}.} %poziom 1
    \renewcommand{\labelenumii}{\Alph{enumi}.\alph{enumii}} %poziom 2
    

## Jak zmienić numer strony na inny niż wynika z kolejności?

    :::latex
    \setcounter{page}{numer}
    

## Jak wyłączyć dzielenie wyrazów?

    :::latex
    \usepackage{hyphenat}
    ...
    \nohyphens{blok tekstu}
    

## Jak pokolorować komórki w tabeli?

    :::latex
    \usepackage[table]{xcolor}
    \cellcolor[gray]{0.9}
    

## Jak scalić komórki w tabeli?

poziomo: \multicolumn{ile_kolumn_scalić}{krawędzie i wyrównanie}{zawartość} Np. \multicolumn{5}{|c|}{NAGŁÓWEK} pionowo (wymaga pakietu multirow): \multirow{ile}{szerokosc}{zawartość} zamiast szerokości można wpisać * - samo się dostosuje.

## Jak przełamać równanie na 2 linie?

    :::latex
    \begin{eqnarray}
    linia 1 xxx \nonumber\\
    linia2
    \end{eqnarray}
    

Aby wyrównać linie wyrażenia tak aby np znaki równości w każdej linii były pod sobą: znaki, względem których wyrównujemy bierzemy w każdej linijce między symbole &; np. &=& .

## Jak tymczasowo wyłączyć obrazki w celu przyspieszenia kompilacji?

do `\documentclass` dodać parametr `draft`.

## Jak umieścić w nagłówku tytuł rozdziału?

Formatujemy nagłówek pakietem fancyhdr. Następnie używamy poleceń: `\leftmark` – zwraca napis ROZDZIAŁ N. TYTUŁ `\rightmark` - NUMER. TYTUŁ `\thesection` - numer sekcji Aby wyłączyć pisanie kapitalkami `\nouppercase{xxx}`
