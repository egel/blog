Title:    Install the latest nVidia drivers for linux Mint 17
Date:     2015-11-02
Author:   Maciej Sypień
Status:   published
Lang:     pl
Tags:     linux, console
Category: How to


<div class="intro-article-image-sm" markdown="1">
  ![Tmux]({filename}/images/terminal_icon.png)
</div>

After while I had to install my Nvidia driver in my Mint distro because some
problem arises with Nvidia proprietary drivers. I just push `ctrl` + `alt` +
`F1`, and get black screen with flashing cursor. YES! It has not broke down for
good.
I read that the problem has to do with the way the framebuffer.
So I make few modifications to `/etc/default/grub`, but backup first!

    :::bash
    sudo cp /etc/default/grub /etc/default/grub.bak

Now edit the grub file by entering

    :::bash
    sudo pluma /etc/default/grub

While editing in your favourite editor, uncomment the lines, simply by removing
the `#` in front of those lines.

    :::apache
    #GRUB_TERMINAL=console
    #GRUB_GFXMODE=640x480

Save the file and run undate-grub to implement the changes

    :::bash
    sudo update-grub


Now I had to resolve and which display manager do I have on it?

    :::bash
    cat /etc/X11/default-display-manager

In my case was `mdm`) you do:

    :::bash
    sudo service mdm stop
    chmod +x /path/to/downloaded/driver/NVIDIA-Linux-x86_64-*.run
    sudo sh /path/to/downloaded/driver/NVIDIA-Linux-x86_64-*.run
    sudo service mdm start

That is it. We are alive again :)

