"""
data types:-
numeric
->int,float,complex
dictionary
list,tuple,strings,set,bool


integers->0,1,2,3..etc
float->5.5,4.89..etc
complex->2+3j
strings-> Eg:- x="gayathri",y="2345", z ="ab@#$%123"
List-> To store multiple values in single variable[we can change values in list/update/delete/add} Eg:- x=[55,88,87], y=[99,98,100], z =[55,88.9,"Gayathri",True]
Tuple-> To store multiple values in single variable[ Wecannot change the tuple values as like list] Eg:- (55,96,87,"Gayathri")
dictionary -> values store in the form of key value pairs,values can repeat but not the key's  Eg:- marks={"Gayathri":88,"Honey":98,"Ram":"98}

"""

# integer
x = 55
print(55)
print(type(x))

# float
y = 66.7
print(y, type(y))

# string
name = "Gayathri"
print(name, type(name))

# boolean
adult = False
print(adult, type(adult))

# list
marks = [33, 44, 52, 65, 67]
print(marks, type(marks))

# tuple
y_marks = (33, 44, 52, 65, 67)
print(y_marks, type(y_marks))

# dictionary
z_marks = {"Gayathri": 99, "Honey": 100}
print(z_marks, type(z_marks))
