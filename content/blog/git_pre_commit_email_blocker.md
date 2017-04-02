Title:	    Git pre commit email blocker
Slug:       git-pre-commit-email-blocker
Date:       2017-03-20
Status:		  Published
Lang:       en
Category:   Diary
Tags:       git, terminal
Authors:	  Maciej Sypień
Summary:    Presenting a simple solution that allows only selected git users to commit.

Since a while, I wondered "how to disable unauthorized git users to commit" for selected repositories. There are many ways how to achieve this task, but in few hours I wrote simple program which (under the hood use git hook) checks git's user email before a real user will commit change.

This simple solution and it may save a lot of time (and potential rebase) especially when real user (you) have multiple git accounts - for example is a freelancer and commit to multiple projects.

### Solution
Below I present the solution and how to implement this into repository.

```shell
#!/bin/sh
#
# An example hook script to verify what is about to be committed.
# Called by "git commit" with no arguments.  The hook should
# exit with non-zero status after issuing an appropriate message if
# it wants to stop the commit.
#
# To enable this hook, rename this file to "pre-commit".

WHITE_LIST=""
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

accept_email "john.doe@example.com"
accept_email "johndoe@example.com"

printf "Your current git user.email <%s> NOT MATCH any approved emails\n" "${CURRENT_USER_EMAIL}"
printf "%b\n\n" "${WHITE_LIST}"
printf "Check ~/.gitconfig for more\n"
exit 1
```

#### Installation
Save above snippet as `.git/hooks/pre-commit` into your git repository and **do not forget to make the file executable** `chmod +x .git/hooks/pre-commit`.

[github]: https://github.com

