usernames = ["Arsh", "Rohit123", "Aman", "Priyanka", "Dev", "CodeMaster"]

result = list(filter(lambda name: len(name) >= 6, usernames))

print(result)