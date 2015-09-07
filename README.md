# The Egel's Blog
Made with Pelican static generator.


## Initial

Downloading plugins, themes, ect

    git clone --recursive https://github.com/getpelican/pelican-plugins ~/.pelican-plugins

Downloading repo:

    git clone --recursive git@bitbucket.org:egel/pelican-egel-blog.git

Setting environment

    mkvirtualenv -p pelicanblog
    workon pelicanblog
    (pelicanblog) pip install -r requirements.txt --no-index
    deactivate

then run server to test (it works in backgroud)

    workon blogging
    ./develop_server.py start


## License
MIT 2015 Maciej Sypień
