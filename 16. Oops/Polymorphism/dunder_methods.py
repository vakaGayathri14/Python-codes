
# class Father:
#     def __init__(self):
#         self.father_name = input("Enter father name: ") # father name can be acessible outside the class fine
#         self._bank_balance = int(input("Enterbank balance: ")) # bank balance can be accessible in this father class and also i want that bank balance to be accessible to the child class which inherits from the father class then it is called protected for that i have to write single under score before variable name
#         self.__phone_model = input("Enter phone model: ") # private


#     # magic methods/dunder methods -> in these methods compulsprily i have to return 
#     def __str__(self) -> str:
#         return "I am a string dunder method"
    
#     def display_father(self):
#         print(f"Father name = {self.father_name}")
#         print(f"Bank balance = {self.bank_balance}")
#         print(f"phone model = {self.phone_model}")

# obj = Father()
# print("-----------")
# print(obj) # previously when i run this i got object name in address 

# # now in the above i used dunder method i don't want to see the obj address rather i want something to be printed so using str method i am print something  like above

# if i have 2 objects then 


# class Father:
#     def __init__(self):
#         self.father_name = input("Enter father name: ") # father name can be acessible outside the class fine
#         self._bank_balance = int(input("Enterbank balance: ")) # bank balance can be accessible in this father class and also i want that bank balance to be accessible to the child class which inherits from the father class then it is called protected for that i have to write single under score before variable name
#         self.__phone_model = input("Enter phone model: ") # private


#     # magic methods/dunder methods -> in these methods compulsprily i have to return 
#     def __str__(self) -> str:
#         return "I am a string dunder method"
    
#     def display_father(self):
#         print(f"Father name = {self.father_name}")
#         print(f"Bank balance = {self.bank_balance}")
#         print(f"phone model = {self.phone_model}")

# obj_1 = Father()
# obj_2 = Father()
# print("-----------")
# print(obj_1) # previously when i run this i got object name in address 
# print(obj_2)
# # above as you created 2 objects you will get that string 2 times

print("-------------")
# where you will use this dunder methods see this example:


class Father:
    def __init__(self):
        self.father_name = input("Enter father name: ") # father name can be acessible outside the class fine
        self._bank_balance = int(input("Enterbank balance: ")) # bank balance can be accessible in this father class and also i want that bank balance to be accessible to the child class which inherits from the father class then it is called protected for that i have to write single under score before variable name
        self.__phone_model = input("Enter phone model: ") # private


    # magic methods/dunder methods -> in these methods compulsprily i have to return 
    def __str__(self) -> str: # here str method will override
        return f"Father name = {self.father_name}\nBank balance = {self._bank_balance}\nphone model = {self.__phone_model}"

obj = Father()
print("-----------")
print(obj) # previously when i run this i got object name in address 

