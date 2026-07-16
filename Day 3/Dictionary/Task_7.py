inventory = {
    "Pen": 20,
    "Book": 10
}

inventory["Pen"] += 10

product = "Book"
quantity = 3

if product in inventory:
    inventory[product] -= quantity
else:
    print("Product not found")

product = "Pencil"

if product in inventory:
    inventory[product] -= 1
else:
    print("Product not found")

print(inventory)