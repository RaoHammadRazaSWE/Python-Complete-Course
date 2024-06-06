# Operator:In Python, an operator is a symbol that represents a specific operation to be performed on one 
# or more operands.Operators allow you to manipulate and perform operations on 
# variables and values.

# Mathematical Operators:Mathematical operators are basic arithmetic symbols used to perform addition, subtraction, multiplication,etc.

# 1) Arithmetic Operators:

# + (Addition)
# - (Subtraction)
# * (Multiplication)
# / (Division)
# % (Modulus)
# ** (Exponentiation)
# // (Floor Division)

#   Operators on Numbers:

# Divisor:
a = 10 
b = 3
result = a / b
# print(result)

# Calculate the Remainder
# print(16%5)

# Display calculate square of number
# print(3**2)

# Multiply two numbers and display using print
# print(3*4)

# Calculate the Remainder
# print(16%5)

# Calculate the Quotient of two numbers
b= 11//4
# print(b)

# Adding two intergers
num1 = 384
num2 = 382
sum = num1 +  num2
# print(sum)

# Simple program to calculate the area of Rectangle:

length = 3.9
height = 5.4
area = length * height
# print(area)

# 2)  Comparison Operators:

# Equal to (==):	If the values of the two operands are equal,
# then the condition becomes true.(a == a) is True.
c = 3320
d = 3204
result = c == d
# Printing the result of the comparison:
# print("is c equal to d?", result)

# Not Equal to (!=):	If the values of the two operands are not equal, then the
# condition becomestrue.	(a != b) is True.
result = c != d
# print("is c not equal to d?" , result)

# Greater Than, Greater than or Equal to (>, >=):If the value of the left operand is
# greater than the value of the right operand then the condition becomes true.
# (2>1) is True.

# Greater than:
result = c > d
# print(result)

# Greater than Equal:
result =  c >= d
# print(result)

# Less Than, Less than or Equal to (<, <=):If the value of the left operand is lessthan 
# the value of the right operand then the condition becomes true.	(1<2) is True.

# Less Than
result = c < d
# print(result)

# Less than is Equel to:
result = c <= d
# print(result)

# 3) Logical Operators: 

# AND &: Returns True if all statements are True.	(1<2 and 2>1) is True.
f = 25
t = 39
output = f > t & t<45
# print(output)

# OR |:	Returns True if one of the statements is True.	(1<2 or 2<4) is True.
output = f < t or t>50
# print(output)

# NOT !=:Reverse the result, returns False if the statement is True.	not(1<5 and 5>3)
# is not True.
output = (f != t)
# print(output)

output = not(t>f and 3==5)
# print(output)

# 4) Assignment Operators:

#  '='  (Assignment)
r = 7
# '+=' (Add and assign)
# r += 5
# print(r)

# '-=' (Subtract and assign)
y = 4
# r -= y
# print(r)

# '*=' (Multiply and assign)
# r *= y
# print(r)

# '/=' (Divide and assign)
# y /= r
# print(y)

# '%=' (Modulus and assign)
r %= y
# print(r)

# 5) Bitwise Operators:in Python are used to perform operations at the bit level.
# These operators work with the individual bits of integers, allowing you to manipulate 
# binary representations of numbers.

#'& '(Bitwise AND):Sets each bit to 1 if both corresponding bits of the operands are 1.

a = 5  # 0101 in binary
b = 3  # 0011 in binary
num = a & b  # result will be 0001 in binary (1 in decimal)
print(num)

#'| '(Bitwise OR):Sets each bit to 1 if at least one of the corresponding 
# bits of the operands is 1.

a = 5  # 0101 in binary
b = 3  # 0011 in binary
num = a | b  # result will be 0111 in binary (7 in decimal)

#'^ '(Bitwise XOR):Sets each bit to 1 if only one of the corresponding
# bits of the operands is 1.

a = 5  # 0101 in binary
b = 3  # 0011 in binary
num = a ^ b  # result will be 0110 in binary (6 in decimal)

#'~ '(Bitwise NOT)
a = 5  # 0101 in binary
num = ~a  # result will be -6 (in two's complement representation)

#'<<' (Left shift):Shifts the bits of the left operand to the left by a specified number of 
# positions.Fills the vacant positions with zeros.
a = 5  # 0101 in binary
result = a << 1  # result will be 1010 in binary (10 in decimal)


#'>>' (Right shift):Shifts the bits of the left operand to the right by a specified number of
# positions. Fills the vacant positions with zeros for non-negative numbers and with the 
# sign bit for negative numbers.
a = 5  # 0101 in binary
num = a >> 1  # result will be 0010 in binary (2 in decimal)


# 6) Membership Operators:in Python are used to test whether a value is a member of a sequence 
# or collection. These operators are commonly used with strings, lists, tuples, and sets. 
#Python provides two membership operators:

# 1) 'in' Ooerator :(True if a value is found in the sequence)
str = 'Rao hammad'
print('r' in str)
print('R' in str)

#2) 'not in' :(True if a value is not found in the sequence)
print('b' not in str)

# 7) Identity Operators:

# 1) 'is' :(True if both operands are the same object)
my_list = [1,2,3,4,5]
is_present = 3 in my_list
print(is_present)

# 2) 'is not' :(True if operands are not the same object)
my_string = "hello"
is_not = "z" not in my_string  # is_not will be True
print(is_not)


# 8) Operators on Strings:we can also use these operators on strings

sentence = 'Hello' + ' ' + 'world'
# print(sentence)

k = 'Ha'
# print(k * 5 + "!")

# You can also use the double equal sign (==) to check if two strings are identical.
# print('ABCD' == 'ABCE')

# > and < will check if one string has more characters than the other.

# print('523445' > '14656')

# The double equal sign is case sensitive:

# print('ABC' == 'ABC')
