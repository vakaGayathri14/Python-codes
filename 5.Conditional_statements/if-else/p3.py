"""
Q. Ask physics and chemistry marks from user
print PASS, if student is passed in  both subjects else print fail
"""

physics_marks = int(input("Enter the physics marks"))
chemistry_marks = int(input("Enter the chemistry marks"))

if (physics_marks>33 and chemistry_marks>33):
    print(f"PASS")
else:
    print(f"fail")