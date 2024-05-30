# Call your function is_empty, it takes a parameter and it checks if
# it is empty or not

def is_empty(parameter):
    """
    Check if the given parameter is empty.
    
    Parameters:
    - parameter (any type): type of data.
    
    Returns:
    bool: True if the parameter is empty, False otherwise.
    """
    if not parameter:
        return True
    else:
        return False
    
# Example usage:
empty_list = []
empty_string = " "
non_empty_list = [1,2,4]
    
print(is_empty(empty_list))
print(is_empty(empty_string))
print(is_empty(non_empty_list))
