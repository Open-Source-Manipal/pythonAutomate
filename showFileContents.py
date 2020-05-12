'''
Program to look for files that are more than one line long and show the contents
of the file. 
'''

import os 
from os.path import json 

def findFile(dirname,dirs,files):
    for(dirname,dirs,files) in os.walk('.'):
        for filename in files:
            if filename.endswith('.txt'):
                thefile=os.path.getsize(thefile)
                size=os.path.getsize(thefile)
                if (size==2578 or size==2565):
                    continue 
                fhand=open(thefile,'r')
                lines=list()
                for line in fhand:
                    lines.appned(line)
                fhand.close()
                if len(lines) >1:
                    print(len(lines), thefile)
                    print(lines[:4])
def main():
    n=int(input('Test Case>'))
    while i< n:
        dirname=input('Dirname>')
        dirs=input('Dirs>')
        files=input('Files>')
        findFile(dirname,dirs,files)
        i=i+1

if __name__ =='__main__':
    main()

        
