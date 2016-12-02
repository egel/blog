Title:		How to partition your hard drive for Linux
Slug:			how-to-partition-your-hard-drive-for-linux
Date:			2016-12-01
<!-- Modified:	2016-12-01 -->
Status:		Draft
Category: Diary
Tags:			apache2, vim
Authors:	Maciej Sypień
<!-- Summary: Sample summary -->

<div class="intro-article-image-sm" markdown="1">
  ![Linux logo]({filename}/images/linux_logo_pinguin.jpg)
</div>



[github]: https://github.com


# Best partition scheme for linux

## Swap

| Amount of RAM  | Recomended                    | Recomenden for hibernation |
| -------------  |:-------------                :| ---------------------------:|
| > 2GB          | 2 times                       | 3 times of RAM |
| 2 - 8GB        | equal to amount of RAM        | 2 times of RAM |
| 8 - 64GB       | minimum 4GB                   | 1.5 times of RAM |
| < 64GB         | minimum 4GB                   | hibernation not recommended |


