#Q1: Write a functions which checks if all items are unique in the list.

def are_all_unique(lst):
    """
    Check if all items are unique in the list.
    
    Parameters:
    lst (list): A list of items.
    
    Return:
    bool: True if all items are unique, otherwise False.
    """
    return len(set(lst)) == len(lst)
print("Part:1")
my_list = [1, 2, 3, 4,4, 5]
print(are_all_unique(my_list))
print(" ")
print("Part:2")
#Q2: Write a function which checks if all the items of the list are of the
# same data type.
def are_all_same_data_type(lst):
    return all (type(item) == type(lst[0]) for item in lst)
print(are_all_same_data_type([1,2,3,4,5]))
print(are_all_same_data_type(['applel','orange','pear']))
print(are_all_same_data_type(['two',2,3,4,5]))

print("Part 3:")
#Q3: Write a function which check if provided variable is a valid python
# variable

def is_valid_variable_name(variable_name):
    return  variable_name.isidentifier()
print(is_valid_variable_name("my_variable"))
print(is_valid_variable_name("123_variable"))
print(is_valid_variable_name("var-with-dash"))
print(is_valid_variable_name("class"))
