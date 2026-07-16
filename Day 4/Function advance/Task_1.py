def build_invoice(customer_name, *args, **kwargs):
    print("Customer Name:", customer_name)

    total = sum(args)
    print("Total Item Price:", total)

    print("Extra Details:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# Example function call
build_invoice(
    "Riya",
    250, 500, 150,
    discount=50,
    tax=90,
    payment_mode="UPI"
)