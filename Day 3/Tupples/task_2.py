product = ("Laptop", 50000, 10)

# product[1] = 55000   # Error: Tuples are immutable

product = (product[0], 55000, product[2])

print(product)