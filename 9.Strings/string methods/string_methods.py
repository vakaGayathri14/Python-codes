"""
Title,capitalized, upper,lower,swapcase

"""

# Title -> It changes the first word into capital and rest to small if wehave next word then again start with capital letter
a = "honey"
x = a.title()
print(x)

b = "code and debug"
y = b.title()
print(y)

c = "code AND debug"
z = c.title()
print(z)

d = "codE AND debug"
i = d.title()
print(i)

# capitalize -> It only keeps initial letter as capital rest all small
e = "honey and RADHA"
u = e.capitalize()
print(u)

# Upper -> It will convert all into uppercase
f = "honey and RADha"
s = f.upper()
print(s)

# Lower ->   It will convert all into lowercase
g = "Honey aND RadHA"
t = g.lower()
print(t)

# swapcase ->uppercase will be converted in to lower and lower case will be converted into upper
h = "Honey aND RadHA"
o = h.swapcase()
print(o)
