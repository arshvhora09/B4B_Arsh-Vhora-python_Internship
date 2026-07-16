count = 0

def call_counter():
    global count
    count += 1
    print("Function called", count, "time(s)")

call_counter()
call_counter()
call_counter()
call_counter()

print("Final count:", count)