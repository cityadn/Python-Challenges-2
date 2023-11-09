def binary(decimal):
    if decimal >= 1:
        return format(decimal, 'b')

decimal = int(input("Enter the decimal representation of your signal:\n"))
print(binary(decimal))