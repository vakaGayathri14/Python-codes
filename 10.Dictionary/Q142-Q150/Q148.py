"""

Q148. Store marks of 5 different subjects in a dictionary. Ask subject name
as an input from the User. Print the marks of that subject entered by User.
If subject does not exist, print “Invalid”.

"""

subject_marks_dict = {
    "Math": 90,
    "English": 85,
    "Science": 92,
    "History": 88,
    "Computer Science": 95,
}
subject = input("Enter the subject name: ")

if subject in subject_marks_dict:
    print(subject_marks_dict[subject])
else:
    print("Invalid")