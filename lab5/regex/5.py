import re

def task(a):
    pattern = r"^a.*b$"
    return re.fullmatch(pattern,a)

str_1 = str(input("Введите строку: "))
print(task(str_1))