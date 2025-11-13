# args-> when you don't know how many number of arguments you will get during the function call then you have to use args [arbitary amount of parameters]
# nowif i know if i have 3 parameters then the below code will work what if i have 2 then also i want the code to be executed without any errors then we have to use args

# args -> arguments

def add(n1, n2, n3):
    total = n1 + n2 + n3
    print(total)


add(1, 2, 3)
add(100, 7, 3)
add(12, 24)


# in place of args you can give xyz any thing you want mostly args will be used and when you run this out will come in tuple
def add(*args):
    print(args)


add(1, 2, 3)
add(100, 7, 3)
add(12, 24)


# and if you want to check the sum then


def add(*args):
    print(sum(args))


add(1, 2, 3)
add(100, 7, 3)
add(12, 24)

# using list


def add(*args):
    print(args)


add([1, 2], [100, 200], 45, 100)  # 4 arguments here
# using tha above arguments you cannot take sum because list and numbers


# kwargs -> keyword arguments -> used to accept any kind of paramters rather than mentioning like if there is any keyword arguments like key value pair that goes under kwargs
# as argsas tuple, kwargs as dictionary
def add(*args, **kwargs):
    print(kwargs)


add(name="honey", age=23, gender="Female")
# o/p: {'name': 'honey', 'age': 23, 'gender': 'Female'}


# example


def add(*args, **kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k, v)


add(name="honey", age=23, gender="Female")


def add(n1, n2, n3, *args, **kwargs):
    print(f"{n1=}")
    print(f"{n2=}")
    print(f"{n3=}")
    print(f"{args=}")
    print(f"{kwargs=}")
    print(f"{kwargs["name"]}")


add(5, 10, 15)  # now these 3 arguments won't go to args because we have n1,n2,n3 we have to provide the values for them so
add(5, 10, 15, 100, 200, 300)  # now rest of the values 100,200,300 will go under args
add(5, 10, 15, 100, 200, 300, name="Honey")  # here kwargs as name:Honey
