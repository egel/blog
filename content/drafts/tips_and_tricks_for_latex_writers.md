Title:      Tips and tricks for LaTeX writers
Date:       2013-10-22
Status:     Draft
Category:   Hacks
Tags:       LaTeX
Summary:

Dear Reader, please be aware, because this post is not a LaTeX course. If you looking for some, please take a peek for [Free & Interactive Online Introduction to LaTeX](https://www.overleaf.com/latex/learn/free-online-introduction-to-latex-part-1).


#### How to make chapter without a number?
It's so simple. Just add `*` between `\chapter` and `{title}`.

    :::latex
    \chapter*{title}

> Becarefoul If add `*` to chapter it will be invisible for `tableofcontents` and other envirionments


#### How to make your landscape?

    :::latex
    \usepackage{lscape}
    ...
    \begin{landscape}
    \end{landscape}


#### To enter slash \ without the use of a mathematical mode?

    ::: latex
    \ textbackslash


#### Why after compiling a new source file still looks the same (or continue to make the same mistakes)?

Delete the file and its compilation AUX (DVI / PDF) and try to compile again. The file can not be empty (to be any sign that will show after compiling may not be the same preamble)

#### As prohibit fracture words by function hyphenation?

    ::: latex
    \ mbox {word}


#### How to get the number of pages in the document (to make the page number in the format x / y)?

    ::: latex
    \ usepackage {lastpage}


Last page number will return \ pageref {LastPage} - note the size of the characters. It should be a minimum of 2x to compile caught.

#### How to insert endnotes?

    ::: latex
    \ usepackage {EndNotes}


Footnote define:

    ::: latex
    \ EndNote {xxx}


At the point of insertion of footnotes:

    ::: latex
    \ theendnotes


#### How to insert German umlaut?

eg. '\ "O` With package [german] {babel}` enough' O`.

#### To enter the horizontal and vertical spacing?

    ::: latex
    \ hspace {distance}
    \ vspace {distance}


#### How to set the width of the image or to the width of the text?

    ::: latex
    \ includegraphics [0.5 \ textwidth] {plik.eps}


#### Free converter to EPS format?

GIMP, ImageMagick (convert command)

#### How to change the name Wall-Table, Figure-Figure Bibliography - A bibliography, etc?

For example. `\ Renewcommand * {\ figurename} {Fig.}` The `\ figurename` you can enter other commands. List learned from the babel package documentation:

    ::: latex
    \ def \ prefacename {Foreword}%
    \ def \ refname {Literature}%
    \ def \ abstractname {Summary}%
    \ def \ bibname {Bibliography}%
    \ def \ chaptername {Chapter \ l}%
    \ def \ appendixname {Appendix}%
    \ def \ contentsname {CONTENTS \ 'sci}% Table of Contents
    \ def \ listfigurename {Spisrysunk \ 'o}% list of figures
    \ def \ listtablename {}% Spistablic list of tables
    \ def \ indexname {index}%
    \ def \ figurename {figure}%
    \ def \ tablename {Table}%
    \ def \ partname {W \ eob {} \ 's \' c}% part
    \ def \ enclname {The \ l \ AOB {}}% attachment switch
    \ def \ ccname {copy:}%
    \ def \ headtoname {The}%
    \ def \ pagename {Home}%
    \ def \ seename {See \ 'ownaj}% compare
    \ def \ alsoname {See \ 'ownajtak \ .that}% compare well
    \ def \ proofname {Dow \ 'of}% proof
    \ def \ glossaryname {Glossary}


#### How to insert a horizontal line in the text?

    ::: latex
    \ hrule


#### How to restart the numbering from the previous list?

    ::: latex
    \ usepackage {enumitem}
    ...
    \ begin {enumerate} [resume]


#### How to change the numbering style chapters, letter, etc? How do I add a dot to the chapter number?

For example. `\ Renewcommand {\ thechapter} {\ arabic {chapter}}` commands: `\ thefigure`` \ thetable` `\ thepage`` \ thepart` `\ The (subsub) section`` \ theequation` `\ The (sub) paragraph` counters are called like, for example chapter. Number formats: arabic, roman, Roman, alpha, alpha numbered lists -przykład how to make a list in alphabetical order:

    ::: latex
    \ renewcommand {\ labelenumi} {\ Alph {enumi}.}% level 1
    \ renewcommand {\ labelenumii} {\ Alph {enumi}. \ alpha {enumii}}% level 2


#### How to change the page number to something other than determined by the order?

    ::: latex
    \ setcounter {page} {number}


#### How to turn off hyphenation?

    ::: latex
    \ usepackage {hyphenat}
    ...
    \ nohyphens {block of text}


#### How to paint the cells in a table?

    ::: latex
    \ usepackage [table] {xcolor}
    \ cellcolor [gray] {0.9}


#### How to merge cells in a table?

Horizontal: \ multicolumn {ile_kolumn_scalić} {edges and alignment} {contents} example. \ multicolumn {5} {| c |} {HEADER} vertically (requires the package multirow): \ multirow {if} {width} {contents} instead of wide You can type * - much to adjust.

#### How do you break the equation for 2 lines?

    ::: latex
    \ begin {eqnarray}
    Line 1 xxx \ nonumber \\
    line2
    \ end {eqnarray}


To align lines of expression so that eg equal signs in each line were under him: signs, in respect of which aligns take on each line between symbols &; eg. & = &.

#### To temporarily turn off images to speed up compilation?

to `\ documentclass` add a` draft`.

#### How to put a header chapter title?

Fancyhdr format the header package. Then we use the command: `\ leftmark` - returns a string CHAPTER N. TITLE` \ rightmark` - NUMBER. TITLE `\ thesection` - the section number kapitalkami To disable writing` \ nouppercase {xxx} `









































