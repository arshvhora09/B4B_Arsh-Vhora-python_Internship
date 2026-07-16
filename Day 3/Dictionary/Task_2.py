students = [
    {"name": "Riya", "marks": 88},
    {"name": "Aman", "marks": 95},
    {"name": "Sara", "marks": 82}
]

topper = students[0]

for student in students:
    if student["marks"] > topper["marks"]:
        topper = student

print(topper)