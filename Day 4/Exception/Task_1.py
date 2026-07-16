def safe_division(a, b):
    try:
        return a / b

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

    except TypeError:
        print("Error: Both inputs must be numbers.")


print(safe_division(10, 2))
print(safe_division(10, 0))
print(safe_division(10, "5"))