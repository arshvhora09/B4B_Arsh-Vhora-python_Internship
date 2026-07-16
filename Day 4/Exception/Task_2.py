def get_value(lst, index):
    try:
        return lst[index]

    except IndexError:
        return None


numbers = [10, 20, 30]

print(get_value(numbers, 1))
print(get_value(numbers, 5))