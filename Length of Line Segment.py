#d = ((x2-x1)**2 + (y2-y1)**2))**(1/2)
def straight_line(x1, y1, x2, y2):
    distance = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
    return round(distance, 2)

x1 = float(input("Enter the x-coordinate for coordinate 1:\n"))
y1 = float(input("Enter the y-coordinate for coordinate 1:\n"))
x2 = float(input("Enter the x-coordinate for coordinate 2:\n"))
y2 = float(input("Enter the y-coordinate for coordinate 2:\n"))
print(straight_line(x1, y1, x2, y2))
