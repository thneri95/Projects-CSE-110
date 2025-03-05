"""
PC103_CSE110 
W07 Project: Windchill Calculator
Author: Tiago Borges 

Introduction:
This project calculates the wind chill factor, which estimates how cold it feels outside based on temperature and wind speed
The formula used follows the guidelines set by the U.S. National Weather Service. Users can input the temperature in either Fahrenheit or Celsius
and the program will convert it if necessary before computing the wind chill for various wind speeds ranging from 5 to 60 mph

Upgrades and Enhancements:
1- Added input validation to ensure the user provides valid numeric values and selects a correct temperature scale
2- Improved output formatting by displaying a structured table for better readability
3- Modularized the code with separate functions for conversion, validation, and wind chill calculation, improving maintainability and clarity
4- Included handling for wind speeds below 3 mph, where the wind chill formula does not apply

"""

# I took the liberty of trying to make the program layout more aesthetic and
# the information easier to understand than in lines
# Let´s do it! 

# Function to calculate wind chill
def calculate_windchill(temperature: float, wind_speed: float) -> float:
    """Calculate wind chill using the National Weather Service formula."""
    if wind_speed < 3:
        return temperature  # Wind chill formula is not valid for wind speeds below 3 mph
    return 35.74 + 0.6215 * temperature - 35.75 * (wind_speed ** 0.16) + 0.4275 * temperature * (wind_speed ** 0.16)

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius temperature to Fahrenheit."""
    return (celsius * 9/5) + 32

# Function to get user input with validation
def get_valid_temperature() -> float:
    """Prompt user for a valid temperature input."""
    while True:
        try:
            return float(input("Enter the temperature: "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_valid_scale() -> str:
    """Prompt user for a valid temperature scale (F or C)."""
    while True:
        scale = input("Temperature scale (F/C): ").strip().upper()
        if scale in ('F', 'C'):
            return scale
        print("Invalid input. Please enter 'F' for Fahrenheit or 'C' for Celsius.")

# Main function
def main():
    """Main function to calculate and display wind chill for various wind speeds."""
    temp = get_valid_temperature()
    scale = get_valid_scale()
    
    if scale == 'C':
        temp = celsius_to_fahrenheit(temp)
    
    print("\nWind Chill Calculations:")
    print("=" * 50)
    print(f"{'Wind Speed (mph)':<20}{'Wind Chill (F)':>20}")
    print("-" * 50)
    
    for wind_speed in range(5, 65, 5):  # Wind speeds from 5 to 60 mph
        wind_chill = calculate_windchill(temp, wind_speed)
        print(f"{wind_speed:<20}{wind_chill:>20.2f}")
    
    print("=" * 50)

# Run the program
if __name__ == "__main__":
    main()

# Thank you for reviewing my code! I appreciate your time and support in evaluating this project 
# May Heavenly Father bless you with wisdom, patience and joy in all that you do!
