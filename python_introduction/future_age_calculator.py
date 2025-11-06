"""
Script that ask a user for their current age and then calculates how
old they will be in a specific future year.
"""

current_age = int(input("How old are you? "))
birth_year = 2025 - current_age
future_age = 2050 - birth_year

print("In 2050, you will be ", future_age, "years old")