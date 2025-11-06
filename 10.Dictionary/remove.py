my_dict = {
    "name": "honey",
    "age": 22,
    "gender": "female",
}

print(my_dict)

#  delete the gender
# del my_dict["gender"]
# print(my_dict)

# delete dictionary
# del my_dict
# print(my_dict)  # because it is deleted

# other method

# my_dict.pop("name")
# print(my_dict)


# my_dict.pop()
print(my_dict)


my_dict.popitem()  # last item is deleting
print(my_dict)
