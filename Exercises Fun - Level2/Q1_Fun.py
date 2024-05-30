# Area of a circle is calculated as follows: area = π x r x r and perimeter = 2 x π x r.
# Write a function that calculates area_of_circle 
# and perimeter_of_circle.

import math
def area_of_circle(radius):
    """
    Calculate the area of a circle.

    Parameters:
    - radius (float): The radius of the circle.

    Returns:
    - float: The calculated area.
    """
    area = math.pi * radius * radius
    return area

def perimeter_of_circle(radius):
    """
    Calculate the perimeter (circumference) of a circle.

    Parameters:
    - radius: The radius of the circle.

    Returns:
    - The perimeter of the circle.
    """
    perimeter = 2 * math.pi * radius
    return  perimeter
# Example usage:
radius_value = 5.0
area_result = area_of_circle(radius_value)
perimeter_result = perimeter_of_circle(radius_value)

print(f"Area of the circle with radius {radius_value}:{area_result:.2f}")
print(f"Perimeter of the circle with radius {radius_value}:{perimeter_result:.2f}")
