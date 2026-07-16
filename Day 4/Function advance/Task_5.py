from functools import reduce

numbers = [12, 45, 67, 23, 89, 34]

largest = reduce(lambda a, b: a if a > b else b, numbers)

print(largest)