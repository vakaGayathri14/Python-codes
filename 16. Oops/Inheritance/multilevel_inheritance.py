class Grandfather:
    grand_Father = " "

    def grand_father(self):
        print(f"Grand father = {self.grand_Father}")


class Father(Grandfather):
    Father = ""

    def father(self):
        print(f"Father = {self.Father}")


class Son(Father):
    son1 = ""

    def son(self):
        print(f"Son = {self.son1}")


s1 = Son()
print(s1)

s1.grand_Father = "AR"
s1.Father = "VNR"
s1.son1 = "GR"

s1.grand_father()
s1.father()
s1.son()

print("-----------------")


class Grandfather:
    def __init__(self):
        print("GRAND FATHER INIT")

    grand_Father = " "

    def grand_father(self):
        print(f"Grand father = {self.grand_Father}")


class Father(Grandfather):
    def __init__(self):
        super().__init__()  # here referring to grandfather class
        print("FATHER INIT")

    Father = ""

    def father(self):
        print(f"Father = {self.Father}")


class Son(Father):
    def __init__(self):
        super().__init__()  # calling to father class
        print("SON INIT")  # initially only this is printing

    son1 = ""

    def son(self):
        print(f"Son = {self.son1}")


s1 = Son()
print(s1)

s1.grand_Father = "AR"
s1.Father = "VNR"
s1.son1 = "GR"

s1.grand_father()
s1.father()
s1.son()
