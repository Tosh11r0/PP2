import os
import math


def multiply(a):
    return math.prod(a)

# Пример использования
a = []
while True:
    b = input("Введите число: ")
    if b == "":  
        break
    try:
        a.append(float(b))  
    except ValueError:
        print("Ошибка! Введите число.")

result = multiply(a)
print( result)
