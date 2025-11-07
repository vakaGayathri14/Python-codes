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

sub =input("Enter the subject: ")

if sub in subject_marks_dict.keys():
    print(subject_marks_dict[sub])
else:
    print("invalid")