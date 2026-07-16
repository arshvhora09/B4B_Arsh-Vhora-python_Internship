def process_order(order):

    try:
        print("Item:", order["item"])
        print("Price:", order["price"])

    except KeyError as e:
        print("Error: Missing key:", e)

    else:
        print("Order processed successfully.")

    finally:
        print("Processing complete")


order1 = {
    "item": "Laptop",
    "price": 50000
}

order2 = {
    "item": "Mobile"
}

process_order(order1)

print()

process_order(order2)