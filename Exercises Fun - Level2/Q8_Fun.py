# Write different functions which take lists. They should 
# calculate_mean, calculate_median, calculate_mode,calculate_range,
# calculate_variance, calculate_std (standard deviation).

# Part 1:
def calculate_mean(num_list):
    """
    This function takes a list of numbers and returns the 
    mean value of the interger.
    
    Parameter:
    num (list) : List of num.
    Return:
    float -- The mean value of the integer in the given list.
    """
    total_sum = 0
    for i in num_list:
        total_sum += i
    return total_sum/len(num_list)

# Part 2:
def calulate_median(num_list):
    """
    This function takes a list of numbers and returns the 
    median value of the interger.
    
    Parameter:
    num (list) : List of num.
    Return:
    float -- The median value of the integer in the given list.
    """
    # Sort the list in ascending order
    sorted_list = sorted(num_list)
    
    # Get the length of the list
    n = len(sorted_list)
    
    # Check if the number of elements is odd or even
    if n % 2 == 1:
        # if odd , return the middle element
        median = sorted_list[n // 2 ]
    else:
        # if even, return the average of the two middle elements 
        middle1 = sorted_list[n // 2 -1]   
        middle2 = sorted_list[n // 2 ]
        median = (middle1 + middle2) / 2   
        
    return median

# Part 3:

from collections import Counter
def calulate_mode(num_list):
    """
    This function takes a list of numbers and returns the 
    mode value of the interger.
    
    Parameter:
    num (list) : List of num.
    Return:
    float -- The mode value of the integer in the given list.
    """
    
    # Count the occurrences of each element in the list
    counts = Counter(num_list)
    
    # Find the maximum frequency
    max_frequency = max(counts.values())
    
    # Get all elements with the maximum frequency (the modes)
    modes = [num for num, freq in counts.items() if freq == max_frequency]
    
    return modes
    
# Part 4:
def calulate_range(num_list):
    """
    This function takes a list of numbers and returns the 
    range of the interger.
    
    Parameter:
    num (list) : List of num.
    Return:
    float -- The range of the input list.
    """
    # Find the mimimum and maximum values in the list
    
    min_val = min(num_list)
    max_val = max(num_list)
    
    # Calculate the range.
    num_range = max_val - min_val
    return num_range

# Part 5:
def calulate_variance(num_list):
    """
    This function takes a list of numbers and returns the 
    variance of the interger.
    
    Parameter:
    num (list) : List of num.
    Return:
    float -- The variance of the numbers in the given list.
    """
    mean = sum(num_list) / len(num_list)
    squared_diff =[(x - mean) ** 2 for x in num_list]
    variance = sum(squared_diff) / len(num_list)
    return variance

# Part 6:
import math
def calulate_std(num_list):
    """
    This function takes a list of numbers and returns the 
    standard deviation.
    
    Parameter:
    num (list) : List of num.
    Return:
    float -- The standard deviation of the numbers in the given list.
    """
    mean = sum(num_list) / len(num_list)
    squared_diff =[(x - mean) ** 2 for x in num_list]
    variance = sum(squared_diff) / len(num_list)
    std_dev = math.sqrt(variance)
    return std_dev

# Example :1
my_list = [1,2,3,4,5,7,5,6]

print("Part1:")
result = calculate_mean(my_list)
print(f"The mean of list, {result}")
print("  ")

# Example :2
print("Part2:")
result = calulate_median(my_list)
print(f"The mean of list, {result}")
print("  ")

# Example :3
print("Part3:")
result = calulate_mode(my_list)
print(f"The mode(s) of list, {result}")
print("  ")

# Example :4
print("Part4:")
result = calulate_range(my_list)
print(f"The range of list, {result}")
print("  ")

# Example :5
print("Part5:")
result = calulate_variance(my_list)
print(f"The variance  of list, {result:.2f}")
print("  ")

# Example :6
print("Part6:")
result = calulate_std(my_list)
print(f"The standard deviation of the list, {result:.2f}")
print("  ")
