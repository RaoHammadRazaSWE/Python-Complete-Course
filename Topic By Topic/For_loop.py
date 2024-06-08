# Loop:A loop is a programming concept that allows for the repetition of a set of
# instructions multiple times.

# For Loop: is a control flow statement in many programming languages, including Python.
# It allows you to iterate over a sequence (such as a list, tuple, string, or range) 
# and execute a block of code for each item in that sequence.

# Why use for loop?

# Definite Iteration: When we know how many times we wanted to run a loop, then we use 
# count-controlled loops such as for loops. It is also known as definite iteration.
# For example, Calculate the percentage of 50 students.
# here we know we need to iterate a loop 50 times (1 iteration for each student).

# Reduces the  code's complexity:Loop repeats a specific block of code a fixed number of times.
# It reduces the repetition of lines of code, thus reducing the complexity of the code.
# Using for loops and while loops we can automate and repeat tasks in an efficient manner.

# Loop through sequences: used for iterating over lists, strings, tuples, dictionaries, etc.,
# and perform various operations on it, based on the conditions specified by the user.

# Print the Hello World using the print statement:
# print("Hello World")
# print(" Hello World")
# print(" Hello World")
# print(" Hello World")
# print(" Hello World")
# print(" Hello World")
# print(" Hello World")
# print(" Hello World")
# print(" Hello World")
# print(" Hello World")
# print(" Hello World")

# Print the string specific number of times:
# for i in range(10):
   # print("Hello World")
    
# Example no1 : Iterating throuth alist of words using a for loop:
# Assume a list of words

# number_list = [ 'one', 'two' , 'Three','four']    

# Iterate through each word in the list
# for  number in number_list:
    # print each word
 #   print(number)
    
# Example no2 : Calculating the Average of a list of numbers

# Assume a list of numbers
number_list = [10, 20 , 30 , 40 , 50]

# Initialize  variables for sum and list size
total_sum = 0
list_size =  len(number_list)

# Iterate through each number in list
#for num in number_list:
    # Accumulate the sum of numbers
    # total_sum = total_sum + num
    # print(total_sum) 
    # total_sum += num
 # Calculate the average by dividing the sum by the number of items in the list
    # average = total_sum / list_size  
  
# print the calculated average
# print ("The average of the numbers is :" , average)     

# Print each fruit in a fruit list:
# fruits = ["apple" ,"mango" , "bannana"]
# for item in fruits:
#       print(item)

# Looping Through a String:Even strings are iterable objects, they contain a sequence of characters:
#Loop through the letters in the word "banana":

# Example : Iterating through each character in the word "banana"
# Iterate through each character (chars) in the word
word_to_iterate = "banana"
for character in word_to_iterate:
    # Print each character
    print(character)

