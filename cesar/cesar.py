
#!/usr/bin/env python

# This Python file uses the following encoding: utf-8

from sys import argv, stdin, stdout
from unidecode import unidecode

# pip install unidecode

ALL_CHARACTERS = []
OPERATION = 'ENCRIPTER' if argv[1] == '-c' else 'DECRIPTER'
KEY_ENCRIPT = int(argv[3]) # quantas casas vai andar cada letra

for i in range(0, 125): # percorre tabela ascii
  if (i > 47 and i < 58) or (i > 64 and i < 91) or (i > 96 and i < 123): # separa números e letras num array
    ALL_CHARACTERS.append(chr(i))  

def getLinesFile():  
  return stdin.readlines()

def writeFile(text):
  stdout.write(text)

def encript():
  lines = getLinesFile()
  text_code = ''
  for textaux in lines:
    text = unidecode(textaux)
    for letter in text:
      try:
        index = ALL_CHARACTERS.index(letter)
        if index + KEY_ENCRIPT > len(ALL_CHARACTERS) - 1:
          text_code += ALL_CHARACTERS[index + KEY_ENCRIPT - len(ALL_CHARACTERS)]
        else:
          text_code += ALL_CHARACTERS[index + KEY_ENCRIPT]
      except:
          text_code += letter
  writeFile(text_code)
  return text_code

def decript():
  lines = getLinesFile()
  text_code = ''
  for textaux in lines:
    text = unidecode(textaux)
    for letter in text:
      try:
        index = ALL_CHARACTERS.index(letter)
        text_code += ALL_CHARACTERS[index - KEY_ENCRIPT]        
      except:
        text_code += letter
  writeFile(text_code)
  return text_code


if OPERATION == 'DECRIPTER':
  decript()
else:
  encript()







