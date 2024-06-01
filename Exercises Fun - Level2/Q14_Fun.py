# Declare a function named add_item. It takes a list and an item parameters. 
# It returns a list with the item added at the end.

def add_item(original_list, new_item):
    """
    Add an item to the end of the given list .
    
    Parameters:
    original_list (list) : The original list to which the item will be added.
    new_item: The item to be added to the list.
    Returns:
    list: A new list with the item added at the end.
    """
    new_list = original_list.copy()
    
    new_list.append(new_item)
    
    return new_list
    
# Example:
original_list = [2,3,4,6]
item_to_add = 12
result_list = add_item(original_list , item_to_add)

print("original list:", original_list)
print("add new item: ", result_list)
