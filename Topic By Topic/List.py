# List items: a list is a mutable and ordered collection of elements. 
# It is one of the built-in data types and is commonly used for
# storing and manipulating sequences of items. 
# Lists are defined by enclosing 
# the elements in square brackets [] and separating them with commas.

# Simple List Example:

student_number = [45,2,46,7,23,8]
print(student_number)

# Some Importan Chracticrsity of list:

# 1) Mutable: Lists can be modified after creation.
# # You can add, remove, or modify elements within a list.

# 2) Ordered: The order of elements in a list is maintained. 
# You can access elements by their index, starting from 0 for the first element. 

# 3) Dynamic: Lists can grow or shrink in size during the execution of a program.
# You can add or remove elements as needed.

integer_num = [1,2,3,4,5,6,7,8]

# Access the first element:
print(integer_num[0])

# Access the last element:
print(integer_num[-1])

# Find the lenght lsit:
print(len(integer_num))

# List items-Data Types: list can be write any data types: For Example.
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = [6,4,3,2,5]

# A list with strings, intergers and boolean values:
multi_list = ["abc", 34, True, "male"]
print(multi_list)

# Slicing:t is possible to access a section of items from the list using the slicing operator:,
# not just a single item

# For Example: Get elements from index 2 to 5 i know that indext always start 0.

print(integer_num[2:5])

# Add new elements in the list:

# Append: add the number in list last is called append.
integer_num.append(520)
print(integer_num)

# Extend: The list with another list is called Extend. This is same work append but only 
# one differenceappend add number last and extend add list last in an other.
integer_num.extend([10,45,16])
print(integer_num)

# Inserting List: Element.
integer_num.insert(4,5000)
print(integer_num)
print(len(integer_num))

# Deleting list: Element.
del integer_num[10]
print(integer_num)

# Remvoing list Element:
list2.remove(3)
print(list2)

# Popped : Remove and return the last element:
popped_element = list4.pop()
print(popped_element)
# print(list4.pop())

# Replace list2 index 1 value 5 change with 55
list2[1]=55
print(list2)

# Get the Index of the list4 occurre
index = list4.index(3)
print(index)

# List Allow Duplicate Values.
my_classroll = [1,5,3,2,6,4,3,2,2,7,9]
print(my_classroll)

#convert tuple in list:
tuple = (1,2,4,5)
print(list[tuple])

# Using the For loop to print the Items of list and their index:

# my_list = [10, 20 , 30, 40 ,40]
# for i in range(len(my_list)):
#     print(i, my_list[i])
    
# Getting the Length of List using the len() function
my_list = [10, 20, 30, 40, 50, 60]
print(len(my_list)) 

# Example 16: Finding Even Numbers in a List

# Assume a list of numbers
list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Iterate through each number in the list
for current_number in list_of_numbers:
    # Check if the current number is even
    if current_number % 2 == 0:
        # If the condition is true, print a message indicating that the number is even
        print("Number is even:", current_number)
    else:
        print("Number is not even:", current_number) 
