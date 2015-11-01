Title:      Benchmark dysku HDD, SSD w Windows
Date:       2014-05-24 00:11:05
Modified:   2014-05-23 22:11:05
Status:     inherit
Category:   
Tags:       
Summary:



Minęło już sporo czasu w świecie informatycznym odkąd została ujawniona technologia dysków SSD. Wraz z popularyzacją nowych dysków flash świat zwrócił baczniejszą uwagę na porównywanie szybkości zapisu i odczytu, do których większość osób nie przykładała zbytniej uwagi. Muszę się przyznać, że również zaliczałem się do tej grupy ;)

Z czystej ciekawości sam chciałem przetestować swój HDD...

<!--more-->

Przeszukując sieć w postaci programu umożliwiającego przeprowadzenie testów spędziłem kilkanaście minut bezskutecznie lawirując pośród stron z programami zajmującymi zazwyczaj sporo miejsca (np: wersje portable) lub/i wymagających koniecznej instalacji na dysku.

<a href="http://blog.egel.pl/?attachment_id=1151" rel="attachment wp-att-1151"><img src="http://blog.egel.pl/media/2-300x192.png" alt="2" width="300" height="192" class="alignleft size-medium wp-image-1151" /></a>

Jak zawsze pomocą posłużyła konsola :)  
Bez instalacji, dodatkowego miejsca na dysku, wbudowane funkcje okazały się idealną, **prostą** i **przejrzystą** odpowiedzią na moje pytanie.

**Uwaga**: W zależności od posiadanych uprawnień, istnieje czasem konieczność uruchomienia linii komend jako administrator aby wykonać poniższe komendy. Aby zobaczyć szybkość **zapisu** na dysku C  w wbijamy konsolę:

    winsat disk -seq -write -drive c
    

Poniżej wynik:

<a href="http://blog.egel.pl/?attachment_id=1150" rel="attachment wp-att-1150"><img src="http://blog.egel.pl/media/3-300x192.png" alt="3" width="300" height="192" class="alignleft size-medium wp-image-1150" /></a>

Poniżej recepta na otrzymanie wyniku **odczytu**  danych z dysku:

    winsat disk -seq -read -drive c
    

<a href="http://blog.egel.pl/?attachment_id=1149" rel="attachment wp-att-1149"><img src="http://blog.egel.pl/media/4-300x192.png" alt="4" width="300" height="192" class="alignleft size-medium wp-image-1149" /></a>

W wyniku powyższych komend testowanie dysków twardych przychodzi dużo łatwiej i szybciej niż monotonne instalacje, które w ostateczności i tak będziemy chcieli usunąć w niedługim czasie. Zachęcam do komentowania i testowania :)
