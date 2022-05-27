# Homework template

Hiya, I'm the readme file, this repository has a homework template developed
particularly for physics and chemistry. Some examples of homework written with
this template will be in the directory examples.

## How compile _terminal_

If you use pdflatex compiler you have a Makefile, just type make on your Terminal. Sometimes
if an error was executed in the `log` files is better if you compile by hand. The
bibtex and makeglossaries commands are just in case that you have bibliography and
glossaries. The command pdflatex is executed two times because the cross references.

~~~
pdflatex homework.tex
bibtex homework.aux
makeglossaries homework
pdflatex homework.tex
~~~


## How compile _overleaf_

You can download the whole repository and upload the files in
[https://www.overleaf.com](overleaf).  I recommend use pdflatex and don't forget
that it's not compiling the main file but the homework.tex

## Troubles?

For any trouble don't be shy, send me a message. Good luck with your
homework, don't worry about $\LaTeX$! The template was already done :gift_heart:
