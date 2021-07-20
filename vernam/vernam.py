from sys import argv, stdin, stdout
from unidecode import unidecode
import os
from random import seed
from random import randint
from operator import xor


# pip install unidecode
ALL_CHARACTERS = []
OPERATION = 'ENCRIPTER' if argv[1] == '-c' else 'DECRIPTER'

RELATIVE_PATH = os.getcwd()

FILE_KEY = argv[2]

# seed random number generator
seed(1)
# generate some integers

for i in range(0, 125): # percorre tabela ascii
  if (i > 47 and i < 58) or (i > 64 and i < 91) or (i > 96 and i < 123): # separa números e letras num array
    ALL_CHARACTERS.append(chr(i))

def getLinesFile():  
  return stdin.read()

def writeFile(text):
  stdout.write(text)


def generatorKey(text):
  keyEncript = ''
  for _ in range(len(text)):
    value = randint(0, 255)
    keyEncript += chr(value)
  keyEncript = ''.join(bin(ord(x))[2:].zfill(8) for x in keyEncript)
  FILE_TO_WRITE = open(RELATIVE_PATH + '/' + FILE_KEY, 'w')
  FILE_TO_WRITE.write(keyEncript)
  return keyEncript

def getKeyEncoded(text):
  keyEncript = ''
  for _ in text:
    value = randint(0, 255)
    keyEncript += chr(value)    
  FILE_TO_WRITE = open(RELATIVE_PATH + '/' + FILE_KEY, 'w')
  FILE_TO_WRITE.write(keyEncript)
  return keyEncript


def encript():
  text = unidecode(getLinesFile())
  KEY_ENCRIPT = generatorKey(text)
  text_code = ''

  for i, c in enumerate(text, start=0):	
    aux_xor = xor(ord(text[i]), ord(KEY_ENCRIPT[i]))	
    text_code += chr(aux_xor)	

  
  writeFile(text_code)
  

def decript():
  text = unidecode(getLinesFile())
  KEY_ENCRIPT = open(RELATIVE_PATH + '/' + FILE_KEY).read()
  
  text_code = ''
  for i, c in enumerate(text, start=0):	
    aux_xor = xor(ord(text[i]), ord(KEY_ENCRIPT[i]))	
    text_code += chr(aux_xor)	

  writeFile(text_code)
  
if OPERATION == 'DECRIPTER':
  decript()
else:
  encript()







