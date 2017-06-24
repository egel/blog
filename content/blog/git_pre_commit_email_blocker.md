Title:	    Git pre commit email blocker
Slug:       git-pre-commit-email-blocker
Date:       2017-03-20
Modified:   2017-06-23
Status:		  Published
Lang:       en
Category:   Diary
Tags:       git, terminal
Authors:	  Maciej Sypień
Summary:    Presenting a simple solution that allows only selected git users to commit in local copy of repository.

Since quite a while Git exists in the big market of software development. Many users using it in the daily basis as standard way of committing their work for employer and it also became de facto standard way of developing in the Open Source world.

I also very much like using Git, but after time I discover my way of working with git especially when need to commit many parts for different employers and almost all the time I have at least 2 local git user (do not confuse with gitlab/github or other user accounts).

Due to usually many employers require a specific company credential while communicating with their main repository server, so I figured out that I can have multiple users in same file, but activate each when I need it.

```config
# ~/.gitconfig

[include]
  # For user, email, ect.
  ; path = ~/.gitconfig.local   # ; make configuration inactive
  path = ~/.gitconfig.local_work
```

```config
# Private configuration
# ~/.gitconfig.local

[user]
	name = Maciej Sypień
	email = firstname.lastname@example.com

[github]
	user = githubUsername
```

```config
# Public work configuration
# ~/.gitconfig.local_work

[user]
	name = Maciej Sypień
	email = firstname.lastname@workmail.com
```

This simple solution give me an opportunity to have multiple Git local users with different credentials hidden into files `~/.gitconfig.local_<company>` and it can be used for my personal accounts, or for specific employers - the field of usage is almost endless.

When I want to switch between different users (for example I am doing something for my personal stuff at weekend and on Monday morning using same laptop begin my work as employer of company ABC) I just commit `~/.gitconfig.local` and enable specific config for work `~/.gitconfig.local_work`.

But hey, no one is infallible, and many times I commit as a wrong user to some repository that I should not commit from personal email address. Therefore, since a while, I wondered:

> "How to disable some not authorized git users to commit in selected local repositories".

There are so many ways how to achieve this task, but I decide to user Git's hooks feature and I wrote simple program, which checks locally enabled Git user's email before a real user will commit.

This simple solution may save a lot of your time (and potential rebase) especially when real user (you) have multiple git accounts - for example when you're a freelancer (or project manager) and you need to commit to multiple projects as completely different git user for some reasons.

So what might be some solution to this problem?

### Solution
Below I present some solution and how to implement it using simple pre-commit hook script into any git repository which using git higher then v1.8.4.

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

What it does? Basically before each commit (`git commit -m "whatever"`) it checks what are allowed email addresses for this repository and allow or reject user with information that only specific group of emails are allowed to commit in this repository.

#### Installation
Save above snippet save as `.git/hooks/pre-commit` into your git repository and **do not forget to make the file executable** `chmod +x .git/hooks/pre-commit`. Modify the list of email addresses and that's it.

Now you can be happy git user with simple pre-commit email guardian :)

[github]: https://github.com

