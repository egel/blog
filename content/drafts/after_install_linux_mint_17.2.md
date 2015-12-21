# After install Linux Mint 17.2

### enable tty

aktualizacja jezyków z bledem warning uft-8
```
sudo locale-gen --purge --no-archive
```

+ reduce GRUB TIMEOUT = 3sek


### docky

+fix chrome icon

work well with:
http://kb.openstudioproject.com/content/fix-double-google-chrome-icon-docky-and-plank


### Pobrlem z Nvidia

disable the “Nouveau Kernel Driver” for install 352.30 driver

sudo update-initramfs -u

to tty1

sudo /etc/init.d/mdm stop



lspci | grep VGA

now check version of your graphic card then open www.nvidia.com/downloads

download


- install soft_script
    - install dotfiles



