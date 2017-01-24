Title:		Tasting of Arch Linux
Slug:			tasting-of-arch-linux
Date:			2016-11-18
Status:		Published
Lang:     en
Category: Diary
Tags:			linux, arch, terminal
Authors:	Maciej Sypień
Summary:  Whole process of installation and my reflections upon the Arch Linux.

<div class="intro-article-image-sm" markdown="1">
  ![Linux logo]({filename}/images/archlinux_logo.png)
</div>


I have to admit that installation of Arch Linux can be difficult for many people, but that exactly is real fun!

Few days ago I've tried to install Arch on my virtual machine then on my laptop and I could not find anything that I didn't like. Yeah, I agree that there are many decisions you have to decide during installation of Arch. For example: manual setting up of partitions, current date, downloading all related packages, then finally install whole system. For many (unfortunately) it's just the beginning, because after the installation you have a bare system - console and that is it. You need to install and configure GUI and other important stuff on your own, but actually that is real fun!

The longest part for me was the downloading and installation packages from the Net. This took me around 45 minutes to download the system and GUI interface (gnome).

Beside the installation process, I love the whole idea of having one release in contrast to Ubuntu. You have only one major version and you stick to it - until that community decide to change it.

Below I would like to share my whole process and preferences during the setting up the Arch.

### Partitioning hard drives
Display all drives on PC. I have only one drive called `/dev/sda`.

```shell
fdisk -l
cfdisk /dev/sda
```

I've got 500GB drive (with real space of 465GB), but the drive has one hidden partition for WinRecovery with size around 18GB (I'm not using it right now).

So, now I split a bit rest of my drive space for 2 additional partitions.

> Many IT guys will be whimper a bit of having only one general partition for `/`, but I found it more useful for me in daily work.
>
> **Note**: If you have disk bigger then 2TB use [`GPT`](https://en.wikipedia.org/wiki/GUID_Partition_Table) instead of `DOS`, if using of `MBR` is not obligatory.

-   18GB hidden WinRecovery partition (not used)
-   16GB for `/swap` with type `linux swap` (82)
-   ~431GB for `/` with **bootable** flag and type `linux` (83)

For more take a look on [partitioning page][arch-partitioning] on Arch wiki.


### Downloading basic packages
> I have tried installation on my virtual box then again on my laptop. The problem that I face to, was internet connection through WiFi. There is several way of doing this. You can use `wifi-menu` to setup temporary connection for downloading packages and after installation setup `network-manager`.

In this part we will format our partitions and enable Linux SWAP:

```shell
mksf.ext4 /dev/sda2
mount /dev/sda2 /mnt
mkswap /dev/sda1
swapon /dev/sda2
pacstrap /mnt base base-devel # most basic packages
```

If you don't want to install anything more for now, you can omit below packages, but I recommend to install them also just for more efficient usage before setting up the `network-manager`.

```shell
pacstrap /mnt dialog wpa_supplicant network-manager-applet ldns # for connecting via wifi-menu after install
pacstrap /mnt sudo zsh wget curl # additional packages
```

### Configuring the installation
```shell
arch-chroot /mnt
passwd root
vi /etc/locale.gen    # uncoment all for you lang: en_US
locale-gen
ln -s /usr/share/zoneinfo/Europe/Berlin /etc/localtime
timedatectl set-ntp true
hwclock --systohc
echo vbox > /etc/hostname

# installing grub
pacman -S grub-bios
grub-install /dev/sda

# generate system info file
mkinitcpio -p linux

grub-mkconfig -o /boot/grub/grub.cfg
exit # from /mnt root

# generate partition info
genfstab /mnt >> /mnt/etc/fstab
umount -R /mnt
```

> This password is the most important of all. Write it down somewhere to not forget, we will need it later.

### Connect to internet

```shell
ip link
systemctl enable dhcpcd.service
systemctl start dhcpcd.service
ping google.com
```

or copy profile from examples

```shell
cp /etc/netctl/examples/ethernet-dhcp /etc/netctl/
vim /etc/netctl/ethernet-dhcp    # change Interface=enp0s3
netctl enable ethernet-dhcp
netctl start ethernet-dhcp
```

> If above not work try manual install upon result from `ip link`, in my case the Ethernet device name is called `enp0s3`
>
>     :::shell
>     ip link
>     dhcpcd enp0s3
>

### Create user

```shell
useradd -m -g users -G wheel,storage,power,sys,adm -s /bin/zsh maciej
passwd maciej
vim /etc/sudoers    # Uncomment: wheel ALL=(ALL) ALL
```

**Now SWITCH to new created user!**
To do it `logout` from root user just to safety purpose.

> Why? Because when you use **root** you can do everything (it is good when you now what you're doing), but it's not about what you can or can't do, it's about you. You're more secure from yourself actions for example just using `sudo` program.
>
> It's good approach - but hey, you already know this, right? ;)


### Further steps
Now we'll install additional useful stuff. You may or may not to install it, it's up to you.

My **must have** list.
```shell
sudo pacman -Syu
sudo pacman -S gvim git tmux htop jack2
```

The list:

-   For bash I usually install `bash-completion`.
-   For checking hardware `lshw hwinfo`.
-   For mini-jack support `jack2`
-   For supporting different drives I install `exfat-utils dosfstools jfsutils ntfs-3g mtools` and for partitioning I like `gparted` and `gpart` for fixing drives.
-   For graphics `gimp inkscape` and `imagemagick` for console operations.
-   For FTP `filezilla`.
-   For SSH `openssh` is obvious choice!
-   For LaTeX I usually install all packages `texlive-most texlive-lang` and `texstudio`


### Install display manager

I choose [Gnome3](https://www.gnome.org/gnome-3/) for my graphical environment, because now many problems has been fixed by maintainers and it's looks quite nice.

```shell
sudo pacman -S gnome gnome-extra gnome-tweek-tool
sudo systemctl enable gdm.service
```

Reboot system with `sudo reboot` and we're done with installation of GUI.


### Install the nVidia drivers
First we check which graphic card we have:

```bash
lspci -k | grep -A 2 -E "(VGA|3D)"
```

In my laptop I've got **GeForce GT 425m**, so according to [Arch Linux wiki about nvidia](). I have to install `nvidia nvidia-libgl` and enable service.

> It might wants to uninstall `mesa-libgl` package (this package have some problems with handling animations for some graphic cards), so agree for that by pressing (Y).

```shell
sudo pacman -S nvidia nvidia-utils nvidia-libgl
sudo systemctl enable nvidia-persistenced.service
```

Then we have to reboot the system and check `lsmod | grep nvidia`.

### The end
Now you should have full operational Arch Linux system - and yes, you should be proud of yourself!

Thanks for staying with me to the end. I hope that little tutorial of mine, help you a bit during your journey of setting up you private Arch instance ;)

[github]: https://github.com
[arch-partitioning]: https://wiki.archlinux.org/index.php/partitioning
