Title:      Install archived app into Linux
Date:       2014-08-16 12:31
Modified:   2015-10-01 19:30
Status:     Published
Category:   How to
Tags:       linux, install
Authors:    Maciej Sypień

<!--
<div class="intro-article-image-sm" markdown="1">
  ![Logo of Sublime Text 3]({filename}/images/linux_logo_pinguin.jpg)
</div>
-->

This should be obvious task for average Linux user, but there are hundreds of
thousands methods how to install program from archive file like `.tar`,
`.tar.gz`, `.zip` or any other.

When I use Debian based Linux distros, I most often install external software
into `/opt` directory. This is because I rarely install program for single user
and that is most evident location for multi users programs.

### Example scenario
As an example app I will install simple **SQLiteStudio** to edit SQLite
database files, you can probably use any other you want to install.

To do so:

*   Extract archive `/opt` directory where are usually stored external apps.
*   Download the icon of program (format `png` or `xpa`) and save into
    `/usr/share/pixmaps/` directory to with `chmod 644`.
*   Create new file for ex: `sqlitestudio.desktop` into `/usr/share/application`
    and paste below entry:


        :::bash
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

If there are any problems with file permissions directly into
program's directory, that is pretty much it. Good job!

You have your external program installed correctly for multiple users and
probably any graphical interface you have should read it properly.

