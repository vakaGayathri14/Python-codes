a = [1, 2, 44, 33]
# suppose if i want toprint from 44 then
print(a[2])

# how can we do the same in dictionary
my_dict = {
    "name": "honey",
    "age": 22,
    "gender": "female",
}

# now i only want to print honey
# there won't be positions in dictionary rather here we have to provide key

# this is a method to get a value
print(my_dict["name"])
print(my_dict["age"])
# print(my_dict["xyz"])  # this will get keyError because that key doesn't exist at all

# another method to get a value
x = my_dict.get("name")
print(x)

# now what is the difference between the first method & second method
# so here print(my_dict["name"]) if i give an unkonwn key it gives an error
# but if i use get with same unknown key it will give o/p as none
# none is a data type
x = my_dict.get("namee")
print(x)
print(x, type(x))


# Question if i want to check wheather the key exists or not
k = input("Enter a key:")
result = my_dict.get(k)
if result is not None:
    print(result)
else:
    print("key does not exists")
