"""
Q149. Store name as a Key, and 5 marks in a List as a value in dictionary.
Store details of at least 5 students. Print the name of the student who got
highest marks.

"""

students_data = {
    "Student1": [85, 90, 78, 92, 88],
    "Student2": [75, 88, 92, 80, 87],
    "Student3": [90, 95, 89, 78, 93],
    "Student4": [80, 85, 88, 92, 87],
    "Student5": [92, 88, 95, 90, 85],
}

highest_score = 0
top_student_name = ""
for name, marks in students_data.items():
    total = sum(marks)
    if total > highest_score:
        highest_score = total
        top_student_name = name
print(f"{top_student_name} got highest {highest_score}marks")
