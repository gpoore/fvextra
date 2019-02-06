# `fvextra` - extensions and patches for `fancyvrb`


`fvextra` is a [LaTeX](https://www.latex-project.org/) package that provides
several extensions to the [`fancyvrb` package](https://www.ctan.org/pkg/fancyvrb).
It also patches some `fancyvrb` internals.

`fancyvrb` is one of the primary packages for working with verbatim text in
LaTeX.  `fvextra` builds on `fancyvrb` by adding support for automatic line
breaking and improving math mode, among other things.  It provides a
reimplemented `\Verb` command that works (with a few limitations) inside other
commands, even in movable arguments and PDF bookmarks.  It also provides
`\EscVerb`, which is similar to `\Verb` except that it works everywhere
without limitations by allowing the backslash to serve as an escape character.

Many of the improvements provided by `fvextra` are geared toward typesetting
computer code.  Parts of `fvextra` were originally developed as part of the
[`pythontex`](https://github.com/gpoore/pythontex) and
[`minted`](https://github.com/gpoore/minted) packages.


## Installation

The easiest option with an up-to-date LaTeX distribution like
[TeX Live](https://tug.org/texlive/) or [MiKTeX](https://miktex.org/)
is to use the package manager.  Depending on how LaTeX is configured,
you may already have `fvextra` installed, and can update it
with the package manager if necessary.

To try the development version, simply download `fvextra.sty` and put it in
the same directory as your document.

There are many resources online for manual package installation. The
[LaTeX Wikibook](https://en.wikibooks.org/wiki/LaTeX/Installing_Extra_Packages#Manual_installation)
might be one place to start.  Note that for manual installation, the style
file `fvextra.sty` is pre-generated and available for download.


## License

This work may be distributed and/or modified under the conditions of the
[LaTeX Project Public License](http://www.latex-project.org/lppl.txt) (LPPL),
version 1.3 or later.
