# Write a function called check_season,it takes a month parameter and returns the season:
# Autumn, Winter, Spring or Summer.

def check_season(month):
    """
    This function checks the season given the month.

    Parameters:
    month (int): Month for which the season is checked.

    Returns:
    str: The corresponding season.
    """
    # Convert month to integer
    month = int(month)

    if 11 <= month <= 12 or 1 <= month < 2:
        return "Winter"
    elif 2 <= month <= 4:
        return "Spring"
    elif 5 <= month <= 8:
        return "Summer"
    elif 9 <= month <= 10:
        return "Autumn"
    else:
        return "Invalid month"

# Example:
month_value = input("Please Enter the Month (as a number): ")
season_result = check_season(month_value)
print(f"The season for month {month_value} is {season_result}")
  
