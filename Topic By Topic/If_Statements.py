# IF Statement: In control statements, The if statement is the simplest form. It takes a 
# condition and evaluates to either True or False.If the condition is True, then the True 
# block of code will be executed, and if the conditionis False, then the block of code is 
# skipped, and The controller moves to the next line.

# Syntax of IF Statement:
# if(condition):
#     statement 1
#     statement 2
#     statement n

# Example 01 of an IF statement

# Assume the student's grade
student_score = 64

# Check if the grade is equal to or higher than the passing threshold
if student_score <= 65:
    # If the condition is true, print a message indicating a passing grade
    print("Students has scored passing grades")   
    
# Example 02 of an IF statement

# Check the positive number and negitive numbers:
positive_num = 3
if positive_num > 0:
    print( positive_num, "This is number is positive")
print("This is always print.")    

negitive_num = -1
if negitive_num < 0:
    print(negitive_num,"This number is negitive")
print("This is always print.")

# Example 03 of an IF statement
#  Calculate the square of number if number is greater than 6
given_num = 9
if given_num > 6:
    square_result = given_num * given_num
    #print('The square of', given_num , "is" ,square_result)

print('Next lines of  code')

# Shortcut for if statement (short=hand if or one-line if)
num1 , num2 = 5,6
if (num1 < num2): print("num1 is less than num2")

# IF-Else Statement:The if-else statement checks the condition and executes the if block of code when
# the condition is True, and if the condition is False, it will execute the else block of code.

# Syntax:

# if condition:

#   statement 1
# else:

#   statement 2

# Example no 1:  Check the student fail and passed
student_marks = 50
if student_marks > 50:
    print("Student Pass This Exam.")
else:
    print("Student Fail This Exam.")    
  
# Example no 2:  check the  v+ , n- , zero num.
given_num = input("Please Enter any number:")
if int(given_num) > 0:
    print(given_num ,"Number is Positve")
elif int(given_num ) == 0:
    print(given_num , "is zero")   
else:
    print(given_num ,"Number is Negative")
    
# Example no 3: Password check function
# def :In Python, def is used to define a function.

def password_check(user_password):  
# check if the provided password matches the expected p
 if user_password == "Hellorao":
    print(" correct password")
 else:
     print("Incorrect password")   
# Test the function with a Incorrect password
password_check("hellora")
# Test the function with a correct password
password_check("Hellorao")

# Question no : 1
# Check the grade of the student.
student_grade = int(input("Enter the student's numerical grade:"))
if student_grade >= 90:
   letter_grade = "A"
elif student_grade >= 80:
   letter_grade = "B"
elif student_grade >= 70:
   letter_grade = "C"
elif student_grade >= 60:
   letter_grade = "D"
else:
   letter_grade = "F"
print(f"The Corresponding letter grade is: {letter_grade}")  

# Question no : 2
# Check the temperature.
temperature_celsius = int(input("Enter the Temperature Celsius:"))
if temperature_celsius < -10:
  print("Freezing")
elif -10 <= temperature_celsius < 0:
  print("Cold")
elif 0 <=temperature_celsius < 20:
  print("Moderate")
elif 20 <= temperature_celsius < 30:  
  print("Warm")
else:
  print("Hot")  
