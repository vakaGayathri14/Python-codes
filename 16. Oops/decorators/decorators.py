# decorators -> starts with @ and those are used to check some predefined conditions before running the functions and if you are writing a decorator you have to create a function of that decorator

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
def ordinary():
    print("I am ordinary")
ordinary()
