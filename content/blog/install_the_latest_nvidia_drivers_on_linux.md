Title:    Install the latest nVidia drivers for Linux
Date:     2015-11-02
Status:   published
Lang:     en
Category: How to
Tags:     linux, terminal, console
Author:   Maciej Sypień

<!--
<div class="intro-article-image-sm" markdown="1">
  ![Tmux]({filename}/images/terminal_icon.png)
</div>
-->

The time has come that I had to face with reinstall of the Nvidia driver on my Mint
17 distribution.

Well, while using my distro, there appear couple of problems with "Nvidia proprietary drivers".
As a pro Linux guy (laugh),  I pressed `ctrl`+`alt`+`F1`, and got a black screen with flashing cursor. YES! - I shouted immediately - the console isn't broken for good - I sad to myself in mind.

I red somewhere, that the problem could have something with the framebuffer. So I made few modifications to `/etc/default/grub`.

> Please remember, backup always go first!

```shell
sudo cp /etc/default/grub /etc/default/grub.bak
```

Now edit the grub file by entering

```shell
sudo vim /etc/default/grub
```

While editing in your favorite editor (I choose `vim`), uncomment the lines, simply by removing the `#` in front of those lines.

> If your monitor support better resolutions you can change `GRUB_GFXMODE` for another value, my highest was `1024x768`.

```
GRUB_TERMINAL=console
GRUB_GFXMODE=640x480
```

Save the file and run `update-grub` to implement the changes

```shell
sudo update-grub
```

Now, I had to resolve which display manager do I have on my Mint?

```shell
cat /etc/X11/default-display-manager
```

In my case, it was `mdm`, so then I stopped display manager, installed drivers and enabled display manager again.

```shell
sudo service mdm stop
chmod +x /path/to/downloaded/driver/NVIDIA-Linux-x86_64-*.run
sudo sh /path/to/downloaded/driver/NVIDIA-Linux-x86_64-*.run
sudo service mdm start
```

That's it. After pressing `Alt` + `Ctrl` + `F8` the graphical interface showed up as well as a smile on my face :)

