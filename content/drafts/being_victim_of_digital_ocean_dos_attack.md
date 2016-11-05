Title:		Being a victim of Digitalocean DOS attack
Slug:			being-a-victim-of-digitalocean-dos-attack
Date:			2016-09-21
Status:		Draft
Category: Diary
Tags:			linux, console
Authors:	Maciej Sypień
<!-- Summary: Sample summary -->

<div class="intro-article-image-sm" markdown="1">
  ![Linux logo]({filename}/images/linux_logo_pinguin.jpg)
</div>

Few days ago it was a weird situaltion on my DO server - it become a attacker of denile of service.

When super scripts of DO discover my little server with 512MB of RAM. My server has been cut out from connection to the Internet, but I was still charged with full amount - it was not much, but hey, I hire this VPS mainy to have a cheap server with connection to the Internet! If I want a simple server with similar amount of RAM I would buy Raspberry PI and connect only to a power adapter without accessing to Internet.

### How to backup you data?

At first, check if your connection to your server have been closed. Just ping it from your PC like that:

```bash
ping <Your server IP>
```

At first need to backup your all databases so we need to use `mysqldump`

```bash
mysqldump -u root -p --all-databases > alldb.sql
```


[github]: https://github.com

