# The Egel's Blog
Made with Pelican static generator.


## Initial
Download main repository

    cd ~/workspace
    git clone --recursive git@bitbucket.org:egel/pelican-egel-blog.git


Download plugins

    git clone --recursive https://github.com/getpelican/pelican-plugins ~/.pelican-plugins
    ln -s $HOME/.pelican-plugins $HOME/workspace/pelican-egel-blog/plugins

Set the environment

    mkvirtualenv -p pelicanblog
    workon pelicanblog
    (pelicanblog) pip install -r requirements.txt --no-index
    deactivate

then run server to test (it works in backgroud)

    workon blogging
    ./develop_server.py start

or run tmux session

    ./tmux-console.sh


## Development

- date 
  + [strftime](http://strftime.org/)

## License
MIT 2015 Maciej Sypień
