# Declare a function named evens_and_odds. It takes a positive integer as parameter and it
# counts number of evens and odds in the number.

def evens_and_odds(start, end):
    """
    Count the number of even and odd numbers in the given positive integer range.
    
    Parameters:
    start (int): The starting number of the range.
    end (int): The ending number of the range (exclusive).
   
    
    Return:
    Tuple : A tuple containing the count of even and odd numbers.
    """
    total_even = total_odd = 0
    
    for num in range(start, end):
        
        if num % 2 == 0:
           total_even += 1
        else:
           total_odd  += 1  
    return total_even , total_odd
        
# Example:
start_range = 0
end_range = 101
even_count, odd_count = evens_and_odds(start_range, end_range)
print(f"Count of even number between {start_range} and {end_range}: {even_count}")
print(f"Count of odd number between {start_range} and {end_range}: {odd_count}")

