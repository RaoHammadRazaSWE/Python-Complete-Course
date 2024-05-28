# Create a function called the most_spoken_languages in the world.
# It should return 10 or 20 mostspoken languages in the world in
# descending order

def most_spoken_language(num_languages=10):
    # Sample data (language: population in millions)
    language_populations = {
        'English': 1200,
        'Mandarin Chinese': 1100,
        'Hindi': 600,
        'Spanish': 560,
        'French': 310,
        'Arabic': 310,
        'Bengali': 230,
        'Russian': 150,
        'Portuguese': 220,
        'Urdu': 230,
        'German': 76,
        'Japanese': 126,
        'Korean': 77,
        'Turkish': 80,
        'Italian': 63,
        'Dutch': 23,
        'Thai': 70,
        'Vietnamese': 90,
        'Swahili': 75,
        'Polish': 45
    }
    
    # Sort languages by population in descending order
    sorted_lanuages = sorted(language_populations.items(), key=lambda x: x[1], reverse=True)
    
    # Extract the top N languages
    top_languages = sorted_lanuages[:num_languages]
    
    return top_languages

# Test the function with 10 most spoken languagesl
result_20_languages = most_spoken_language(num_languages=20)
print("\nTop 20 Most Spoken Lnaguages:")
for language, population in result_20_languages:
    print(f"{language}: {population} million speakers.")
    
    
