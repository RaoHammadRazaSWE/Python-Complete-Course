# Write a function called is_prime, which checks if a number is prime.
import math
def is_prime(num):
    """
    Checks whether the given non-negative integer is a prime number or not.
    
    Parameters:
    num (int) : check the numbers prime or not
    
    Return:
    bool : True if the number is prime otherwise False
    """
    if num < 2:
        return False
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            return False
    return True    
print(is_prime(7))
print(is_prime(13))
print(is_prime(10))
