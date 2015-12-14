Title:      Install packed app into Debian based Linux distro
Date:       2014-08-16 12:31
Modified:   2015-10-01 19:30
Status:     Published
Category:   How to
Tags:       linux, install
Authors:    Maciej Sypień


<div class="intro-image-sm" markdown="1">
  ![Logo of Sublime Text 3]({filename}/images/Sublime_Text_Logo.png)
</div>

As an exmple app we will install simple SQLiteStudio to edit SQLite database.

1.  Extract
2.  Copy to `/opt` directory where are usually stored external apps.
3.  Download the icon (format `png` or `xpa`) and save into
    `/usr/share/pixmaps/` directory to with chmod 644.
3.  Copy to `/usr/share/application` below entry


        [Desktop Entry]
        Name=SqliteStudio
        Comment=SQLite editor
        Exec=/opt/SQLiteStudio/sqlitestudio
        Icon=/usr/share/pixmaps/sqlite.png
        Terminal=false
        Type=Application
        Encoding=UTF-8
        Categories=Network;Application;
        Path=




