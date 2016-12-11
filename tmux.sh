#!/bin/bash

START_INDEX_NUMBER=1
SESSION=pelican
FOLDER=$PWD    # to assign to a variable
WORKON_ENV=pelicanblog

#create detached session named $SESSION
tmux new-session -d -s ${SESSION}
tmux splitw -v -p 50 -t $((START_INDEX_NUMBER+0))
tmux splitw -h -p 50 -t $((START_INDEX_NUMBER+0))

tmux selectp -t $((START_INDEX_NUMBER+0))
tmux send-keys "cd ${FOLDER} && workon pelicanblog && pelican content --autoreload" 'C-m'

tmux selectp -t $((START_INDEX_NUMBER+1))
tmux send-keys "cd ${FOLDER} && workon ${WORKON_ENV}" 'C-m'

tmux selectp -t $((START_INDEX_NUMBER+2))
tmux send-keys "cd ${FOLDER} && cd ../egelance-pelican-theme" 'C-m'
tmux send-keys "gulp watch" 'C-m'

tmux -2 attach-session -t ${SESSION}
