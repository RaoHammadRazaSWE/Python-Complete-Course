# Write a function called add_all_nums which takes arbitrary number of arguments and sums all
#the arguments.Check if all the list items are number types. If not do give a reasonable feedback.

def add_all_nums(*args):
    """
    Calculate the sum of all numeric arguments.
    
    Parameters:
    *args : Arbitrary number of arguments.
    
    
    Returns: 
    int or float: The calculated sum.
    """
    total = 0
    for num in args:
        if not isinstance(num,(int, float)):
            # Provide feedback for non-numeric values
            return "Error: All list items must be numeric."
        total += num
    return total
# Example usage:      
number_values = [3,56,7]
# number_values = [3,56,7,'Roa',4.5]
number_result = add_all_nums(*number_values)
print(f"sum of the numbers {number_values}:{number_result}")

