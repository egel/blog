Title:      Thesis in LaTeX - part 1
Date:       2014-10-12 19:00:05
Modified:   2014-10-12 17:00:05
Lang:       en
Status:     published
Category:   Self improvement
Tags:       latex, university
<!-- Summary: -->


<div class="intro-article-image-md" markdown="1">
  ![LaTeX logo]({filename}/images/LaTeX_logo.png)
</div>

In one simple sentence, LaTeX it is an extension of TeX language, although TeX
in real life is a collation of macros. This is not a real definition, rather
some sort of visualization, but what it is actually, we will get later.

I say this all, because in this small series of articles I will talk about how
to make a professional thesis and not catch breathless or get bald ;)

This part is basically an introduction to text processing. I will compare
commonly known Word/Writer text preprocessors with LaTeX one. Furthermore I will
say a bit, why LaTeX is actually better option for this kind of documents
(documents longer then 10-15 pages, like semester assignments and yes...thesis).

You will not find this type of knowledge anywhere in so easy and condensed
version, so if you are interested, so lets get start! :)

### Listen and learn on mistakes of others
I can honestly say that my first chapter of Bachelor's dissertation went very
smooth and petty quick. Yes, I was surprised that in few days I have 20+ pages.
Then I sent my work to my supervisor to make some corrections and point weak
points, meanwhile I wrote more pages of next chapter (second) and correct many
sentences from first chapter (this one I already sent to my supervisor). Then
few days later I get my corrected first chapter.  But then I wonder how can I
implement appropriate version from supervisor with changed content I have fixed
in the meantime?

If you wonder a while about previous paragraph, this can become a huge problem,
if you do not want to spend few more hours to track every change from corrected
version of first chapter from your professor (this before your fixes).  Stop!
This makes me dizzy - you say. Yes I agree with you, but believe me, it can be
just a tip of iceberg.

But hello, no worry :) This is why I am writing this series of articles and I
can assure you that I have solved almost all of this problems if you're not
afraid of new things.

### WYSIWYG or WYSIWYM
It can not be so obvious for all, but Word/Writer is program of WYSIWYG (What
you see is what you get) type. It means that every change in document you will
make affect on text you will receive finally. For example if you type a sentence
and in some part of this sentence you will put 7 spaces, you will get a text
with those 7 spaces.

This is very convenient way of typing if you write a short document 3-8 pages
max. This is why Word has been so popular. But you can probably think:

> I can write as many pages in Word/Writer as I want and it's very easy, isn't it?

Yes and no. It's very easy to write, but for short distance. You can also write
as many pages as you want, if you do not care about potential loosing this data
in future. The Word's documents like `.docx` it's not a plain text, it is
actually an archive of multiple sub-objects. If you do not believe me, open some
`.docx` in any archive program to make sure.

Also as I mention in the heading, LaTeX is an extended version of TeX, but TeX
is not actually a programming language, though set of macros that helps you type
better. LaTeX is a WYSIWYM (What you see is what you mean) type of editor. In
other words this means that the writer can concentrate on content which he
writing, rather then playing with changing the type of font, size, color or
other stuff useless at the moment of writing. That is a true advantage of many
which LaTeX has, but usually not seen nor appreciated by people. That is because
when you want to write, you should write, not correcting the size of font of
chapter or section.

### Mistakes during first approach
After writing my BA thesis in Word (yes, shame on me) I can honestly point a few
problems that is worth to mention here:

*   During writing I constantly and accidentally changing or removing a style.
    (Usually whole document has changed and I did not notice it in reasonable
    time!)
*   Using and defining tons of styles (for a font of subscript, heading
    1,2,3..., quoted text, the chapter without numbering... - a horror, even
    for those who writing it constantly, but what about if you want to make a
    break 2 weeks. You probably forgot what style do what and what its name)
*   Clicking on some unidentified keybinding can call some default exotic Word's
    shortcut and if you did not noticed it on time, it can make you, to check all
    thesis that nothing has changed for your previous work.
*   Sometimes I have noticed that some objects just disappear or has been
    modified without my conscious action on it.
*   Afraid of make hidden mistakes and just in case, I save my work in endless
    list of `name` + (`version` or `date`) + `.docx`. Then my folder of thesis
    contain almost 100 files and all next one was bigger then previous one.
    First one was 0.3KB, the last 2.8MB.
*   Managing bibliography in Word is a horror, even with additional bibliography
    managers (What? Additional managers for private software? That is wrong or
    Word was not meant to be a tool for writing long documents with multiple
    bibliography sources. Or if you can do it all, learn how to do in LaTeX is
    far more simpler and better in final look.)

Those were a few irritating things I came across while writing in any kind of
WYSIWYG editor a document that is longer then 10-15 pages (2-4 are easy, 5-9 are
medium, but 9-15 are hard to maintenance, and that is the maximum).

I thought a lot why this kind of mistake happen to my (lastly I write programs
daily and I did not have any of those problems before). Firstly I wonder the
most of those problem can appears to me, because I am a perfectionist type of
person - everything should (not must) be in order. But in time I realize that
was not me - I was perfectly fine and still I am - I just choose wrong tools for
this job. **So, that why the tools you use in this type of things are
relevant.**


### If tools matters, so which should I use?
This is also not easy question, because it depends on what style typing you like
the most. I have met so many types of person on my way that I can in general
determinate 2 kind of person.

1.  **"Sure, I'll try"** - this types are open to new things, even if this new
    stuff can be a pain for first days/weeks of work with it.
2.  **"I'll not do this"** - this types are true conservationists. They usually
    knew what they knew and they do not want to change this state.

This is just results of my observation when I show the sample text written in
LaTeX to them. If you are in first group you are good, but if you assign
yourself to the second group, you will probably suffer a lot (your EGO may not
agree with your mind and actions of your body)

I also must say that writing in LaTeX is a kind of writing that looks
"programming" like, in large part of opinions. Most of time you will spend in
usual text editor. And to be more precise by text editor I mean
[SDI not MDI][1].  This is very important and basic knowledge. Well if you do
not know, take your time and find it out, I will wait for you here :)

Ok. So, to start writing in LaTeX you will need basically, a **TeX library**
(texlive, miktex or mactex) and text editor. TeX libs are a standard, you
will install this type, which operating system you have, but what is for what
I will say later.

### Text editors
By writing this heading I feel, like I just put a stick in an anthill. *Why?*
This topic is so huge, that I am afraid, even a few big books can not completely
fulfill all its aspects.

Although I can get you a fair start. I will point you 2 best articles about
comparison of multiple text editors (includes some IDEs) and also say which
editors I like the most till this moment and why I like them. I think is the
fare start.

Take a peak on:

*   <http://tex.stackexchange.com/q/339/48903> - This is the most rich source of
    knowledge I have came across till now. You will find there REALLY smart
    comparison for almost any popular editor you can choose from.
*   <https://en.wikipedia.org/wiki/Comparison_of_TeX_editors> - yes, it is wiki,
    I know, but this article has outstanding comparison table. It is also worth
    to look which editor suites you the most.

I like two editor the most. Among LUI type I definitely prefer
[Vim][vim-webpage] with [latex-suite][latex-suite-website] plugin. If you want
to start with using vim I can recommend my [dotfiles][egel-dotfiles] not as a
ready-made solution (it also can work in this way), but as a handy help to begin
your journey with Vim. If you are wondering or hesitating it is worth to begin
this journey I highly suggest to read my another article called
[Is&nbsp;worth&nbsp;to&nbsp;know&nbsp;the&nbsp;Vim&nbsp;editor&nbsp;an&nbsp;why]({filename}is_worth_to_know_the_vim_editor_and_why.md)

From the GUI type, my favorite one is [TeXstudio][texstudio-webpage] and here I
write another article
[How&nbsp;to&nbsp;configure&nbsp;TeXstudio]({filename}configure_texstudio.md)
where I describing how to smoothly start with this program. I also like
[Sublime&nbsp;Text&nbsp;3][sublime3-webpage], although it has more common with
usual text editor then with special LaTeX IDE. And here I write my thoughts
about [Discover&nbsp;the&nbsp;Sublime&nbsp;Text&nbsp;3](discover_the_sublime_text_3.md)

I will not try to convince you which one is better, because it basically does
not matter. You can follow my footsteps and try one of those which I mention.
Nevertheless decision which one to start with, I am laying on your hands.

I hope you will not be disappointed, because as a programmer I have my writing
standards, that are important to me during work. Those editors have gorgeous
features (especially Vim) that is why I use them even after work for my personal
purposes.  But unfortunately they are have not candy-like appearance if you
demand this from modern editors.

### Online alternatives vs local TeX library
Nowadays we are not obligate to use only locally installed programs. There are
few online tools which can replace editor and TeX compiler only by entering
website. One is Overleaf and another is Sharelatex and I intentionally not given
links, because I not promote those services. I want to say that there are
similar alternatives, but most interesting features like git integration,
demands extra charge (or subscription).

We can achieve all this with much more high security level without paying
anything (only for amortization of you computer and electricity). Why is better
to have it locally then in one of those services?

*   Working offline
*   Much more faster compiling on local machine
*   Your data is on your hard drive (some services have in regulations that
    if it free account your work can be treated as the property of them)
*   If you want you can secure loss of data with version control systems like
    Git
*   Free, unlimited collation using version control systems
*   If afraid that your computer can broke down, you can secure data with any
    instant cloud store synchronization (dropbox or mega). TeX files are just
    text files so they are small and light, ideal to be quickly synchronized.

### Installing standard TeX library
This part should be peace of cake to you if you reach this part of article (I
realize that it could be hard, because many things has been said this good or
bad).

There are 3 most popular standard TeX libraries (for Linux, Mac OSX and
Windows):

*   [Texlive][texlive-webpage] - available on Linux
*   [MacTeX][mactex-webpage] - for Mac OSX
*   [MikTeX][miktex-webpage]  - for Windows

For Windows and Mac OSX installation is trivial. You are downloading the
installer, follow the wizard and you are done.

In this moment I highly recommend to install full library. We live in times that
1-2GB of data are no longer a problem. Full installation can prevent LaTeX
beginners from "no installed package" errors (some packages are differently
named, name of package and name of used library, so sometime can be difficult to
debug).

For Linux users full installation looks even simpler:

    :::shell
    # Debian based systems
    sudo apt-get install texlive-full biber

And that is all for this part. You have best information about which text editor
you can use and which TeX library to install. That is all you may need for now
to start writing in LaTeX.

### Next part
But how to start building a LaTeX thesis I will discuss on next article
[Thesis in LaTeX - part 2]({filename}thesis_in_latex_part_2.md).
I will based on my implementation of [uekthesis][uekthesis-repo] class created
for my university the Cracow University of Economics but it can be modified for
any other University in a fly.

  [1]: http://technology.blurtit.com/114838/what-is-a-basic-difference-between-a-notepad-and-microsoft-word
  [egel-dotfiles]: http://github.com/egel/dotfiles
  [uekthesis-repo]: https://github.com/egel/uek-latex-thesis-class
  [vim-webpage]: http://www.vim.org/
  [latex-suite-website]: http://vim-latex.sourceforge.net/
  [texstudio-webpage]: http://www.texstudio.org/
  [sublime3-webpage]: https://www.sublimetext.com/3
  [texlive-webpage]: https://www.tug.org/texlive/
  [miktex-webpage]: http://miktex.org/
  [mactex-webpage]: https://tug.org/mactex/

