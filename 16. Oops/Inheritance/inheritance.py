class Car:
    def __init__(self, color:str, type:str, mileage:float, seat_capacity:int) -> None:
        self.color = color  # self.color is a class variable and color is a parameter
        self.type = type
        self.mileage = mileage
        self.seat_capacity = seat_capacity


    def base_info(self):
        print(f"color = {self.color} ") # self.color is a class variable and color is a parameter
        print(f"type = {self.type} ")
        print(f"mileage = {self.mileage} ")
        print(f"seat_capacity = {self.seat_capacity} ")

# c1 = Car() # here i will get error because i haven't provided parameter values as the init run

# c1 = Car("Black","petrol",22.5,4) # whie creating an object we have to provide arguments if we have parameters
# c1.base_info()


class Audi(Car):  # here Audi class is inheriting Car class
    def __init__(self) ->None:
        print("Audi INIT") # here also you can create variables




c1 = Audi() # if run this o/p is Audi INIT now the above init runs 
# c1.base_info() # error because we haven't initialize those variables so error I i want that to executed without an error then 
c1.color = "White"
c1.type="Petrol"
c1.mileage=22.8
c1.seat_capacity=6
c1.base_info() # here now i will get output as the above values


# #now if i remove car during the creation of audi class i will get error 
# # class Audi(): -> error


print("----------------------------")

# # Without using init method
class Car:

    def set_info(self,color:str, type:str, mileage:float, seat_capacity:int) -> None:
        self.color = color  # self.color is a class variable and color is a parameter
        self.type = type
        self.mileage = mileage
        self.seat_capacity = seat_capacity

    def base_info(self):
        print(f"color = {self.color} ") # self.color is a class variable and color is a parameter
        print(f"type = {self.type} ")
        print(f"mileage = {self.mileage} ")
        print(f"seat_capacity = {self.seat_capacity} ")



class Audi(Car):  # here Audi class is inheriting Car class

    def set_audi_info(self,electric:bool,city:str):
        self.electric = electric
        self.city = city

    def audi_info(self):
        print(f"Electric = {self.electric}")
        print(f"city = {self.city}")
        


c1 = Audi() # object created in audi class
c1.set_info("Black","petrol",12.2,4)
c1.set_audi_info(True,"Mumbai")
c1.base_info()
c1.audi_info()



print("---------------")

# # now in the above case i am writing set info  and as well as set audio info as 2 why can't i write as in one below is the way

# # method - 1
class Car:

    def set_info(self,color:str, type:str, mileage:float, seat_capacity:int) -> None:
        self.color = color  # self.color is a class variable and color is a parameter
        self.type = type
        self.mileage = mileage
        self.seat_capacity = seat_capacity

    def base_info(self):
        print(f"color = {self.color} ") # self.color is a class variable and color is a parameter
        print(f"type = {self.type} ")
        print(f"mileage = {self.mileage} ")
        print(f"seat_capacity = {self.seat_capacity} ")



class Audi(Car):  # here Audi class is inheriting Car class

    def set_audi_info(self,electric:bool,city:str):
        # calling set_info here 
        self.set_info("Black","petrol",12.2,4)
        self.electric = electric
        self.city = city

    def audi_info(self):
        print(f"Electric = {self.electric}")
        print(f"city = {self.city}")
        



c1 = Audi() # object created in audi class
# c1.set_info("Black","petrol",12.2,4)
c1.set_audi_info(True,"Mumbai")
c1.base_info()
c1.audi_info()

print("------------------")
#method - 2

class Car:

    def set_info(self,color:str, type:str, mileage:float, seat_capacity:int) -> None:
        self.color = color  # self.color is a class variable and color is a parameter
        self.type = type
        self.mileage = mileage
        self.seat_capacity = seat_capacity

    def base_info(self):
        print(f"color = {self.color} ") # self.color is a class variable and color is a parameter
        print(f"type = {self.type} ")
        print(f"mileage = {self.mileage} ")
        print(f"seat_capacity = {self.seat_capacity} ")



class Audi(Car):  # here Audi class is inheriting Car class

    def set_audi_info(self,color:str, type:str, mileage:float, seat_capacity:int,electric:bool,city:str):
        # calling set_info here 
        self.set_info(color,type,mileage,seat_capacity)
        self.electric = electric
        self.city = city

    def audi_info(self):
        print(f"Electric = {self.electric}")
        print(f"city = {self.city}")
        



c1 = Audi() # object created in audi class
# c1.set_info("Black","petrol",12.2,4)
c1.set_audi_info("Black","petrol",12.2,4,True,"Mumbai")
c1.base_info()
c1.audi_info()

print("------------------")
# now if i want to see full info at once rather than calling base_info once and audi info once then


class Car:

    def set_info(self,color:str, type:str, mileage:float, seat_capacity:int) -> None:
        self.color = color  # self.color is a class variable and color is a parameter
        self.type = type
        self.mileage = mileage
        self.seat_capacity = seat_capacity

    def base_info(self):
        print(f"color = {self.color} ") # self.color is a class variable and color is a parameter
        print(f"type = {self.type} ")
        print(f"mileage = {self.mileage} ")
        print(f"seat_capacity = {self.seat_capacity} ")



class Audi(Car):  # here Audi class is inheriting Car class

    def set_audi_info(self,color:str, type:str, mileage:float, seat_capacity:int,electric:bool,city:str):
        # calling set_info here 
        self.set_info(color,type,mileage,seat_capacity)
        self.electric = electric
        self.city = city

    def audi_info(self):
        print(f"Electric = {self.electric}")
        print(f"city = {self.city}")

    def show_full_info(self):
        self.base_info()
        self.audi_info()
        



c1 = Audi() # object created in audi class
# c1.set_info("Black","petrol",12.2,4)
c1.set_audi_info("Black","petrol",12.2,4,True,"Mumbai")
# c1.base_info()
# c1.audi_info()
c1.show_full_info()


print("------------------")
# in the above method each time i have to call info inorder to overcome this we use init

class Car:
    def __init__(self) -> None:
        print("CAR INIT")

    def set_info(self,color:str, type:str, mileage:float, seat_capacity:int) -> None:
        self.color = color  # self.color is a class variable and color is a parameter
        self.type = type
        self.mileage = mileage
        self.seat_capacity = seat_capacity

    def base_info(self):
        print(f"color = {self.color} ") # self.color is a class variable and color is a parameter
        print(f"type = {self.type} ")
        print(f"mileage = {self.mileage} ")
        print(f"seat_capacity = {self.seat_capacity} ")

print("------------------")

class Audi(Car):  # here Audi class is inheriting Car class
    
    def __init__(self) -> None:
        # above case i can able to only print audi init not car nit why because it is not going into car init as i have initialized it in the funcction so to overcome this we use super() init -> it means run the previous class now car init also will print
        super().__init__()
        print("AUDI INIT")

    def set_audi_info(self,color:str, type:str, mileage:float, seat_capacity:int,electric:bool,city:str):
        # calling set_info here 
        self.set_info(color,type,mileage,seat_capacity)
        self.electric = electric
        self.city = city

    def audi_info(self):
        print(f"Electric = {self.electric}")
        print(f"city = {self.city}")

    def show_full_info(self):
        self.base_info()
        self.audi_info()
        



c1 = Audi() # object created in audi class
# c1.set_info("Black","petrol",12.2,4)
c1.set_audi_info("Black","petrol",12.2,4,True,"Mumbai")
# c1.base_info()
# c1.audi_info()
c1.show_full_info()


print("-----------------")

# above case i can able to only print audi init not car nit why because it is not going into car init as i have initialized it in the funcction so to overcome this we use super() init 

#now i want to implement usinng init


class Car:
    def __init__(self,color:str, type:str, mileage:float, seat_capacity:int) -> None:
        self.color = color  # self.color is a class variable and color is a parameter
        self.type = type
        self.mileage = mileage
        self.seat_capacity = seat_capacity


    def base_info(self):
        print(f"color = {self.color} ") # self.color is a class variable and color is a parameter
        print(f"type = {self.type} ")
        print(f"mileage = {self.mileage} ")
        print(f"seat_capacity = {self.seat_capacity} ")



class Audi(Car):  # here Audi class is inheriting Car class
    
    def __init__(self,electric:str,city:str) -> None:
        # above case i can able to only print audi init not car init why because it is not going into car init as i have initialized it in the funcction so to overcome this we use super() init -> it means run the previous class now car init also will print, here super is refering to the parent class
        super().__init__("Black","petrol",12.2,4)
        self.electric = electric
        self.city = city

    def audi_info(self):
        print(f"Electric = {self.electric}")
        print(f"city = {self.city}")

    def show_full_info(self):
        self.base_info()
        self.audi_info()
        


c1 = Audi(True,"Mumbai") # object created in audi class
c1.show_full_info()
