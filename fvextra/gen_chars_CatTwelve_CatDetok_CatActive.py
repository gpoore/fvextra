# For all ASCII printable, non-alphanumeric characters, generate macros of the
# following forms:
#  *  \FV@Char@CatTwelve:<char>
#  *  \FV@Char@CatDetok:<char>
#  *  \FV@Char@CatActive:<char>
#
# Copyright (C) 2025 by Geoffrey M. Poore <gpoore@gmail.com> Licensed under
# the LaTeX Project Public License (LPPL) version 1.3


import textwrap


alphanumeric_n_s = set()
for c_i, c_f in [('0', '9'), ('a', 'z'), ('A', 'Z')]:
    alphanumeric_n_s.update(range(ord(c_i), ord(c_f) + 1))

command_chars = ('\\', '{', '}')
special_handling_chars = (' ', '%')

skipped_n_s = alphanumeric_n_s.copy()
skipped_n_s.update(ord(c) for c in command_chars)
skipped_n_s.update(ord(c) for c in special_handling_chars)

print(textwrap.dedent(r'''
    \begingroup
    \catcode`\!=0
    \catcode`\<=1
    \catcode`\>=2
    \catcode`\&=14!relax&
    '''.split('\n', 1)[1]), end='')

for char in command_chars + special_handling_chars:
    print(textwrap.dedent(
        rf'''
        !edef!FVCharNum<!number`!{char}>&
        !catcode`!{char}=12!relax&
        !expandafter!gdef!csname!detokenize<FV@Char@CatTwelve:>!FVCharNum!endcsname<{char}>&
        !expandafter!xdef!csname!detokenize<FV@Char@CatDetok:>!FVCharNum!endcsname<!detokenize<{char}>>&
        !catcode`!{char}=!active&
        !expandafter!gdef!csname!detokenize<FV@Char@CatActive:>!FVCharNum!endcsname<{char}>&
        '''.split('\n', 1)[1]), end='')

print(r'!endgroup')

for n in range(ord(' '), ord('~') + 1):
    if n in skipped_n_s:
        continue
    char = chr(n)
    print(textwrap.dedent(
        rf'''
        \begingroup
        \edef\FVCharNum{{\number`\{char}}}
        \catcode`\{char}=12
        \expandafter\gdef\csname\detokenize{{FV@Char@CatTwelve:}}\FVCharNum\endcsname{{{char}}}
        \expandafter\xdef\csname\detokenize{{FV@Char@CatDetok:}}\FVCharNum\endcsname{{\detokenize{{{char}}}}}
        \catcode`\{char}=\active
        \expandafter\gdef\csname\detokenize{{FV@Char@CatActive:}}\FVCharNum\endcsname{{{char}}}
        \endgroup
        '''.split('\n', 1)[1]), end='')
