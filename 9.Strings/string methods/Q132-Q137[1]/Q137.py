"""
Q137. Ask a string from user. Print the count of how many alphabets, digits,
spaces and symbols (everything else) are there in that string.
"""

my_str = input("Enter a string: ")
alphabets_count = 0
digits_count = 0
spaces_count = 0
symbols_count = 0

x = "0"
print(ord(x))

for i in my_str:
    ascii = ord(i)
    if (ascii >= 65 and ascii <= 90) or (ascii >= 97 and ascii <= 122):
        alphabets_count += 1
    elif ascii >= 48 and ascii <= 57:
        digits_count += 1
    elif ascii == 32:
        spaces_count += 1
    else:
        symbols_count += 1
print(f"alphabets_count is {alphabets_count}")
print(f"digits_count is {digits_count}")
print(f"spaces_count is {spaces_count}")
print(f"symbols_count is {symbols_count}")
