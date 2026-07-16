def marks_info(marks):
    lowest = min(marks)
    highest = max(marks)
    average = sum(marks) / len(marks)
    return lowest, highest, average

marks = [78, 85, 92, 67, 88]

low, high, avg = marks_info(marks)

print(low)
print(high)
print(avg)