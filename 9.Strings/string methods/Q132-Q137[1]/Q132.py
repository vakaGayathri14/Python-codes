"""
Q132. Ask a string from user. Count how many alphabets are there in that
string.

"""

# method:1 usingstring method
st = input("Enter a string: ")
total = 0
for ch in st:
    if ch.isalpha():
        total = total + 1
print(total)

# method:2 using ASCII

st1 = input("Enter a string: ")
total_1 = 0
for ch in st1:
    ascii = ord(ch)
    if (ascii >= 65 and ascii <= 90) or (ascii >= 97 or ascii <= 122):
        total_1 = total_1 + 1
print(total_1)
