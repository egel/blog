Title: Sublime Text 3 - instalacja i konfiguracja
Date: 2014-08-16 12:31
Modified: 2015-06-27 19:30
Status: published
Category: Installation, Configuration
Tags: text editor, sublime
Authors: Maciej Sypień


<div style="float:left">
  <a href="http://blog.egel.pl/instalacja-konfiguracja-sublime-text-3/sublime_text_logo/" rel="attachment wp-att-1500"><img src="http://blog.egel.pl/media/Sublime_Text_Logo-150x150.png" alt="Sublime Text Logo" width="150" height="150" class="alignnone size-thumbnail wp-image-1500" /></a>
</div>

Sublime Text to po prostu niezwykły edytor tekstu. Jednak jego niezwykłość i pewna przewaga nad innymi podobnymi edytorami (tj. Notepad++), to wielka wszechstronność wykorzystania oraz duża liczba rozmaitych dodatków wspomagających pracę użytkownika.

Sublime Text jest dostępny w bezpłatnej wersji trialowej na większość znanych platform systemowych (tj. Windows, Mac OSX, Linux) jednak w tym artykule skupię się na instalacji dla systemów z rodziny Linux Debian/Ubuntu (Ubutnu 14.04 LTS 64-bit).

<!--more-->

<p style="clear:both">
</p>

#### Instalacja:

*   [Instalacja Sublime Text 3 Beta][1]
*   [Instalacja Package Control][2]

#### Dodatki

*   [All Autocomplete][3]
*   [Syntax highlight for Sass][4]
*   [Less Syntax][5]
*   [CoffeeScript Sublime Plugin][6]
*   [Live Loader][7]
*   [Markdown Preview][8]
*   [Markdown Extended][9]
*   [GitGutter][10]
*   [Git-Status​Bar][11]
*   [Sublime linter (core)][12]
*   [Sidebar Enhancements][13]
*   [Djaneiro][14]
*   [VimL][15]
*   [Soda Theme][16]
*   [Tommorow Theme][17]
*   [Color Scheme Selector][18]
*   [Vintageous][19]

#### Konfiguracja

*   [Key Bindings - User][20]
*   [Settings - User][21]

* * *

### **Instalacja**

Prosta instalacja programu wraz managerem pakietów.

### <a name="instalacja-edytora" class="jumptarget"></a> Instalacja Sublime Text 3 Beta

Pewnie już dostrzegłeś w nagłówku słowo "beta". Autorzy edytora tworzą niezwykle stabilne oprogramowanie, nawet jeśli są to wersje beta --- sam byłem mocno zaskoczony jakością i stabilnością tych wersji (beta).

Ręczna instalacja z [oficjalnej strony Sublime Text 3][22] lub **autmatyczna** w terminalu:

    $ wget http://c758482.r82.cf2.rackcdn.com/sublime-text_build-3059_amd64.deb -P /tmp && \
    sudo dpkg -i /tmp/sublime-text_build-3059_amd64.deb && \
    rm /tmp/sublime-text_build-3059_amd64.deb


### <a name="package-control" class="jumptarget"></a> Package Control

Na oficjalnej stronie [packagecontrol.io][23] znajdujemy link dla Sublime Text 3 (celowo nie podaje go tutaj, gdyż często ulega zmianie) i już w bezpośrednio uruchomionym programie wciskamy kompinacje: `Ctrl + ~` i wklejamy skopiowany kod, zatwierdzając `Enter`-em.

* * *

### **Dodatki**

W tej części skupimy się na modalności naszego edytora, czyli dokonamy instalacji i konfiguracji kilku doskonałych dodatków.

> Otwarcie *Package Manager'a* to kombinacja klawiszy: `Shift`+`Ctrl`+`P`

### <a name="all-autocomplete" class="jumptarget"></a> All Autocomplete

Instalacja przez Package Manager: Install Package > All Autocomplete

### <a name="syntax-highlight-for-sass" class="jumptarget"></a> Syntax highlight for Sass

Repozytorium dodatku: [Syntax highlight for Sass][24]

Instalacja przez Package Manager: Install Package > Syntax highlight for Sass

### <a name="less-syntax" class="jumptarget"></a> Less Syntax

Instalacja przez Package Manager: Install Package > Less Syntax

### <a name="coffeescript-sublime-plugin" class="jumptarget"></a> CoffeeScript Sublime Plugin

Repozytorium dodatku: [CoffeeScript Sublime Plugin][25]

    $ cd ~/.config/sublime-text-3/Packages \
      && rm -rf CoffeeScript \
      && git clone https://github.com/Xavura/CoffeeScript-Sublime-Plugin.git CoffeeScript


### <a name="live-loader" class="jumptarget"></a> Live Loader

Repozytorium dodatku: [Github repo][26]

    $ cd ~/.config/sublime-text-3/Packages \
      && rm -rf LiveReload \
      && git clone -b devel https://github.com/dz0ny/LiveReload-sublimetext2.git LiveReload


Można pobrać również dodatk do przeglądarki [LiveReload][27] i podczas zapisu pliku w Sublime, treść będzie automatycznie odświeżana w przeglądarce.

*   [Dodatek dla Chrome][28]

### <a name="markdown-preview" class="jumptarget"></a> Markdown Preview

Instalacja przez Package Manager: Install Package > Markdown Preview

### <a name="markdown-extended" class="jumptarget"></a> Markdown Extended

Instalacja przez Package Manager: Install Package > Markdown Extended

### <a name="gitgutter" class="jumptarget"></a> GitGutter

Instalacja przez Package Manager: Install Package > GitGutter

### <a name="git-status​bar" class="jumptarget"></a> Git-Status​Bar

Instalacja przez Package Manager: Install Package > Git-Status​Bar

### <a name="sublime-linter" class="jumptarget"></a> Sublime linter (core)

Instalacja przez Package Manager: Install Package > Sublime linter v3

**Rozszerzenia dodatku**:

*   [SublimeLinter-annotations][29] - marks annotations like TODO, README, FIXME
*   [SublimeLinter-csslint][30]
*   SublimeLinter-contrib-scss-lint
*   SublimeLinter-php

### <a name="sidebar-enhancements" class="jumptarget"></a> Sidebar Enhancements

Instalacja przez Package Manager: Install Package > Sidebar Enhancements

### <a name="djaneiro" class="jumptarget"></a> Djaneiro

Instalacja przez Package Manager: Install Package > Djaneiro

### <a name="viml" class="jumptarget"></a> VimL

Instalacja przez Package Manager: Install Package > VimL

### <a name="soda-theme" class="jumptarget"></a> Soda Theme

Strona skórki: <http://buymeasoda.github.io/soda-theme/>

    $ cd ~/.config/sublime-text-3/Packages \
      && rm -rf "Theme - Soda" \
      && git clone https://github.com/buymeasoda/soda-theme/ "Theme - Soda"


Aby całość zadziałała, należy dodać linikję konfiguracyjną do pliku `Settings - User`. Podgląd jak to osiągnąć znajduje się w [Settings - User][21].

### <a name="tommorow-theme" class="jumptarget"></a> Tommorow Theme

Instalacja przez Package Manager: Install Package > Tommorow Theme

Aktywacja: `Preferences` > `Color Scheme` > `Tommorow Color Scheme` > i wybrać skórkę.

### <a name="color-scheme-selector" class="jumptarget"></a> Color Scheme Selector

Strona dodatku: <https://github.com/jugyo/SublimeColorSchemeSelector>

    $ cd ~/.config/sublime-text-3/Packages \
      && rm -rf "ColorSchemeSelector" \
      && git clone https://github.com/jugyo/SublimeColorSchemeSelector.git "ColorSchemeSelector"


### <a name="vintageous" class="jumptarget"></a> Vintageous

Jeden z moich najbardziej lubianych pluginów do sublime, wprowadzający klawiszologię Vi/Vim. **Ten dodatek nie jest przeznaczony dla osób nieznających Vi/Vim!**

Strona dodatku: <https://github.com/guillermooo/Vintageous>

    $ cd ~/.config/sublime-text-3/Packages \
      && rm -rf "Vintageous" \
      && git clone git@github.com:guillermooo/Vintageous.git "Vintageous"


* * *

### **Konfiguracja**

### <a name="key-bindings-user" class="jumptarget"></a> Ustawienia: Key Bindings - User

    [
      { "keys": ["alt+up"], "command": "swap_line_up" },
      { "keys": ["alt+down"], "command": "swap_line_down" },

      { "keys": ["ctrl+shift+up"], "command": "duplicate_line" },
      { "keys": ["ctrl+shift+down"], "command": "duplicate_line" },

      { "keys": ["ctrl+shift+x"], "command": "swap_case" },

      { "keys": ["ctrl+f5"], "command": "refresh_folder_list"},

      // Quick rename of current file (require SideBar Enhancements plugin)
      { "keys": ["f2"], "command": "side_bar_move" },

      // Toggle side bar
      { "keys": ["f9"], "command": "toggle_side_bar" }
    ]


### <a name="settings-user" class="jumptarget"></a> Settings - User

    {
      // Colors + Themes
      "theme": "Soda Dark 3.sublime-theme",
      "color_scheme": "Packages/Tomorrow Color Schemes/Tomorrow-Night.tmTheme",

      // Font
      "font_face": "Ubuntu Mono",
      "font_size": 15.0,
      "line_padding_bottom": 0,
      "line_padding_top": 0,
      "highlight_line": true,
      "font_options":
      [
        "subpixel_antialias",
        "no_bold"
      ],

      // Editor behavior
      "spell_check": false,
      "dictionary": "Packages/Language - English/en_US.dic",
      "open_files_in_new_window": false,
      "highlight_modified_tabs": true,
      "always_show_minimap_viewport": true,
      "bold_folder_labels": true,
      "fade_fold_buttons": false,
      "draw_minimap_border": true,
      "find_selected_text": true,
      "rulers": [ 79, 100 ],
      "show_encoding": true,
      "scroll_past_end": false,
      "caret_style": "solid",
      "wide_caret": true,

      // Ignored packages
      "ignored_packages":
      [
        "Vintage"
      ],

      // Whitespace - no tabs, trimming, end files with \n
      "tab_size": 4,
      "translate_tabs_to_spaces": true,
      "trim_automatic_white_space": true,
      "trim_trailing_white_space_on_save": true,
      "ensure_newline_at_eof_on_save": true,

      // Sidebar - exclude distracting files and folders
      "file_exclude_patterns":
      [
        "*.pyc",
        "*.pyo",
        "*.exe",
        "*.dll",
        "*.obj",
        "*.o",
        "*.a",
        "*.lib",
        "*.so",
        "*.dylib",
        "*.ncb",
        "*.sdf",
        "*.suo",
        "*.pdb",
        "*.idb",
        ".DS_Store",
        "*.class",
        "*.psd",
        "*.db"
      ],
      "folder_exclude_patterns":
        [
            ".git",
            "__pycache__",
            "env",
            "env3"
        ],
    }

 [1]: #instalacja-edytora
 [2]: #package-control
 [3]: #all-autocomplete
 [4]: #syntax-highlight-for-sass
 [5]: #less-syntax
 [6]: #coffeescript-sublime-plugin
 [7]: #live-loader
 [8]: #markdown-preview
 [9]: #markdown-extended
 [10]: #gitgutter
 [11]: #git-status​bar
 [12]: #sublime-linter
 [13]: #sidebar-enhancements
 [14]: #djaneiro
 [15]: #viml
 [16]: #soda-theme
 [17]: #tommorow-theme
 [18]: #color-scheme-selector
 [19]: #vintageous
 [20]: #key-bindings-user
 [21]: #settings-user
 [22]: https://www.sublimetext.com/3
 [23]: https://packagecontrol.io/installation
 [24]: https://github.com/P233/Syntax-highlighting-for-Sass
 [25]: https://github.com/Xavura/CoffeeScript-Sublime-Plugin
 [26]: https://github.com/dz0ny/LiveReload-sublimetext2
 [27]: http://livereload.com/
 [28]: https://chrome.google.com/webstore/detail/livereload/jnihajbhpnppcggbcgedagnkighmdlei
 [29]: https://sublime.wbond.net/packages/SublimeLinter-annotations
 [30]: https://github.com/SublimeLinter/SublimeLinter-csslint
