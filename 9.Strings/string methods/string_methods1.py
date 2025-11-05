"""
isupper,islower,isalpha,isalnum,isspace -> these methods gives output in boolean
"""

# isupper -> it will check the given variable is in totaly uppercase based on that it will give the output
a = "honey AND raDHA"
x = a.isupper()
print(x)

a = "HONEY#$%^&*!1211"
x = a.isupper()
print(x)

# islower -> it will check for the given variable is in lower case or not
b = "honey1234"
y = b.islower()
print(y)

c = "hOney2345"
z = c.islower()
print(z)

# isalpha ->if it has only alphabets then it will be true ese false even if we have space also it will be false and also in case of numbers also false
d = "honey"
e = d.isalpha()
print(e)

f = "honey13"
g = f.isalpha()
print(g)

h = "honey radha"
i = h.isalpha()
print(i)

# isalnum -> aplhabets or numbers notspecial characters
j = "anuradha124"
k = j.isalnum()
print(k)

l = "anuradha.$124"
m = l.isalnum()
print(m)

# isdigit -> It allows only digits

n = "anuradha.$124"
o = n.isdigit()
print(o)

p = "124"
q = p.isdigit()
print(q)

r = "12.4"
s = r.isdigit()
print(s)

# isspace -> only if it has "\n or \t or space space" in those conditions only it will work
t = "\nfgh"
u = t.isspace()
print(u)

v = "\n\t  "  # only in this case it is true
x = v.isspace()
print(x)


# question
# so if this is string is digit then convert it into integer if not then say cannot be converted into integer

p = input("enter a string: ")
x = p.isdigit()
if x:
    y = int(p)
    print(y, type(y))
else:
    print("cannot be converted into integer")
