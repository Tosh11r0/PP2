import re

def task (a):
    pattern = r"(?=[A-Z])"
    return " ".join(re.split(pattern,a))

b = str(input("Input new string: "))
print(task(b))