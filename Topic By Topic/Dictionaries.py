# Dictionaries : Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is unordered, changeable and do not allow duplicates.
# Dictionaries are also known as associative arrays or hash maps in other programming languages.

# Dictionaries are written with curly brackets, and have keys and values:
#1) Create and print a dictionary:

mydict = {"brand": "Ford",  "model": "Mustang","year": 1964}
# print(mydict)

#2) Accessing Values:You can access the values in a dictionary using the keys. brand is key.
print(mydict["brand"]) # Output:value1

#3) If the key is not present, it will raise a KeyError. To avoid this, you can use the get method:
print(mydict.get('key4','default_value')) # output:default_value

#4) Modifying Values:You can modify the value associated with a key:
mydict['year'] = '2024'
print(mydict)

#5) Adding New key-value Pairs:You can add new key-value pairs to a dictionary:
mydict['color']='Red'
print(mydict)

# Dictionary Items:Dictionary items are ordered, changeable, and does not allow duplicates.
# Dictionary items are presented in key:value pairs, and 
# can be referred to by using the key name.

#6) Remvoing Key-Value Pairs:You can remove a key-value pair using 
# the 'del' statement or the 'pop' method:

# By using "del":
del mydict['model']
print(mydict)

# By using "pop": pop is always uses () in between put key.
mydict.pop('brand')
print(mydict)

#7) Iterating Over a Dictionary:You can iterate through the keys, values, 
# or items (key-value pairs) in a dictionary: Using For loop:
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# Loop over keys and values:
for key in my_dict:
    print(key, my_dict[key])

# Loop over values:
for value in my_dict.values():
    print(value)

# Loop over keys and values using items:
for key, value in my_dict.items():
    print(key,value)

#Dictionaries are versatile and widely used in Python for various tasksdue to their efficiency
#in providing fast lookups and mappings.They are commonly employed in situations where
# you need to store and retrieve data using a specific identifier (key).

# Duplicates Not Allowed:Dictionaries cannot have two items with the same key.
# Duplicates values will overwrite existing values:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

# Looping through a dictionary: keys() You can step through the keys of a dictionary.
# printing the values from the Dictionary

my_dict = { "brand": "Ford",  "model": "Mustang",  3 : 1964,  "year": 2020}

for value in my_dict.values():
    print(value)
    
# Example: Printing keys from the dictionary

# Assume a dictionary with information about a car
car_info_dict = {"brand": "Ford", "model": "Mustang", "year": 2020}

# Iterate through each key in the dictionary
for car_key in car_info_dict.keys():
    # Print each key
    print(car_key)
