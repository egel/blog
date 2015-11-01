Title:      Vim - instalacja i konfiguracja
Date:       2014-12-11 
Modified:   2015-05-24
Status:     Draft
Category:   
Tags:       vim, text-editor
Summary:   


<div style="float:left">
  <a href="http://blog.egel.pl/?attachment_id=1410" rel="attachment wp-att-1410"><img src="http://blog.egel.pl/media/Vim_logo-150x150.png" alt="Logo programu Vim" width="150" height="150" class="alignnone size-thumbnail wp-image-1410" /></a>
</div>

Vim, vi - to edytor tekstu; Dla jednych to tzw. "coś nie do ogarnięcia", dla innych normalne, rzekłbym codzienne środowisko pracy.

<!--more-->

<p style="clear:both">
</p>

> Instalacja w Ubuntu 14.04 domyślnie instaluje Vim 7.4

### Instalacja Debian/Ubuntu/Mint

    sudo apt-get install vim;
    

### Pathogen-Vim

Obowiązkowo na sam początek, zgodnie z zaleceniami autorów:

    mkdir -p ~/.vim/autoload ~/.vim/bundle && \
    curl -LSso ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim
    

W razie problemów, adres repozytorium pakietu znajduje się [tutaj][1]

### The NERD Tree

    cd ~/.vim/bundle
    git clone https://github.com/scrooloose/nerdtree.git
    

Repozytorium: [`nerdtree` strona www][2]

### Syntastic

    cd ~/.vim/bundle && \
    git clone https://github.com/scrooloose/syntastic.git
    

Repozytorium: [`syntastic` strona www][3]

### Less syntax

    cd ~/.vim/bundle
    git clone https://github.com/groenewege/vim-less
    

Repozytorium: [`vim-less` strona www][3]

### Vim instant markdown

    sudo apt-get install ruby-dev gem xdg-utils
    sudo gem install pygments.rb
    sudo gem install redcarpet -v 2.3.0
    cd ~/.vim/bundle
    git clone git@github.com:suan/vim-instant-markdown.git
    

Repozytorium: [`vim-instant-markdown` strona www][4]

### Theme

    cd ~/.vim/colors/ && wget https://raw.githubusercontent.com/Lokaltog/vim-distinguished/develop/colors/distinguished.vim
    

Repozytorium: [`vim-instant-markdown` strona www][5]

 [1]: https://github.com/tpope/vim-pathogen
 [2]: https://github.com/scrooloose/nerdtree
 [3]: https://github.com/scrooloose/syntastic
 [4]: https://github.com/suan/vim-instant-markdown
 [5]: https://github.com/Lokaltog/vim-distinguished
