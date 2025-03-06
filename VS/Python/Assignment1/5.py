students = []
i=0
for i in range(10):
    name = input("Enter student name (max 15 chars): ")[:15] 
    students.append(name)

print("\nOriginal Names:")
print(students)

print("\nReversed Names:")
print([name[::-1] for name in students])