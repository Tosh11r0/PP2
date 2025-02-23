import re

def task(a):
    pattern = r'[ ,.]'
    ans = re.sub(pattern,":",a)
    return ans

b = str(input("Input new string: "))
print(task(b))