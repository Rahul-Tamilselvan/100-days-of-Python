# BMI calculator 2.0
# BMI below 18.5 underweight, 18.5 - 25 normal weight, 25 - 30 overweight, 30 - 35 obese, above 35 clinically obese

# BMI calculator
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
BMI = round(weight / height ** 2)

# Statements
if BMI < 18.5:
  print(f"Your BMI is {BMI}, you are underweight")
elif BMI < 25:
  print(f"Your BMI is {BMI}, you have a normal weight")
elif BMI < 30:
  print(f"Your BMI is {BMI}, you are slightly over weight")
elif BMI < 35:
  print(f"Your BMI is {BMI},you are obese")
else:
  print(f"Your BMI is {BMI}, you are clinically obese")