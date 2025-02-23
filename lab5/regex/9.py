import re

def task (a):
    pattern = r"(?=[A-Z])"
    return re.sub(pattern," ",a)

b = str(input("Input new string: "))
print(task(b))