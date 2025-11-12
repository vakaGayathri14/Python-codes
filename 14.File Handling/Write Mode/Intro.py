# Write Mode and AppendMode
#write mode: If i want to write in a file  then we use write mode

with open("C:\\Users\\Gayathri\\OneDrive\\Desktop\\Python\\Python-codes\\14.File Handling\\Write Mode\\hello.txt","w") as f:
    f.write("Honey") #here we have to provide what we want to write
    #In write it will override the previous values
    f.write("Honeyq")
    f.write("learn\n")
    f.write("and grow")

# for example if i don't have that file there in the registry it will automatically creates a file with that file name
with open("hello1.txt","w") as f:
    f.write("Honey") #here we have to provide what we want to write
    #In write it will override the previous values
    f.write("Honeyq")
    f.write("learn\n")
    f.write("and grow")
