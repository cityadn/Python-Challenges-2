def FizzBuzz(num):
    if (num % 3 == 0) and (num % 5 == 0):
        return "FizzBuzz"
    elif (num % 3 == 0) and (num % 5 != 0):
        return "Fizz"
    elif (num % 3 != 0) and (num % 5 == 0):
        return "Buzz"
    else:
        num = str(num)
        return num
    
num = int(input("Enter a number:\n"))
print(FizzBuzz(num))
