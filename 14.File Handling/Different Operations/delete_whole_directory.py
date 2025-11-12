import shutil  # using this it will delete the content in the directory as well
import os

# Deleting a directory and it's contents

if os.path.exists("folder 2"):
    shutil.rmtree("folder 2") # rmtree-> tree has branches like wise folder inside the files
    print("Directory and it's contents deleted")
else:
    print("Directory does not exist.")