def num_length(counter, num):
    num = str(num)
    for i in num:
        counter += 1
    return counter

counter = 0
num = int(input("Enter a number:\n"))
print(num_length(counter, num))
