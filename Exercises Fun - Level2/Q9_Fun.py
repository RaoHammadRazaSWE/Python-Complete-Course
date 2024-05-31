# Write a function called calculate_slope which return the slope of a linear equation.

def calculate_slope(x1,y1, x2, y2):
    """
     Calculate the slope of a linear equation given two points(x1, y1) and (x2, y2).
     
     Parameter:
     x1 (float): x-coordinate of the first point.
     y1 (float): y-coordinate of the first point.
     x2 (float): x-coordinate of the second point.
     y2 (float): y-coordinate of the second point.
     
     Returns:
     float:  The calculated slope of the linear equation.
    """
    # Ensure the denominator is not zero to avoid division by zero
    if x1 == x2:
        raise ValueError("The x-coordinates of the two points must be different.") 
    # Calculate the slope using the formula: (y2 - y1) / (x2 - x1)
    slope = (y2 - y1) / (x2 - x1)
    return slope
# Example usage:
x1, y1 = 2,6
x2, y2 = 4,8

slope_result = calculate_slope(x1, y1 , x2 , y2)
print(f"The slope of the line is  : {slope_result}")
