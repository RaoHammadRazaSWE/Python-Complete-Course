# Quadratic equation is calculated as follows: ax² + bx + c = 0.Write a function which 
# calculates solution set of a quadratic equation, solve_quadratic_eqn.

# Import the cmath module for handling complex numbers
import cmath 
def solve_quadratic_equ(a,b,c):
    """
    calculates the solution set of a quadratic equation ax² + bx + c = 0.
    
    Parameter:
    a (float): Coefficient of x².
    b (float): Coefficient of x.
    c (float): Constant term.
    
    Return:
    tuple: A tuple containing the solutions. Depending on the case:
        - Two real solutions: (root1, root2)
        - One real solutions: (root,)
        - Two complex solutions: (complex_root1, complex_root2)
    
    """
# Calculate the discriminant
    discriminant = b**2 - 4*a*c 
# Check the discriminant and calculate solutions accordingly
    if discriminant > 0:
        root1 = (-b + cmath.sqrt(discriminant) / (2*a))  
        root2 = (-b - cmath.sqrt(discriminant) / (2*a))  
        return (root1, root2)
    elif discriminant == 0:
        root = -b / (2*a)
        return (root,)
    else: 
        complex_root1 = (-b + cmath.sqrt(discriminant) / (2*a)) 
        complex_root2 = (-b - cmath.sqrt(discriminant) / (2*a)) 
        return (complex_root1, complex_root2)
    # Example:
a_val, b_val , c_val = 3,-5,6
soulation_set = solve_quadratic_equ(a_val , b_val , c_val)   
print(f"The  Soulation set: {soulation_set}")
