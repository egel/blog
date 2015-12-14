Title:    Install the latest nVidia drivers for linux Mint 17
Date:     2015-11-02
Modified: 2015-08-09
Author:   Maciej Sypień
Status:   published
Lang:     pl
Tags:     linux, console
Category: Tutorial


<div class="intro-article-image-sm" markdown="1">
  ![Tmux]({filename}/images/terminal_icon.png)
</div>


For Linux Mint 17 distro

This has been an issue that has been an annoyance with Nvidia proprietary drivers for two or three years, and has kept me away from Ubuntu-based distros for some time. Finally, on the Nvidia forum, I found the workaround I'd been looking for. The problem arises with Nvidia proprietary drivers (Nouveau doesn't show this behavior): when you push ctrl-alt-F1, you get only a black screen or, at best, a flashing cursor that does nothing. The problem apparently, has to do with the way the framebuffer in implemented and this needs to be disabled. To see if this is the problem, first you need to make a couple of minor modifications to /etc/default/grub - but first, make a backup!

sudo cp /etc/default/grub /etc/default/grub.bak

Now edit the file by entering

sudo pluma /etc/default/grub

in the editor, uncomment the lines
#GRUB_TERMINAL=console
#GRUB_GFXMODE=640x480
by removing the "#". Save the file and run undate-grub to implement the changes

sudo update-grub


Which display manager you have?

    cat /etc/X11/default-display-manager

    sudo service mdm stop
    chmod +x /path/to/downloaded/driver/NVIDIA-Linux-x86_64-331.67.run
    sudo sh /path/to/downloaded/driver/NVIDIA-Linux-x86_64-331.67.run
    sudo service mdm start

