Title:		Git pre commit email blocker
Slug:			git-pre-commit-email-blocker
Date:			2017-03-20
Status:		Draft
Lang:     en
Category: Diary
Tags:			git, terminal
Authors:	Maciej Sypień


```shell
#!/bin/sh
#
# An example hook script to verify what is about to be committed.
# Called by "git commit" with no arguments.  The hook should
# exit with non-zero status after issuing an appropriate message if
# it wants to stop the commit.
#
# To enable this hook, rename this file to "pre-commit".

WHITE_LIST=''
accept_email() {
  CURRENT_USER_EMAIL=$(git config --list | grep user.email | awk -F"=" '{print $2}')
  substring="$1"
  if [ "${CURRENT_USER_EMAIL}" != "${substring}" ]; then
    printf "Not match" > /dev/null
    WHITE_LIST="${WHITE_LIST}\n> ${substring}"
  else
    exit 0
  fi
}

accept_email "maciejsypien@gmail.com"
accept_email "maciej.sypien@gmail.com"

printf "Your current git user.email <%s> NOT MATCH any approved emails\n" "${CURRENT_USER_EMAIL}"
printf "%b\n\n" "${WHITE_LIST}"
printf "Check ~/.gitconfig for more\n"
exit 1
```


[github]: https://github.com

