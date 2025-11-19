# polymorphism : Many forms


class Animal:
    def sound(self):
        print("Animal speaking")


class Dog(Animal):
    def sound(self):
        print("Bhaw bhaw bhaw")


class Cat(Animal):
    def sound(self):
        print("Meow Meow Meow")


obj = Dog()
obj.sound()  # it wll check that function in dog class if present then it will run that function

# Method Overriding
# for example in the dog if we don't have a functino like sound then?


class Animal:
    def sound(self):
        print("Animal speaking")


class Dog(Animal):
    def sound_1(self):
        print("Bhaw bhaw bhaw")


class Cat(Animal):
    def sound(self):
        print("Meow Meow Meow")


obj = Dog()
obj.sound()  # here first it checks at dog class wheather that sound function present or not if it present then it will execute in this case it was not present there then it will check the parent class of the class dog then it is animal then it will check wheather that function exists or not if exists then it will execute that is called method overriding


# now even if user modified the function in parent class and tried to access then you will get an error

# method overloading is not there in python 
# each method has different forms