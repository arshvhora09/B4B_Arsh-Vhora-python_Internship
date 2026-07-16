numbers = [12, 45, 78, 34, 90, 67, 89]

largest = second_largest = float("-inf")

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif largest > num > second_largest:
        second_largest = num

print(second_largest)