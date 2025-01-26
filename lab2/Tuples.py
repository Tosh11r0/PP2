# Python Tuples

# Tuples are used to store multiple items in a single variable.
# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.

# Example: Create a Tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Tuple Items
# Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

# Ordered
# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

# Unchangeable
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

# Allow Duplicates
# Since tuples are indexed, they can have items with the same value.

# Example: Tuples allow duplicate values
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# Tuple Length
# To determine how many items a tuple has, use the len() function.

# Example: Print the number of items in the tuple
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# Create Tuple With One Item
# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

# Example: One item tuple, remember the comma
thistuple = ("apple",)
print(type(thistuple))

# NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# Tuple Items - Data Types
# Tuple items can be of any data type.

# Example: String, int and boolean data types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

# A tuple can contain different data types.

# Example: A tuple with strings, integers and boolean values
tuple1 = ("abc", 34, True, 40, "male")

# type()
# From Python's perspective, tuples are defined as objects with the data type 'tuple'.

# Example: What is the data type of a tuple?
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

# The tuple() Constructor
# It is also possible to use the tuple() constructor to make a tuple.

# Example: Using the tuple() method to make a tuple
thistuple = tuple(("apple", "banana", "cherry"))  # note the double round-brackets
print(thistuple)

# Python Collections (Arrays)
# There are four collection data types in the Python programming language:
# - List is a collection which is ordered and changeable. Allows duplicate members.
# - Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# - Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# - Dictionary is a collection which is ordered** and changeable. No duplicate members.
# *Set items are unchangeable, but you can remove and/or add items whenever you like.
# **As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.



# Python - Access Tuple Items

# You can access tuple items by referring to the index number, inside square brackets:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])  # Outputs: banana

# Note: The first item has index 0.

# Negative Indexing:
# Negative indexing means start from the end.
# -1 refers to the last item, -2 refers to the second last item, and so on.
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])  # Outputs: cherry

# Range of Indexes:
# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new tuple with the specified items.
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])  # Outputs: ('cherry', 'orange', 'kiwi')

# Note: The search will start at index 2 (included) and end at index 5 (not included).
# Remember that the first item has index 0.

# By leaving out the start value, the range will start at the first item:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])  # Outputs: ('apple', 'banana', 'cherry', 'orange')

# By leaving out the end value, the range will go on to the end of the tuple:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])  # Outputs: ('cherry', 'orange', 'kiwi', 'melon', 'mango')

# Range of Negative Indexes:
# Specify negative indexes if you want to start the search from the end of the tuple:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])  # Outputs: ('orange', 'kiwi', 'melon')

# Check if Item Exists:
# To determine if a specified item is present in a tuple, use the 'in' keyword:
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")  # Outputs: Yes, 'apple' is in the fruits tuple




# Python - Update Tuples

# Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.
# However, there are some workarounds to modify a tuple.

# Change Tuple Values:
# Although tuples are immutable, you can convert the tuple into a list, change the list, and convert it back into a tuple.

# Example: Convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)  # Outputs: ('apple', 'kiwi', 'cherry')

# Add Items:
# Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple.

# Method 1: Convert into a list:
# Convert the tuple into a list, add your item(s), and convert it back into a tuple.

# Example: Convert the tuple into a list, add "orange", and convert it back into a tuple:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)  # Outputs: ('apple', 'banana', 'cherry', 'orange')

# Method 2: Add tuple to a tuple:
# You can add tuples to tuples, so if you want to add one item (or many), create a new tuple with the item(s), and add it to the existing tuple.

# Example: Create a new tuple with the value "orange", and add that tuple:
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)  # Outputs: ('apple', 'banana', 'cherry', 'orange')

# Note: When creating a tuple with only one item, remember to include a comma after the item, otherwise it will not be identified as a tuple.

# Remove Items:
# Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as for changing and adding tuple items.

# Example: Convert the tuple into a list, remove "apple", and convert it back into a tuple:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)  # Outputs: ('banana', 'cherry')

# Or you can delete the tuple completely:

# Example: The del keyword can delete the tuple completely:
thistuple = ("apple", "banana", "cherry")
del thistuple
# print(thistuple)  # This will raise an error because the tuple no longer exists.




# Python - Unpack Tuples

# Unpacking a Tuple:
# When we create a tuple, we normally assign values to it. This is called "packing" a tuple.
fruits = ("apple", "banana", "cherry")  # Packing a tuple

# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
(green, yellow, red) = fruits

print(green)   # Outputs: apple
print(yellow)  # Outputs: banana
print(red)     # Outputs: cherry

# Note: The number of variables must match the number of values in the tuple; otherwise, you must use an asterisk to collect the remaining values as a list.

# Using Asterisk *:
# If the number of variables is less than the number of values, you can add an * to the variable name and the remaining values will be assigned to the variable as a list:
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits

print(green)   # Outputs: apple
print(yellow)  # Outputs: banana
print(red)     # Outputs: ['cherry', 'strawberry', 'raspberry']

# If the asterisk is added to another variable name other than the last, Python will assign values to the variable until the number of values left matches the number of variables left.
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits

print(green)   # Outputs: apple
print(tropic)  # Outputs: ['mango', 'papaya', 'pineapple']
print(red)     # Outputs: cherry



# Python - Loop Tuples

# Loop Through a Tuple
# You can loop through the tuple items by using a for loop.
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)
# Output:
# apple
# banana
# cherry

# Loop Through the Index Numbers
# You can also loop through the tuple items by referring to their index number.
# Use the range() and len() functions to create a suitable iterable.
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])
# Output:
# apple
# banana
# cherry

# Using a While Loop
# You can loop through the tuple items by using a while loop.
# Use the len() function to determine the length of the tuple,
# then start at 0 and loop your way through the tuple items by referring to their indexes.
# Remember to increase the index by 1 after each iteration.
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i += 1
# Output:
# apple
# banana
# cherry



# Python - Join Tuples

# Join Two Tuples:
# To join two or more tuples, you can use the + operator.

# Example: Join two tuples
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)  # Outputs: ('a', 'b', 'c', 1, 2, 3)

# Multiply Tuples:
# If you want to multiply the content of a tuple a given number of times, you can use the * operator.

# Example: Multiply the fruits tuple by 2
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)  # Outputs: ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')






# Python - Tuple Methods

# Python has two built-in methods that you can use on tuples:

# 1. count()
#    - Description: Returns the number of times a specified value occurs in a tuple.
#    - Syntax: tuple.count(value)
#    - Parameters:
#        - value: Required. The item to search for.
#    - Example:
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)  # Outputs: 2

# 2. index()
#    - Description: Searches the tuple for a specified value and returns the position of where it was found.
#    - Syntax: tuple.index(value)
#    - Parameters:
#        - value: Required. The item to search for.
#    - Example:
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)  # Outputs: 3





