def total_marks(physics, maths, science, english, hindi):
    print(f"your marks in physics = {physics}")
    print(f"your marks in maths = {maths}")
    print(f"your marks in science = {science}")
    print(f"your marks in english = {english}")
    print(f"your marks in hindi = {hindi}")
    total = physics + maths + science + english + hindi
    print(f"Your total marks = {total}")


total_marks(56, 98, 79, 32, 83)

# In the above when you are calling the function you have to provide the arguments in the same order if you have 2 you can remember them and do it in order if you have more than 10 it will be difficult write so to overcome this we have a concept of named paramters

# named parameters: If you write the parameter name and assignvalue to it simple see the example below we just have to modify where we are calling the function

# total_marks(science=98, hindi=43, maths=89, physics=94, english=73)


# now if i want first 2 parameters to be in same order and rest should not be in the same order so give the numbers in same order after that you can do named parameters wise # here you can have this named parameters in right but in left side

total_marks(56, 98, hindi=85, science=98, english=23)

# here you can have this named parameters in right but in left side

# total_marks(english=23,56, 98, hindi=85, science=98) # error because of the named parameter is used in the left side
