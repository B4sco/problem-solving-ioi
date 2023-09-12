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

nbMesures = int(input())
diffMax = float(input())
nbLissages = 0

def estLisse(n1, n2, diffMax):
   if abs(n1-n2) <= diffMax :
      return True
   else :
      return False 
      
def lissage(n0, n2):
   nbr_lisse = float(n0+n2)/2
   return nbr_lisse
   
frequences = []
for i in range(nbMesures):
   frequences.append(float(input()))
   
fin = False 

while fin == True:
   for i in range(nbMesures-1):
      reussite = 0
      if estLisse(frequences[i], frequences[i+1], diffMax) == False :
         n = lissage(frequences[i], frequences[i+2])
         frequences[i+1] = n
         nbLissages += 1
      elif estLisse(frequences[i], frequences[i+1], diffMax) == True :
         reussite += 1
         if reussite == nbMesures-1:
            fin = True 
            break
      
print(nbLissages)
         