# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32.
# Write a function which converts °C to °F,convert_celsius_2_fahrenheit.

def convert_celsius_to_fahrenheit(C):
    """
    Convert temperature from Celsius to Fahrenheit.
    
    Parameters:
    C : Temperature in Celsius .
    
    Returns: 
    Celsius to Fahrenheit: Converts the Temperature.
    """
    Fahrenheit = (C * 9/5) + 32
    
    return Fahrenheit
# Eample :
C_valuse = 45
fahrenheit_result = convert_celsius_to_fahrenheit(C_valuse)
print(f"Convert temperature from Celsius to Fahrenheit {C_valuse} is equal to  {fahrenheit_result}")

