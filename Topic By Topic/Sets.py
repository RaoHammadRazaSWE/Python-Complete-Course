# Set : Sets are used to store multiple items in a single variable.
# A set is a collection which is unordered, unchangeable, and unindexed. *Note:** Set 
# items are unchangeable, but you can remove items and add new items.

# Creating a set using curly braces:
my_set =  {1,2,4,5,6}
print(my_set)

# Some characticey of set  :

# 1) Uniqueness: A set cannot contain duplicate elements.
# If you try to add an element that is already present, the set will not change.

thisset = {"apple" , "banana" , "cherry" , "apple"}
print(thisset)
print(len(thisset))

# 2) Order: Unlike lists, sets are unordered, meaning the elements do not have a specific order.
# This means that sets do not support indexing or slicing.

num_set = {1,2,3,4,5,6}
print(len(num_set))
# print(num_set[3]) # no work

# 3) Mutability:  Sets are mutable, meaning you can add or remove elements after the set is
# created. However,the elements themselves must be immutable (e.g., numbers, strings, or tuples).

# Adding elements to a set:
my_set.add(800)
print(my_set)

# Removing elements from a set:
my_set.remove(5)
print(my_set)

# Remove Rendam element in set:
print(my_set.pop())

# Another method Remove element in set by using Discard:
my_set.discard(6)
# print(my_set)

# Clear all Set :
my_set.clear()
# print(my_set)

# Creating a set using the set() constructor: another method writing set.
another_set = set([2,3,4,5,6])
# print(another_set)

# Set items - Data Types: set can be write in any data type:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

# A set can contain different data types:
# A set with strings, integers and boolean values:
set_mul = {"abc", 34, True, 40, "male"}
# print(set_mul)

# Type() :From Python's perspective, sets are defined as objects with the data type 'set':
fruits_set = {"apple" , "banana", "cherry"}
# print(type(fruits_set))

# Set is not allowed List add:
# my_set.add([12,3,45])
# print(my_set)

name_set = {"ali" , "hammad",3}
name2_set = {"rao", "hammad",}

# Union of set:

# un_set =name_set.union(name2_set)
# print(un_set)
# Another method of Union of set: Multi sets
# print(name_set | name2_set | set1)

# Conver Tuples in set:
# print(set1.union(("ali" , "Jenny")))

# Update Set:
set1.update(set2)
# print(set1)

# Update set Using List:
set2.update(['Khan',"Imran"])
# print(set2)

# Another method used set update:
set1.update(["hammad","raza"])
# print(set1)

# Intersection of set:

setf = {1, 5, 7, 9, 3}
setk= {1, 15, 7, 9, 13,"raza"}
setj = {1, 5, 7, 9,"rao",34}

# M1:
# print(setf.intersection(setk,set3))

# M2:
# print(setf & setk & setj)
setf.intersection_update(setk)
# print(setf)

# Differenc between Set:

# print(setk.difference(setj))
# print(setk - setf)

# Symmetric Difference:

# M1: this is used only two and more three .
# print(setk.symmetric_difference(setj))

# M1 : this is used multip of set difference:
# print(setf ^ setk ^ setk)

# Symmetric Difference Update:

# setk.symmetric_difference_update(setf)

# setk.symmetric_difference_update(('ali','hadi'))
# print(setk)

# Types of Set:
setA = {1,2,3,4,5,}
setB = {6,7,8,1,2,3,4,5}

# Disjoin Set: both set element is no same is True other wise False.
# print(setA.isdisjoint(setB)) # False.
# print(setA.isdisjoint(['Mone','Aliza'])) # True.

# Subset: SetA is  subset of setB if everyelement of setA is in setB. setB <= setA.
# print(setA.issubset(setB))
# print(setA <= setB)

# Superset: SetB is superset of setA if setB contains everyelement of SetA. setB >= setA.
print(setB.issuperset(setA))
print(setB >= setA)

# Deleting of set:
del setA
# print(setA) this time  setA is not show output because above statement delet of setA.
