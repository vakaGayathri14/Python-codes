my_string = "code and debug"

# iterate by index
for index in range(0, len(my_string)):
    print(my_string[index], end="")

# iterate by value
for ch in my_string:
    print(ch, end="")

# iterate from reverse

for rev in range(len(my_string) - 1, -1, -1):
    print(my_string[rev], end="")
