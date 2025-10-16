num = input("Enter your name")
print(num)
print(type(num))

# #type conversion of user inputs if not in string

num= int(input("Enter a number"))
print(num)

# Taking multiple inputs we have 2 methods 1)list() 2)map()

num = int(input("Enter the number of elements:"))
lst = []
for i in range(num):
    ele = int(input("Enter the element:"))
    lst.append(ele)
print(lst)


# 2) map() print user entered elements

x = list(map(int,input("Enter the elements").split()))
print(x)


