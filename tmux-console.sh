#!/bin/bash

SESSION="pelican"
FOLDER=$PWD    # to assign to a variable

#create detached session named $SESSION
tmux new-session -d -s $SESSION


tmux new-session -d -s $SESSION
tmux splitw -v -p 50 -t 0
tmux splitw -h -p 50 -t 0

tmux selectp -t 0
tmux send-keys "cd $FOLDER && workon pelicanblog && pelican content --autoreload" 'C-m'

tmux selectp -t 1
tmux send-keys "cd $FOLDER" 'C-m'

tmux selectp -t 2
tmux send-keys "cd $FOLDER && cd ../egelance-pelican-theme" 'C-m'
tmux send-keys "grunt watch" 'C-m'

tmux -2 attach-session -t $SESSION
