# lst = [4, 5, 5, 34, 2, 3, 6]
# # now if i want to print the 1ist of index 1
# print(lst[1])
# print(lst(65)) # error  because index doesn't exist the below lines doesn't even run because of the error In order to handle this type of situation we use exception handling
# print(lst(2))
# print(lst(3))
# print(lst(4))

#the above error is index error like wise there are so many exception names

# print(10/0) # here I will get an ZeroDivisionError 

# Multiple Exception handling

try:
    my_list=[2,5,6,7,88,0]
    # print(my_list[76])
    # print(my_list[0]/my_list[-1])
    my_list = my_list * "abc"

except IndexError:
    print("Invalid Index")
except ZeroDivisionError:
    print("You cannot divide by zero")
except:
    print("some error occured")

