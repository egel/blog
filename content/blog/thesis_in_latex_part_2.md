Title:      Thesis in LaTeX - part 2
Date:       2014-10-19 12:21:49
Modified:   2014-10-19 10:21:49
Lang:       en
Status:     published
Category:   Self improvement
Tags:       latex, university


<div class="intro-article-image-md" markdown="1">
  ![LaTeX logo]({filename}/images/LaTeX_logo.png)
</div>

I assume, that at the moment of reading this second part of writing thesis in
LaTeX, you have allready red the previous part:
[Thesis&nbsp;in&nbsp;LaTeX&nbsp;part&nbsp;1]({filename}thesis_in_latex_part_1.md)
and install required software. If you do, then perfect carry on, but if not you
should catch up.

I this part I will try to make some very basic introduction **How to use LaTeX in
practice**. But it will not be so easy - not by writing, because paper can take
everything. The real thing hides into a simple question:

> How condense a huge knowledge in acceptable short time for average person.

You can not read this article for more then 5 days, that is obvious ;) In this
time you could read few book in this time and far more detailed then my article.
But this series of articles have some advantages over other publications I have
met till writing this post. Books are solid knowledge - articles by its
definition should be short.

My main goal for this series is to assure and show you, that creating thesis in
LaTeX is **the best you can get in reasonable period of time**. I assume that if
you are reading this article you are probably woring on your thesis or
considering how to start writing.

By the way, if you are interesting to work as scientists or any technical
person, this quote below might be inspiring for you to make a good decision ;)

> "LaTeX is the de facto standard for the communication and publication of
> scientific documents." - Get from official LaTeX webpage
> <https://www.latex-project.org/>

I agree, LaTeX can be scary, with its complex examples and "programming" syntax,
but to be honest those examples are usually very rare for average documents. In
this part I will only guide you though the basics of LaTeX and point the best
practices which I discovered during few years of writing - It will be a very
good starting point for you.

## Learning of creating basic document
TeX is a compiling type of text processor. In plain words that means it
generates from source files the final product (whatever it would be `*.dvi`,
`*.pdf` or whatever it might be) and during this process it creating some helping
meta files to achieve this final result. So please, do not panic if among your
source files, some another will arise - that is norm for LaTeX.

I recommend to start by creating new folder with some obvious name for you (and
you, after a while). I would use `yourFirstName_yourLastName_thesis`. This file
saved into a folder should lay into a location easy get - because you will we
regularly use it. As a programmer I usually use `~/workspace` as a container of
my projects (most git project), but any other reasonable location is also fine,
for example like: `~/Desktop`. It should be easy access for you.

So we have got folder location for your thesis. This is imporant, because LaTeX
generate many meta files while preparing final result - in our way is acctually
a PDF file. That is structure of files is essential for your health and your
project.

The most commonly used files we will create and maintain during writing are:
`.tex` and `.bib`.  The `.tex` is acctually a plain text files with TeX marcos
inside, the `.bib` files are related with bibliography and store all positions
which can be used (or not) in our thesis. The `bib` files can be understood as
our bibliography management files and they can be used in many other documents.

We create 4 simple text files:

*   `main.tex`
*   `chap_one.tex`
*   `chap_two.tex`
*   and `chap_three.tex`

The first one (main.tex) will store our document configuration and order files
will represent out chapters in the thesis.

> It is good practice to separate chapters to different files, mainly for for
> further quick enable/disable, changing the order of chapters or if you write
> document with other people, they can focus only on theirs part without
> conflicts into document.

As you probably notice, the names of files which represents chapters begins with
`chap`. It is not required to work (because you can put any name to files), but
this convention is also known as namespace or pointers and is commonly used in
LaTeX documents - more on [LaTeX labels and cross referencing][wiki-latex-labels-and-cross-ref].

The namespace **chap** stands for a chapter and is well helps with multiple
elements that you can create in LaTeX, but more details about this we will cover
later.

### Preamble and actual document
Any each new document whether is an `article`, `report`, or perhaps a `book`
(There is a number of different ready-made patterns) consists normally of
so-called **preamble** and the **document**.

> This name `document` can be tricky at first time, because in lazy thinking any
> document is a document. But into the meaning of LaTeX, this refers to content
> of a document written by human, the author - and that is truly reasonable.

Preamble
:   This is a collation of rules which program must know before it generate
final document.

Document
:   This is a place where author writing a text of document and using proper
commands for formatting text.

The standard and also the simplest preamble (not quite for thesis) looks similar
to this below:

```latex
\documentclass[12pt, oneside, a4paper]{report}
\usepackage[OT4, plmath]{polski}  % definition of using platex
\usepackage[utf8]{inputenc}       % UTF-8 for multiple languages
\usepackage[OT4]{fontenc}
\usepackage{url}
\title{Project and implementation of content management system}
\author{Maciej Sypień}
\date{\today}
```

The most commonly, the preamble is being inserted into the main file of our work,
that is, in our case, the `main.tex` file. The name can be any other as you like
but for conventionally this is the name for main file.
Chapters will contain only the content of the document (without preamble),
because they will be directly included to the main document - it helps a lot in
further steps.

It is worth mentioning something about classes. Class is in short a set of rules
that define how the document will look like. LaTeX already contains predefined
classes, for example, a few of them are mentioned earlier:

*   book
*   report
*   article
*   letter


Fairly well illustrated this a line
`\documentclass[12pt, oneside, a4paper]{report}` which is clearly written a
definition of class `report` and its optional arguments as **font size**, **type
of printing** and **the document size** of the resulting paper.

This is only a small part of the wide range of available options, because each
of these classes (book, report, etc.) may contain the same optional arguments,
but also other not defined in any of the core classes.

These words are not in order to frighten you, but to advice that it is sometimes
refer to the documentation used class. While yet another thing is the fact that
often the newly created class tend to be very poorly documented and usually due
to lack of time to maintain it properly.

The second part of the content of document. From the writer point of view this
is most important, because it contains content that appears later in the output
file. That part of the file is one of the easiest to define because it looks
like the example below:

```latex
\begin{document}
\maketitle

\begin{abstract}
Dokument ten prezentuje kilka zasad składu tekstu w~systemie \LaTeX.
\end{abstract}


\chapter{Nasz pierwszy rozdział}
% pierwsza sekcja
\section{Tekst}\label{sec:tekst}
\LaTeX\ ułatwia autorowi tekstu zarządzanie numerowaniem sekcji, wypunktowaniami oraz odwołaniami do tabel, rysunków i~innych elementów. W~łatwy sposób możemy się odwołać do wzoru \ref{eqn:wzor1}.

% sekcja
\section{Matematyka}\label{sec:matematyka}
Poniższy wzór prezentuje możliwości \LaTeX\ w~zakresie składu formuł matematycznych. Wzory są numerowane automatycznie, podobnie jak inne elementy o~których mowa w~sekcji~\ref{sec:tekst}.

\begin{equation}
  E = mc^2,
  \label{eqn:wzor1}
\end{equation}

gdzie

\begin{equation}
  m = \frac{m_0}{\sqrt{1-\frac{v^2}{c^2}}}.
\end{equation}

% --------------------------------------

\chapter{Nasz drugi rozdział}
Bardzo długa treść rozdziału drugiego.

\section{Sekcja rozdziału drugiego}
\label{sec:sekcjaRozdzialuDrugiego}
Bardzo długa treść sekcji rozdziału drugiego.

\subsection{Podsekcja sekcji rozdziału drugiego}
\label{subsec:podsekcjaRozdzialuDrugiego}
Bardzo długa treść podsekcji rozdziału drugiego.

% --------------------------------------

\chapter{Nasz trzeci rozdział}
Bardzo długa treść rozdziału trzeciego.

\section{Sekcja rozdziału trzeciego}
\label{sec:sekcjaRozdzialuTrzeciego}
Bardzo długa treść sekcji rozdziału trzeciego.

\subsection{Podsekcja sekcji rozdziału trzeciego}
\label{subsec:podsekcjaRozdzialuTrzeciego}
Bardzo długa treść podsekcji rozdziału trzeciego.

\end{document}
```

Above snippet contains the actual content of the document and you have probably
noticed that the actual content begin phrase `\begin{document}` and end
`\end{document}`. But one big file can be difficult to edit and navigate into it.
So I have to talk about how to split whole document into smaller peaces and also
why it so important.

### Split document for smaller peaces
As I mention before, we will be interesting to divide our documnet into smaller
part that every single chapter will be put into separate file.

The file `main.txt` should look like this:

```latex
\documentclass[12pt, oneside, a4paper]{report}
\usepackage[OT4, plmath]{polski}                % definicja użycia platex
\usepackage[utf8]{inputenc}                     % kodowanie na UTF-8
\usepackage[OT4]{fontenc}
\usepackage{url}
\title{Projekt i implementacja autorskiego systemu zarządzania treścią}
\author{Maciej Sypień}
\date{\today}

\begin{document}
\maketitle

\begin{abstract}
Dokument ten kilka podstawowych zasad składu tekstu w~systemie \LaTeX.
\end{abstract}

\tableofcontents
\clearpage

\include{chap_wstep}
\include{chap_rozdzial_1}
\include{chap_rozdzial_2}
\include{chap_rozdzial_3}

\end{document}
```

As you see, main file of our document is simple, cleat and well readable. Every
chapter is attached by `\include{}` command - and yes it can be written also
without additional `.tex` extension ;) It is very comfortable, because writer
can clearly read the file name and to not be bothered by the its extension.

But back to ours chapters. Each of them begins usually. You just write what you
need, to fill the content. For better visualization of this situation I will
paste some snippets.

Prolog, **chap_prolog.tex**:

```latex
\chapter{Wstęp}
Tu będzie się znajdować wstęp do naszej bardzo obszernej pracy ;)
```

First file, **chap_1.tex**:

```latex
\chapter{Nasz pierwszy rozdział}
% pierwsza sekcja
\section{Tekst}\label{sec:tekst}
\LaTeX\ ułatwia autorowi tekstu zarządzanie numerowaniem sekcji, wypunktowaniami oraz odwołaniami do tabel, rysunków i~innych elementów. W~łatwy sposób możemy się odwołać do wzoru \ref{eqn:wzor1}.

% sekcja
\section{Matematyka}\label{sec:matematyka}
Poniższy wzór prezentuje możliwości \LaTeX\ w~zakresie składu formuł matematycznych. Wzory są numerowane automatycznie, podobnie jak inne elementy o~których mowa w~sekcji~\ref{sec:tekst}.

\begin{equation}
    E = mc^2,
    \label{eqn:wzor1}
\end{equation}

gdzie

\begin{equation}
    m = \frac{m_0}{\sqrt{1-\frac{v^2}{c^2}}}.
\end{equation}
```

Second file, **chap_2.tex**

```latex
\chapter{Nasz drugi rozdział}
Bardzo długa treść rozdziału drugiego.

\section{Sekcja rozdziału drugiego}
\label{sec:sekcjaRozdzialuDrugiego}
Bardzo długa treść sekcji rozdziału drugiego.

\subsection{Podsekcja sekcji rozdziału drugiego}
\label{subsec:podsekcjaRozdzialuDrugiego}
Bardzo długa treść podsekcji rozdziału drugiego.
```


Third file, **chap_3.tex**

```latex
\chapter{Nasz trzeci rozdział}
Bardzo długa treść rozdziału trzeciego.

\section{Sekcja rozdziału trzeciego}
\label{sec:sekcjaRozdzialuTrzeciego}
Bardzo długa treść sekcji rozdziału trzeciego.

\subsection{Podsekcja sekcji rozdziału trzeciego}
\label{subsec:podsekcjaRozdzialuTrzeciego}
Bardzo długa treść podsekcji rozdziału trzeciego.
```

Dividing of our whole document into separate fragment did not bring us some
astonishing results (just for now), you will appreciate these changes when these
files (chapters) grow. This allows you to better work organization while writing
(ex: when you want to omit some chapters, you just comment `\include{}` command
with `%` sign, compile document and done.

<a href="https://www.sharelatex.com/project/543aad2f69870b1d3e39c26b" title="Pełny przykład online" class="btn btn-primary">Pełny przykład online</a>

I think that pretty much it for this part. Thank you for attention and leave
comment if you like this.

* * *

But if you do not hate LaTeX yet, and you still want to get know it better I
will be peased to invite to to next, third part and it will contain:

*   we will discuss about LaTeX{}'s elements (environments)
*   how to add and use new packages
*   basic **good practices** during writing in LaTeX
*   and we will make the title page for our thesis

...well, fun will be guarantee ;)


 [1]: http://blog.egel.pl/praca-dyplomowa-w-latex-cz1/
 [wiki-latex-labels-and-cross-ref]: https://en.wikibooks.org/wiki/LaTeX/Labels_and_Cross-referencing
