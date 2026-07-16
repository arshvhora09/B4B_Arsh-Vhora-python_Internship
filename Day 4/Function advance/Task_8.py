def require_positive(func):
    def wrapper(*args):
        for value in args:
            if value <= 0:
                print("Error: All arguments must be positive numbers.")
                return

        return func(*args)

    return wrapper


@require_positive
def divide(a, b):
    print("Result:", a / b)


divide(10, 2)
divide(10, -2)
divide(10, 0)