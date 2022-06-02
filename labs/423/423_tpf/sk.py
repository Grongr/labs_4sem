import re
import os

import sys
inFile = sys.argv[1]
outFile = sys.argv[2]

with open(inFile, 'r') as file :
  filedata = file.read()

filedata = re.sub(r'(,)(\d)', r'.\2',filedata)
filedata = filedata.replace(';', '&')
with open(outFile, 'w') as file:
  file.write(filedata)

with open(outFile, 'r') as file:
  file_lines = [''.join([x.strip(), '\\\\ \hline', '\n']) for x in file.readlines()]
with open(outFile, 'w') as file:
  file.writelines(file_lines)


with open(outFile, 'r') as file:
	filedata = file.read()

filedata = re.sub(r'(&)(\\)', r'\2',filedata)
with open(outFile, 'w') as file:
  file.write(filedata)	
