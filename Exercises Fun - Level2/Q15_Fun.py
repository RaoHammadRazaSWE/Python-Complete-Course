# Declare a function named remove_item. It takes a list and an item parameters.
# It returns a list with the item removed from it

def remove_item (original_list, item_to_remove):
    """
    Remove an item to the end of the given list .
    
    Parameters:
    original_list (list) : The original list to which the item will be remove.
    new_item_remove: The item to be remove from the list.
    Returns:
    list: A new list with the item removed.
    """
    new_list = original_list.copy()
    
    if item_to_remove in new_list:
        new_list.remove(item_to_remove)
    else: 
        print("The element not avabile in this list")    
    
    return new_list
    
# Example:
original_list = [1,2,3,4,5,6]
item_to_remove = 2
result_list = remove_item(original_list , item_to_remove)

print("original list:", original_list)
print("List after removing  the item: ", result_list)
