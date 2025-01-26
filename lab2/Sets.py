# Python Sets

# Sets are used to store multiple items in a single variable.
# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
# A set is a collection which is unordered, unchangeable*, and unindexed.
# *Note: Set items are unchangeable, but you can remove items and add new items.
# Sets are written with curly brackets.

# Example: Create a Set
thisset = {"apple", "banana", "cherry"}
print(thisset)

# Note: Sets are unordered, so you cannot be sure in which order the items will appear.

# Set Items
# Set items are unordered, unchangeable, and do not allow duplicate values.

# Unordered
# Unordered means that the items in a set do not have a defined order.
# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

# Unchangeable
# Set items are unchangeable, meaning that we cannot change the items after the set has been created.
# Once a set is created, you cannot change its items, but you can remove items and add new items.

# Duplicates Not Allowed
# Sets cannot have two items with the same value.

# Example: Duplicate values will be ignored
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

# Note: The values True and 1 are considered the same value in sets, and are treated as duplicates.

# Example: True and 1 is considered the same value
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

# Note: The values False and 0 are considered the same value in sets, and are treated as duplicates.

# Example: False and 0 is considered the same value
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)

# Get the Length of a Set
# To determine how many items a set has, use the len() function.

# Example: Get the number of items in a set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

# Set Items - Data Types
# Set items can be of any data type.

# Example: String, int and boolean data types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

# A set can contain different data types.

# Example: A set with strings, integers and boolean values
set1 = {"abc", 34, True, 40, "male"}

# type()
# From Python's perspective, sets are defined as objects with the data type 'set'.

# Example: What is the data type of a set?
myset = {"apple", "banana", "cherry"}
print(type(myset))

# The set() Constructor
# It is also possible to use the set() constructor to make a set.

# Example: Using the set() constructor to make a set
thisset = set(("apple", "banana", "cherry"))  # note the double round-brackets
print(thisset)

# Python Collections (Arrays)
# There are four collection data types in the Python programming language:
# - List is a collection which is ordered and changeable. Allows duplicate members.
# - Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# - Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# - Dictionary is a collection which is ordered** and changeable. No duplicate members.
# *Set items are unchangeable, but you can remove items and add new items.
# **As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.








# Python - Access Set Items

# Access Items
# You cannot access items in a set by referring to an index or a key.
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

# Example: Loop through the set, and print the values:
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

# Example: Check if "banana" is present in the set:
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

# Example: Check if "banana" is NOT present in the set:
thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset)

# Change Items
# Once a set is created, you cannot change its items, but you can add new items.







# Python - Add Set Items

# Add Items
# Once a set is created, you cannot change its items, but you can add new items.
# To add one item to a set, use the add() method.

# Example: Add an item to a set using the add() method
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
# Output: {'apple', 'banana', 'cherry', 'orange'}

# Add Sets
# To add items from another set into the current set, use the update() method.

# Example: Add elements from 'tropical' into 'thisset'
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
# Output: {'apple', 'banana', 'cherry', 'pineapple', 'mango', 'papaya'}

# Add Any Iterable
# The object in the update() method does not have to be a set; it can be any iterable object (tuples, lists, dictionaries, etc.).

# Example: Add elements of a list to a set
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)
# Output: {'apple', 'banana', 'cherry', 'kiwi', 'orange'}




# Python - Remove Set Items

# Remove Item
# To remove an item in a set, use the remove(), or the discard() method.

# Example: Remove "banana" by using the remove() method:
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
# Output: {'apple', 'cherry'}

# Note: If the item to remove does not exist, remove() will raise an error.

# Example: Remove "banana" by using the discard() method:
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
# Output: {'apple', 'cherry'}

# Note: If the item to remove does not exist, discard() will NOT raise an error.

# You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
# The return value of the pop() method is the removed item.

# Example: Remove a random item by using the pop() method:
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
# Output:
# apple
# {'banana', 'cherry'}

# Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

# Example: The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
# Output: set()

# Example: The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}
del thisset
# print(thisset)  # This will raise an error because the set no longer exists.






# Python - Loop Sets

# Loop Items
# You can loop through the set items by using a for loop:

# Example: Loop through the set, and print the values:
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)
# Output:
# apple
# banana
# cherry




# Python - Join Sets

# There are several ways to join two or more sets in Python.

# The `union()` and `update()` methods join all items from both sets.

# The `intersection()` method keeps ONLY the duplicates.

# The `difference()` method keeps the items from the first set that are not in the other set(s).

# The `symmetric_difference()` method keeps all items EXCEPT the duplicates.

# Union
# The `union()` method returns a new set with all items from both sets.

# Example: Join set1 and set2 into a new set:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
# Output: {'a', 1, 2, 3, 'b', 'c'}

# You can use the `|` operator instead of the `union()` method, and you will get the same result.

# Example: Use `|` to join two sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)
# Output: {'a', 1, 2, 3, 'b', 'c'}

# Join Multiple Sets
# All the joining methods and operators can be used to join multiple sets.

# When using a method, just add more sets in the parentheses, separated by commas:

# Example: Join multiple sets with the `union()` method:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)
# Output: {1, 2, 3, 'John', 'Elena', 'a', 'b', 'c', 'apple', 'bananas', 'cherry'}

# When using the `|` operator, separate the sets with more `|` operators:

# Example: Use `|` to join multiple sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 | set4
print(myset)
# Output: {1, 2, 3, 'John', 'Elena', 'a', 'b', 'c', 'apple', 'bananas', 'cherry'}

# Join a Set and a Tuple
# The `union()` method allows you to join a set with other data types, like lists or tuples.

# The result will be a set.

# Example: Join a set with a tuple:
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)
# Output: {1, 2, 3, 'a', 'b', 'c'}

# Note: The `|` operator only allows you to join sets with sets, and not with other data types like you can with the `union()` method.

# Update
# The `update()` method inserts all items from one set into another.

# The `update()` method changes the original set, and does not return a new set.

# Example: The `update()` method inserts the items in set2 into set1:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
# Output: {'a', 1, 2, 3, 'b', 'c'}

# Note: Both `union()` and `update()` will exclude any duplicate items.

# Intersection
# Keep ONLY the duplicates

# The `intersection()` method will return a new set, that only contains the items that are present in both sets.

# Example: Join set1 and set2, but keep only the duplicates:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)
# Output: {'apple'}

# You can use the `&` operator instead of the `intersection()` method, and you will get the same result.

# Example: Use `&` to join two sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)
# Output: {'apple'}

# Note: The `&` operator only allows you to join sets with sets, and not with other data types like you can with the `intersection()` method.

# The `intersection_update()` method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.

# Example: Keep the items that exist in both `set1`, and `set2`:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)
print(set1)
# Output: {'apple'}

# The values `True` and `1` are considered the same value. The same goes for `False` and `0`.

# Example: Join sets that contain the values `True`, `False`, `1`, and `0`, and see what is considered as duplicates:
set1 = {"apple", 1, "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)
print(set3)
# Output: {1, 'apple'}

# Difference
# The `difference()` method will return a new set that will contain only the items from the first set that are not present in the other set.

# Example: Keep all items from set1 that are not in set2:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)
print(set3)
# Output: {'banana', 'cherry'}

# You can use the `-` operator instead of the `difference()` method, and you will get the same result.

# Example: Use `-` to join two sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)
# Output: {'banana', 'cherry'}

# Note: The `-` operator only allows you to join sets with sets, and not with other data types
#::contentReference[oaicite:0]{index=0}
 


# Python Set Methods

# Python предоставляет несколько встроенных методов для работы с множествами:

# 1. add()
#    - Описание: Добавляет элемент в множество.
#    - Синтаксис: set.add(element)
#    - Параметры:
#        - element: Обязательный. Элемент, который нужно добавить.
#    - Пример:
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)  # Вывод: {'apple', 'banana', 'cherry', 'orange'}

# 2. clear()
#    - Описание: Удаляет все элементы из множества.
#    - Синтаксис: set.clear()
#    - Пример:
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)  # Вывод: set()

# 3. copy()
#    - Описание: Возвращает копию множества.
#    - Синтаксис: set.copy()
#    - Пример:
fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print(x)  # Вывод: {'apple', 'banana', 'cherry'}

# 4. difference()
#    - Описание: Возвращает множество, содержащее разницу между двумя или более множествами.
#    - Синтаксис: set.difference(set1, set2, ...)
#    - Пример:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)  # Вывод: {'banana', 'cherry'}

# 5. difference_update()
#    - Описание: Удаляет элементы из этого множества, которые также присутствуют в другом указанном множестве.
#    - Синтаксис: set.difference_update(set1, set2, ...)
#    - Пример:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)  # Вывод: {'banana', 'cherry'}

# 6. discard()
#    - Описание: Удаляет указанный элемент из множества.
#    - Синтаксис: set.discard(value)
#    - Параметры:
#        - value: Обязательный. Элемент, который нужно удалить.
#    - Пример:
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)  # Вывод: {'apple', 'cherry'}

# 7. intersection()
#    - Описание: Возвращает множество, являющееся пересечением двух других множеств.
#    - Синтаксис: set.intersection(set1, set2, ...)
#    - Пример:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)  # Вывод: {'apple'}

# 8. intersection_update()
#    - Описание: Удаляет элементы из этого множества, которые не присутствуют в других указанных множествах.
#    - Синтаксис: set.intersection_update(set1, set2, ...)
#    - Пример:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)  # Вывод: {'apple'}

# 9. isdisjoint()
#    - Описание: Возвращает True, если два множества не имеют общих элементов.
#    - Синтаксис: set.isdisjoint(set)
#    - Параметры:
#        - set: Обязательный. Множество для сравнения.
#    - Пример:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)  # Вывод: True

# 10. issubset()
#     - Описание: Возвращает True, если все элементы множества присутствуют в указанном множестве.
#     - Синтаксис: set.issubset(set)
#     - Параметры:
#         - set: Обязательный. Множество для сравнения.
#     - Пример:
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)  # Вывод: True

# 11. issuperset()
#     - Описание: Возвращает True, если все элементы указанного множества присутствуют в исходном множестве.
#     - Синтаксис: set.issuperset(set)
#     - Параметры:
#         - set: Обязательный. Множество для сравнения.
#     - Пример:
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)  # Вывод: True

# 12. pop()
#     - Описание: Удаляет случайный элемент из множества.
#     - Синтаксис: set.pop()
#     - Пример:
fruits = {"apple", "banana", "cherry"}
x = fruits.pop()
print(x)  # Вывод: 'apple' (или другой элемент, так как порядок не определен)
print(fruits)  # Вывод: оставшиеся элементы множества

# 13. remove()
#     - Описание: Удаляет указанный элемент из множества.
#     - Синтаксис: set.remove(value)
#     - Параметры:
#         - value: Обязательный. Элемент, который нужно удалить.
#     - Пример:
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)  # Вывод: {'apple', 'cherry'}

# 14. symmetric_difference()
#     - Описание: Возвращает множество с симметричной разницей двух множеств.
#     - Синтаксис: set.symmetric_difference(set)
#     - Пример:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)  # Вывод: {'banana', 'cherry', 'google', 'microsoft'}

# 15. symmetric_difference_update()
#     - Описание: Обновляет множество с симметричной разницей между
#::contentReference[oaicite:0]{index=0}
 
