# Call your function factorial, it takes a whole number as a parameter
# and it return a factorial of the number.

def factorial(num):
    """
    Calculate the factorial of a whole numbers.
    
    Parameters:
    num (int) : A positive integer.
    
    Returns:
    int : The factorial of the inputted integer.
    """
    if num < 0:
        return "Please enter a positive integer."
    elif num == 0 or num == 1:
        return 1
    else:
        result = 1
        for i in range(2, num + 1):
           result *= i
        return result   
# Example : 
num = 5
result = factorial(num)
print(f"The factorial of {num} is {result}")
