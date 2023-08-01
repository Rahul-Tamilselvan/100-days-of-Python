# Project Tip Calculator
print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you give? 10, 12, 15? "))
split = int(input("How many people to split the bill? "))
total = bill + (bill * (tip / 100))
each_person = round(total / split, 2)
print(f"Each person should pay ${each_person}")
