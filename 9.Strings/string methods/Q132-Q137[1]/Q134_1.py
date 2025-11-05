"""
Q134. Ask a string from user. Convert all the alphabets to lowercase.
"""

# using string methods
my_str = input("Enter a string: ")
x = my_str.lower()
print(x)


# using normal logic
my_str1 = input("Enter a string: ")
result = ""

for i in my_str1:
    ascii = ord(i)
    if ascii >= 65 and ascii <= 90:
        new_ascii = ascii + 32
        new_chr = chr(new_ascii)
        result += new_chr
    else:
        result += i
print(result)
