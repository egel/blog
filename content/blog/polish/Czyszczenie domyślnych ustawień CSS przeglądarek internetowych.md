Title:      Czyszczenie domyślnych ustawień CSS przeglądarek internetowych
Date:       2013-10-14 00:56:45
Modified:   2013-10-13 22:56:45
Status:     inherit
Category:   
Tags:       
Summary:  


Kiedyś, bardzo, bardzo dawno temu, gdy jeszcze rozpoczynałem swoja walkę z kaskadowymi arkuszami stylów zastanawiałem się:

> Dlaczego ta strona na hostingu nie wygląda tak jak u mnie na localhost?

Problem ten, jak teraz spoglądam z perspektywy czasu, był tak prosty, aż uśmiech rysuje się na twarzy, lecz kto mógł wtedy wyjaśnić, że robię błąd w tym i tym miejscu. Nikt :).  
Początki zazwyczaj bywają ciężkie.

<!--more-->

Wracając do problemu. Tak wiec obecne przeglądarki, ale również poprzednie ich wersje, ustawiały *domyślne style* dla wyświetlanych stron (każdej bez wyjątku), chyba że sami "powiedzieliśmy" przeglądarce:

> Słuchaj, ja chce tu mieć "czyste" pole do popisu moich umiejętności, rozumiemy się?!;)

Najczęściej jednak jak to w początkach bywa, nie wiadomo co się do końca robi, ale się to robi - a końcowy wynik pracy uzgadnia się w stylu:

> Może tak być? Powiedz, że tak...

Dopiero z czasem można powiedzieć z pełną odpowiedzialnością, że umie się wykonać to, czy tamto, ponieważ wynik naszej pracy jest identyczny z założeniami projektu.

Poniżej umieszczam kod, który po cichu liczę, że zaoszczędzi wielu osobom trudu tworzenia nowych arkuszy stylów od podstaw ;)

    /* —————————————————————————————— clear.css —————————————————————————————— */ 
    html, body, div, span, applet, object, iframe, h1, h2, h3, h4, h5, h6, p, blockquote, pre, a, abbr, acronym, address, big, cite, code, del, dfn, em, font, img, ins, kbd, q, s, samp, small, strike, strong, sub, sup, tt, var, b, u, i, center, dl, dt, dd, ol, ul, li, fieldset, form, label, legend, table, caption, tbody, tfoot, thead, tr, th, td, input, textarea {
        margin:0;
        padding:0;
        border:0;
        outline:0;
        font-size:12px;
        font-weight:normal;
        vertical-align:top;
        background:transparent;
        outline:none;
    } 
    b {font-weight:bold;} 
    i {font-style:italic;} 
    ol, ul {list-style:none;} 
    blockquote, q {quotes:none;} 
    table {border-collapse:collapse; border-spacing:0;} 
    a, span {vertical-align:baseline;} 
    img {vertical-align:top; text-decoration:none;}
