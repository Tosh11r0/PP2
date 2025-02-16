import math

sides = int(input("Num of sides: "))
length = int(input("their length: "))

x = math.pi
area = (sides* length ** 2) / (4 * math.tan(math.pi / sides))

print (area)