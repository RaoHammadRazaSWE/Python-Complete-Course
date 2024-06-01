# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the
# numbers in that range.

def sum_of_num(start, end):
    """
    Calculate the sum of numbers in the given range.
    
    Parameters:
    start (int): The starting number of the range.
    end (int) : The ending number of the range (exclusive).
    
    Return:
    int : The sum of numbers in the specified range.
    """
    sum_num = 0
    for num in range(start , end):
        sum_num += num
    return sum_num
        
# Example:
result = sum_of_num(1,5)
print("Sum of numbers:" , result)
