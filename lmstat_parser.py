from tkinter import Tk
from tkinter.filedialog import askopenfilename
import runpy
import sys
import pathlib
import re

def quit():
    input()
    exit()

Tk().withdraw()
filename = askopenfilename()
console_output=True #needed for eventual implementation of output to file
output=[] #list of strings that contains the lines of output
beginning_found=False


if not '.txt' in filename: 
    print("chosen file is not a .txt, exiting")
    quit()

with open(filename) as infile:
    for line in infile:
        
        #header lines per module
        res = re.match(r' *Users of (\w+): .*', line)
        if(res): 
            if not beginning_found: beginning_found=True
            output.append("\n"+line.strip())

        if not beginning_found: continue

        #user@machine lines
        res=re.match(r'\s*(\w+) (\w+) (\S|\.)* \(.*\)', line)
        if(res): output.append("   User: "+res.group(1)+" Machine: "+res.group(2))


    if(console_output):
        for line in output:
            print(line)

    quit()