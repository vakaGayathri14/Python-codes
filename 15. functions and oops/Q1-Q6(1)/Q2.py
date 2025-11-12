"""
Q2. Write a python functin that accepts a string and counts the number of upper and lower case letters.

"""

# upper case


def charCount(st):
    upper_count = 0
    lower_count = 0
    for i in range(len(st)):
        x = ord(st[i])
        # print(x)
        if x >= 65 and x <= 90:
            upper_count = upper_count + 1
        elif x >= 97 and x <= 122:
            lower_count = lower_count + 1
    return upper_count, lower_count


x = input("Enter a string: ")
# print(charCount(x))

upper, lower = charCount(x)
print(f"Uppercase letters: {upper}, Lowercase letters: {lower}")


# x = "A"
# print(ord(x))


# x = "Z"
# print(ord(x))


# x = "a"
# print(ord(x))


# x = "z"
# print(ord(x))
