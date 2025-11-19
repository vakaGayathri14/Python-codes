# class Father:
#     father_name=""

#     def display_father_name(self):
#         print(self.father_name)


# class Mother:
#     mother_name = ""

#     def display_mother_name(self):
#         print(self.mother_name)


# class Child(Father, Mother): # now i want properties of both father and mother in child class 
#     child_name = ""

#     def display_child_name(self):
#         print(self.child_name)

# c1 = Child()
# c1.father_name = "VNR"
# c1.mother_name = "Anuradha"
# c1.child_name = "Honey"

# c1.display_father_name()
# c1.display_mother_name()
# c1.display_child_name()

print("------------------")
# want to implement init and wan to see if i write super which will it refer because her child is referring to 2 classes if we call super in child class then it will refer to the first class where we provide as parameters


class Father:
    def __init__(self) -> None:
        print("Father INIT")

    father_name=""

    def display_father_name(self):
        print(self.father_name)


class Mother:
    def __init__(self) -> None:
        print("Mother INIT")

    mother_name = ""

    def display_mother_name(self):
        print(self.mother_name)


class Child(Father, Mother): # now i want properties of both father and mother in child class 
    def __init__(self) -> None:
        super().__init__() # if i don't write this only child init will print in the console if i write this it is now refering to first parameter in the class it is father so it will print father as it is in print statement of father init class
        print("child INIT")

    child_name = ""

    def display_child_name(self):
        print(self.child_name)

c1 = Child()
c1.father_name = "VNR"
c1.mother_name = "Anuradha"
c1.child_name = "Honey"

c1.display_father_name()
c1.display_mother_name()
c1.display_child_name()
