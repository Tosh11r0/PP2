# Python Dictionaries

# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable, and does not allow duplicates.
# *As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

# Creating a Dictionary:
# Dictionaries are written with curly brackets, and have keys and values.

# Example:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
# Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# Dictionary Items:
# - Ordered (as of Python 3.7)
# - Changeable
# - Do not allow duplicates

# Accessing Items:
# You can access items by referring to its key name, inside square brackets.

# Example:
print(thisdict["brand"])
# Output: Ford

# There is also a method called get() that will give you the same result.

# Example:
print(thisdict.get("model"))
# Output: Mustang

# Changing Items:
# You can change the value of a specific item by referring to its key name.

# Example:
thisdict["year"] = 2018
print(thisdict)
# Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2018}

# Loop Through a Dictionary:
# You can loop through a dictionary by using a for loop.

# Example: Print all key names in the dictionary, one by one:
for key in thisdict:
    print(key)
# Output:
# brand
# model
# year

# Example: Print all values in the dictionary, one by one:
for key in thisdict:
    print(thisdict[key])
# Output:
# Ford
# Mustang
# 2018

# You can also use the values() method to return values of a dictionary.

# Example:
for value in thisdict.values():
    print(value)
# Output:
# Ford
# Mustang
# 2018

# You can use the keys() method to return the keys of a dictionary.

# Example:
for key in thisdict.keys():
    print(key)
# Output:
# brand
# model
# year

# Loop through both keys and values, by using the items() method.

# Example:
for key, value in thisdict.items():
    print(key, value)
# Output:
# brand Ford
# model Mustang
# year 2018

# Check if Key Exists:
# To determine if a specified key is present in a dictionary, use the in keyword.

# Example:
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")
# Output: Yes, 'model' is one of the keys in the thisdict dictionary

# Dictionary Length:
# To determine how many items a dictionary has, use the len() function.

# Example:
print(len(thisdict))
# Output: 3

# Adding Items:
# Adding an item to the dictionary is done by using a new index key and assigning a value to it.

# Example:
thisdict["color"] = "red"
print(thisdict)
# Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2018, 'color': 'red'}

# Removing Items:
# There are several methods to remove items from a dictionary.

# Example: The pop() method removes the item with the specified key name:
thisdict.pop("model")
print(thisdict)
# Output: {'brand': 'Ford', 'year': 2018, 'color': 'red'}

# Example: The popitem() method removes the last inserted item:
thisdict.popitem()
print(thisdict)
# Output: {'brand': 'Ford', 'year': 2018}

# Example: The del keyword removes the item with the specified key name:
del thisdict["year"]
print(thisdict)
# Output: {'brand': 'Ford'}

# Example: The clear() method empties the dictionary:
thisdict.clear()
print(thisdict)
# Output: {}

# Copying a Dictionary:
# You cannot copy a dictionary simply by typing dict2 = dict1, because dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.

# There are ways to make a copy, one way is to use the built-in Dictionary method copy().

# Example:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2018
}
mydict = thisdict.copy()
print(mydict)
# Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2018}

# Another way to make a copy is to use the built-in function dict().

# Example:
mydict = dict(thisdict)
print(mydict)
# Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2018}

# Nested Dictionaries:
# A dictionary can contain dictionaries, this is called nested dictionaries.

# Example:
myfamily = {
  "child1": {
    "name": "Emil",
    "year": 2004
  },
  "child2": {
    "name": "Tobias",
    "year": 2007
  },
  "child3": {
    "name": "Linus",
    "year": 2011
  }
}
print(myfamily)
# Output: {'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}

# The dict() Constructor:
# It is also possible to use the dict() constructor to make a new dictionary.

# Example:
thisdict = dict(brand="Ford", model="Mustang", year=2018)
print(thisdict)
# Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2018}



# Python - Access Dictionary Items

# Accessing Items
# You can access the items of a dictionary by referring to its key name, inside square brackets:

# Example: Get the value of the "model" key:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)  # Output: Mustang

# There is also a method called get() that will give you the same result:

# Example: Get the value of the "model" key using get():
x = thisdict.get("model")
print(x)  # Output: Mustang

# Get Keys
# The keys() method will return a list of all the keys in the dictionary.

# Example: Get a list of the keys:
x = thisdict.keys()
print(x)  # Output: dict_keys(['brand', 'model', 'year'])

# The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.

# Example: Add a new item to the original dictionary, and see that the keys list gets updated as well:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.keys()
print(x)  # before the change

car["color"] = "white"
print(x)  # after the change
# Output:
# dict_keys(['brand', 'model', 'year'])
# dict_keys(['brand', 'model', 'year', 'color'])

# Get Values
# The values() method will return a list of all the values in the dictionary.

# Example: Get a list of the values:
x = thisdict.values()
print(x)  # Output: dict_values(['Ford', 'Mustang', 1964])

# The list of the values is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list.

# Example: Make a change in the original dictionary, and see that the values list gets updated as well:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.values()
print(x)  # before the change

car["year"] = 2020
print(x)  # after the change
# Output:
# dict_values(['Ford', 'Mustang', 1964])
# dict_values(['Ford', 'Mustang', 2020])

# Example: Add a new item to the original dictionary, and see that the values list gets updated as well:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.values()
print(x)  # before the change

car["color"] = "red"
print(x)  # after the change
# Output:
# dict_values(['Ford', 'Mustang', 1964])
# dict_values(['Ford', 'Mustang', 1964, 'red'])

# Get Items
# The items() method will return each item in a dictionary, as tuples in a list.

# Example: Get a list of the key:value pairs:
x = thisdict.items()
print(x)  # Output: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

# The returned list is a view of the items of the dictionary, meaning that any changes done to the dictionary will be reflected in the items list.

# Example: Make a change in the original dictionary, and see that the items list gets updated as well:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()
print(x)  # before the change

car["year"] = 2020
print(x)  # after the change
# Output:
# dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
# dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2020)])

# Example: Add a new item to the original dictionary, and see that the items list gets updated as well:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()
print(x)  # before the change

car["color"] = "red"
print(x)  # after the change
# Output:
# dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
# dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964), ('color', 'red')])

# Check if Key Exists
# To determine if a specified key is present in a dictionary use the in keyword:

# Example: Check if "model" is present in the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
# Output: Yes, 'model' is one of the keys in the thisdict dictionary





# Python - Change Dictionary Items

# Change Values
# You can change the value of a specific item by referring to its key name:

# Example: Change the "year" to 2018:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)
# Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2018}

# Update Dictionary
# The update() method will update the dictionary with the items from the given argument.
# The argument must be a dictionary, or an iterable object with key:value pairs.

# Example: Update the "year" of the car by using the update() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)
# Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}




# Python - Add Dictionary Items

# Adding Items
# To add an item to a dictionary, assign a value to a new key.

# Example: Add a new key "color" with the value "red" to the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
# Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

# Update Dictionary
# The update() method updates the dictionary with the items from a given argument.
# If the item does not exist, it will be added.
# The argument must be a dictionary or an iterable object with key:value pairs.

# Example: Add a new key "color" with the value "red" using the update() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
print(thisdict)
# Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}






# Python - Remove Dictionary Items

# Removing Items
# There are several methods to remove items from a dictionary:

# 1. pop()
#    - Description: Removes the item with the specified key name.
#    - Syntax: dictionary.pop(keyname, defaultvalue)
#    - Parameters:
#        - keyname: Required. The key name of the item you want to remove.
#        - defaultvalue: Optional. A value to return if the specified key does not exist.
#    - Example:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
# Output: {'brand': 'Ford', 'year': 1964}

# 2. popitem()
#    - Description: Removes the last inserted item (in versions before 3.7, a random item is removed instead).
#    - Syntax: dictionary.popitem()
#    - Example:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
# Output: {'brand': 'Ford', 'model': 'Mustang'}

# 3. del
#    - Description: Removes the item with the specified key name or deletes the dictionary completely.
#    - Syntax: del dictionary[keyname] or del dictionary
#    - Example (remove specific item):
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
# Output: {'brand': 'Ford', 'year': 1964}

#    - Example (delete entire dictionary):
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
# print(thisdict)  # This will raise an error because "thisdict" no longer exists.

# 4. clear()
#    - Description: Empties the dictionary.
#    - Syntax: dictionary.clear()
#    - Example:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)
# Output: {}



# Python - Loop Dictionaries

# Loop Through a Dictionary
# You can loop through a dictionary by using a for loop.
# When looping through a dictionary, the return value is the keys of the dictionary, but there are methods to return the values as well.

# Example: Print all key names in the dictionary, one by one:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)
# Output:
# brand
# model
# year

# Example: Print all values in the dictionary, one by one:
for x in thisdict:
  print(thisdict[x])
# Output:
# Ford
# Mustang
# 1964

# You can also use the values() method to return values of a dictionary:

# Example:
for x in thisdict.values():
  print(x)
# Output:
# Ford
# Mustang
# 1964

# You can use the keys() method to return the keys of a dictionary:

# Example:
for x in thisdict.keys():
  print(x)
# Output:
# brand
# model
# year

# Loop through both keys and values, by using the items() method:

# Example:
for x, y in thisdict.items():
  print(x, y)
# Output:
# brand Ford
# model Mustang
# year 1964



# Python - Copy Dictionaries

# Copying a Dictionary
# You cannot copy a dictionary simply by typing dict2 = dict1, because dict2 will only be a reference to dict1,
# and changes made in dict1 will automatically also be made in dict2.

# There are ways to make a copy; one way is to use the built-in Dictionary method copy().

# Example: Make a copy of a dictionary with the copy() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
# Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# Another way to make a copy is to use the built-in function dict().

# Example: Make a copy of a dictionary with the dict() function:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)
# Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}







# Python - Nested Dictionaries

# Nested Dictionaries
# A dictionary can contain other dictionaries, which is referred to as nested dictionaries.

# Example: Create a dictionary that contains three dictionaries:
myfamily = {
  "child1": {
    "name": "Emil",
    "year": 2004
  },
  "child2": {
    "name": "Tobias",
    "year": 2007
  },
  "child3": {
    "name": "Linus",
    "year": 2011
  }
}
print(myfamily)
# Output:
# {
#   'child1': {'name': 'Emil', 'year': 2004},
#   'child2': {'name': 'Tobias', 'year': 2007},
#   'child3': {'name': 'Linus', 'year': 2011}
# }

# Alternatively, you can create individual dictionaries and then nest them into a new dictionary:

# Example: Create three dictionaries, then create one dictionary that will contain the other three:
child1 = {
  "name": "Emil",
  "year": 2004
}
child2 = {
  "name": "Tobias",
  "year": 2007
}
child3 = {
  "name": "Linus",
  "year": 2011
}

myfamily = {
  "child1": child1,
  "child2": child2,
  "child3": child3
}
print(myfamily)
# Output:
# {
#   'child1': {'name': 'Emil', 'year': 2004},
#   'child2': {'name': 'Tobias', 'year': 2007},
#   'child3': {'name': 'Linus', 'year': 2011}
# }

# Access Items in Nested Dictionaries
# To access items from a nested dictionary, use the names of the dictionaries, starting with the outer dictionary:

# Example: Print the name of child 2:
print(myfamily["child2"]["name"])
# Output: Tobias

# Loop Through Nested Dictionaries
# You can loop through a dictionary by using the items() method:

# Example: Loop through the keys and values of all nested dictionaries:
for key, value in myfamily.items():
  print(key)
  for sub_key, sub_value in value.items():
    print(f"  {sub_key}: {sub_value}")
# Output:
# child1
#   name: Emil
#   year: 2004
# child2
#   name: Tobias
#   year: 2007
# child3
#   name: Linus
#   year: 2011






# Python Dictionary Methods

# Python предоставляет набор встроенных методов, которые можно использовать со словарями.

# 1. clear()
#    - Описание: Удаляет все элементы из словаря.
#    - Синтаксис: dictionary.clear()
#    - Пример:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
print(car)  # Вывод: {}

# 2. copy()
#    - Описание: Возвращает копию словаря.
#    - Синтаксис: dictionary.copy()
#    - Пример:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.copy()
print(x)  # Вывод: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# 3. fromkeys()
#    - Описание: Возвращает словарь с указанными ключами и значением.
#    - Синтаксис: dict.fromkeys(keys, value)
#    - Параметры:
#        - keys: Обязательный. Последовательность ключей.
#        - value: Необязательный. Значение для всех ключей. По умолчанию None.
#    - Пример:
keys = ('key1', 'key2', 'key3')
value = 0
new_dict = dict.fromkeys(keys, value)
print(new_dict)  # Вывод: {'key1': 0, 'key2': 0, 'key3': 0}

# 4. get()
#    - Описание: Возвращает значение указанного ключа.
#    - Синтаксис: dictionary.get(keyname, value)
#    - Параметры:
#        - keyname: Обязательный. Ключ элемента, значение которого вы хотите получить.
#        - value: Необязательный. Значение, которое нужно вернуть, если ключ не существует. По умолчанию None.
#    - Пример:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.get("model")
print(x)  # Вывод: Mustang

# 5. items()
#    - Описание: Возвращает объект представления, содержащий пары ключ-значение словаря в виде кортежей в списке.
#    - Синтаксис: dictionary.items()
#    - Пример:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.items()
print(x)  # Вывод: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

# 6. keys()
#    - Описание: Возвращает объект представления, содержащий ключи словаря.
#    - Синтаксис: dictionary.keys()
#    - Пример:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.keys()
print(x)  # Вывод: dict_keys(['brand', 'model', 'year'])

# 7. pop()
#    - Описание: Удаляет элемент с указанным ключом.
#    - Синтаксис: dictionary.pop(keyname, defaultvalue)
#    - Параметры:
#        - keyname: Обязательный. Ключ элемента, который нужно удалить.
#        - defaultvalue: Необязательный. Значение, которое нужно вернуть, если ключ не существует.
#    - Пример:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
print(car)  # Вывод: {'brand': 'Ford', 'year': 1964}

# 8. popitem()
#    - Описание: Удаляет последнюю вставленную пару ключ-значение.
#    - Синтаксис: dictionary.popitem()
#    - Пример:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.popitem()
print(car)  # Вывод: {'brand': 'Ford', 'model': 'Mustang'}

# 9. setdefault()
#    - Описание: Возвращает значение указанного ключа. Если ключ не существует, вставляет ключ с указанным значением.
#    - Синтаксис: dictionary.setdefault(keyname, value)
#    - Параметры:
#        - keyname: Обязательный. Ключ для поиска.
#        - value: Необязательный. Значение, которое нужно вставить, если ключ не существует. По умолчанию None.
#    - Пример:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("color", "white")
print(x)  # Вывод: white
print(car)  # Вывод: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'white'}

# 10. update()
#     - Описание: Обновляет словарь указанными парами ключ-значение.
#     - Синтаксис: dictionary.update(iterable)
#     - Параметры:
#         - iterable: Обязательный. Словарь или итерируемый объект с парами ключ-значение.
#     - Пример:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.update({"color": "red"})
print(car)  # Вывод: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

# 11. values()
#     - Описание: Возвращает объект представления, содержащий значения словаря.
#     - Синтаксис: dictionary.values()
#     - Пример:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.values()
print(x)  # Вывод: dict_values(['Ford', 'Mustang', 1964])
