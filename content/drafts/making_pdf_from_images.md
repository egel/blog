Title:      Making PDF from images
Date:       2014-08-10 23:15
Status:     draft
Category:   Hacks
Tags:       pdf, terminal
Author:     Maciej Sypień


<div class="intro-article-image-sm" markdown="1">
  ![Making custom PDF]({filename}/images/pdf_book.png)
</div>

Zapewne nie raz odczułeś potrzebę złożenia sobie wygodnego ebook'a z luźnych zdjęć jakiegoś tekstu np.: na Twoje nowe mobilne urządzenie (telefon, tablet lub czytnik ebook'ów). Czy to były notatki kolegi potrzebne do nauki na jakiś przedmiot, czy skany jakiejś książki, którą kupiłeś sobie, lecz nie ma jej elektronicznego odpowiednika. Wpadasz wtedy na genialny pomysł realizacji własnego PDF-a samodzielnie. Jednak na drodze do sukcesu staje bariera techniczna w realizacji tej idei.

W tym krótkim artykule postaram się przedstawić "domowy" proces złożenia własnego PDF-a z luźnych zdjęć, zachowując przy tym b.dobrą jakość pliku wynikowego. Cały proces opisałem poniżej, a do realizacji użyłem konsoli systemu Linux Ubuntu 14.04.

<!--more-->

<p style="clear:both">
</p>

* * *

#### Krótki spis treści:

*   [Instalacja potrzebnego oprogramowania][1]
*   [Skanowanie tekstu][2]
*   [Konwersja na jednolity format obrazków][3]
*   [Sortowanie i zamiana nazw plików][4]
*   [Obracanie obrazków zgodnie z ich prawidłowym położeniem][5]
*   [Przycinanie obrazków oraz dostrojenie kąta obrazka][6]
*   [Konwersja do stałej (najmniejszej) szerokości wszystkich obrazków][7]
*   [Redukcja wagi i jakości zdjęcia (opcjonalne)][8]
*   [Weryfikacja kolejności i zgodności stron][9]
*   [Złożenie obrazków do PDF-a][10]

### <a name="instalacja-oprogramowania" class="jumptarget"></a> Instalacja potrzebnego oprogramowania

Do wykonania naszego zadania przyda nam się program `imagemagick` --- swoisty szwajcarski scyzoryk jeśli chodzi o obróbkę plików graficznych z poziomu konsoli.

**Instalacja**:

    $ sudo apt-get install imagemagick


### <a name="skanowanie-tekstu" class="jumptarget"></a> Skanowanie tekstu

Proces ten powinien być dość prosty. Skanujesz wybrane kartki do dobrej jakości plików graficznych (w zupełności wystarczy już 250dpi). Jeśli możesz wybrać format zalecam `PNG`, jeśli nie masz wyboru formatu wynikowego, później zajmiemy się konwersją do PDF'ów :)

**Zrób gdzieś kopię zapasową katalogu ze zdjęciami na wypadek, jeśliby coś nie wyszło taj jak potrzeba.**

Jeśli masz już gotowe zdjęcia proces ten możesz pominąć, jednak zanim przejdziesz dalej zapoznaj się z poniższą informacją.

> Pamiętaj o tym że jeśli posiadasz już zeskanowane zdjęcia karetek, powinny one być w miarę dobrej jakości (większej 250dpi) w przeciwnym razie później może być problem jeśli chodzi o końcową jakość PDF-a. Lepiej więc poświecić chwilkę na dobrą konfigurację skanera (zdjęcia powinny być duże i nierozmazane), aby później cieszyć się ładnym PDF-em.

### <a name="konwersja-na-jednolity-format" class="jumptarget"></a> Konwersja na jednolity format obrazków

Jak wspominałem wcześniej, wszystkie obrazki powinny mieć to samo rozszerzenie --- najlepiej PNG (bezstratne).

Poniższa komenda zamienia wszystkie obrazki z formatu `jpg` na `png` w aktualnym katalogu.

    $ mogrify -format jpg *.png


### <a name="sortowanie-i-zamiana-nazw-plikow" class="jumptarget"></a> Sortowanie i zamiana nazw plików

Będziemy zmieniac nazwy plików tak, aby ułożyć je w kolejno jeden po drugim. Konsola Linuksa (Bash) nieco inaczej sortuje pliki od eksploratora (np: Nautilus). Tak wiec jeśli mamy powiedzmy 100 obrazków i pliki te nazwane są odpowiednio: `1.jpg`, `2.jpg`, `3.jpg`, ..., `100.jpg` to Bash nieco zmieni nam ich kolejność i w rezutacie będzie to: `1.jpg`, `10.jpg`, `100.jpg`, `2.jpg`, ..., `99.jpg`.

Aby temu zaradzić zmienimy je na `001.jpg`, `002.jpg`, `003.jpg`, ..., `100.jpg` --- zasada myśle jest jasna.

Można to zrobić automatycznie lub manualnie.

##### Automatycznie

Do zamiany nazw plików można użyć bardzo prostego programu [bash-filename-converter][11] napisanego specjalnie do automatycznego konwertowania nazw plików do formatu przyjaznego konsoli Linuksa.

Mój skaner wykonuje automatyczne nazwy skanów w postaci `Obraz.jpg`, `Obraz(2).jpg`, `Obraz(3).jpg`, ..., `Obraz(100).jpg`. W celu pewnej automatyzacji napisałem krótki program, który automatycznie zmienia nazwy [Bash Filename Converter][11]. Program napisany jest całkowicie w Bash'u, możesz go pobrać [**z mojego repozytorium na Github**][11] i śmiało dostosować go do swoich potrzeb.

##### Ręcznie

Jeśli nie masz na tyle umiejętności aby dostosować mój skrypt [Bash Filename Converter][11] do swoich potrzeb, pozostaje Ci ręczna modyfikacja plików.

### <a name="obracanie-obrazkow" class="jumptarget"></a> Masowe obracanie obrazków zgodnie z ich prawidłowym położeniem

Zdarza się tak, że podczas robienia skanów zdjęcia zapisują się w nienaturalnym położeniu i trzeba je "poobracać".

Można to zrobić automatycznie lub manualnie.

##### Automatycznie

Przygotowałem również do tego krótki skrypt dostępny [w tym miejscu][12]. Skrypt napisany jest również w 100% w Bash'u. Jego zadaniem jest obrót wszystkich nieparzystych stron `001.jpg`, `003`, `005.jpg` o 90 stopni, natomiast wszystkie parzyste o 270 stopni. Oczywiście skrypt możesz dostosować do swoich potrzeb (jest z grubsza jest opisany).

##### Ręcznie

W systemie Linux Ubuntu dobrym, domyślnym narzędziem jest program `Shotwell Viewer`. Pozwala ona na szybkie i sprawne obrócenie obrazów, a na końcu (po wykonaniu wszytkich obrotów) Shotwell wykonuje zbiorowy, automatyczny obrót wszystkich fotografii --- przyspieszając tym samym cały proces.

### <a name="przycinanie-i-wyrownanie-obrazow" class="jumptarget"></a> Przycinanie i wyrównywanie wszystkich obrazów.

Aby wykonać to dobrze należy wykonać tą część ręcznie. Do tej pracy również świetnie posłuży program `Shotwell Viewer` --- potrafi obracać obrazki o zadany stopień (`obróć`, `wyrównaj`)

### <a name="konwersja-do-stalej-szerokosci" class="jumptarget"></a> Konwersja do stałej (najmniejszej) szerokości wszystkich obrazków

Po tylu czynnościach jakie już wykonaliśmy nadeszła ostatnia bardzo ważna --- ujednolicenie rozmiaru wszystkich plików.

W tym celu należy sprawdzić czy wszystkie zdjęcia mają podobne parametry. Posłuży do tego polecenie znajdujące się poniżej, które zapisze do pliku najważniejsze dla nas dane o wszystkich obrazkach w aktualnym katalogu.

**Wykonanie poniższej komendy zwykle zajmuje parę minut** --- w zależności od ilości obrazków i parametrów komputera.

    $ identify -verbose *.png | grep "Image:\|Resolution:\|Geometry:\|Filesize:\|Colorspace:" > images_stats.txt


Wszystkie wydruki powinny się mniej więcej zgadzać. Jednie dla wartości `Geometry` mogą być inne wyniki drugiego wymiaru (zaraz po `x...`, czyli 1152x**1702+0+0**). Pierwszy wymiar Geometry to szerokość strony, drugi to wysokość.

Zawartość wygenerowanego pliku `images_stats.txt` powinna wyglądać mniej więcej tak jak poniżej:

    ...
    Image: 001.png
      Geometry: 1152x1702+0+0
      Resolution: 28.35x28.35
      Colorspace: Gray
      Filesize: 664KBB
    Image: 003.png
      Geometry: 1152x1702+0+0
      Resolution: 72x72
      Colorspace: Gray
      Filesize: 246KBB
    Image: 004.png
      Geometry: 1152x1698+0+0
      Resolution: 72x72
      Colorspace: Gray
      Filesize: 187KBB
    Image: 005.png
      Geometry: 1152x1700+0+0
      Resolution: 72x72
      Colorspace: Gray
      Filesize: 200KBB
    ...


> Jak widać wszystkie parametry są podobne, jedynie **Geometry** oraz **Filesize** powinien się zmieniać. To wszystko da nam gwarancję że nie będzie różnej wielkości stron w końcowym pliku PDF.

Aby **sprawdzić najmniejszy wymiar** obrazka można użyć polecenia poniżej:

    $ cat images_stats.txt | grep "Geometry:"


Szukamy najmniejszej wartości dla szerokości strony spośród wszystkich zdjęć (czyli: Geometry: **1152**x1700+0+0). Polecenie to można jeszcze delikatnie zmienić, aby uzyskać mniejsze wartości i wyłapać najmniejszy wymiar :)

    $ cat images_stats.txt | grep "Geometry: 12"


Po ustaleniu **najmniejszej** szerokości strony (width) wykonujemy poniższą komendę która zmieni szerokość wszystkich zdjęć do tej najmniejszej (zadanej przez nas).

    $ mogrify -geometry 1152x *.png   // zamiana z szerokości na jedną wspólną wszystkich png


Dla pewności można wykonać jeszcze raz komendę która zbada wszystkie właściwości zdjęć dla nas i zapiszę do pliku:

    $ identify -verbose *.png | grep "Image:\|Resolution:\|Geometry:\|Filesize:\|Colorspace:" > images_stats_fixed.txt


### <a name="redukacja-wagi-i-jakosci-zdjecia" class="jumptarget"></a> Redukcja wagi i jakości zdjęcia (opcjonalne)

> **Uwaga:** Zmiana zdjęć odbywa się na aktualnych zdjęciach!!!
> Warto więc zrobić kopię do nowego folderu i pracować na nim.

    $ mogrify -resize 50% -quality 80% *.jpg


Powyższa komenda zmieni domyślny rozmiar naszych zdjęć o połowę (50%) i dodatkowo zmniejszy jakość wszystkich zdjęć do 80%.

### <a name="zlozenie-pdfa" class="jumptarget"></a> Złożenie obrazków do PDF-a

Konwertowania dokonujemy komendą

    convert *.png ksiazka.pdf


### <a name="weryfikacja-kolejnosci-i-zgodnosci-stron" class="jumptarget"></a> weryfikacja kolejności i zgodności stron

Teraz pozostała już tylko ostateczna weryfikacja naszych plików przed konwersją.

##### Weryfikacja kolejności

Mam na myśli proste sprawdzenie poprawnej numeracji kolejnych stron i tym samym czy dobrze złożyło plik PDF.

##### Weryfikacja kolejności

Zwróć uwagę na numeracje stron, tak by zgadzała się z stronami wybieranymi w wyszukiwarce PDF (przejdź do strony).

### Koniec :)

Gratuluje! Jeśli wszystko wykonałeś poprawnie, powinieneś uzyskać wysokiej jakości PDF-a z identyczną szerokością wszystkich stron.

Nie pozostaje mi nic innego jak życzyć Ci przyjemnej lektury :)

 [1]: #instalacja-oprogramowania
 [2]: #skanowanie-tekstu
 [3]: #konwersja-na-jednolity-format
 [4]: #sortowanie-i-zamiana-nazw-plikow
 [5]: #obracanie-obrazkow
 [6]: #przycinanie-i-wyrownanie-obrazow
 [7]: #konwersja-do-stalej-szerokosci
 [8]: #redukacja-wagi-i-jakosci-zdjecia
 [9]: #weryfikacja-kolejnosci-i-zgodnosci-stron
 [10]: #zlozenie-pdfa
 [11]: https://github.com/egel/bash-filename-converter
 [12]: https://gist.github.com/egel/58132176b716d96dada2
