import os

# Deleting a directory has 2 types
# 1. when the folder is empty then only this below process works
if os.path.exists("Folder 1"):
    os.rmdir("Folder 1")  # rmdir-> remove directory
    print("Directory deleted.")
else:
    print("Directory does not exists.")

# remember if under folder 1 it has some content then the above process gives you an error
