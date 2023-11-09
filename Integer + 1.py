import random
def calc(num):
    num = num + 1
    return num

num = random.randint(-1000000, 1000000)
print("Original Number:", num)
plus_one = calc(num)
print("Add 1:", plus_one)
