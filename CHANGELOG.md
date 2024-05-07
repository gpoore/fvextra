# Changelog


## v1.7 (dev)

*  Added new command `\VerbatimClearBuffer`.

*  `VerbatimBuffer` environments with the same buffer name now append to the
   same buffer, regardless of the value of `globalbuffer`.  Previously,
   `globalbuffer=false` caused any pre-existing buffer to be cleared.

*  `\FVExtraUnexpandedReadStarOArgMArgBVArg` now checks that the final argument
   it reads is braced (#22).

*  Text that immediately follows `\VerbatimInsertBuffer` is no longer indented
   to start a new paragraph.

*  Updated `tcblisting` usage in docs for compatibility with the latest
   `tcolorbox`.


## v1.6.1 (2023/11/28)

*  Fixed bug from v1.6 that caused a space following a comma to be lost (#21).


## v1.6 (2023/11/19)

*  Added new environment `VerbatimWrite`.  This is similar to `fancyvrb`'s
   `VerbatimOut`, except that it allows for writing to a file multiple times
   and guarantees truly verbatim output via `\detokenize`.

*  Added new environment `VerbatimBuffer`.  This stores the contents of an
   environment verbatim in a "buffer," a sequence of numbered macros each of
   which contains one line of the environment.  The "buffered" lines can then
   be looped over for further processing or later use.

*  Added new command `\VerbatimInsertBuffer`.  This inserts an existing buffer
   created by `VerbatimBuffer` as a `Verbatim` environment.

*  Redefined visible space `\FancyVerbSpace` so that it now has the correct
   width.  It had previously been redefined as `\textvisiblespace`, but that
   was slightly too narrrow.

*  Added option `spacebreak`.  This determines the line break that is inserted
   around spaces when `showspaces=true` or `breakcollapsespaces=false`, by
   defining the new macro `\FancyVerbSpaceBreak`.

*  `breakbefore`, `breakafter`, and `breakanywhere` now produce plain breaks
   around spaces when `showspaces=true`, instead of breaks with a break symbol
   at the end of wrapped lines.  `\FancyVerbBreakAnywhereBreak`,
   `\FancyVerbBreakBeforeBreak`, and `\FancyVerbBreakAfterBreak` are no longer
   inserted next to spaces.  Instead, `\FancyVerbSpaceBreak` is inserted or
   (depending on options) `\FV@Space` is defined to include
   `\FancyVerbSpaceBreak`.

*  Added option `breakcollapsespaces`.  When `true` (default), a line break
   within a run of regular spaces (`showspaces=false`) replaces all spaces
   with a single break, and the wrapped line after the break starts with a
   non-space character.  When `false`, a line break within a run of regular
   spaces preserves all spaces, and the wrapped line after the break may start
   with one or more spaces.  This causes regular spaces to behave exactly like
   the visible spaces produced with `showspaces`; both give identical line
   breaks, with the only difference being the appearance of spaces.

*  `breaklines` now automatically enables breaks after space characters when
   `showspaces=true`.

*  Reimplemented definition of `\FV@Space` to work with new space options.

*  Added documentation about how reimplemented commands handle the `codes`
   option differently compared to `fancyvrb` (#17).

*  Starred commands such as `\Verb*` now use both visible spaces and visible
   tabs instead of just visible spaces.  This is more similar to the current
   behavior of `\verb*`, except that `\verb*` converts tabs into visible
   spaces (#19).

*  The `mathescape` option now resets the ampersand `&` catcode (#18).


## v1.5 (2022/11/30)

*  Added `\FancyVerbFormatInline` for customizing the formatting of inline
   verbatim, such as `\Verb`.  This parallels `\FancyVerbFormatLine` and
   `\FancyVerbFormatText`.

*  Added line breaking option `breaknonspaceingroup`.  When `commandchars` is
   used to allow macros within verbatim, this inserts breaks within groups
   `{...}`.

*  Added `\FVExtraUnexpandedReadStarOArgMArgBVArg` to support reimplementation
   of `\mintinline` for `minted`.

*  Added `VerbEnv` environment, which is an environment variant of `\Verb`.
   This supports reimplementation of `\mintinline` for `minted`.

*  `breakbefore` and `breakafter` now support the escaped comma `\,` (#15).

*  Fixed unintended line breaks after hyphens under LuaTeX (#14).

*  Added documentation on Pandoc compatibility (#11).

*  Replaced `breakbeforegroup` with `breakbeforeinrun`, and replaced
   `breakaftergroup` with `breakafterinrun`.  With the introduction of
   `breaknonspaceingroup`, "`group`" is now reserved for referring to TeX
   groups `{...}`.

*  Removed dependency on `ifthen` package.

*  `breakautoindent` now works correctly with Pygments output that treats
   leading whitespace as a separate token or as part of a token.


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
