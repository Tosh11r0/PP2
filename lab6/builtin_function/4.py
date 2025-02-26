import time
import math


a = int(input("Number: "))
timer = int(input("milliseconds: "))

time.sleep (timer/1000)

answer = math.sqrt(a)

print(f"Square root of {a} after {timer} is {answer}")