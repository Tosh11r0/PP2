import re

def task(a):
    pattern = r"_([a-z])"
    ans = re.sub(pattern,lambda match: match.group(1).upper(),a)
    return ans

b = str(input("Input new string: "))
print(task(b))