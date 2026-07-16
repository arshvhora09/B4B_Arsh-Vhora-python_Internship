# A frozenset is immutable, so it can be used as a dictionary key.

def to_frozenset(items):
    return frozenset(items)

numbers = [1, 2, 3, 2, 1]

result = to_frozenset(numbers)

print(result)