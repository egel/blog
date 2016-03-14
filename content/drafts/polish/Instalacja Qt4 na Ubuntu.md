Title:      Instalacja Qt4 na Ubuntu
Date:       2014-07-24 01:44:43
Modified:   2014-07-23 23:44:43
Status:     inherit
Category:   
Tags:       
Summary:


<div style="float: left;">
  <a href="http://blog.egel.pl/instalacja-qt4-ubuntu/qt_master_logo_cmyk_300dpi/" rel="attachment wp-att-1292"><img src="http://blog.egel.pl/media/Qt_master_logo_CMYK_300dpi-150x150.png" alt="Qt Logo" width="150" height="150" class="alignnone size-thumbnail wp-image-1292" /></a>
</div>

Zestaw popularnych bibliotek Qt, to nie lada gratka dla każdego programisty aplikacji okienkowych. Świetna integracja oraz doskonała przenośność tworzonych aplikacji to nie jedyne zalety korzystania z tych bibliotek.

<!--more-->

<p style="clear:both">
</p>

Instalacja bibliotek Qt4 jest w Ubuntu jak zwykle dziecinnie prosta. W terminalu wpisujemy:

    $ sudo apt-get install -y libxaw7-dev qt4-default qt4-qmake qt4-dev-tools qt4-bin-dbg
    

Powyższy zestaw zainstaluje nam oprócz standardowego Creator Qt, programu qmake, doinstaluje również Qt Designer jako osobną aplikację.

Teraz, aby sprawdzić poprawną instalację oraz ostateczną wersję zainstalowanego programu wpisujemy:

    $ qmake -v
    

Qt Designer i NetBeans to idealnie połączenie do szybkiej i wydajnej pracy :)

*Note*: testowano na Ubuntu 14.04.
