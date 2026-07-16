employees = {
    "Riya": 45000,
    "Aman": 60000,
    "Sara": 52000,
    "Karan": 70000,
    "Neha": 65000
}

sorted_employees = sorted(employees.items(), key=lambda x: x[1], reverse=True)

for name, salary in sorted_employees[:3]:
    print(name, salary)