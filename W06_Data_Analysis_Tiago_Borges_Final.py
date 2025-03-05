"""
PC103_CSE110 
W06 Project:  Life Expectancy Data Analysis Program

Author: Tiago Borges 

About the project:
This program analyzes life expectancy data from "OurWorldInData.org " and provides:
- The year and country with the highest and lowest life expectancy.
- Insights for a user-specified year, including average, min, and max life expectancy.

The program processes the dataset without external libraries, using basic 
Python functions for file handling and data analysis.
"""
# New - additional features added:
# 1- User can input a country and see: Minimum, Maximum, and Average life expectancy for that country
# 2- Identifies the biggest drop in life expectancy for each country across consecutive years


# Open the dataset file
file_path = "life-expectancy.csv"

# Variables to store overall highest and lowest life expectancy data
min_life_exp = float("inf")
max_life_exp = float("-inf")
min_country = ""
min_year = 0
max_country = ""
max_year = 0

# Dictionary to store country-specific data for biggest drop calculation
country_data = {}

# Load the dataset manually (without external libraries)
with open(file_path, "r") as file:
    next(file)  # Skip the header row

    # Read and process each line in the file
    for line in file:
        parts = line.strip().split(",")  # Split the line into columns
        
        country = parts[0]  # Country name
        year = int(parts[2])  # Year
        life_expectancy = float(parts[3])  # Life expectancy

        # Update overall min and max life expectancy values
        if life_expectancy < min_life_exp:
            min_life_exp = life_expectancy
            min_country = country
            min_year = year

        if life_expectancy > max_life_exp:
            max_life_exp = life_expectancy
            max_country = country
            max_year = year

        # Store country-specific data for later analysis
        if country not in country_data:
            country_data[country] = []
        country_data[country].append((year, life_expectancy))

# Display overall max and min life expectancy details
print(f"The overall max life expectancy is: {max_life_exp} from {max_country} in {max_year}")
print(f"The overall min life expectancy is: {min_life_exp} from {min_country} in {min_year}")

# Allow the user to input a year for further analysis
year_of_interest = int(input("\nEnter the year of interest: "))

# Variables for year-specific calculations
total_life_exp = 0
count = 0
year_min_life_exp = float("inf")
year_max_life_exp = float("-inf")
year_min_country = ""
year_max_country = ""

# Reopen the file to process data for the selected year
with open(file_path, "r") as file:
    next(file)  # Skip header again

    for line in file:
        parts = line.strip().split(",")
        
        country = parts[0]
        year = int(parts[2])
        life_expectancy = float(parts[3])

        # Process data only for the selected year
        if year == year_of_interest:
            total_life_exp += life_expectancy
            count += 1

            # Update min and max values for the selected year
            if life_expectancy < year_min_life_exp:
                year_min_life_exp = life_expectancy
                year_min_country = country

            if life_expectancy > year_max_life_exp:
                year_max_life_exp = life_expectancy
                year_max_country = country

# Calculate and display results for the selected year
if count > 0:
    avg_life_exp = total_life_exp / count
    print(f"\nFor the year {year_of_interest}:")
    print(f"The average life expectancy across all countries was {avg_life_exp:.2f}")
    print(f"The max life expectancy was in {year_max_country} with {year_max_life_exp}")
    print(f"The min life expectancy was in {year_min_country} with {year_min_life_exp}")
else:
    print(f"\nNo data available for the year {year_of_interest}.")

# Allow the user to input a country for analysis
country_of_interest = input("\nEnter a country to analyze: ").strip()

if country_of_interest in country_data:
    country_values = country_data[country_of_interest]
    country_values.sort()  # Ensure data is sorted by year

    # Calculate min, max, and average life expectancy for the country
    min_country_life = min(country_values, key=lambda x: x[1])
    max_country_life = max(country_values, key=lambda x: x[1])
    avg_country_life = sum(x[1] for x in country_values) / len(country_values)

    print(f"\nFor {country_of_interest}:")
    print(f"Minimum life expectancy: {min_country_life[1]} in {min_country_life[0]}")
    print(f"Maximum life expectancy: {max_country_life[1]} in {max_country_life[0]}")
    print(f"Average life expectancy: {avg_country_life:.2f}")

    # Identify the biggest drop in life expectancy for the country
    biggest_drop = 0
    drop_year = 0
    for i in range(1, len(country_values)):
        prev_year, prev_life = country_values[i - 1]
        curr_year, curr_life = country_values[i]
        drop = prev_life - curr_life
        if drop > biggest_drop:
            biggest_drop = drop
            drop_year = curr_year

    if biggest_drop > 0:
        print(f"The biggest drop in life expectancy was {biggest_drop:.2f} years in {drop_year}.")
    else:
        print(f"No significant drops in life expectancy for {country_of_interest}.")

else:
    print(f"\nNo data found for {country_of_interest}.")

# Project Completed - Cheers! 

# This program successfully analyzes life expectancy data, providing valuable insights about historical trends  
# Thank you for taking the time to review my code  
# May Heavenly Father bless you with wisdom, patience and joy in all that you do!
