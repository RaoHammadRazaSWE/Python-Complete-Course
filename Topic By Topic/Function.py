# python Functions: A function in Python is a block of reusable code that performs
# a specific task.It allows you to organize your code, make it more readable, and 
# promote code reuse.

# Types of Functions:python support two types of functions:

# 1.[Built-in]function:
#These are functions that are already defined in Python.
# Examples include print(), len(), type(), etc.
# for i in range (1,10):
#     print(i , end=' ')

# 3.Anonymous Functions (Lambda Functions):
# Short, one-line functions defined using the lambda keyword.
#Example:1
# add = lambda x, y: x + y
# result = add(3, 5)
# print(result)

# 2.[User-defined] function:Functions created by the user to perform specific tasks.
# Syntax:
# def function_name(parameter1, parameter2):
#   """docstring"""
  # function body
  # write some action
#  return value 

# Defining a Function:
# 1. def is a keyword that marks the start of the function header.

# 2. function_name to uniquely identify the function. Function naming follows the same
# rules of writing identifiers in Python.

# 3.  Parameter :is the value passed to the function. They are optional.

# 4. : (colon) to mark the end of the function header.

# 5. function body : is a block of code that performs some task and all the statements in
# function body must have the same indentation level (usually 4 spaces).

# 6. """docstring""" documentation string is used to describe what the function does.

# 7. return is a keyword to return a value from the function.. A return statement with
# no arguments is the same as return None.

# Note: While defining a function, we use two keywords, def (mandatory) and return (optional).

# Example:
def add(num1,num2):          #>>> # Function name: 'add', Parameters: 'num1', 'num2'
 print("Number 1: ", num1)   #>>> #  Function body
 print("Number 2: ", num2)   #>>> #  Function body
 addition = num1 + num2      #>>> #  Function body
 return addition             #>>> #  return value
 res = add(2, 4)             #>>> #  Function call
 print("Result: ", res)      #>>> #  Print value
 
# Defining a function without any parameters : Function can be declared without parameters.

# Example 1: Define and call a greeting function.

# Define a function named 'greet' to print a welcome message
def greet():
    print("Welcome to python for Artificial Intelligence")
    
# call the 'greet' function
greet()    

# Example 2: Define and call a function to add two numbers.

# Define a function named 'add_two_num'
def add_two_nums():
    # Assing values to two numbers
    num_one = 3
    num_two = 45
    # Calculate the total by adding the  two numbers
    total = num_one + num_two
    
    # Print the result 
    print(total)
    
# Call the 'add_two_num' function
add_two_nums()    

# Defining a function without parameters and return value: Function can also return values,
# if a function does not have a return statement, the value of the function is None.
# Let us rewrite the above functions using return.
# From now on, we get a value from a function when we call the function and print it.

# Example 1: Define and  call a function to add two numbers,

# Define a function named 'add_two_numbers
def add_two_nums():
    # Assing values to two numbers
    num_first = 3
    num_second = 49
    
    # Calculate the total by adding the  two numbers
    sum_total = num_first + num_second
    
    # Return the total
    return sum_total

# Print the result  of calling  the 'add_two_num' function
print(add_two_nums())

# Example 2: Define and call a function to generate a full name.

# Define a function named 'generate_full_name'
def generate_full_name():
    first_name = 'Hammad'
    last_name = 'Raza'
    
    # Create a variable for the space between first and last names
    space = ' '
    
    # Concatenate the first and last names to form the full name
    full_name = first_name + space + last_name
    
    # Return the full name
    return full_name

# print the result of calling the 'generate_full_name' function

Answer = generate_full_name()
print(Answer)

# Defining a function with parameters : In a function we can pass different data type
# (number, string, boolean, list, tuple, dictionary or set)as a parameter.

# Single Parameter:If our function takes a parameter we should call our function with
# an argument.

# Example 1: Greeting
def greet(person_name):
    """
    This function greets the person passed in as a parameter 
    """
    print("Hello, " + person_name + ". Good morning!") # No output!
    
# Example 2: Calculate the sum of numbers up to the specified limit

def sum_of_numbers_up_to_n(limit):
    """
    This function calculates the sum of numbers up to the specified limit (inclusive)
    """
    total_sum = 0

    # Iterate through numbers from 0 to 'limit' and add them to the total
    for i in range(limit + 1):
        total_sum += i

    # Print the calculated sum
    print(total_sum)

# Calculate and print the sum for different limits
sum_of_numbers_up_to_n(10)   # Expected output: 55
sum_of_numbers_up_to_n(100)  # Expected output: 5050    

# Two Parameter: A function may or may not have a parameter or parameters.
# A function may also have two or more parameters.If our function takes parameters
# we should call it with arguments.

# Example 1: Welcome message for a python Data Scinece course participant

def welcome_participant(student_name, course_title):
    """
    This function generates a  welcome message for a participant in a python Data Science course.
    """
    print("Hello", student_name + ",Welcome to python for Artificaial Intelligence! ")
    print("Your course name is " , course_title)
    
# Call the 'welcome_participant' function with specific arguments
welcome_participant('Mubasir', 'Hope to skill')    

# Defining a function with parameters and return value

# Example 1: Greeting Message Generator
def generate_greeting_message(name):
    """
    This function generates a personalized greeting message for a person.
    """
    greeting_message = name + ', welcome to python for Artificial Intelligence'
    return greeting_message
# Call the 'generate_greeting_message' function with a specific argument
print(generate_greeting_message('Ali'))

# Example 2: Square of a Number Calculator
def calculate_square(x):
    """
    This function calculates the square of a given number.
    """
    square_result = x * x
    return square_result
# Call the 'calculate_square' function with a specific argument
print(calculate_square(3))

# Example 3: Age Calculator
def calculate_age(current_year, birth_year):
   """This function calculates the age based on the current year and birth year.
   """
   person_age = current_year - birth_year
   return person_age
# Call the 'calculate_age' function with specific arguments
print('Age: ', calculate_age(2024, 2001))

# Function return Statement:In Python, to return value from the function,
# a return statement is used.
# It returns the value of the expression following the returns keyword.

# Syntax:
# def fun():
#     statement-1
#     statement-2
#     statement-3
#     .
#     .
#     return [expression]

# The return value is nothing but a outcome of function.

# The return statement ends the function execution.
# For a function, it is not mandatory to return a value.
# If a return statement is used without any expression, then the None is returned.
# The return statement should be inside of the function block.

# Return Single Value
print(greet("Hammad"))

# Return Multiple Values :You can also return multiple values from a function.
# Use the return statement by separating each expression by a comma.

# Example 1: Arithmetic Operations  Calculator
def perform_arithmetic_operationss(num1, num2):
    """
    This function performs addition, subtraction, multiplication, and division on two numbers.
    """
    addition_result = num1 + num2
    subtraction_result = num1 - num2
    multiplication_result = num1 * num2
    division_result = num1 / num2
    
    
    # Return four values representing the results of the arithmetic operations
    return addition_result, subtraction_result, multiplication_result, division_result

# Call the 'perform_arithmetic_operations' function with specific arguments
addition, subtraction, multiplication, division = perform_arithmetic_operationss(10,2)

# Display the results
print("Addition:", addition)
print("Subtraction: ", subtraction)
print("Multiplication: ", multiplication)
print("Division:", division)

# Return Boolean Values
# Example 1: check if a Number is Even
def is_even(number):
    """
    This function checks if a given number is evne.
    """
    if number % 2 == 0:
        print("Even")
        return True
    else:
        print("Odd")
        return False
    # Check and print the results for different numbers
    print(is_even(10)) # Expected output: True
    print(is_even(7))  # Expected output: False
