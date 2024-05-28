# Create a function called the most_populated_countries. It should 
# return 10 or 20 most populated countries in descending order.

def most_populated_countries(num_countries=10):
    # Sample data (country: population in millions)
    country_populations = {
        'China': 1441,
        'India': 1393,
        'United States': 331,
        'Indonesia': 273,
        'Pakistan': 225,
        'Brazil': 213,
        'Nigeria': 211,
        'Bangladesh': 166,
        'Russia': 146,
        'Mexico': 130,
        'Japan': 126,
        'Ethiopia': 118,
        'Philippines': 113,
        'Egypt': 104,
        'Vietnam': 97,
        'DR Congo': 89,
        'Turkey': 84,
        'Iran': 84,
        'Germany': 83,
        'Thailand': 69,
    }
    
    # Sort countries by population in descending order
    sorted_countries = sorted(country_populations.items() , key=lambda x: x[1], reverse=True)
    
    # Extract the top N countries
    top_countries = sorted_countries[:num_countries]
    return top_countries
# Test the function with 10 most populated countries
result_10_countries = most_populated_countries(num_countries=10)
print("Top 10 Most Populated Countries:")
for country, population in result_10_countries:
    print(f"{country}:  {population} million")
    
    
    
    
