numbers = [12, 45, 23, 45, 67, 12, 89, 34, 67, 90, 23, 11, 56, 89, 78]

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print(unique)