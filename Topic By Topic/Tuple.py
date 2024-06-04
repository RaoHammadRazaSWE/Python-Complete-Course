# Tuple : Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets '()'.

#  Create a Tuple:
my_tuple = ("apple","Ali", "cherry")
print(my_tuple)

# Accessing elements of a tuple
print(my_tuple[1])

# Tuples are immutable (cannot be changed)
# The following line would result in an error:
# my_tuple[0] = 10

# Some  Characteristics of Tuples:

# 1) Immutable:Once a tuple is created, you cannot modify its elements. You cannot add, remove, 
# or change elements after the tuple is defined.

# 2) Ordered: Tuples maintain the order of elements, 
# meaning the order in which elements are defined is preserved.

# 3) Allows Heterogeneous Elements: Tuples can contain elements of different data types.

# 4) Can Be Used as Dictionary Keys: Because of their immutability, 
# tuples can be used as keys in dictionaries, unlike lists.

# Create Tuple with one item:To create a tuple with only one item,
# you have to add a comma after the item,otherwise Python will not recognize it as a tuple.

# One item tuple, remember the  comma:
thistuple = ("apple",)
print(type(thistuple))

# Not a tuple
nottuple = ("apple")
print(type(nottuple))

#Tuple items-Data Types: tuple can be write any data type.

# String, int and boolean data types:
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

# A tuple can contain different data types:
# A tuple with strings, integers and boolean values:
tuple6 = ("abc", 34, True, 40, "male",34)

# This code mean first element misse output
print(tuple6[1:])

print(tuple6[2:4])

# This code work print last side 40
print(tuple6[-2])

# This code work print first two element:
print(tuple6[:2])

# Tuple with in a Tuples:
tuple4 = (tuple1,tuple2)
print(tuple4)

# cancatinate tuples:
tuple4 = tuple2 + tuple1
print(tuple4)

# Convert List in Tuples:
list1 = [1,4,6,7]
print(tuple(list1))

# Convert Tuples in List:
tuple = (1,2,4,5)
print(list[tuple])
