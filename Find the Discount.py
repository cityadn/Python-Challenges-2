def discount(price, discount_percentage):
    new_price = price * (1-(discount_percentage/100))
    return new_price

price = int(input("Enter the price of the product:\n"))
discount_percentage = int(input("Enter the discount provided, as a percentage:\n"))
print(discount(price, discount_percentage))
