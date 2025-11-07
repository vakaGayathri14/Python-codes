"""
Q142. Ask subject name and marks from the user and keep adding it to
dictionary.

"""

total_subjects = int(input("Enter tota no.of subjects: "))
marks = {}

for _ in range(0, total_subjects):
    subject = input("Enter the subject")
    sub_marks = int(input(f"Enter the marks for {subject}"))
    # marks[subject]=sub_marks
    marks.update({subject: sub_marks})
print(marks)