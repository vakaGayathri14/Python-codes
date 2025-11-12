# with keyword 
# using with keyword we don't need to specify to close the file it will automatically closes the file

with open("C:\\Users\\Gayathri\\OneDrive\\Desktop\\Python\\Python-codes\\14.File Handling\\hello.txt","r") as f:
    print(f.read())
#here i will get error because after the above line it will close the file that's why we will get error
# print(f.read())

