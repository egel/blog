Title:      Moving from Wordpress to Pelican
Date:       2016-02-25
Status:     published
Category:   Diary
Tags:       wordpress, pelican
Authors:    Maciej Sypień
Summary:    I'm talking a bit about "why I migrate my blog from wordpress to
            pelican", the static pages web framework.

I have to start with words "I used wordpress for 2 yeas constantly". During
this period of time, several times I had problems with many basic stuff like
uploading and managing images, insert some code snippets (like simple `<pre>` or
`<code>` elements), constantly updating framework core, but is not the point.

## Objective of frameworks
IMHO Wordpress is great for PR guys, not for programmers/hackers. PR guys
usually wants to quickly upload news with few sample photos, and they use for it
some [WYSIWYG][wiki-WYSIWYG] HTML editors like [TinyMCE][tinymce-webpage]
or [CKEditor][ckeditor-webpage]. This editors can be really "smart" and do
amazing job - saving text with HTML conventions, but after some time you will
realize that this kind of making content may not suites you, your idea of
writing, which was in my case.

I hope I would not say lie to you that programmers, web admins or hackers really
loved Markdown syntax - I loved it. It has a very clean and simple syntax, which
can allows you to focus on making some content and do not concern anything else
(your content will always have the same generated HTML code).  Markdown power is
especially visible for blogs and basic documentation (like simple README files)
where you can mainly focus on content with some basic graphics which illustrate
the whole content.

In time I realize that kind of magic what those WYSYWIG live editors are
making is not for me, not for my profession - programmer. But here not
profession is important, but the care about the code you are writing, and that
is why programmers and hackers find in those web pages generators a true ally.

## Finding the single point of truth
After while I take a look around market and instantly remembered that is
something like static pages generators. After few minutes, I just surfing among
some rankings that gather some basic data about many frameworks like this one
<https://www.staticgen.com/>.

There are many of them, and most popular at the moment of choosing one was:
Jekyll, Gitbook, Octopress, Hexo or Hugo, then was the Pelican.

Why pelican? You will probably as... Hmmm, the answer is simple, because I
really like Python language.

I will not favoring any of those frameworks, because it point less and actually
depends on user preferences and language taste, then just start writing in it :)

## Pros and cons of migration

As an advantage of migration to static webpages generators I can point:

  - Writing directly through your SSH connection.
  - Writing posts extremely fluent in Vim or Emacs - I realize that is not an
      advantage for all ;)
  - Improve performance of displaying your webpage (non database framework is
      faster then static web generator)
  - Improve content visibility by adding many useful plugins (cloud tags,
      code syntax highlighting, and many more)
  - Host it anywhere
  - It likes to be [git][git-webpage]-ed ;)
  - Making articles in 3 types of text syntax (`.rst`, `.md` or `.adoc`)
  - Articles written in markdown can be easy to migrated almost any type of text
      processor like LaTeX or Word/Writer.

In the other side, disadvantages can be:

  - Face the problem of fast and clean migrating HTML content to reStructuredText, Markdown, or
      AsciiDoc
  - Change your habits of directly web editing content into CMS
  - Generate content after changes (there are some easy techniques which
      constantly watch the content for any changes)

## It is worth it?
If you want to just write blog or blog-like page in easy to write syntax (like
markdown) I definitely say YES, it is worth the time.

But if you expect whole next level of writing articles like you do in CMS, turn
around and go back to your stuff, you will waste your time implement it.

  [git-webpage]: https://git-scm.com/
  [wiki-WYSIWYG]: https://en.wikipedia.org/wiki/WYSIWYG
  [ckeditor-webpage]: http://ckeditor.com/
  [tinymce-webpage]: https://www.tinymce.com/
