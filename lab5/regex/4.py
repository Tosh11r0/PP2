import re

def task(a):
    pattern = r"[A-Z][a-z]+"
    return re.findall(pattern,a)

str_1 = str(input("Введите строку: "))
print(task(str_1))