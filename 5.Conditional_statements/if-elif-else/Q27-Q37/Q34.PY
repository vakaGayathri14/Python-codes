"""
Q34. A student will not be allowed to sit in exam if his/her attendance is
less than 75%.
a. Take following input from user
i. Number of classes held
ii. Number of classes attended.
b. Print percentage of class attended
c. Print Is student is allowed to sit in exam or not
"""

Number_of_classes_held = int(input("Enter the total number of classes held: "))
Number_of_classes_attended = int(input("Enter the total number of classes that you attended: "))

percentage_of_class_attended = (Number_of_classes_attended/Number_of_classes_held)*100

print(f"{percentage_of_class_attended:.2f}%")

if (percentage_of_class_attended < 75):
    print(f"not allowed to sit in exam")
else:
    print(f"allowed to sit in exams")