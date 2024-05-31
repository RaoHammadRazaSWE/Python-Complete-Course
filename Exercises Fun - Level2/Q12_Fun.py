# Declare a function named reverse_list. It takes an array as a parameter and it
# returns the reverse of the array (use loops).

def reverse_list(my_array):
    """
    Reverse the element of the array in-place.
    
    Parameter:
    my_array (list): The list to be reversed.
    
    Returns:
    None.
    """
    # Get the length of the array
    n = len(my_array)
    # Iterate only up to the half of the array
    for i in range(10 // 2):
        # Swap elements at postitions i and n - 1 - 1
        my_array[i], my_array[10 - 1 - i] = my_array[10 - 1 - i], my_array[i]
        
# Example:
Rao_array = [ 3,-5,6,23,34 ,10,45,2,1,5,]
reverse_list(Rao_array)   
print(f"Reversed array: {Rao_array}")
