def task():

    status = "pending"

    def complete():
        nonlocal status
        status = "completed"

    complete()

    print("Final status:", status)

task()