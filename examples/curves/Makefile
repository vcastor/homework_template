#Makefile

ALL=$(wildcard *.tex */*.tex bibl/*.bib)
MAIN=homework.tex
LATEX=pdflatex
PYPLOT=$(wildcard ./img/plots/*.py)
PYTHON=python3

all: tex

plots:
	$(foreach var,$(PYPLOT),$(PYTHON) $(var);)

tex:                               ## here we go! 🥳
	$(LATEX) $(MAIN)                # main run
	bibtex $(MAIN:.tex=)            # bibliography
	#makeglossaries $(MAIN:.tex=)    # list of abbreviations, nomenclature
	$(LATEX) $(MAIN)

clean:
	@rm -rf *.aux *.bbl *.blg *.glg *.glo *.gls *.ist *.log *.not *.ntt *.out *.sbl *.sym *.tld *.toc */*.aux
