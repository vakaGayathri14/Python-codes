my_dict = {
    "name": "honey",
    "age": 22,
    "gender": "female",
}

"""
Question: I want o/p as below

name -> honey
age -> 22
gender -> female

"""
#my approach
for i in my_dict.keys():
    print(f"{i} -> {my_dict[i]}")

# we have a method to get the both keys and values in list using items

print(my_dict.items()) #o/p -> dict_items([('name', 'honey'), ('age', 22), ('gender', 'female')])

# in the above now we got first list and inside that we have  one key value is in one position followed by 1 etc using tuple

# now how can we print in one go of key and value

#here you willget all keys in k and all values in v
for k,v in my_dict.items():
    print(k) # if i print k i  will get all keys
    print(v) # if i print k i  will get all values
    print(f"{k} -> {v}") # using this i can print keys and values


#
