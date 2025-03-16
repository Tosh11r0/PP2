import math
import os
import datetime
from datetime import datetime

def gen(a):
    while(a >= 0):
        yield a
        a-=1

n = int(input("Enter a number: "))
for num in gen(n):
    print (num)


x = datetime.now()

ans =x.replace(second= 0)

print(ans)

