students_data = {
    "anirudh": {
        "roll_number": 431,
        "gender": "Male",
        "marks": {"physics": 78, "maths": 89, "chemistry": 67},
    },
    "Sailu": {
        "roll_number": 122,
        "gender": "Female",
        "marks": {"physics": 90, "maths": 75, "chemistry": 82},
    },
    "honey": {
        "roll_number": 124,
        "gender": "Female",
        "marks": {"physics": 82, "maths": 91, "chemistry": 56},
    },
}

for names, details in students_data.items():
    # print(names)
    # print(details)
    # print(details["marks"])
    marks = (
        details["marks"]["physics"]
        + details["marks"]["maths"]
        + details["marks"]["chemistry"]
    )
    print(f"{names} scored {marks} marks")
