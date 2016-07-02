Title:      Thesis in LaTeX - part 1
Date:       2014-10-12 19:00:05
Lang:       en
Status:     published
Category:   Self improvement
Tags:       latex, university
<!-- Summary: -->


<div class="intro-article-image-md" markdown="1">
  ![LaTeX logo]({filename}/images/LaTeX_logo.png)
</div>

In one simple sentence, LaTeX it is an extension of TeX language, although TeX
in real life is a collation of macros. This is not a official definition, rather
some sort of visualization - but what it is actually, we will get later.

I say this all, because in this small series of articles I will talk about how
to make a professional thesis and during this process not catch breathless or
get bald ;)

This part is basically an introduction to text processing. I will compare
commonly known Word/Writer text preprocessors with LaTeX one. Furthermore I will
say a bit, why LaTeX is actually better option for this kind of documents
(documents longer then 10-15 pages, like semester assignments, long scripts and
thesis of course).

You will not find this type of knowledge anywhere in so easy and condensed
version, so if you are interested, lets get start! :)

### Listen and learn on mistakes of others
I can honestly say that my first chapter of Bachelor's dissertation went very
smooth and petty quick while writing in MS Word. Yes, I was surprised that in
few days I have 20+ pages. Then I sent my work to my supervisor to make some
corrections and point weak points of my 1st chapter, meanwhile I wrote few pages
more of next chapter (second one) and correct many sentences from the first
chapter (this one I already sent to my supervisor). Then few days later I get my
corrected first chapter from the supervisor. Now begins interesting part, I start
wondering:

> How can I implement appropriate version from supervisor with changed content I
> have fixed in the meantime?

If you, just like me before start wondering about this you probably noticed
that, this can become a huge problem, if you do not want to spend few more hours
to track every change from corrected version of first chapter from your
professor. Trying solving this problem using just MS Word to fix this makes me
fill dizzy. Believe me or not, but this kinds of problems if you use MS Wors or
LibreOffice Writer, can be just a tip of iceberg.

But hello, no worry :) These are just warnings for you and that is why I am
writing this series of articles. I also can assure you that I have solved almost
all of this kings of problems only if you are not afraid of learning new things
;)

### WYSIWYG or WYSIWYM
It can not be so obvious for all, but Word/Writer are programs of WYSIWYG type
(What you see is what you get). It means that every change in document you will
make affect on document you will receive finally. For example if you type a
sentence and in some part of this sentence you will put 7 spaces, you will get a
final document with those 7 spaces. This is obvious behavior for WYSIWYG
editors.

This is very convenient way of typing if you write a short document 3-8 pages
max - that is essential! This is why Word has been so popular. But you can
probably think:

> I can write as many pages as I want into Word/Writer and it's very easy, isn't
> it?

Yes and no. It is very easy to write into Word/Writer, but only for short
distance.  You can also write as many pages as you want, if you do not care
about migrating or potential loosing this data in future. The Word's documents
like `.docx` it is not a plain text, it is actually an archive of multiple
sub-objects. If you do not believe me, open some `.docx` in any archive program
to make sure.

Also as I mention in the heading that LaTeX is an extended version of TeX, but
TeX is not actually a programming language, though set of macros that helps you
type better. LaTeX is a WYSIWYM (What you see is what you mean) type of editor.
In other words this means that the writer can concentrate on content that he is
writing, rather then playing with changing the type of font, size, color or
other stuff useless at the moment of writing. That is a true advantage of many,
which LaTeX has, but usually not seen nor appreciated by people. That is because
when you want to write, you should write, not correcting the size of font of
chapter or section.

### My mistakes during first approach
After writing my BA thesis in Word (yes, shame on me) I can honestly point a few
problems that I met during writing and are worth to mention here:

*   During writing I constantly and accidentally changing or removing a style,
    probably by some default shortcut.  (Usually whole document has changed and
    I did not notice it in reasonable time!)
*   Using and defining tons of styles for a document (for a font of subscript,
    heading 1,2,3..., quoted text, the chapter without numbering... - it is a
    horror, even for those who constantly writing in Word, but what about if you
    want to make a break 2 weeks. You will probably forget what style do what
    and what its name)
*   Clicking on some random, unidentified keybindings can call some default
    exotic Word's shortcut and if you did not noticed it on time, it can make
    you, to check all document that nothing has changed for your previous work.
    (You have no info log that some has been changed)
*   Sometimes I have noticed that some objects just disappear from the scree
    or has been modified without my conscious action on it (It might was a bug
    in software).
*   Making copy of current work. I have saved my work in endless
    list of `name` + (`version` or `date`) + `.docx`. Then my folder with thesis
    files contain almost 100 files and next one was always bigger then previous
    one. And at the end, first document had 0.3KB and the last one 2.8MB.
    (That is waist of disc space, moreover you have no idea which document
    amongs all backup copies has desired part of thesis because any part of your
    document can constantly evolving)
*   Managing bibliography in Word is a horror, even with additional bibliography
    managers (What? Additional managers for private software? That is wrong or
    Word was not meant to be a tool for writing long documents with multiple
    bibliography sources.). Or even if you can do it all in some basic Word
    tool, learning how to do into LaTeX is far more simpler and better in final
    result (I have not met sharing bibliography between documents in
    Word/Writer editors, but even if it might exsist somewhere it is )

Those were a few irritating things I came across while writing in any kind of
WYSIWYG editor a document that is longer then 10-15 pages (2-4 are easy, 5-9 are
medium, but 9-15 are hard to maintenance, and 15 pages is absolute maximum for
fluent writing documents into WYSIWYG).

I thought a lot, why this kind of mistake happen to me. Firstly I wonder that
these problems happens to me, because I am a perfectionist type of person -
everything should (not must) be in order. But in time I realize that was not me
- I was perfectly fine and still I am - I just choose wrong tools for this job.
**So, that why the tools you use in this type of things are relevant.**


### If tools matters, so which should I use?
This is also not easy question, because it depends on what style of typing you
like the most. I have met so many types of person on my way, that I can in
general determinate 2 kind of person which are faced to learn LaTeX.

1.  **"Sure, I'll try"** - this types of persons are usually open to new things,
    even if this new stuff can be a pain for first days/weeks of work with it.
2.  **"I'll not do this"** - this types of persons are true conservationists.
    They usually knew what they knew and they do not want to change this state.

This is just results of my observation when I show the sample text written in
LaTeX to them. If you are in first group, that is good, but if you assign
yourself to the second group, you will probably suffer a lot during writing
completly new things with LaTeX. There is probability that LaTeX will not suite
you.

I also must say that writing in LaTeX is that kind of writing which looks
"programming" like (in large part of opinions). Most of time you will spend
using usual text editor. And to be more precise by text editor I mean [SDI not
MDI][1].  This is very important basic knowledge. Well if you do not know,
take your time, read this article and find it out. I will wait for you here :)

Ok. So, to start writing in LaTeX you will need basically, a **TeX library**
(TeXlive, MikTeX or MacTeX) and simple text editor. TeX libs are a standard
libraries. You will install one them based on which operating system you
have (Linux, Windows or OSX), but what is for what I will say later.

### Text editors
By writing this heading I feel, like I just put a stick in an anthill. *Why?*
This topic is so huge, that I am afraid, even a few big books could not
completely fulfill all its aspects about text editors.

Although I can get you a fair start. I will point you 2 best articles about
comparison of multiple text editors (includes some IDEs) and also say which
editors I like the most till this moment and why I like them. I think is the
fare start.

Take a peak on below websites:

*   <http://tex.stackexchange.com/q/339/48903> - This is the most rich source of
    knowledge I have came across till now. You will find there REALLY smart
    comparison for almost any popular editor you can choose from.
*   <https://en.wikipedia.org/wiki/Comparison_of_TeX_editors> - yes, it is wiki,
    I know, but this article has outstanding comparison table. It is also worth
    to look which editor suites you the most.

I like two editor the most. Among LUI type I definitely prefer
[Vim][vim-webpage] with [latex-suite][latex-suite-website] plugin. If you want
to start with using Vim I can recommend my [dotfiles][egel-dotfiles] not as a
ready-made solution (although it also can work in this way), but as a handy help
to begin your journey with Vim. If you are wondering or hesitating (like I was)
it is worth to begin long learnign journey with Vim I highly suggest you to read
my another article called
[Is&nbsp;worth&nbsp;to&nbsp;know&nbsp;the&nbsp;Vim&nbsp;editor&nbsp;an&nbsp;why]({filename}is_worth_to_know_the_vim_editor_and_why.md).

From the GUI type, my favorite one is [TeXstudio][texstudio-webpage] and here I
write another article
[How&nbsp;to&nbsp;configure&nbsp;TeXstudio]({filename}configure_texstudio.md)
where I describing how to smoothly start with this program and why use it for
writing LaTeX. I also very like [Sublime&nbsp;Text&nbsp;3][sublime3-webpage],
although it has more common with usual text editor then with special LaTeX IDE.
And here I write my thoughts
about [Discover&nbsp;the&nbsp;Sublime&nbsp;Text&nbsp;3](discover_the_sublime_text_3.md)

I will not try to convince you which one is better, because it basically does
not matter. You can follow my footsteps and try one of those, which I mention
before.  Nevertheless decision which one to start with, I am laying on your
hands.

I hope you will not be disappointed, because as a programmer I have my writing
standards, that are important to me during daily work. Those editors have
gorgeous features (especially Vim) that is why I use them even after work for my
personal purposes.  But unfortunately they are have not candy-like appearance if
you demand this from modern editors.

### Online alternatives vs local TeX library
Nowadays we are not obligate to use only locally installed programs. There are
few online tools, which can replace editor and TeX compiler only by entering
website. One is Overleaf and another is Sharelatex. I intentionally not given
links, because I am not taking some benefits by promoting those services. I just
want to say that there are similar alternatives that might suite you, but most
interesting features like git integration, will demands from you an extra charge
(or buying subscription).

We can achieve all this with much more high security level without paying
anything (only for amortization of you computer and electricity). And here you
have:

**Why is better to have it locally then in one of those services?**

*   Working offline
*   Much more faster compiling on local machine
*   Your data is on your hard drive (some services have in regulations that
    if it free account your work can be treated as the property of them)
*   If you want you can secure loss of data with version control systems like
    [Git][git-website]
*   Free, unlimited collation using version control systems
*   If afraid that your computer can broke down during work, you can secure data
    with any instant cloud store synchronization (dropbox or mega). TeX files
    are just text files, so they are small and light, ideal to be quickly
    synchronized.

### Installing standard TeX library
This part should be peace of cake to you if you get here (I realize that it
could have been difficult, because many things has been said this positive and
negative).

There are 3 most popular standard TeX libraries (for Linux, Mac OSX and
Windows):

*   [Texlive][texlive-webpage] - available on Linux
*   [MacTeX][mactex-webpage] - for Mac OSX
*   [MikTeX][miktex-webpage]  - for Windows

For Windows and Mac OSX installation is trivial. You are downloading the
installer, follow the wizard and that is all.

> In this moment I highly recommend to install full library. We live in times
> that 1-2GB of data are no longer a problem. Full installation can prevent
> LaTeX beginners from "no installed package" errors (some packages are
> differently named, name of package and name of used library, so sometime can
> be difficult to debug).

For Linux users full installation looks even simpler:

    :::shell
    # Debian based systems
    sudo apt-get install texlive-full biber

And that is all for this part. You have received IMHO the best information how
to start with LaTeX. Also obtain answers for those questions that are not easy
to get.

### Next part
But how to start building a LaTeX thesis, I will discuss on next article [Thesis
in LaTeX - part 2]({filename}thesis_in_latex_part_2.md).  I will based on my
implementation of [uekthesis][uekthesis-repo] class which I created for my
university: Cracow University of Economics, but it can be modified and adjust
for any other University in a fly.

  [1]: http://technology.blurtit.com/114838/what-is-a-basic-difference-between-a-notepad-and-microsoft-word
  [git-website]: https://git-scm.com/
  [egel-dotfiles]: http://github.com/egel/dotfiles
  [uekthesis-repo]: https://github.com/egel/uek-latex-thesis-class
  [vim-webpage]: http://www.vim.org/
  [latex-suite-website]: http://vim-latex.sourceforge.net/
  [texstudio-webpage]: http://www.texstudio.org/
  [sublime3-webpage]: https://www.sublimetext.com/3
  [texlive-webpage]: https://www.tug.org/texlive/
  [miktex-webpage]: http://miktex.org/
  [mactex-webpage]: https://tug.org/mactex/

