# # what is Exception Handling

lst = [4, 5, 5, 34, 2, 3, 6]
# # now if i want to print the 1ist of index 1
print(lst[1])

# # now if i want to print the 1ist of index at 65 I know it doesn't exist
print(lst(65)) # error  because index doesn't exist the below lines doesn't even run because of the error In order to handle this type of situation we use exception handling
print(lst(2))
print(lst(3))
print(lst(4))


#syntax of exception handling

try:
    lst = [4, 5, 5, 34, 2, 3, 6]
    print(lst[1])
    print(lst(65)) # error  because index doesn't exist the below lines doesn't even run because of the error In order to handle this type of situation we use exception handling now in this we have written exception so we don't error ratherwe will get that exception message and the below lines doesn't run. 
    print(lst(2))
    print(lst(3))
    print(lst(4))
except:
    print("Some error occured")

print("Done")
print("Bye")