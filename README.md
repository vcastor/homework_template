# Homework template

This repository has a homework template developed particularly for physics and
chemistry homeworks. However, it can be used also to write a letter. Some examples of
homeworks and letters can be found in the directory examples.

The file in which you'll write is `main.tex`, the file `homework.tex` has the
dependecies to the printing.

## How compile _terminal_

If you use pdflatex compiler you have a Makefile, just type make on your
Terminal.  The `bibtex` and `makeglossaries` commands are just in case that you
have bibliography and glossaries. The commands to execute if you want to do it
by hand and/or stop in some part are:

~~~
pdflatex homework.tex
bibtex homework.aux
makeglossaries homework
pdflatex homework.tex
~~~

If you see the next error: `make: *** [all] Error 2` don't worry about it, it's
just because there are no any glossary or biblography.

A really cool alias that I personally have on my computer to write a
new letter or homework asap is the next one:

`alias newhomework="cp -r ~/LaTeX/template_homework__/* . && vi main.tex"`

It just to copy the template and edit the `main.tex` with vim, you can
use your favourite plain text editor.

The Makefile has also the option clean to remove the axuliar files if you want.

If you're using the Makefile, it's also possible to run python3, I use it to
update the figures that I plot it with python.

## How compile _overleaf_

I've already upload the template to Overleaf. You
just need to use the template by the next [](link). Or download the repository
and upload by yourself. Just not forget that it's not compiling the main file
but the homework.tex

## Troubles?

If you're having troubles don't be shy, send me a message, I'll try to answer
asap. Good luck with your homework and don't worry about $\LaTeX$! The template
was already done :gift_heart: .
