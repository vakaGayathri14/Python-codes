class Student:
    def __init__(self,name,age,gender) ->None:
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        print(f"My name is {self.name}")
        print(f"My age is {self.age}")
        print(f"My gender is {self.gender}")

s1 = Student("Honey",23,"Female")
#  # above the is the way to create an object using parameters
s1.display()
 # above the is the way to create an object using parameters 
 # I want to create an object only but in file like i will create student.txt inside of it honey 23 female
 # 2 ways of creating an object
#  1. creating n object on the spot like above using parameters
# 2. needs to read from the file and create an object for this we use class methods



# Classmethod

class Student:
    def __init__(self,name,age,gender) ->None:
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        print(f"My name is {self.name}")
        print(f"My age is {self.age}")
        print(f"My gender is {self.gender}")

    @classmethod # return compulsory
    def create_student_using_params(cls,name,age,gender):
        obj = cls(name,age,gender)
        return obj
    
    @classmethod
    def create_student_using_file(cls,filename):
        f = open(filename,"r")
        student_data = f.read()
        name,age,gender = student_data.split()
        f.close()
        obj=cls(name,age,gender)
        return obj
    

s1 = Student.create_student_using_params("Honey",23,"Female")
s1.display()
print("---------")
s2 = Student.create_student_using_file("C:\\Users\\Gayathri\\OneDrive\\Desktop\\Python\\Python-codes\\16. Oops\\Polymorphism\\student.txt")
s2.display()
