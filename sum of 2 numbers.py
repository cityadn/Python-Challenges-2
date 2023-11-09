#Return the Sum of Two Numbers
def sum(num1, num2):
    total = num1 + num2
    return total

num1 = float(input("Enter a number:\n"))
num2 = float(input("Enter a number:\n"))
total = sum(num1, num2)
print("The total is ", total)
