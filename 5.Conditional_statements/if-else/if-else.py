"""
Ask age from user
you can vote if 18 above
"""

age = int(input("Enter your age: "))

if(age >= 18):
    print(f"You can vote")
    print("You are allowed to vote")
else:
    print(f"You cannot vote")

print("okay done")