# Changes


## v1.4 (2019/02/04)
*  Reimplemented `\Verb`.  It now works as expected inside other commands
   (with a few limitations), including in movable arguments, and is compatible
   with `hyperref` for things like PDF bookmarks.  It now supports
   `breaklines` and relevant line-breaking options.

*  Reimplemented `\SaveVerb` and `\UseVerb` to be equivalent to the new
   `\Verb`.  The new option `retokenize` allows saved verbatim material to be
   retokenized under new `commandchars` and `codes` when it is inserted with
   `\UseVerb`.

*  New command `\EscVerb` works like the reimplemented `\Verb`, except that
   special characters can be escaped with a backslash.  It works inside other
   commands without any limitations, including in movable arguments, and is
   compatible with `hyperref` for things like PDF bookmarks.

*  Added `extra` option for switching between the reimplemented  `\Verb`,
   `\SaveVerb`, `\UseVerb` and the original `fancyvrb` definitions.
   Reimplemented versions are used by default.  This option will apply to any
   future reimplemented commands and environments.

*  New command `\fvinlineset` only applies options to commands related to
   typesetting verbatim inline, like `\Verb`, `\SaveVerb`, `\UseVerb`.  It
   only works with commands that are defined or reimplemented by `fvextra`.
   It overrides options from `\fvset`.

*  Patched `fancyvrb` so that `\Verb` (either reimplemented version or
   original) can use characters like `%` for delimiters when used outside any
   commands.

*  `obeytabs` now works with the `calc` package's redefined `\setcounter`.
    Since `minted` loads `calc`, this also fixes `minted` compatibility
    (`minted` #221).

*  Added new option `fontencoding` (`minted` #208).

*  `highlightlines` now works correctly with `frame` (#7).


## v1.3.1 (2017/07/08)

* `beameroverlays` now works with `VerbatimOut`.


## v1.3 (2017/07/08)

*  Added `beameroverlays` option, which enables `beamer` overlays using the
   `<` and `>` characters.

*  Added options `breakindentnchars`, `breaksymbolsepleftnchars` (alias
   `breaksymbolsepnchars`), `breaksymbolseprightnchars`,
   `breaksymbolindentleftnchars` (alias `breaksymbolindentnchars`), and
   `breaksymbolindentrightnchars`.  These are identical to the pre-existing
   options without the `nchars` suffix, except that they allow indentation to
   be specified as an integer number of characters rather than as a dimension.
   As a result of these new options, `\settowidth` is no longer used in the
   preamble, resolving some font incompatibilities (#4).

*  Clarified in the docs that `breaksymbolsepright` is a *minimum*, rather
   than exact, distance.


## v1.2.1 (2016/09/02)

*  The package is now compatible with classes and packages that redefine
   `\raggedright`.

*  Fixed a bug that introduced extra space in inline contexts such as
   `\mintinline` when `breaklines=true` (#3).



## v1.2 (2016/07/20)

*  Added support for line breaking when working with Pygments for syntax
   highlighting.

* The default `highlightcolor` is now defined with `rgb` for compatibility
  with the `color` package.  Fixed a bug in the conditional color definition
  when `color` and `xcolor` are not loaded before `fvextra`.



## v1.1 (2016/07/14)

*  The options `rulecolor` and `fillcolor` now accept color names directly;
   using `\color{<color_name>}` is no longer necessary, though it still works.

*  Added `tabcolor` and `spacecolor` options for use with `showtabs` and
   `showspaces`.

*  Added `highlightlines` option that takes a line number or range of line
   numbers and highlights the corresponding lines.  Added `highlightcolor`
   option that controls hightlighting color.

*  `obeytabs` no longer causes lines to vanish when tabs are inside macro
   arguments.  Tabs and spaces inside a macro argument but otherwise at the
   beginning of a line are expanded correctly.  Tabs inside a macro argument
   that are preceded by non-whitespace characters (not spaces or tabs) are
   expanded based on the starting position of the run of whitespace in which
   they occur.

*  The line breaking options `breakanywhere`, `breakbefore`, and `breakafter`
   now work with multi-byte UTF-8 code points under pdfTeX with `inputenc`.
   They were already fully functional under XeTeX and LuaTeX.

*  Added `curlyquotes` option, which essentially disables the `uquote` package.



## v1.0 (2016/06/28)

*  Initial release.
