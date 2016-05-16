Title:      Git push guardian
Date:       2016-05-16
Lang:       en
Status:     published
Category:   Self improvement
Tags:       git, terminal
<!-- Summary: -->


<div class="intro-article-image-md" markdown="1">
  ![LaTeX logo]({filename}/images/git_logo-mini.png)
</div>

Recently I wondering how to improve my workflow with Git. I came across the Web
and found some article which pointed on git hooks and were introduced in
version 1.8.2.

That cool feature, allows to execute some code before/after some actions made in
git. My team have decided that we will compleate our tasks into feature branches,
and to do it so, we mark our main branches: `master`, `stage` and `develop` as
protected. That means, only users with master access or grater (for repository),
can push directly to this branches. I have that privilage, but switching between
so many branches, checking, pushing, checking, pushing - this all can confuse a
mind for a second.

Than I realize, if there any available option to prevent important actions (like
push) on those protected branches. And puff...there git hooks came in on the
stage.

## Guardian Script
With some examples on web and git documentation, I wrote simple git **pre-push**
script that will check on which branch you are in and it will ask you "Are you
intend to push?" to those protected branches.

Full script are available into my gist on github - [HERE][gist-pre-push], but
also paste this snippet here to complete the article.

### Implemented features:
- Array with protected branches (easy to maintain)
- Base terminal colors to improve visibility
- Question that only work when confirm with enter (time to wonder it is correct action)
- Default value of question set to `No`
- Message of committed action

### Things which may be improved in the future:
- Download list of protected branches direct from repository
- Add support for some popular flags like: `--force`

```bash
#!/bin/bash

# General colors
black='\x1B[0;30m'
red='\x1B[0;31m'
green='\x1B[0;32m' # '\e[1;32m' is too bright for white bg.
blue='\x1B[1;34m'
yellow='\x1B[0;33m'
purple='\x1B[1;35m'
cyan='\x1B[0;36m'
endColor='\x1B[0m'


protected_branches=( master develop )
current_branch=$(git symbolic-ref HEAD | sed -e 's,.*/\(.*\),\1,')

for i in "${protected_branches[@]}"
do
  if [ ${i} == ${current_branch} ]; then
    echo -en "${yellow}[Git pre-push]${endColor} You're about to push to ${red}${i}${endColor}, is that what you intended?"
    read -p " [y/N] " -r < /dev/tty
    if echo ${REPLY} | egrep -E '^[yY]$' > /dev/null
    then
      echo -e "Continue of pushing to ${red}${i}${endColor}"
      exit 0 # push will execute
    fi
    echo -en "Abort pushing to ${red}${i}${endColor}\n"
    exit 1 # push will not execute
  fi
done
exit 0 # push will execute when won't match protected_branches
```

  [1]: http://technology.blurtit.com/114838/what-is-a-basic-difference-between-a-notepad-and-microsoft-word
  [gist-pre-push]: https://gist.github.com/egel/2058f19cf78df84ade741b7a77a38006
