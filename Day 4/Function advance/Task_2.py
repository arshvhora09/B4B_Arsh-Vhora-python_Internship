def apply_discount(price, percent=10):
    final_price = price - (price * percent / 100)
    print("Original Price:", price)
    print("Discount:", percent, "%")
    print("Final Price:", final_price)


# Call using only the price (default discount = 10%)
apply_discount(1000)

print()

# Call using both arguments (discount passed as a keyword argument)
apply_discount(1000, percent=20)