# latextlt
Python script to ease the translation of latex files to other languages

This script replaces non-text contents of the latex files (e.g., equation, figure, tikz) and all commands (e.g., \frametitle{.}, \section{.}, etc.) for a hash. After translation, the script is called another time to replace back the hash contents for the original contents. Although the process is not perfect, it saves a considerable amount of post-processing time.

Usage: 

(1) Coding tex file: 

python latextlt.py -f yourlatexfile.tex

(2) Translate yourlatexfile.CODED.txt using google translator or similar 

(3) Decoding tex file:

python latextlt.py -d -f yourlatexfile.tex > yourlatexfile.tlt.tex

(4) Manually review the output yourlatexfile.tlt.tex
