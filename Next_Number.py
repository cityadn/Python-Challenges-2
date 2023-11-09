def next_number(a, b):
    count = 0
    while True:
        count = count + 1
        if a < b:
            return "a must be greater than b, invalid input"
        elif (count > a) and (count % b == 0):
            return count
            break
        else:
            continue

a = int(input("Enter a number (a must be greater than b):\n"))
b = int(input("Enter a number (a must be greater than b):\n"))
print(next_number(a, b))
