from random import randint # randint will give us a random integer

class Bank:
    def __init__(self) -> None:
        self.account_number=randint(100000,999999) # now this means generate a random number between 1 lakh to 999999
        self.full_name=input("Enter name: ")
        self.balance = 0
        self.phone_number=int(input("Enter phone number: "))

    def show_balance(self) -> None:
        print(f"Current balance: {self.balance}")
        

    
    def withdraw(self) -> None:
        amount=int(input("Enter amount to withdraw: "))
        if amount>self.balance:
            print("In Sufficient balance")
        else:
            self.balance=self.balance-amount
    
    def deposit(self) -> None:
        amount=int(input("Enter the amount to deposit: "))
        if amount<0:
            print("Not possible to deposit")
        else:
            self.balance=self.balance+amount
    
    def show_info(self):
        print(f"full_name : {self.full_name}")
        print(f"account_number: {self.account_number}")
        print(f"balance: {self.balance}")
        print(f"phone_number: {self.phone_number}\n")

# v1 = Bank()
# v1.show_balance()
# v1.deposit()
# v1.show_balance()
# v1.withdraw()
# v1.show_balance()

#now if i want accounts for 3 users then we can create each object one by one rather than like that we need some limit then we have to use list
# v2 = Bank()
# v3 = Bank()
# v4 = Bank()


banks = [] # empty list with a variable banks
# print(banks)

# x = Bank()
# banks.append(x)
# print(banks)

# y = Bank() # here we are creating
# banks.append(y)
# print(banks)

# banks[0].show_balance()
# banks[1].deposit()
# banks[1].show_balance()
# rather than creating for each object like above here we use while loop


def check_account_exists(acc_no:int):
    global banks
    for i in banks:
        if i.account_number == acc_no:
            # return True
            return i
    # return False
    return None


while True:
    print("1. Create account")
    print("2. Show all bank details")
    print("3. Deposit amount")
    print("4.Withdraw amount")
    print("5.Transfer amount") # hard
    print("6. Exit")
    choice=int(input("Enter choice = "))
    if choice == 1:
        obj = Bank()
        banks.append(obj)
        print(banks)
    elif choice == 2:
        if len(banks) == 0:
            print("No accounts have been created yet")
        else:
            for i in banks:
                i.show_info()
    elif choice == 3:
        if len(banks) ==0:
            print("Please create your account \n")
            
        else:
            acc_no=int(input("Enter account number to deposit: "))
            for i in banks:
                if i.account_number == acc_no:
                    i.deposit()
                    i.show_info()
                    break
            else:
                print("Enter a valid account number")
                break
    elif choice == 4:
        if len(banks)==0:
            print("No accounts found Create an account")
        else:
            acc_no=int(input("Enter account no to withdraw: "))
            for i in banks:
                if i.account_number == acc_no:
                    # amount=int(input("Enter amount to withdraw: "))
                    # if i.balance>=500 and i.balance>amount:
                        i.withdraw()
            else:
                print("Enter a valid account number")
    elif choice == 5:
        from_acc_no= int(input("Enter account number from which you want to transfer: "))
        to_acc_no= int(input("Enter account number to which you want to transfer: "))
        
        # if check_account_exists(from_acc_no) and check_account_exists(to_acc_no):
        from_acc_obj = check_account_exists(from_acc_no)
        to_acc_obj =check_account_exists(to_acc_no)
        if from_acc_obj!=None and to_acc_obj!=None:
            transfer_amount = int(input("Enter transfer amount = "))
            if from_acc_obj.balance<transfer_amount:
                print("Insufficient amount")
            else:
                from_acc_obj.balance=from_acc_obj.balance - transfer_amount
                to_acc_obj.balance=to_acc_obj.balance + transfer_amount

        else:
            print("Account doesn't exists")

    elif choice == 6:
        break
    else:
        print("Invalid Choice")





