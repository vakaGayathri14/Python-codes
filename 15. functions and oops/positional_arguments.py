def total_marks(maths, science, english, hindi, history):
    total = maths + science + english + hindi + history
    print(total)


# here i have to give arguments in the same order of parameter inorder to overcome this we have a concept of positional argumenrs
total_marks(89, 74, 84, 11, 23)

# named argument
total_marks(english=100, history=88, science=11, maths=88, hindi=66)
