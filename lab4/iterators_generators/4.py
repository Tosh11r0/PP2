import math

def square_roots(a, b):
    for i in range(a, b):
        yield math.sqrt(i)

a = int(input("Введи 1е число: "))
b = int(input("Введи 2е число: "))

for i in square_roots(a,b):
    print(i)