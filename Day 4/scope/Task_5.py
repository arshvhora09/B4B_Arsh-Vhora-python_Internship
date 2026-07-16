mode = "Global"

def outer():

    mode = "Outer"

    print("Outer mode:", mode)

    def inner():

        mode = "Inner"

        print("Inner mode:", mode)

    inner()

    print("Outer mode after inner:", mode)

outer()

print("Global mode:", mode)