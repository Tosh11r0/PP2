import os
import math


def multiply(a):
    return math.prod(a)

a = []
while True:
    b = input("Введите число: ")
    if b == "":  
        break
    a.append(float(b))

result = multiply(a)
print( result)
