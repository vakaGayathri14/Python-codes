# Q134. Ask a string from user. Convert all the alphabets to uppercase.

# using string methods
my_string = input("Enter a string:")
x = my_string.upper()
print(x)

# using normal logic
# firstly have to remember that string is immutable
my_string1 = input("Enter a string:")
result = ""
for i in my_string:
    ascii = ord(i)
    if ascii >= 97 and ascii <= 122:
        new_ascii = ascii - 32
        ch = chr(new_ascii)
        result += ch
    else:
        result += i
print(result)
