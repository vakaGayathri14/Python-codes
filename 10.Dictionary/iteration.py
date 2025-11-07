my_dict = {
    "name": "honey",
    "age": 22,
    "gender": "Female",
}

# if i want to print only the keys in the dictionary then there is a method called keys
print(my_dict.keys())  # you will get sort of listsnof dictionary keys

# now i can iterate them as they are in list
for k in my_dict.keys():
    print(k)

# now how can i get values using keys
for k in my_dict.keys():
    print(my_dict[k])  # you ccan use this or the below one
    # print(my_dict.get(k))

# other method to get values

for k in my_dict.values():
    print(k)

# note: through values i cannot get keys because those are not unique as they are repitative

# Question if i want the sum of all the values in the dictionay

my_dict = {
    "history": 67,
    "computer": 99,
    "science": 78,
    "maths": 11,
}

total_marks = 0
for i in my_dict.values():
    total_marks = total_marks + i
print(total_marks)
