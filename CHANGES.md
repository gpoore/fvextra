# Changes


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
