Title:      Praca dyplomowa w LaTeXu - cz. 1
Date:       2014-10-12 19:00:05
Modified:   2014-10-12 17:00:05
Status:     inherit
Category:
Tags:
Summary:


<div style="float: left;">
  <img class="alignleft size-medium wp-image-626" alt="LaTeX_logo" src="http://blog.egel.pl/wp-content/uploads/2013/05/LaTeX_logo-300x124.png" width="300" height="124" />
</div>

**LaTeX** (wymowa: lejtech) - rozszerzona wersja języka TeX o dodatkowe zestawy mark - to oprogramowanie stworzone z myślą o profesjonalnym składowaniu tekstu, który z początku może przerazić ilością różnych możliwości, lecz jeśli poświęci się chwilę na poznanie go nieco bliżej (nie jest trudny, jeśli przykładowo rozumiesz idee języka HTML) to Twoje dokumenty zyskają nowego życia.

<!--more-->

<p style="clear: both;">
</p>

Przyznam szczerze, pisząc pierwszy rozdział swojej pracy licencjackiej w edytorze **Word** było to bardzo wygodne i szybkie rozwiązanie, ale pisanie dłuższych dysertacji może być kłopotliwe. Edytory takie jak Word czy Libre Office to świetne programy do małych i krótkich tekstów - jednak w moim odczuciu są toporne przy większych publikacjach.

Może nie być to oczywiste dla wszystkich, lecz Word to program typu **WYSIWYG** (What You See Is What You Get, tłum. dostajesz to co widzisz). WYSIWYG oznacza to, że każdy znak jaki postawimy w dokumencie (w tym również *znaki białe* np: spacje, tabulatory) są wyświetlane na ekranie. Jeśli więc przez pomyłkę wciśniemy wielokrotnie spację, to w na wydruku strony również pojawi się wielokrotnie powtórzony odstęp. Przy skupieniu się na krótkim tekście 1-3 stron człowiek bez problemu wyłapie wzrokiem niedoskonałości poprawiając je bardzo szybko i efektownie - do tego WYSIWYG jest idealny. Jednak przy pisaniu dłuższej publikacji, książki czy pracy dyplomowej uwaga autora powinna się skupić wyłącznie na treści, a nie dodatkowo na wyłapywaniu błędów.

Często podczas pisania własnej pracy dyplomowej (jeszcze w Wordzie):

*   Przypadkowa zmieniana lub usunięcie stylu (i cały tekst ulegał deformacji),
*   Wykorzystywanie ogromnej ilości różnych stylów z czego trzeba większość zapamiętać, który do czego służy (a co jeśli sięgniemy do pracy po pewnym odstępie czasu? ...i weź tu nie popełnij błędu),
*   Naciśnięcie przypadkowego przycisku lub skrótu przez nieuwagę zmienia całość tekstu w dziwny "twór",
*   Niezidentyfikowane zaginięcie lub zmodyfikowanie spisu treści, przypisów, bądź bibliografii,

powodowały u mnie dużą frustrację podczas pisania. Zamiast pisania treści pracy skupiałem się na tym, że *coś* zdeformowało mój tekst w dziwny sposób i zamiast pisać pracę to poprawiałam dokument tak, aby praca powróciła do poprzedniego stanu. Alternatywą było jeszcze cofanie (CTRL + Z) ale gdy błąd dostrzegłem zbyt późno zmiany musiałem wykonywać ręcznie.

Nie to jednak było powodem mojej późniejszej zmiany ogólnego sposobu składowania tekstu. Głównym powodem zmiany była prostota i profesjonalizm LaTeXa z jakim można uzyskać tekst wynikowy. Nie bez powodu TeX/LaTeX jest wykorzystywany przy profesjonalnym składowaniu tekstu w wydawnictwach.

LaTeX kładzie nacisk na treść dokumentu odsuwając wygląd na dalszy plan, który można zrealizować pod koniec pisania pracy (lub z początku, jak kto woli - chodź jest nieco trudniej, bo jeszcze nie wiemy jakie elementy zastosujemy w pracy) bez dodatkowego stresu.
Dodatkowym atutem jest to, że nie ma znaczenia w jakim programie do edycji tekstu piszemy - możemy korzystać z dowolnego, ulubionego edytora tekstu.

> Ale by była jasność w kwestii edytora tekstu - nie mówię tu o programach takich jak Libre Office, Microsoft Word, ect. Mam na myśli raczej program nie zawierający dedykowanych modułów formatowania tekstu jak np.: Notepad++, Sublime, Vim. Więcej na ten temat możesz dowiedzieć się czytając o [SDI oraz MDI][1]

Plusów LaTeXa można by wymieniać w nieskończoność, ponieważ odkąd lepiej poznałem to środowisko należę do grona jego dużych zwolenników - proszę nie mylić z fanatykami.

Jednak w gąszczu samych plusów są również i minusy - niestety.
Piszę "niestety" z tego względu, że **nie jest to styl pisania dla każdego**, w szczególności dla tych nie lubiących programistycznych "robaczków", a LaTeX chodź niewielkim stopniu ale taki jest.

Można oczywiście znaleźć odpowiednie środowisko programistyczne będące na styku świata Worda i LaTeXa jak np: program [Lyx][2], program ułatwiający pracę z LaTeX ze względu na swoje podobieństwo do wyglądu Worda czy Libre Office'a, ale nawet mimo tego Lyx jakoś mnie nie zdołał przekonać się do siebie - chodź był moment że usilnie starałem się go nauczyć.

Mój wybór padł na program [Texmaker][3].
Moim skromnym zdaniem to ideał programu w 100% spełniających to do czego został stworzony - prostota oraz wieloplatformowość programu połączona z ogromnymi możliwościami edycyjnymi przystosowanymi do pisania w LaTeXu zaskarbiła sobie moją uwagę.
Chodź samym wyglądem może delikatnie przestraszyć użytkowników na co dzień nie obcujących z pisaniem programów lub skryptów (jednolity, sztywny tekst z cyferkami na boku), to mimo wszystko po pewnym czasie przyzwyczajenie może odepchnąć pozostałych konkurentów na długie miesiące ;)

Tworzenie dokumentu w LaTeX jest niezwykle łatwe, chodź słowo "łatwy" jest tu kwestią dyskusyjną, ponieważ każda osoba posiada różny poziom szybkości i łatwości nauki. Sam LaTeX jest podobny do języków meta-znaczników jak HTML czy XML. Wystarczy poznać kilka prostych instrukcji i naturalnych zwyczajów rodem z prac pisanych na kartce zeszytu, aby zacząć pisać wspaniałe dokumenty.

## Instalacja niezbędnego oprogramowania (lub wersja online)

Zanim jednak przejdziemy do właściwego pisania pracy, musimy zaopatrzyć się w odpowiednie oprogramowanie.
Będą nam potrzebne:

*   [TexLive][4] (Linux) lub [MikTeX][5] (Windows)
*   [Texmaker][3]

### LaTeX Online

Jeśli jednak nie chcesz bezpośrednio instalować całego oprogramowania związanego z LaTeXem na swoim komputerze to możliwe, że zainteresują Cię możliwości tworzenia projektów bezpośrednio w przeglądarce, a także szybkiego współdzielenia projektu czy udostępnianie go innym.

W tym momencie serwisami godnymi polecenia są:

1.  [Sharelatex.com][6] - genialny portal do pisania początkujących oraz abrdzo zaawansowanych dokumentów LaTeXa.
2.  [Writelatex.com][7] - znakomity serwis do pisania dokumentów LaTeXa.

Tak więc jeśli nie chcesz marnować czasu na instalowanie całego oprogramowania związanego z LaTeXem, to wypróbowanie któregoś z powyższych portali jest prawdopodobnie najlepszym rozwiązaniem dla Ciebie :)

### Linux Ubuntu

Instalacja obu programów to jedna krótka komenda wykonana w terminalu:

    sudo apt-get install texlive-full texmaker


W powyższej komendzie instalujemy co prawda wszystkie możliwe pakiety biblioteki [TexLive][4] (ok. 1,5GB) - to dość dużo, jak na większość bibliotek, ale to działanie spowoduje, że nie będą tak często wyskakiwać błędy typu *brak wymaganej biblioteki* - a ze swoich początków w LaTeXu wiem, że to częsty błąd występujący przy początkowych kompilacjach dokumentu.

### Windows

W systemie Windows sprawa nie jest już taka szybka i prosta (jako że jestem zwolennikiem Linuksa), ale jest równie łatwa do ogarnięcia ;)

Bibliotekę *texlive* w Windows reprezentuje program o nazwie [MikTeX][5].

**MikTeX**
:   to w dużym skrócie zbiór różnych bibliotek zebranych w jeden wygodny instalator. Wygodną nowością w MikTeX dla systemu Windows jest automatyczne doinstalowanie pakietów nie zawartych w domyślnej instalacji (zwykle nieco dłużej trwa sama kompilacja, ponieważ w tle są pobierane i instalowane pakiety).

Texmaker można również pobrać ze [strony producenta][3] i zainstalować poprzez prosty instalator.

*Kolejność instalacji programów nie ma prawdopodobnie znaczenia, ale z Windowsem to nigdy nie wiadomo więc lepiej jest zainstalować na początek biblioteki, a następnie Texmaker'a.*

* * *

A już wkrótce, w kolejnej [2 części][8] przedstawię Wam proces utworzenia dokumentu w LaTeXu.

 [1]: http://technology.blurtit.com/114838/what-is-a-basic-difference-between-a-notepad-and-microsoft-word
 [2]: http://www.lyx.org/
 [3]: http://www.xm1math.net/texmaker/
 [4]: https://www.tug.org/texlive/
 [5]: http://miktex.org/
 [6]: http://www.sharelatex.com/
 [7]: https://www.writelatex.com/
 [8]: http://blog.egel.pl/praca-dyplomowa-w-latex-cz2/
