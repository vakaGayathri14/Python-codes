# here with try and except we can write else this is optional
# [else clause]
try:
    my_list = [2, 5, 6, 7, 88, 0]
    print(my_list[1])
    # print(my_list[76])
    # print(my_list[0]/my_list[-1])
    # my_list = my_list * "abc"

except IndexError:
    print("Invalid Index")
except ZeroDivisionError:
    print("You cannot divide by zero")
except:
    print("some error occured")

# when this else part will work when we don't have any errors in the try block when the try block executes successfully then the else block will run
else:
    print("Everything worked fine")
