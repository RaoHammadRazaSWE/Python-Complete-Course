# String :Strings in python are surrounded by either single quotation marks,
# or double quotation marks.
# 'hello' is the same as "hello".You can display a string literal with the print() function:

# Simple String in one line:
print("Hello Rao")

# Multiline  Strigns:

# a = """ Without AI, or Artificial Intelligence, refers to the development and implementation of computer systems
#       or machines that can perform tasks that would typically require human intelligence.
#       It is a multidisciplinary field that encompasses various subfields, such as machine learning,
#       natural language processing, computer vision, robotics, and more."""
# print(a.find("Without"))

# Lower Case:

b = "hallo world"
print(b.upper())

# Lower Case:

print(b.lower())

# Type Find krna ka Method:
print(type(b))

# Remove Whitespace: side wala space remove hoja ta hai.
a = "Rao , Hammad "
print(a.strip())

# Replace String:
print(a.replace("Hammad","Raza"))

# Split String: The split() method returns a 
# list where the text between the specified separator
# becomes the list items. The split() method splits 
# the string into 
# substrings if it finds instances of the separator.

R = "Rao , Hammad"
print(R.split(","))

# F_String: This is bacially work two and more print statemetn uses one line code.

name = 'Hammad'
age = 22
height = 1.6
# Simple method 1:

# print("My name is : "+name,"I am "+str(age), "years old")

# Simple method 2:

# print("My name is : ",name,"I am ",age, "years old", "My height is",height,"meters")

# Same Work using F_String

print(f"My name is {name}.I am {age} years old. My height is {height} meters")

print(f"Hammad father is {age*2} years old.")


