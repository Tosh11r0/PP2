import re

def task(a):
    pattern = r'^ab{2,3}$'
    if re.fullmatch(pattern,a):
        return True
    else: return False

str1 = str(input("Введите свою строку: "))

if (task(str1)):
    print("Match")
else: print ("Not match")