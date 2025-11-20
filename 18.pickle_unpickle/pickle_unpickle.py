# Write
x = "Code and debug"
with open("name.txt", "w") as f:
    f.write(x)

# read

with open("name.txt",'r') as f:
    x = f.read()
    print(x)
    f.close()

