# protected : Won't be accessible outside the class only accessible to the parent class and child class which inherits through the parent class

class Father:
    def __init__(self):
        self.father_name = input("Enter father name: ") # father name can be acessible outside the class fine
        self._bank_balance = int(input("Enterbank balance: ")) # bank balance can be accessible in this father class and also i want that bank balance to be accessible to the child class which inherits from the father class then it is called protected for that i have to write single under score before variable name
        self.__phone_model = input("Enter phone model: ") # private

    def display_father(self):
        print(f"Father name = {self.father_name}")
        print(f"Bank balance = {self.bank_balance}")
        print(f"phone model = {self.phone_model}")


class Child(Father):

    def __init__(self):
        super().__init__()
        self.child_name = input("Enter the child name: ")

    def display_child_info(self):
        print(f"Child name = {self.child_name}")
        print(f"MY father has  {self._bank_balance} amount")

c = Child()
c.display_child_info()