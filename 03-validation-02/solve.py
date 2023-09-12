'''

Template for France-IOI programming tasks with debugger in gitpod

The Python version on gitpod is 3.11, whereas the python version on france-ioi
is sadly stuck at 3.4.2 ... This means no type hints, no dataclasses, ... The
code should therefore remain pretty basic to run flawlessly on france-ioi

'''

##################################################################
# read input from file tests/test1.in as if type on the keyboard
# This shouldn't run on France-IOI
# replace this with the name of your test file
test_file = 'test1.in'

import sys, os, platform
# only if executed on Python 3.11 (gitpod), will be false on france-ioi
if platform.python_version_tuple()[:2] == ('3', '11'):
    os.chdir(os.path.dirname(__file__))
    sys.stdin = open(os.path.join('tests', test_file), "r")
##################################################################

nbr_lettres = int(input())
nbr_lignes = nbr_lettres * 2 - 1

import string
alphabet = list(string.ascii_lowercase)
lettres_utiles = []
for i in range(nbr_lettres) :
   lettres_utiles.append(alphabet[i])

texte = []

for j in range(nbr_lignes // 2 + 1):
   ligne = []
   for k in range(nbr_lignes-2*j) :
      ligne.append(lettres_utiles[j])
   l = 1
   while len(''.join(ligne)) < nbr_lignes :
      ligne.insert(0, lettres_utiles[j-l])
      ligne.append(lettres_utiles[j-l])
      l += 1
   if j == 0 :
      texte.insert(j, ''.join(ligne))
      texte.append(''.join(ligne))
   if 0 < j < nbr_lignes // 2 :
      texte.insert(j,''.join(ligne))
      texte.insert(-j,''.join(ligne)) 
   if j == nbr_lignes // 2 :
      texte.insert(j,''.join(ligne))
      
for m in range(nbr_lignes) :
   print(texte[m])
