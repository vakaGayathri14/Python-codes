my_dict = {
    "name": "honey",
    "age": 22,
    "gender": "female",
}
print(my_dict)

# now i want to modify my age from 22 to 24 how to do this

# method 1
my_dict["age"] = 100
print(my_dict)

# method 2
my_dict["xyz"] = (
    100  # using this you can add/update if that key present then it will update rather it will create a key value with this details
)
print(my_dict)


# method 3
# I want to add marks and address

my_dict["marks"] = 100
my_dict["address"] = "Hyd"
print(my_dict)

# if you want to write 5 times then below is the shortcut
my_dict.update({"marks": 99, "address": "Hyd"})

# now if i want to add name already we have a key called name that will bereplaced my new one
my_dict.update({"marks": 99, "address": "Hyd", "name": "Xyz"})
print(my_dict)
