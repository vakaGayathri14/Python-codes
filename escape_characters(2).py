"""Escape sequences/characters : alway be in double quotes or single quotes
"""

print("Hello World \n This is new") #\n -> new line
print(" My name is Gayathri \n my age is 22 \n my gender is female")

print("Start your \t\t\t coding journey") #\t ->tab space

#This is a code in "python language"
print('This is a code in "python language"') #'' used as we need ""
print("This is a code in \"python language\"") # here we are using \before ""

print('This is a code in \'python language\'') # here we are using \before ''

# My name is A\nuradha
print("My name is A\\nuradha") # here used \\ it ignore \n 

#practice

# Q1. Write a program that prints a path like this:C:\Users\John\Desktop\File.txt using the appropriate escape sequences
print("C:\\Users\\John\\Desktop\\File.txt")

#Q2. Write a Python program that prints a message with a double-quote character inside it  Eg:- He said, "Hello!"
print("He said, \"Hello!\"")

# Q3. Create a program that prints a message containing both single and double quotes, like this: She said, 'It's cold'
print('She said, \'It\'s cold\'')