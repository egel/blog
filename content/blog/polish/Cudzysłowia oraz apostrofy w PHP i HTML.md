Title:      Cudzysłowia oraz apostrofy w PHP i HTML
Date:       2013-10-13 20:27:07
Modified:   2013-10-13 18:27:07
Status:     inherit
Category:   
Tags:       
Summary: 


Od początku moich zmagań z pisaniem w PHP wiązało się wiele małych pojedynczych, ale także wielkich i obszernych problemów. Do tych mniejszych właśnie mogę zaliczyć stosowanie cudzysłowów pojedynczych (apostrofów) i podwójnych. Chodź jak przyjrzeć się całości, to nie jest to taki mały problem.    
Jak to zwykle bywa pojawiające się pytania w rozwiązaniu głównego problemu powodują masowe generowanie nowych pytań pobocznych, lecz owe poboczne pytania okazują się również bardzo istotne w świetle całości problemu. Główkując nad stosowaniem apostrofów i cudzysłowów zadałem sobie wtedy kilka ważnych pytań:

> *   Jaka jest miedzy różnica miedzy apostrofem, a cudzysłowem? 
> *   Kiedy i w jakich sytuacjach je stosować? 
> *   Co jeśli chce połączyć kilka języków razem (tj. PHP i HTML) w jednym pliku? 
> *   Jak ich używać by w przyszłości nie było problemów? 
> *   Jaki nawyk obrać za właściwy?

To tylko niektóre z pytań, a z pewnością było ich o wiele więcej, lecz pisząc niniejszy post problem opisywany tutaj został przeze mnie rozgryziony parę lat wcześniej. Zaznaczam, że są to moje przemyślenia i analizy na rozwiązanie błahego problemu i niekoniecznie może być on zgodny z nomenklaturą pisania - natomiast mi znacznie ułatwiły życie ;)

**W takim razie do rzeczy!**

<!--more-->

Na początek przedstawię kilka bardzo prostych przykładów i postaram się odpowiedzieć na wcześniej postawione pytania w sposób taki, aby nawet adept programowania bez kłopotu zrozumiał zagadnienie. Poniższe przykłady będą maksymalnie zgodne z popranym pisaniem w danym języku, lecz nie musi być to 100% zgodność. Robię tak ze względu na chęć zwrócenia uwagi na sam problem, a nie na ogół formy.

## Przykład 1: <small>PHP</small>

    <?php 
        $wiek= 23; 
        $imie= 'Maciek'; 
        echo 'Jestem '.$imie.' i mam '.$wiek.' lata.'; 
    ?>
    

Pierwszy przykład jest bardzo prosty. Znajdziemy w nim 2 zmienne `$wiek` oraz `$imie`. `echo` wyświetla zmienne oddzielone kropkami od ciągu znaków umieszczonych w apostrofach (łączenie zmiennych/stringów => [konkatenacja stringów][1]).

> Dlaczego użyłem pojedynczych, a nie podwójnych cudzysłowów?

W PHP apostrofy nie interpretują zmiennych wewnątrz siebie (nie wyświetlają wartości, którą przechowują wewnątrz siebie), natomiast cudzysłowy interpretują zmienne podmieniając ich wywołanie w programie na wartość przechowywaną wewnątrz.

Tą sytuacje można zaobserwować uruchamiając skrypt z **przykładu 2**. Wielu programistów (ja również przyjąłem tą konwencję) stara się stosować wyłącznie apostrofy (ciekawostka: szybciej wyświetlane, w przeciwieństwie do cudzysłowów).

> Dlaczego?

Ze względu poprawność składniową języka programowania oraz czytelność preparowanego kodu. Zmienne są wtedy doskonale widoczne w tekście (podświetlane w popularnych edytorach jak np: *Notepad++*, czy *Netbeans*) i programista jest w stanie na pierwszy rzut oka odnaleźć to czego szuka, co jest niesamowicie ważne przy dużej ilości tekstu z którym przyjdzie mu pracować. Nie jest to jednak jeszcze pełna odpowiedź na postawione pytanie, lecz podążając dalej zostanie przedstawiona odpowiedź uzupełniająca zagadnienie.

## Przykład 2:

    // zmienne użyte w zadaniu zdefiniowane w wcześniejszym przykładzie 
    /* 
     * interpretacja znaków będzie "dosłowna" 
     * to znaczy że uzyskamy dokładnie taki sam ciąg 
     * znaków jaki zdefiniowaliśmy w stringu. 
     */ 
    
    echo 'Jestem $imie i mam $wiek lata'; 
    
    /* 
     * zdefiniowane zmienne będą podmienione. 
     * To znaczy, że otrzymamy ciąg znaków wraz 
     * z podmienionymi wartościami w wyjściowym stringu. 
     */ 
    
    echo "Jestem $imie i mam $wiek lata";
    

### Przykład 3: <small>HTML</small>

    <html> 
         <head>
             <title>Mój tytuł</title>
         </head>
         <body> 
              <img src="adres_obrazka/obrazek.jpg" alt="Mój tytuł obrazka" title="Mój tytuł obrazka"> 
         </body> 
    </html>
    

Kod przykładu 2 ukazuje poprawność stawiania cudzysłowów w pliku HTML. Mówiąc inaczej, umieszczając np. kolejne atrybuty dla elementu `img` powinno umieszczać się miedzy cudzysłowy.

> Zatem w jakich sytuacjach stosować cudzysłowy i apostrofy?

Na wstępnie osoby mające do napisania kod mieszany HTML/PHP powinny ustalić sobie jakie założenia przyjmują do każdego z języka - chodź ujednolicenie notacji dla programistów jest zawsze obowiązkowe.  
*Na potrzeby przykładu umawiamy się że w języku **HTML** będziemy starać się używać jedynie cudzysłowów `"`, natomiast dla kodu **PHP** wyłącznie apostrofów `'`*.

Ułatwia to później zrozumienie kodu, a nawet bezproblemowe łączenie go z innymi projektami. Pomaga odseparować je wzajemnie od siebie. Argumentem za jest również to, że programy do edycji takie jak *Notepad++* idealnie podświetlają składnie mieszanych stylów - jeśli ktoś taki styl preferuje oraz oczywiście, jeśli stosuje się do początkowych założeń notacji.

### Przykład 4: <small>HTML wraz z wydzielonymi elementami PHP</small>

    <?php 
        $tytulStrony = 'Moja strona'; 
        $adresObrazka = 'adres_obrazka/'; 
        $nazwaObrazka = 'obrazek'; 
        $tytulObrazka = 'Mój tytuł obrazka'; 
    ?> 
    
    <html>
       <head>
            <title><?php echo $tytulStrony ?></title>
       </head>
       <body>
            <img src="<?php echo $adresObrazka ?>" 
                alt="<?php echo $adresObrazka.$nazwaObrazka.'.jpg' ?>" 
                title="<?php echo $tytulObrazka ?>" /> 
        </body>
    </html> 
    

Następny przykład języka HTML wraz z wydzielonymi elementami PHP ujawnia ładnie odseparowaną składnie obu języków oraz zwraca uwagę na zastosowane wymienne obydwu rodzajów cudzysłowów wraz z łączeniem ze sobą wartości zmiennych. Przykład ten nie jest jednak do końca poprawny - mam tu na myśli mieszanie kodu języka PHP w kod pliku HTML. Od tego służy pisanie programu zgodnego z modelem MVC (Model-Viewer-Controler)  i podział na layout (template) oraz logikę biznesową, lecz to wykracza poza ramy zagadnienia.

### Przykład 5: <smallPHP wraz z dołączonymi elementami HTML</small>

    <?php 
        $tytulStrony = 'Moja strona'; 
        $adresObrazka = 'adres_obrazka/'; 
        $pelnaNazwaObrazka = 'obrazek.jpg'; 
        $tytulObrazka = 'Mój tytuł obrazka'; 
        $content = '
            <html> 
                <head>
                    <title>'.$tytulStrony.'</title> 
                </head> 
                <body> 
                     <img src="'.$adresObrazka.'" 
                         alt="'.$adresObrazka.'" 
                         title="'.$tytulObrazka.'"> 
                </body>
            </html>'; 
        echo $content; 
    ?>
    

Ostatni z przykładów (*przykład 5*) jest typowym plikiem PHP w którym ukazany jest jeszcze inny sposób spojrzenia na sprawę cudzysłowów.  
Jest tu nakreślone typowe (chodź jest kilka metod) łączenie ciągów w jedną całość. Tutaj również doskonale widać (przy podświetlanej składni), gdzie są rozmieszczone zmienne w tekście, o czym wspominano wcześniej.

> Wiec jak używać cudzysłowów pojedynczych i podwójnych tak, aby nie pogubić się w tym wszystkim?

Odpowiedź jest zaskakująco prosta - unikać mieszania - lecz jeśli sytuacja wymaga notacji mieszanej założenia, które ustalimy wraz z zespołem są podstawą dalszego działania.  
Należy również unikać mieszania logiki biznesowej z wyglądem prezentowanej strony nawet w zwykłych, pojedynczych skryptach, gdyż później, osoba zajmująca się skryptem będzie mogła przedwcześnie osiwieć z nadmiernej dawki nerwów ;)

Ponownie dla ogólnego sprostowania. Powyższe przykłady nie są do końca dobre spoglądając z perspektywy wielu różnych języków. Ale omawiając jedną rzecz niestety nie można omawiać miliona innych o których warto by przy okazji wspomnieć.  
Pragnę tutaj jedynie pokazać sposoby z jakimi młodzi adepci prędzej czy później spotkają się podczas swojej wędrówki w gąszcz języków programowania. Tak więc krytyka jest wskazana, lecz wraz z pewną dozą umiaru ;)

Na sam koniec muszę dodać, że podczas tworzenia owego artykułu kod umieszczany w artykule "wykrzaczał" mi się wielokrotnie podczas zapisu to wizualnie, to tekstowo.  
Więc za drobne niedociągnięcia przepraszam, lecz ciągle poszukuje odpowiedniego plugin'u do podświetlania składni. Tu również sugestie mile widziane :)

 [1]: http://pl.wikipedia.org/wiki/Konkatenacja#Konkatenacja_w_programowaniu
