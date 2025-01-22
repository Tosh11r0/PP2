#mylist = ["apple", "banana", "cherry"]

#List
#Lists are used to store multiple items in a single variable.
#Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

thislist = ["apple", "banana", "cherry"]
print(thislist)

"""
List Items
List items are ordered, changeable, and allow duplicate values.

List items are indexed, the first item has index [0], the second item has index [1] etc. 
"""

""" 
ORDERED
When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
If you add new items to a list, the new items will be placed at the end of the list.

Changeable
The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

Allow Duplicates
Since lists are indexed, lists can have items with the same value:
"""

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#To determine how many items a list has, use the len() function:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#List items can be of any data type:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#A list can contain different data types:
list1 = ["abc", 34, True, 40, "male"]

#From Python's perspective, lists are defined as objects with the data type 'list':
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#The list() Constructor
#It is also possible to use the list() constructor when creating a new list.
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)








# Python - ACCESS LIST ITEMS

# List items are indexed and you can access them by referring to the index number:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])  # Outputs: banana

# Note: The first item has index 0.

# Negative Indexing:
# Negative indexing means start from the end. -1 refers to the last item, -2 refers to the second last item, and so on.
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])  # Outputs: cherry

# Range of Indexes:
# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new list with the specified items.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])  # Outputs: ['cherry', 'orange', 'kiwi']

# Note: The search will start at index 2 (included) and end at index 5 (not included).
# Remember that the first item has index 0.

# By leaving out the start value, the range will start at the first item:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])  # Outputs: ['apple', 'banana', 'cherry', 'orange']

# By leaving out the end value, the range will go on to the end of the list:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])  # Outputs: ['cherry', 'orange', 'kiwi', 'melon', 'mango']

# Range of Negative Indexes:
# Specify negative indexes if you want to start the search from the end of the list:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])  # Outputs: ['orange', 'kiwi', 'melon']

# Check if Item Exists:
# To determine if a specified item is present in a list, use the 'in' keyword:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")  # Outputs: Yes, 'apple' is in the fruits list









# Python - СHANGE LIST ITEMS

# To change the value of a specific item, refer to the index number:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)  # Outputs: ['apple', 'blackcurrant', 'cherry']

# To change the value of items within a specific range, define a list with the new values,
# and refer to the range of index numbers where you want to insert the new values:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)  # Outputs: ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']

# If you insert more items than you replace, the new items will be inserted where you specified,
# and the remaining items will move accordingly:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)  # Outputs: ['apple', 'blackcurrant', 'watermelon', 'cherry']

# Note: The length of the list will change when the number of items inserted does not match the number of items replaced.

# If you insert fewer items than you replace, the new items will be inserted where you specified,
# and the remaining items will move accordingly:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)  # Outputs: ['apple', 'watermelon']

# To insert a new list item, without replacing any of the existing values, we can use the insert() method.
# The insert() method inserts an item at the specified index:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)  # Outputs: ['apple', 'banana', 'watermelon', 'cherry']

# Note: As a result of the example above, the list will now contain 4 items.





# Python - ADD LIST ITEMS

# Append Items
# To add an item to the end of the list, use the append() method:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)  # Outputs: ['apple', 'banana', 'cherry', 'orange']

# Insert Items
# To insert a list item at a specified index, use the insert() method.
# The insert() method inserts an item at the specified index:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)  # Outputs: ['apple', 'orange', 'banana', 'cherry']

# Note: As a result of the examples above, the lists will now contain 4 items.

# Extend List
# To append elements from another list to the current list, use the extend() method.
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)  # Outputs: ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

# The elements will be added to the end of the list.

# Add Any Iterable
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)  # Outputs: ['apple', 'banana', 'cherry', 'kiwi', 'orange']



# Python - Remove List Items

# Remove Specified Item
# The remove() method removes the specified item.
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)  # Outputs: ['apple', 'cherry']

# If there are more than one item with the specified value, the remove() method removes the first occurrence.
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)  # Outputs: ['apple', 'cherry', 'banana', 'kiwi']

# Remove Specified Index
# The pop() method removes the specified index.
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)  # Outputs: ['apple', 'cherry']

# If you do not specify the index, the pop() method removes the last item.
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)  # Outputs: ['apple', 'banana']

# The del keyword also removes the specified index.
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)  # Outputs: ['banana', 'cherry']

# The del keyword can also delete the list completely.
thislist = ["apple", "banana", "cherry"]
del thislist
# print(thislist)  # This will raise an error because "thislist" no longer exists.

# Clear the List
# The clear() method empties the list. The list still remains, but it has no content.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)  # Outputs: []



# Python - Loop Lists

# Loop Through a List
# You can loop through the list items by using a for loop:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
# Output:
# apple
# banana
# cherry

# Loop Through the Index Numbers
# You can also loop through the list items by referring to their index number.
# Use the range() and len() functions to create a suitable iterable.
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])
# Output:
# apple
# banana
# cherry

# Using a While Loop
# You can loop through the list items by using a while loop.
# Use the len() function to determine the length of the list,
# then start at 0 and loop your way through the list items by referring to their indexes.
# Remember to increase the index by 1 after each iteration.
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i += 1
# Output:
# apple
# banana
# cherry

# Looping Using List Comprehension
# List Comprehension offers the shortest syntax for looping through lists:
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
# Output:
# apple
# banana
# cherry





# Python - List Comprehension

# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

# Example:
# Based on a list of fruits, you want a new list containing only the fruits with the letter "a" in the name.

# Without list comprehension, you will have to write a for statement with a conditional test inside:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)  # Outputs: ['apple', 'banana', 'mango']

# With list comprehension, you can do all that with only one line of code:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)  # Outputs: ['apple', 'banana', 'mango']

# The Syntax:
# newlist = [expression for item in iterable if condition == True]

# The return value is a new list, leaving the old list unchanged.

# Condition:
# The condition is like a filter that only accepts the items that evaluate to True.

# Example:
# Only accept items that are not "apple":
newlist = [x for x in fruits if x != "apple"]
print(newlist)  # Outputs: ['banana', 'cherry', 'kiwi', 'mango']

# The condition is optional and can be omitted:
newlist = [x for x in fruits]
print(newlist)  # Outputs: ['apple', 'banana', 'cherry', 'kiwi', 'mango']

# Iterable:
# The iterable can be any iterable object, like a list, tuple, set, etc.

# Example:
# You can use the range() function to create an iterable:
newlist = [x for x in range(10)]
print(newlist)  # Outputs: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Same example, but with a condition:
# Accept only numbers lower than 5:
newlist = [x for x in range(10) if x < 5]
print(newlist)  # Outputs: [0, 1, 2, 3, 4]

# Expression:
# The expression is the current item in the iteration, but it is also the outcome,
# which you can manipulate before it ends up like a list item in the new list.

# Example:
# Set the values in the new list to upper case:
newlist = [x.upper() for x in fruits]
print(newlist)  # Outputs: ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']

# You can set the outcome to whatever you like:
# Example:
# Set all values in the new list to 'hello':
newlist = ['hello' for x in fruits]
print(newlist)  # Outputs: ['hello', 'hello', 'hello', 'hello', 'hello']

# The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
# Example:
# Return "orange" instead of "banana":
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)  # Outputs: ['apple', 'orange', 'cherry', 'kiwi', 'mango']






# Python - Sort Lists

# Sort List Alphanumerically
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)  # Outputs: ['banana', 'kiwi', 'mango', 'orange', 'pineapple']

# Sort the list numerically:
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)  # Outputs: [23, 50, 65, 82, 100]

# Sort Descending
# To sort descending, use the keyword argument reverse = True:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)  # Outputs: ['pineapple', 'orange', 'mango', 'kiwi', 'banana']

# Sort the list descending:
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist)  # Outputs: [100, 82, 65, 50, 23]

# Customize Sort Function
# You can also customize your own function by using the keyword argument key = function.
# The function will return a number that will be used to sort the list (the lowest number first):
def myfunc(n):
    return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)  # Outputs: [50, 65, 23, 82, 100]

# Case Insensitive Sort
# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)  # Outputs: ['Kiwi', 'Orange', 'banana', 'cherry']

# Luckily we can use built-in functions as key functions when sorting a list.
# So if you want a case-insensitive sort function, use str.lower as a key function:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)  # Outputs: ['banana', 'cherry', 'Kiwi', 'Orange']

# Reverse Order
# What if you want to reverse the order of a list, regardless of the alphabet?
# The reverse() method reverses the current sorting order of the elements.
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)  # Outputs: ['cherry', 'Kiwi', 'Orange', 'banana']



# Python - Copy Lists

# You cannot copy a list simply by typing list2 = list1, because:
# list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

# Use the copy() method
# You can use the built-in List method copy() to copy a list.
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)  # Outputs: ['apple', 'banana', 'cherry']

# Use the list() method
# Another way to make a copy is to use the built-in method list().
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)  # Outputs: ['apple', 'banana', 'cherry']

# Use the slice operator
# You can also make a copy of a list by using the slice operator [:].
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)  # Outputs: ['apple', 'banana', 'cherry']



# Python - Join Lists

# There are several ways to join, or concatenate, two or more lists in Python.

# 1. Using the + operator:
# One of the easiest ways is by using the + operator.
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)  # Outputs: ['a', 'b', 'c', 1, 2, 3]

# 2. Appending all items from one list into another:
# Another way to join two lists is by appending all the items from list2 into list1, one by one.
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
for x in list2:
    list1.append(x)
print(list1)  # Outputs: ['a', 'b', 'c', 1, 2, 3]

# 3. Using the extend() method:
# Or you can use the extend() method, which purpose is to add elements from one list to another list.
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)  # Outputs: ['a', 'b', 'c', 1, 2, 3]



# Python List Methods

# Python has a set of built-in methods that you can use on lists.
""" 
 Method           Description
 append()         Adds an element at the end of the list
 clear()          Removes all the elements from the list
 copy()           Returns a copy of the list
 count()          Returns the number of elements with the specified value
 extend()         Adds the elements of a list (or any iterable) to the end of the current list
 index()          Returns the index of the first element with the specified value
 insert()         Adds an element at the specified position
 pop()            Removes the element at the specified position
 remove()         Removes the first item with the specified value
 reverse()        Reverses the order of the list
 sort()           Sorts the list
"""