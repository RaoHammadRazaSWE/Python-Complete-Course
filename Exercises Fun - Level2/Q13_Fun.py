# Declare a function named capitalize_list_items. It takes a list as a parameterand it returns a
# capitalized list of items.

def capitalize_list_items(my_list):
    """
    Capitalized the item given list.
    
    parameters:
    my_list : A new list with capitalized itmes.
    
    Return:
    list: A new list with capitalized itmes.
    """
    capitalize_list = []
    for item in my_list:
        capitalize_item = item.capitalize()
        capitalize_list.append(capitalize_item)
    return capitalize_list    
# Example usage:
original_list = ["apple" , "banana" , "cherry"]
capitalized_result = capitalize_list_items(original_list)

print("Original List:", original_list)
print("Capitalized List:", capitalized_result)
