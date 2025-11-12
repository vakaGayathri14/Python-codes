import os

# now I want to remane hello.txt
if os.path.exists("hello.txt"):
    os.rename("hello.txt", "new_hello.txt")
    print("File renamed.")
else:
    print("File does not exist.")
