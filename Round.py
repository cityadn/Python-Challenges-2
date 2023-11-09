import random
def round10(num):
  rounded_up = round(num/10)*10
  return rounded_up

num = int(input("Enter a number:\n"))
print(num)
print(round10(num))
