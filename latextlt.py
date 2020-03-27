import re # Regexps
import pickle # Save and load hashtable
import random
import string
from argparse import ArgumentParser
from pathlib import Path
from os.path import splitext

hashtable = dict()
counter=0

def randomString(stringLength=4):
    """Generate a random string of fixed length """
    letters = string.ascii_uppercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def hashreplace(match):
    global counter
    global hashtable
    
    hash = randomString()
    #print(hash,match.group())
    hashtable[hash]=match.group()
    counter += 1
    return hash


def encode(filename):
    global counter

    filebase = splitext(filename)[0]
    latex = Path(filename).read_text()

    fig = re.compile(r'\\begin{figure}.*?\\end{figure}', re.DOTALL)
    eq = re.compile(r'\\begin{equation}.*?\\end{equation}', re.DOTALL)
    eqn = re.compile(r'\\begin{equation\*}.*?\\end{equation\*}', re.DOTALL)
    eqs = re.compile(r'\$.*?\$', re.DOTALL)
    cmd = re.compile(r'\\[a-z]*', re.DOTALL)
    slash = re.compile(r'[{,}]', re.DOTALL)

    for ex in [eq, eqn, eqs, cmd, slash]:
        latex = ex.sub(hashreplace,latex)

    print(f'File processed, total hashs: {counter}.\n\nNext steps:\n\t(1) Translate {filebase}.CODED.txt using google translator (or similar)\n\t(2) Save translation to {filebase}.CODED.tlt\n\t(3) Run "python {__file__} -d -f {filename} > {filebase}.tlt.tex"\n\t(4) Manually review the output {filebase}.tlt.tex\n\t(5) Remove auxiliary files "rm {filebase}.hsh {filebase}.CODED.*"') 

    # Save hashtable and outputfile
    fh = open(f'{filebase}.hsh',"wb")
    fw = open(f'{filebase}.CODED.txt',"w")
    pickle.dump(hashtable,fh)
    fw.write(latex)
    fh.close()
    fw.close()

def decode(filename):

    filebase = splitext(filename)[0]
    latex = Path(f'{filebase}.CODED.tlt').read_text()

    fh = open(f'{filebase}.hsh',"rb")
    hashtable = pickle.load(fh)

    print(f'Hashtable contains {len(hashtable)} hashes')

    for key, value in hashtable.items():
        latex = re.sub(key,re.escape(value),latex)

    sanity = {'\\\,\\\,\\\,': ',', '\\\{': '{', '\\\}': '}', '\\\\\$': '$', '\\\\ ': ' ', '\\\\\n': '\n','\\\\\*': '*', '\\\\\[': '[', '\\\\\]': ']', '\\\\\(': '(', '\\\\\)': ')', '\\\\\|': '|', '\\\\\-': '-', '\\\\\+': '+' , '\\\\\?': '?', '\\\\\^': '^', ' ,': ','}
    for key, value in sanity.items():
        latex = re.sub(key,value,latex)

    print(latex)


# MAIN
parser = ArgumentParser()
parser.add_argument("-d", "--decode", dest="decode", action="store_true")
parser.add_argument("-f", "--file", dest="filename",
                                    help="code FILE", metavar="FILE")
args = parser.parse_args()
filename = args.filename
print(filename)

if args.decode==False:
    print('Encoding')
    encode(filename)
else:
    print('Decoding')
    decode(filename)
