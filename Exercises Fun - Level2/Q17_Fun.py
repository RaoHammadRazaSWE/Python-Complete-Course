# Qno:13 Declare a function named sum_of_odds. It takes a number parameter and it adds all
# the odd numbers in that range.

def sum_of_odds(start, end):
    """
    Calculate the sum of odds numbers in the given range.
    
    Parameters:
    start (int): The starting number of the range.
    end (int) : The ending number of the range (exclusive).
    
    Return:
    int : The sum of odds numbers in the specified range.
    """
    sum_odds = 0
    for num in range(start , end):
        
        if num % 2 != 0:
            sum_odds += num
    return sum_odds
        
# Example:
result = sum_of_odds(1,5)
print("Sum of odds numbers:" , result)

#Qno:14 Declare a function named sum_of_even. It takes a number parameter and it adds all
# the even numbers in that - range.

def sum_of_even(start, end):
    """
    Calculate the sum of even numbers in the given range.
    
    Parameters:
    start (int): The starting number of the range.
    end (int) : The ending number of the range (exclusive).
    
    Return:
    int : The sum of even numbers in the specified range.
    """
    sum_even = 0
    for num in range(start , end):
        
        if num % 2 == 0:
            sum_even += num
    return sum_even
        
# Example:
result = sum_of_even(1,6)
print("Sum of odds numbers:" , result)
