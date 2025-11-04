a = "honey"
b = "Honey"

print(a + b)  # possible
# print(a * b)  # not possible with 2 strings but possible with one string
print(a * 3)  # possible as it has one string
c = [1, 2, 4]
print(c * 3)

# print(a/3) #not possible
# print(a-3) #not possible

print(a == b)

# ASCII VALUES

first_ch = "a"
second_ch = "A"
print(first_ch > second_ch)
print(first_ch < second_ch)

first_ch1 = "honey"
second_ch1 = "Honey"
print(first_ch1 > second_ch1)
print(first_ch1 < second_ch1)

first_ch2 = "honey"
second_ch2 = "honeY"
print(first_ch2 > second_ch2)
print(first_ch2 < second_ch2)

ch3 = "a"
print(ord(ch3))  # ord is ntg but the ordinal values of the character

num = 97
print(chr(num))  # return unicode of string
