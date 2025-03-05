"""
Author: Tiago  Borges

Purpose: Areas of shapes
"""


import math

# Function to calculate area of a square
def calculate_square_area():
    side = float(input("What is the length of a side of the square in centimeters? "))
    area_cm = side ** 2
    area_m2 = area_cm / 10_000
    print(f"The area of the square in square centimeters is: {area_cm} cm²")
    print(f"The area of the square in square meters is: {area_m2} m²")

# Function to calculate area of a rectangle
def calculate_rectangle_area():
    length = float(input("What is the length of the rectangle in centimeters? "))
    width = float(input("What is the width of the rectangle in centimeters? "))
    area_cm = length * width
    area_m2 = area_cm / 10_000
    print(f"The area of the rectangle in square centimeters is: {area_cm} cm²")
    print(f"The area of the rectangle in square meters is: {area_m2} m²")

# Function to calculate area of a circle using math.pi
def calculate_circle_area():
    radius = float(input("What is the radius of the circle in centimeters? "))
    area_cm = math.pi * radius ** 2
    area_m2 = area_cm / 10_000
    print(f"The area of the circle in square centimeters is: {area_cm} cm²")
    print(f"The area of the circle in square meters is: {area_m2} m²")

# Function to calculate volumes of a cube and a sphere
def calculate_volumes_from_single_length():
    value = float(input("Enter a single length value in centimeters: "))
    
    # Area of square
    square_area_cm = value ** 2
    square_area_m2 = square_area_cm / 10_000
    print(f"The area of the square in square centimeters is: {square_area_cm} cm²")
    print(f"The area of the square in square meters is: {square_area_m2} m²")

    # Area of circle using math.pi
    circle_area_cm = math.pi * value ** 2
    circle_area_m2 = circle_area_cm / 10_000
    print(f"The area of the circle in square centimeters is: {circle_area_cm} cm²")
    print(f"The area of the circle in square meters is: {circle_area_m2} m²")

    # Volume of cube
    cube_volume = value ** 3
    print(f"The volume of the cube is: {cube_volume} cm³")
    
    # Volume of sphere
    sphere_volume = (4/3) * math.pi * value ** 3
    print(f"The volume of the sphere is: {sphere_volume} cm³")

# Main function to run the program
def main():
    print("Core Requirements:")
    calculate_square_area()
    calculate_rectangle_area()
    calculate_circle_area()
    
    print("\nStretch Challenge 1:")
    calculate_volumes_from_single_length()

# Run the program
if __name__ == "__main__":
    main()
