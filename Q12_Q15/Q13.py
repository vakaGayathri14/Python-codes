"""
Q13. Write a Python program to swap the values of two variables without
using a temporary variable.

"""

a = int(input("Enter a number"))
b = int(input("Enter another number"))

print(f"{a},{b}")
# using temp variable

temp = a
a = b
b = temp
print(f"{a},{b}")



# without using 3rd variable # in this methos we are wasting 3 bits so there is other approach caled xor

a = a+b 
b = a-b
a = a-b

print(f"{a},{b}")


# XOR Approach - xor will not waste extra bits

a = a^b
b =a^b
a =a^b

print({a},{b})


#simple approach
a,b = b,a
print(f"{a},{b}")