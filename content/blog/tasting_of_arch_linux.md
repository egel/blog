Title:		Tasting of Arch Linux
Slug:			tasting-of-arch-linux
Date:			2016-11-18
Status:		Published
Category: Diary
Tags:			linux, arch, terminal
Authors:	Maciej Sypień
Summary:  Whole process of installation and my reflections upon the Arch Linux.

<div class="intro-article-image-sm" markdown="1">
  ![Linux logo]({filename}/images/archlinux_logo.png)
</div>


I have to admit that installation of Arch Linux can be difficult for many people, but that exactly is real fun!

Few days ago I've tried to install Arch on my virtual machine then on my laptop and I could not find anything that I didn't like. Yeah, I agree that there are many decisions you have to decide during installation of Arch. For example: manual setuping of partitions, current date, downloading all related packages, then finally install whole system. For many (unfortunately) it is just the begining, because after the installation you have a bare system - console and that is it. You need to install and configure GUI and other important stuff on your own, but actually that is real fun!

The longest part for me was the downloading and installation packages from the Net. This took me arount 45 minutes to download the system and GUI interface (gnome).

Beside the installation process, I love the whole idea of having one release in contrast to Ubuntu. You have only one major version and you stick to it - unitil that community decide to change it.

Below I would like to share my whole process and preferences during the setuping the Arch.

### Partitioning hard drives
Display all drives on pc. I have only one drive called `/dev/sda`.

```shell
fdisk -l
cfdisk /dev/sda
```

I've got 500GB drive (with real space of 465GB), but the dirive has one hidden partition for WinRecovery with size around 18GB (I'm not using it right now).

So, now I split a bit rest of my drive space for 2 additional partitions.

> Many IT guys will be whimper a bit of having only one general partition for `/`, but I found it more useful for me in daily work.
>
> **Note**: If you have disk bigger then 2TB use [`GPT`](https://en.wikipedia.org/wiki/GUID_Partition_Table) instead of `DOS`, if using of `MBR` is not obligatory.

-   18GB hidden WinRecovery partition (not used)
-   16GB for `/swap` with type `linux swap` (82)
-   ~431GB for `/` with **bootable** flag and type `linux` (83)

For more take a look on [partitioning page][arch-partitioning] on Arch wiki.


### Downloading basic packages
> I have tried installation on my virual box then again on my laptop. The problem that I face to, was internet connection through WiFi. There is several way of doing this. You can use `wifi-menu` to setup temporary connection for downloading packages and after installation setup `network-manager`.

In this part we will format our partitions and enable Linux SWAP:

```shell
mksf.ext4 /dev/sda2
mount /dev/sda2 /mnt
mkswap /dev/sda1
swapon /dev/sda2
pacstrap /mnt base base-devel # most basic packages
```

If you don't want to install anything more for now, you can omit below packages, but I recomend to install them also just for more efficient usage before setuping the `network-manager`.

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
> ```shell
> ip link
> dhcpcd enp0s3
> ```


### Further steps
Now we have system installed.


```shell
pacman -Syu
pacman -S vim git tmux

# Additional packages
bash-completion

# not checked but needed
exfat-fuse exfat-utils
```


User

```shell
useradd -m -g users -G wheel,storage,power,sys,adm -s /bin/zsh maciej
passwd maciej
vim /etc/sudoers    # Uncomment: wheel ALL=(ALL) ALL
```

**Now SWITCH to new created user!**

```shell
su maciej
```


### Install display manager

I choose Gnome3

```shell
sudo pacman -S gnome gnome-extra gnome-tweek-tool
sudo systemctl enable gdm.service
```

reboot and done


```shell
sudo pacman -S nvidia nvidia-utils
```
and check by `lsmod | grep nvidia`

> No animations with nvidia? Try install `nvidia-libgl` instead of default `mesa-libgl`.


### Other programs for Arch

```shell
sudo pacman -S openssh
```

[github]: https://github.com
[arch-partitioning]: https://wiki.archlinux.org/index.php/partitioning
