from sys import stdin, stdout
import os
import collections

ALL_CHARACTERS = []

RELATIVE_PATH = os.getcwd()

CHARACTER_MORE_USED = ['a', 'e', 'o', 's', 'r']

for i in range(0, 125): # percorre tabela ascii
  if (i > 47 and i < 58) or (i > 64 and i < 91) or (i > 96 and i < 123): # separa números e letras num array
    ALL_CHARACTERS.append(chr(i))

VALUE_CHARACTER_MORE_USED = []

for char in CHARACTER_MORE_USED:
  VALUE_CHARACTER_MORE_USED.append(ALL_CHARACTERS.index(char))
  

def getLinesFile():  
  return stdin.read()

def writeFile(text):
  stdout.write(text)

text_raw = getLinesFile()

text_cripted =  text_raw.replace(' ', '', 999999999999).lower()


frequencies = collections.Counter(text_cripted)
frequencies = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
repeated = {}
distanceForFrequences = []
for i, (key, value) in enumerate(frequencies[:5]):
  index = ALL_CHARACTERS.index(key)
  distanceForFrequences.append(index - VALUE_CHARACTER_MORE_USED[i])
  repeated[key] = value

def decript():  
  text_code = ''  
  for letter in text_raw:
    try:
      index = ALL_CHARACTERS.index(letter)
      text_code += ALL_CHARACTERS[index - distanceForFrequences[0]] # vai funcionar se o texto tiver mais a, se tiver mais E funciona com o segundo e até o quinto mais utilizado.
    except:
      text_code += letter
  writeFile(text_code) 

decript()