"""
Logical Operators: Logical operators are used to combine conditional statements

Operator    Description                                                 Example
and         Returns True if both statements are true                    x<10 and y<15
or          Return true if one of the statements is true                x<15 or x<24
not         Reverse the result,returns false if the result is true      not(x<15 and x<120)

"""

# 1.Ask physics marks, 2. ask chemistry marks from user, select a student who has passed in both physcics and chemistry, to pass in each subject marks should be more than 33

# # AND
physics_marks = int(input("Enter the physics marks:"))
chemistry_marks = int(input("Enter the chemistry marks:"))

if(physics_marks>33 and chemistry_marks>33):
    print(f"selected")
else:
    print(f"not selected")

# OR

if(physics_marks>33 or chemistry_marks>33):
    print(f"selected")
else:
    print(f"not selected")

# NOt
print(not(physics_marks>33 or chemistry_marks>33))
print(not physics_marks>33)


