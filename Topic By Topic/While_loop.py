# While Loops: With the while loop we can execute a set of statements as long as a condition is true.

# Syntax :
# while condition:

    # body of while loop
# Example: Printing numbers as long as they are less than 60 using a while loop

# Initialize a counter variable
current_number = 1

# Continue looping as long as the current number is less than or equal to 60
while current_number <= 60:
    # Print the current number
   # print(current_number)

    # Increment the current number by 1 in each iteration
    current_number = current_number + 1
    # current_number +=1   # this can also be used
    
# Example : Using a while loop to print "Hello" multiple times
 # Initialize  a counter variable
loop_counter = 0

# Continue the loop as long as the counter is less then 3
while loop_counter < 3:
    # print the message along with the  current count
   # print("print hello", loop_counter)
    
    # Increment the counter by 1 in each iteration
    loop_counter = loop_counter + 1   
    
# Exanple : User Input Validation for a password

# Initialize an empty string for the user's password
user_password = ""
# while user_password != "secret":
    # user_password = input("Enter the password:")
    # if user_password == "secret":
    #     print("Access granted!")
    # else:
    #     print("Access denied!")    
        
# Example : Summing Numbers from 1 to 10 using a while loop

# Initialize a variable to store the running total
# sum_of_numbers = 0

# Start with the first number
# current_number = 1

# Continue adding numbers to the total as long as the current number is less than or equal to 10
# while current_number <= 10:
    # Add the current number to the running total
    # sum_of_numbers = sum_of_numbers + current_number

    # Increment the current number by 1 in each iteration
    # current_number = current_number + 1

# Print the final sum
# print("The sum is:", sum_of_numbers)        

# Example 1: Print numbers less than 5
# Initialize the counter variable
# current_number = -10

# Run the loop until the current number is less than 5
# while current_number < 5:
    # Print the current number
    # print(current_number)

    # Increment the current number by 1 for the next iteration
    # current_number = current_number + 1
    
# Example 2: Calculate the sum of the first 10 natural  numvers:
# num = 10
# total_sum = 0
# i = 1
# while i <= num:
#     total_sum = total_sum + i
#     i = i + 1
# print("Sum of the first 10 numbers is :" , total_sum)    

# While loop with IF-else: A while loop can have an optional block. We use if-else statement in
# the loop when conditional iteration is needed. i.e., If the condition is True,
# then the statements inside the if block will execute othwerwise, the else block will execute.

# Example 1: print even and odd numbers between 1 and the entered number.
# Get user input for the upper limit:
user_num = int(input('Please Enter the number:'))

# Start the loop while the entered number is greater than 0
while user_num > 0:
    # Check if the current number is even and old
    if user_num % 2 == 0:
        print(user_num," is and even number")
    else:
        print(user_num ," is an odd num") 
    user_num = user_num -1   
    
