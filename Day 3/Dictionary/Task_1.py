products = {
    "Pen": 20,
    "Book": 150,
    "Bag": 800,
    "Bottle": 120,
    "Notebook": 90
}

expensive = {k: v for k, v in products.items() if v > 100}

print(expensive)