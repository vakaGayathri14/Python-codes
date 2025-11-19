# # Encapsulation: Encapsulation is ntg but Data hiding , data hiding through access modifiers
# from random import randint


# class Bank:
#     def __init__(self) -> None:
#         self.name = input("Enter name = ")
#         self.account_no = randint(100000, 999999)
#         self.balance = 0

#     def display(self) -> None:
#         print(f"Name = {self.name}")
#         print(f"Account no = {self.account_no}")
#         print(f"Balance = {self.balance}")

# obj = Bank()
# obj.display() # here account no is randomly generated one
# print("--------------")

# obj.account_no =1 # here when i assign 1 to account no then account no will be now 1 not the random value but this is wrongit should not change like this then we have a concept of access modifiers
# obj.display()

# access modifiers -> will say that that variable should access only within the class not outside of the class
# for this there are 3 they are below 
# public, protected, private, 

# public :- class variables can even access outside the class those are called public here above is the way of public 
# private :- only accessible inside the class cannot be acessible outside the class, for this for variable  have to write __ prior to the name
# example below

print("----------------------")

# Encapsulation: Encapsulation is ntg but Data hiding , data hiding through access modifiers
# from random import randint


# class Bank:
#     def __init__(self) -> None:
#         self.name = input("Enter name = ")
#         self.__account_no = randint(100000, 999999)
#         self.__balance = 0

#     def display(self) -> None:
#         print(f"Name = {self.name}")
#         print(f"Account no = {self.__account_no}")
#         print(f"Balance = {self.__balance}")

# obj = Bank()
# obj.display() # here account no is randomly generated one
# print("--------------")

# obj.account_no =1 # here when i assign 1 to account no then account no will not change because we are using private
# obj.__account_no =1# same as above no change
# obj.display()

print("----------------------")

# now i want to display only balance of that object we basically say that as getter and setter

# from random import randint


# class Bank:
#     def __init__(self) -> None:
#         self.name = input("Enter name = ")
#         self.__account_no = randint(100000, 999999)
#         self.__balance = 0

#     def display_balance(self): # getter
#         print(self.__balance)

#     def display(self) -> None:
#         print(f"Name = {self.name}")
#         print(f"Account no = {self.__account_no}")
#         print(f"Balance = {self.__balance}")

# obj = Bank()
# obj.display() # here account no is randomly generated one
# print("--------------")

# print(obj.display_balance()) # getter here that display balance function is public so i can access outside the class


print("----------------------")

# now if i want to modify the balance then it is called setter
from random import randint


class Bank:
    def __init__(self) -> None:
        self.name = input("Enter name = ")
        self.__account_no = randint(100000, 999999)
        self.__balance = 0

    def display_balance(self): # getter
        print(self.__balance)

    def set_balance(self,new_amount): # setter
        self.__balance = new_amount

    def display(self) -> None:
        print(f"Name = {self.name}")
        print(f"Account no = {self.__account_no}")
        print(f"Balance = {self.__balance}")

obj = Bank()
obj.display() # here account no is randomly generated one
print("--------------")
obj.set_balance(1000)
obj.display_balance()# getter here that display balance function is public so i can access outside the class


# even though i have written variables in python but still i can access in python publc provate are not strictly followed as like as c++
# how to access a priavte variable outside the class below:-

print(obj._Bank__balance) # syntax -> object._class name.__class variable name  # never do this this is called name mangling






