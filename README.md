# latextlt
Python script to ease the translation of latex files to other languages

This script replaces non-text contents of the latex files (e.g., equation, figure, tikz) and all commands (e.g., \frametitle{.}, \section{.}, etc.) for a hash. After translation, the script is called another time to replace back the hash contents for the original contents. Review must be done on the resulting output, but this saves a considerable amount of post-processing time.

Usage: 

<ol>

<li>Code tex file: 
  
```
python latextlt.py -f yourlatexfile.tex
```

<li>Translate <b>yourlatexfile.CODED.txt</b> using google translator or similar 

<li>Decode translation file:

```
python latextlt.py -d -f yourlatexfile.tex > yourlatexfile.tlt.tex
```

<li> Manually review the output <b>yourlatexfile.tlt.tex</b>
</ol>
