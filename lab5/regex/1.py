import re

def task(a):
   pattern = r'^a*b*$' 
   if re.fullmatch (pattern,a):
    return True
   else: return False

b = str(input("Введите свою строку: "))
if task(b):
    print ("True")
else: print ("False")