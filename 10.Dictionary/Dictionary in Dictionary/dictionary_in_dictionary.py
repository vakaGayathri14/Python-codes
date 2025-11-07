students_data = {
    "anirudh": {
        "roll_number": 431,
        "gender": "Male",
        "physics": 78,
        "chemistry": 89,
    },
    "Sailu": {
        "roll_number": 122,
        "gender": "Female",
        "physics": 90,
        "chemistry": 82,
    },
    "honey": {
        "roll_number": 124,
        "gender": "Female",
        "physics": 82,
        "chemistry": 91,
    },
}


print(students_data)
print(students_data["Sailu"])
print(students_data["Sailu"]["roll_number"])
print(
    students_data["Sailu"]["roll_number"]
    + students_data["honey"]["roll_number"]
    + students_data["anirudh"]["roll_number"]
)


"""
Question :
o/p:
anirudh -> 234[total marks]
sailu -> 567[total marks]

"""

for names, details in students_data.items():
    print(names)
    print(details)
    print(details["physics"])
    print(details["chemistry"])

    total = details["physics"] + details["chemistry"]
    print(f"{names} -> {total}")
