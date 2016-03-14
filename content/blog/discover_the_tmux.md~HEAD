Title:    Discover the Tmux
Date:     2014-08-16 12:42
Author:   Maciej Sypień
Status:   published
Lang:     en
Tags:     tmux, console
Category: Discovery
Summary:  In this article I will try to take a look on tmux and extract its
advantages and disadvantages for admires or developer.

<div class="intro-article-image-sm" markdown="1">
  ![Tmux]({filename}/images/terminal_icon.png)
</div>

Tmux is terminal multiplexer. What does it mean, anyway? To say it in other
words, more understandable, tmux is a program which allow the user divide
console screen and gently manage them in something that is called a session.

*But why, am I even try to look at tmux and spent my time with it?*

This tool IMHO is the most useful program for network administrators and
programmers, because it allows to simultaneously work with one console window
devided for multiple sub-screens.

Tmux also allow to prepare simple script which can setup your project so easily.
A good exampe can be a setup of enabling Django with virtualenv and run a
server.

But telling you that is good is pointless. You should not believe me, which is
actually a very adequate reaction. You should try it yourself and get build you
own opinion about tmux.

At the end of introduction I can assure you it is worth 15 minutes of your time.

<p style="clear:both">
</p>

*   [Instalacja tmux + xclip][1]
*   [Ustawienia dla pliku konfiguracyjnego tmux'a][2]
*   [Początkowe przydatne komendy][3]
*   [Kopiowanie i wklejanie][4]

* * *

### Installation

Dla dystrybucji Linux Ubuntu 14.04

    $ sudo add-apt-repository ppa:pi-rho/dev
    $ sudo apt-get update
    $ sudo apt-get install tmux

for Mac:

    brew install tmux

or manual installation from [tmux's repository][5]

Następnie sprawdzenie wersji programu:

    $ tmux -V
    tmux 1.9a


Aby jeszcze wygodnie móc kopiować pomiędzy terminalem tmux'a, a systemem niezbędny będzie program `xclip` (lub inny, jednak niniejszy artykuł nie pokrywa innej konfiguracji) do kopiowania pomiędzy schowkiem tmux'a, a schowkiem systemowym.

    $ sudo apt-get install xclip


Teraz tylko zastosowanie konfiguracji z kolejnego akapitu i gotowe.

### <a name="konfiguracja" class="jumptarget"></a> Ustawienia dla pliku konfiguracyjnego tmux'a

Poniższy kod zawiera konfigurację polecanych przeze mnie ustawień dla programu. Całość zapisujemy jako `~/.tmux.conf`

    #############################################################
    ##  Configuration for Linux (Ubutnu 14.04)
    #############################################################

    # Change prefix key to
    unbind C-b
    set-option -g prefix C-a  # first prefix
    set-option -g prefix2 C-b # second prefix

    # C-a a should send ctrl-a to the underlying shell (move to start of line)
    bind-key a send-prefix

    # C-a C-a
    bind-key C-a last-window

    # So we can still use ` when needed
    #bind-key C-a set-option -g prefix C-a
    #bind-key C-b set-option -g prefix `

    # Make mouse useful in copy mode
    setw -g mode-mouse on

    # Allow mouse to select which pane to use
    #set -g mouse-select-pane on

    # start window index at 1
    #set -g base-index 1

    # start pane index at 1
    #setw -g pane-base-index 1

    # highlight window when it has new activity
    setw -g monitor-activity on
    set -g visual-activity on

    # re-number windows when one is closed
    set -g renumber-windows on

    # Scroll History
    set -g history-limit 30000

    # Set ability to capture on start and restore on exit window data when running
    # an application
    setw -g alternate-screen on

    # Lower escape timing from 500ms to 50ms for quicker response to scroll-buffer
    # access.
    set -s escape-time 50



    ############################################################
    ## Key Bindings
    ############################################################

    # Use vim keybindings in copy mode
    # vim keys in copy or choice mode
    set-window-option -g mode-keys vi

    # copying selection vim style
    # http://jasonwryan.com/blog/2011/06/07/copy-and-paste-in-tmux/
    # https://github.com/myfreeweb/dotfiles/blob/master/tmux.conf
    bind-key Escape copy-mode               # enter copy mode; default [
    bind-key -t vi-copy Escape cancel       # exit copy mode; or hit q
    bind-key p paste-buffer                 # paste; default ]
    bind-key -t vi-copy 'v' begin-selection   # begin visual mode
    bind-key -t vi-copy 'V' select-line         # visual line
    bind-key -t vi-copy 'y' copy-selection    # yank
    bind-key -t vi-copy 'r' rectangle-toggle    # visual block toggle

    # read and write and delete paste buffer ( xsel method)
    # https://wiki.archlinux.org/index.php/Tmux#ICCCM_Selection_Integration
    # ctrl+shift+v
    # or see this config video: https://www.youtube.com/watch?v=OW-lKJDFOzc


    ##CLIPBOARD selection integration
    ###Requires prefix key before the command key
    ##Copy tmux paste buffer to CLIPBOARD
    bind y run-shell -b "tmux save-buffer - | xclip -i -selection clipboard" \; display-message "Copied tmux buffer to system clipboard"
    bind C-v run-shell -b "tmux set-buffer \"$(xclip -o)\"; tmux paste-buffer" \; display-message "Paste system clipboard to tmux buffer"



    ###########################################################
    ## Status Bar
    ###########################################################

    # enable UTF-8 support in status bar
    set -g status-utf8 on

    # set refresh interval for status bar
    set -g status-interval 30

    # center the status bar
    set -g status-justify left

    # show session, window, pane in left status bar
    set -g status-left-length 40
    set -g status-left '#[fg=green]#S#[fg=blue] #I:#P#[default]'

    # show hostname, date, time, and battery in right status bar
    set-option -g status-right '#[fg=green]#H#[default] %m/%d/%y %I:%M\
     #[fg=red]#(battery discharging)#[default]#(battery charging)'

    # This option below is for removing administrative debris (session name, hostname, time) in status bar
    # set -g status-left ''
    # set -g status-right ''



    ###########################
    ## Colors
    ###########################

    ## use 256 term for pretty colors
    set -g default-terminal "screen-256color"

    # color status bar
    set -g status-bg colour235
    set -g status-fg white

    # highlight current window
    set-window-option -g window-status-current-fg black
    #set-window-option -g window-status-current-bg green
    set -g pane-border-bg black
    set -g pane-active-border-fg green
    set -g pane-active-border-bg black


Następnie przeładujemy konfigurację bezpośrednio z terminala:

    $ tmux source-file ~/.tmux.conf


lub już w programie tmux:

    <prefix> :source-file ~/.tmux.conf


> `<prefix>` domyślny wykorzystywany w tmux to połączenie klawiszy: `ctrl`+`b`, po przeładowaniu powyższych ustawień zostanie ono zmienione na wygodniejszą dla dłoni kombinacje czyli po prostu: `ctrl`+`a`.

### <a name="przydatne-komendy" class="jumptarget"></a> Początkowe przydatne komendy

*   `<prefix>` `"` - dzieli ekran poziomo (split pane horizontally).
*   `<prefix>` `%` - dzieli ekran poziomo (split pane vertically).
*   `<prefix>` `x` - wyłącza aktualny pane (kill the current pane).
*   `<prefix>` `klawisz strzałki` - zmienia pane (switch pane).
*   Przytrzymaj `<prefix>`, nie puszczając wciskaj kalwisze strzełek - zmienia szerokość pane (resize pane).
*   `<prefix>` `c` - tworzy nowe okno (`c`reate a new window).
*   `<prefix>` `n` - idź do następnego okna (`n`ext window).
*   `<prefix>` `p` - idź do poprzedniego okna (`p`revious window).
*   `<prefix>` `}` - zamienia pane (swamp screens).
*   `<prefix>` `q` - pokazuje numery pane (shows pane numbers).

### <a name="kopiowanie-i-wklejanie" class="jumptarget"></a> Kopiowanie i wklejanie

**Kopiowanie z tmux do systemowego schowka**

1.  `<prefix>` `Esc` (edit mode)
2.  `v` (copy mode)
3.  `y` (yank)
4.  `<prefix>` `y` (paste to system clipboard)

**Wklejanie do tmux z systemowego schowka**

1.  Skopiuj cokolwiek, na przykład z przeglądarki (`ctrl`+`c`)
2.  Przełącz się na okno tmux i użyj `<prefix>` `v`

Aby zobaczyć wklejenie można podejrzeć schowek tmux'a poprzez skrót: `<prefix>` `=`

 [1]: #instalacja
 [2]: #konfiguracja
 [3]: #przydatne-komendy
 [4]: #kopiowanie-i-wklejanie
 [5]: http://sourceforge.net/projects/tmux/files/tmux/
