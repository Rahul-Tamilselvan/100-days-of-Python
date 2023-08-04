# Pizza order exercise
# small = $15, medium = $20, large = $25
# pepperoni for small = +$2, for medium & large = +$3
# extra cheese for any size = +$1

print("Welcome to Python Pizza Exercise")
size = input("What size pizza dou you want? S, M or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0

# Small size
if size == 'S':
  bill = 15
  if add_pepperoni == 'Y':
    bill += 2
    if extra_cheese == "Y":
      bill += 1
      print(f"your  bill is {bill}")
    else:
      print(f"your  bill is {bill}")
  else:
    if extra_cheese == 'Y':
      bill += 1
      print(f"Your bill is {bill}")
    else:
      print(f"Your bill is {bill}")

# Medium Size
elif size == "M":
  bill = 20
  if add_pepperoni == "Y":
    bill +=3
    if extra_cheese == "Y":
      bill += 1
      print(f"Your bill is {bill}")
    else:
      print(f"Your bill is {bill}")
  else:
    if extra_cheese == "Y":
      bill += 1
      print(f"Your bill is {bill}")
    else:
      print(f"Your bill is {bill}")

# Large size
elif size == "L":
  bill = 25
  if add_pepperoni == "Y":
    bill +=3
    if extra_cheese == "Y":
      bill += 1
      print(f"Your bill is {bill}")
    else:
      print(f"Your bill is {bill}")
  else:
    if extra_cheese == "Y":
      bill += 1
      print(f"Your bill is {bill}")
    else:
      print(f"Your bill is {bill}")

# case sensitive
else:
  print("Please enter the correct size")
