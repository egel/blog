Title:    Install the latest nVidia drivers for Linux
Date:     2015-11-02
Status:   published
Lang:     en
Category: How to
Tags:     linux, console
Author:   Maciej Sypień


<div class="intro-article-image-sm" markdown="1">
  ![Tmux]({filename}/images/terminal_icon.png)
</div>

And it's time that I had to face with reinstall of the Nvidia driver on my Mint
17 distribution.

There arises some problems with Nvidia proprietary drivers. As a pro Linux guy
I pressed `ctrl`+`alt`+`F1`, and got a black screen with flashing cursor. YES! -
I shouted immediately - the console not broke down for good - I sad to myself in
mind.

I red somewhere that the problem could to do something with the framebuffer. So
I made few modifications to `/etc/default/grub`. Remember - backup always go
first!

    :::bash
    sudo cp /etc/default/grub /etc/default/grub.bak

Now edit the grub file by entering

    :::bash
    sudo pluma /etc/default/grub

While editing in your favorite editor, uncomment the lines, simply by removing
the `#` in front of those lines.

    :::apache
    #GRUB_TERMINAL=console
    #GRUB_GFXMODE=640x480

Save the file and run `update-grub` to implement the changes

    :::bash
    sudo update-grub


Now I had to resolve and which display manager do I have on it?

    :::bash
    cat /etc/X11/default-display-manager

In my case was `mdm`, then:

    :::bash
    sudo service mdm stop
    chmod +x /path/to/downloaded/driver/NVIDIA-Linux-x86_64-*.run
    sudo sh /path/to/downloaded/driver/NVIDIA-Linux-x86_64-*.run
    sudo service mdm start

That is it. We are alive again :)

