"""
Q147. Store “name” of a student as Key, “list of 5 marks” of that student as
a Value. Store atleast 5 student names. Print the sum and percentage of all
the students.

"""

students_data = {
    "Student1": [85, 90, 78, 92, 88],
    "Student2": [75, 88, 92, 80, 87],
    "Student3": [90, 95, 89, 78, 93],
    "Student4": [80, 85, 88, 92, 87],
    "Student5": [92, 88, 95, 90, 85],
}
print(students_data.items())
for name, marks in students_data.items():
    total = sum(marks)
    print(total)
    percentage = total / 500 * 100
    print(f"{name} has scored total {total} marks, percentage = {percentage:.2f}")
