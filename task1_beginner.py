# -------------------------------
# SHADOWFOX PYTHON INTERNSHIP
# TASK 1 - BEGINNER LEVEL
# -------------------------------


# ===============================
# 1. VARIABLES
# ===============================

print("----- VARIABLES -----")

pi = 22/7
print("Value of pi:", pi)
print("Type of pi:", type(pi))

# Trying to use reserved keyword
# for = 4   # This gives SyntaxError because 'for' is a keyword

# Simple Interest Calculation
principal = 5000
rate = 4
time = 3

simple_interest = (principal * rate * time) / 100
print("Simple Interest for 3 years:", simple_interest)


# ===============================
# 2. NUMBERS
# ===============================

print("\n----- NUMBERS -----")

# Format function
number = 145
formatted_number = format(number, 'o')
print("Octal representation of 145:", formatted_number)

# Area of circular pond
radius = 84
area = 3.14 * radius * radius
print("Area of pond:", area)

water = int(area * 1.4)
print("Total water in pond:", water)

# Speed calculation
distance = 490
time_seconds = 7 * 60
speed = int(distance / time_seconds)
print("Speed in m/s:", speed)


# ===============================
# 3. LIST
# ===============================

print("\n----- LIST -----")

justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

print("Original list:", justice_league)
print("Number of members:", len(justice_league))

# Adding new members
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("After adding new members:", justice_league)

# Moving Wonder Woman to front
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("After making Wonder Woman leader:", justice_league)

# Replace whole team
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("New team formed:", justice_league)

justice_league.sort()
print("Sorted team:", justice_league)
print("New Leader:", justice_league[0])


# ===============================
# 4. IF CONDITION
# ===============================

print("\n----- BMI CALCULATOR -----")

height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kg: "))

bmi = weight / (height ** 2)

if bmi >= 30:
    print("Obesity")
elif bmi >= 25:
    print("Overweight")
elif bmi >= 18.5:
    print("Normal")
else:
    print("Underweight")


print("\n----- COUNTRY CHECK -----")

Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city = input("Enter a city name: ")

if city in Australia:
    print(city, "is in Australia")
elif city in UAE:
    print(city, "is in UAE")
elif city in India:
    print(city, "is in India")
else:
    print("City not found in list")


# ===============================
# 5. FOR LOOP
# ===============================

print("\n----- DICE SIMULATION -----")

import random

rolls = []
six_count = 0
one_count = 0
double_six = 0

for i in range(20):
    roll = random.randint(1, 6)
    rolls.append(roll)

for i in range(len(rolls)):
    if rolls[i] == 6:
        six_count += 1
    if rolls[i] == 1:
        one_count += 1
    if i > 0 and rolls[i] == 6 and rolls[i-1] == 6:
        double_six += 1

print("Dice rolls:", rolls)
print("Number of times 6 appeared:", six_count)
print("Number of times 1 appeared:", one_count)
print("Two 6s in a row:", double_six)

print("\nTask 1 Completed Successfully!")
