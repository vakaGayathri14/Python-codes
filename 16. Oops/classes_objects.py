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

#now if i comment the attributes in the class then also it will work without an error 
    # roll_no = 0
    # name = ""
    # age = 0
    # gender = ""
    # address = ""

# because in self_info function if i don't have any attributes inside a class it will create a new attribute using this
        # self.name=input("Enter name = ") # here name variable will create inside a class
        # self.age=int(input("Enter age = ")) # here age variable will create inside a class
        # self.gender=input("Enter gender = ") # here gender variable will create inside a class
        # self.roll_no=int(input("Enter roll number = ")) # here roll no variable will create inside a class

# if i do s1.info() it will print the values inside the class of that object s1

# now if i call s1.info() prior than set_info() creating attributes then I will get an error because i don't have attributes itsef how can i print them

#now if we 2 objects then we can first set the attributes and then print the info of them for example if i have  100 objects it might be difficult to over come to check that each steps are going correctly for 100 right then we have a concept of special method called "init"

#syntax

class Subject1:
    # init is an initializer 
    def __init__(self): # this is how the syntax is you should not change
        # print("In INIT") # this block inside the init method will run automatically if we create a new object
        self.name=input("Enter name = ")
        self.age=int(input("Enter age = "))
        self.gender=input("Enter gender = ")
        self.roll_no=int(input("Enter roll number = "))

    def info(self):
        print(f"Name = {self.name}") # whose name/age/gender -> which objects calls this those name/age/gender will be printed
        print(f"Age = {self.age}")
        print(f"Gender = {self.gender}")
        print(f"Roll no = {self.roll_no}")


s1 = Subject1()
s1.info()

s2 = Subject1()
s2.info()






