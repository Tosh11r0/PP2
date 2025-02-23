import re

def task(a):
    pattern = r"(?=([A-Z]))"
    ans = re.sub(pattern,"_", a).lower()
    return ans

b = str(input("Input new string: "))
print(task(b))