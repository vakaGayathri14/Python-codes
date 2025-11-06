"""
Q141. Write a program that converts a string in camelCase to snake_case.
For example, converting "helloWorldHowAreYou" should result in
"hello_world_how_are_you"

"""

my_str = input("Enter a string: ")
res = " "
for i in my_str:
    if i.isupper():
        res += "_" + i.lower()
    else:
        res += i
print(res)
