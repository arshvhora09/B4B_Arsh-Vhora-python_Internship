admin = {"read", "write", "delete", "manage"}
editor = {"read", "write"}

action = "delete"

if action in editor:
    print("Permission Granted")
else:
    print("Permission Denied")