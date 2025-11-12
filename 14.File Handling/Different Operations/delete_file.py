import os

if os.path.exists("hello.txt"):
    os.remove("hello.txt")
    print("file deleted")
else:
    print("File does not exist.")
