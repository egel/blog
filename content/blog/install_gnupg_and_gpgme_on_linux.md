Title:		Configuring Mutt email client
Slug:			configuring-mutt-email-client
Date:			2017-07-16
Status:		Draft
Lang:     en
Category: Diary
Tags:			mutt, terminal
Authors:	Maciej Sypień
Summary:  We will configure a great terminal-based email client called Mutt.

<div class="intro-article-image-sm" markdown="1">
  ![Linux logo]({filename}/images/linux_logo_pinguin.jpg)
</div>

Software to install

```
sudo apt-get install \
              build-essential \
              libncurses5-dev \
              python-gpgme
              gnupg2
```

A very good article by Justin R. Miller [Everything You Need To Know To Start Using GnuPG with Mutt](http://codesorcery.net/old/mutt/mutt-gnupg-howto).

[github]: https://github.com

Installing libgpg-error

```bash
wget -c ftp://ftp.gnupg.org/gcrypt/libgpg-error/libgpg-error-1.27.tar.gz && \
wget -c ftp://ftp.gnupg.org/gcrypt/libgpg-error/libgpg-error-1.27.tar.gz.sig && \
gpg --verify libgpg-error-1.27.tar.gz.sig && \
tar -xzf libgpg-error-1.27.tar.gz && \
cd libgpg-error-1.27/ && \
./configure && \
make && \
make install && \
cd ../
```

Installing libgcrypt

```bash
wget -c ftp://ftp.gnupg.org/gcrypt/libgcrypt/libgcrypt-1.7.6.tar.gz && \
wget -c ftp://ftp.gnupg.org/gcrypt/libgcrypt/libgcrypt-1.7.6.tar.gz.sig && \
gpg --verify libgcrypt-1.7.6.tar.gz.sig && \
tar -xzf libgcrypt-1.7.6.tar.gz && \
cd libgcrypt-1.7.6 && \
./configure && \
make && \
sudo make install && \
cd ../
```


```bash
wget -c ftp://ftp.gnupg.org/gcrypt/libassuan/libassuan-2.4.3.tar.bz2 && \
wget -c ftp://ftp.gnupg.org/gcrypt/libassuan/libassuan-2.4.3.tar.bz2.sig && \
gpg --verify libassuan-2.4.3.tar.bz2.sig && \
tar -xjf libassuan-2.4.3.tar.bz2 && \
cd libassuan-2.4.3 && \
./configure && \
make && \
make install && \
cd ../
```

Installing libksba

```bash
wget -c  ftp://ftp.gnupg.org/gcrypt/libksba/libksba-1.3.5.tar.bz2 && \
wget -c ftp://ftp.gnupg.org/gcrypt/libksba/libksba-1.3.5.tar.bz2.sig && \
gpg --verify libksba-1.3.5.tar.bz2.sig && \
tar -xjf libksba-1.3.5.tar.bz2 && \
cd libksba-1.3.5 && \
./configure && \
make && \
sudo make install && \
cd ../
```
