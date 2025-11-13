# create a class
class Student:
    roll_no = 0
    name = ""
    age = 0
    gender = ""
    address = ""


# create an object
# as how you create a varible to store a value like x=5 like wise to create an object

# s1 = Student()
# print(s1) #cannot print an object

# for s1 object we have roll no,name,age,gender,address.. these are all attributes

s1 = Student()
print(s1.roll_no)
print(s1.name)
s1.roll_no = 1
s1.name = "Honey"
print(s1.roll_no)
print(s1.name)
print("----------------")
# now i am creating another object s2
s2 = Student()
