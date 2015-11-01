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

    sudo apt-get install libffi-dev libssl-dev # [issue InsecurePlatformWarning][issue-InsecurePlatformWarning]
    mkvirtualenv -p pelicanblog
    workon pelicanblog
    (pelicanblog) pip install -r requirements.txt --no-index --allow-external
    deactivate

then run server to test (it works in backgroud)

    workon pelicanblog
    ./develop_server.py start

or run tmux session

    ./tmux-console.sh


## Development

- date 
  + [strftime](http://strftime.org/)

## License
MIT 2015 Maciej Sypień


[issue-InsecurePlatformWarning]: http://stackoverflow.com/questions/29134512/insecureplatformwarning-a-true-sslcontext-object-is-not-available-this-prevent
