# now if you want to read the file then

# if read mode.py and hello.txt is in same folder then we can just give the file path as hello.txt as given below, and you have to give mode by default it is read mode
# f = open("hello.txt", "r")
f = open("C:\\Users\\Gayathri\\OneDrive\\Desktop\\Python\\Python-codes\\14.File Handling\\hello.txt", "r")

#read the file
# x = f.read()
# if i want to read via first 5 character then below
# x = f.read(5)
#now if i run read file then the below print statements don't give the result because already cursor is at end
# print(x)
# if you want all values in one row in single line 
print(f.readline())

#again if you want to read the next row then use this
print(f.readline())

#it will give the all the values in the txt in single list 
print(f.readlines())



#shortcut
# print(f.read(5))

#now i want to print the 5 characters agin then 
# print(f.read(5)) # now the initial 5 characters won't come now they will continue from where they stopped

# close the file
f.close()


# once you open the file you have to close the file
# if hello.txt is in differnt folder like it might be in c drive or d drive then you have to copy that path of that file
# f=open("path you have to paste here")
