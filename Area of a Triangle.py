import random
def area(base, height):
    triangle_area = (base * height) / 2
    return triangle_area

base = random.randint(1,10)
height = random.randint(1,10)
print(base, ",", height)
triangle_area = area(base,height)
print("The area of the triangle is:", triangle_area)
