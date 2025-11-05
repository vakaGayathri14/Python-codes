"""
Q133. Ask a string from user. Count the number of uppercase and
lowercase characters in that String.

"""

# method using string methods
my_string = input("enter a string")
count_upper = 0
count_lower = 0
for i in my_string:
    if i.isupper():
        count_upper += 1
    elif i.islower():
        count_lower += 1
    else:
        print("none")
print(f"upper case count {count_upper}")
print(f"Lower case count {count_lower}")


# methods using ascii

my_string1 = input("enter a string")
count_upper1 = 0
count_lower1 = 0

for i in my_string1:
    ascii = ord(i)
    if ascii >= 65 and ascii <= 90:
        count_upper1 += 1
    elif ascii >= 97 and ascii <= 122:
        count_lower1 += 1

print(f"upper case count {count_upper1}")
print(f"Lower case count {count_lower1}")


# just for checking purpose
ch4 = "A"
print(ord(ch4))

ch1 = "Z"
print(ord(ch1))

ch2 = "a"
print(ord(ch2))

ch3 = "z"
print(ord(ch3))
