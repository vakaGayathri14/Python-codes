students_data = {
    "anirudh": {
        "roll_number": 431,
        "gender": "Male",
        "marks": [78, 89, 67, 92, 54],
    },
    "Sailu": {
        "roll_number": 122,
        "gender": "Female",
        "marks": [90, 75, 82, 68, 91],
    },
    "honey": {
        "roll_number": 124,
        "gender": "Female",
        "marks": [82, 91, 56, 78, 69],
    },
}

"""
Question:

o/p:
anirudh -> 234[total marks]
sailu -> 567[total marks]

"""

print(students_data)

for names, details in students_data.items():
    # print(names)
    # print(details)
    # print(details["marks"])
    total = sum(details["marks"])
    print(f"{names} scored {total} marks")


# do without sum of above sum

for names, details in students_data.items():
    # print(names)
    # print(details)
    # print(details["marks"])
    total = sum(details["marks"])
    print(f"{names} scored {total} marks")


for names, details in students_data.items():
    x = 0
    # print(details["marks"])
    for i in range(len(details["marks"])):
        x = x + details["marks"][i]
    print(f"{names} scored {x} marks")
