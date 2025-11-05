"""
Q135. Ask a string from user. Convert uppercase to lowercase and convert
lowercase to uppercase and don’t change the other letters.
"""

# using string methods
my_str = input("Enter a string: ")
x = my_str.swapcase()
print(x)


# using logic
my_str1 = input("Enter a string: ")
res = ""

for i in my_str:
    ascii = ord(i)
    # uppercase
    if ascii >= 65 and ascii <= 90:
        new_ascii = ascii + 32
        ch = chr(new_ascii)
        res += ch
    # lower case
    elif ascii >= 90 and ascii <= 122:
        new_ascii1 = ascii - 32
        ch1 = chr(new_ascii1)
        res += ch1
    else:
        res += i
print(res)
