# Prime Number
def prime_checker(number):
  is_prime = True
  for i in range(2 , number):
    if number % i == 0:
      is_prime = False
  if is_prime:
      print("It's a Prime Number")
  else:
      print("It's not a Prime Number")

n = int(input("check this number: "))
prime_checker(number = n)