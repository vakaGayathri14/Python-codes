# create a class and name of class should be capital here Student
class Student:
    # variables inside a class are called Attributes/ Class Variables
    roll_no = 0
    name = ""
    age = 0
    gender = ""
    address = ""

    # Inside the class not only variables we also get functions
    # Functions inside class are called Methods
    def info(self):
        print(f"Name = {self.name}") # whose name/age/gender -> which objects calls this those name/age/gender will be printed
        print(f"Age = {self.age}")
        print(f"Gender = {self.gender}")
        print(f"Roll no = {self.roll_no}")

    def set_info(self):
        self.name=input("Enter name = ")
        self.age=int(input("Enter age = "))
        self.gender=input("Enter gender = ")
        self.roll_no=int(input("Enter roll number = "))


# create an object
# as how you create a varible to store a value like x=5 like wise to create an object

# s1 = Student()
# print(s1) #cannot print an object

# for s1 object we have roll no,name,age,gender,address.. these are all attributes

s1 = Student()  # object 1
# print(s1.roll_no)
# print(s1.name)
# s1.roll_no = 1
# s1.name = "Honey"
# print(s1.roll_no)
# print(s1.name)
# print("----------------")
# now i am creating another object s2
s2 = Student()  # object 2
# print(s2.roll_no)
# print(s2.name)
# s2.roll_no = 2
# print(s2.roll_no)

# s1.age=23
# #accessing methods using objects
# s1.info()
# print("--------")
# s2.name="Radha"
# s2.info()

s1.set_info()
print("-------")
s1.info()

s2.set_info()
print("-----")
s2.info()
