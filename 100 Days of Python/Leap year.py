# Leap year
# / by 4, remainder 0 -> leap year
# / by 100, remainder 0 -> not a leap year
# / by 400, remainder 0 -> leap year

# get input from the user
year = int(input("Enter the year : "))

# conditions

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print(f"The year {year}, is a leap year")
    else:
      print(f"The year {year}, is not a leap year")
  else:
    print(f"The year {year}, is a leap year")
else:
  print(f"The year {year}, is not a leap year")
