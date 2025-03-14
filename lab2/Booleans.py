# Booleans represent one of two values: True or False.

""" 
Python Booleans
Booleans represent one of two values: True or False.

Boolean Values
In programming you often need to know if an expression is True or False.

You can evaluate any expression in Python, and get one of two answers, True or False.

When you compare two values, the expression is evaluated and Python returns the Boolean answer:

"""

print(10 > 9)
print(10 == 9)
print(10 < 9)

#example
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#The bool() function allows you to evaluate any value, and give you True or False in return,
x = "Hello"
y = 15

print(bool(x))
print(bool(y))
""" 
Most Values are True
Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones.
"""

bool("abc") #true
bool(123) #true
bool(["apple", "cherry", "banana"]) #true

""" 
Some Values are False
In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.
 """

bool(False) #false
bool(None)#false
bool(0)#false
bool("")#false
bool(())#false
bool([])#false
bool({})#false

#Functions can Return a Boolean
#You can create functions that returns a Boolean Value:
def myFunction() :
  return False

print(myFunction())