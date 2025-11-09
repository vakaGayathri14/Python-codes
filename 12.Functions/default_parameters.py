# default parameters: if i provide all the parameters values when calling a function that is perfectly fine

# But if didn't provide some of the values and those should not provide any error then we have to provide 0 in the parameters it is called default parameters those will be assigning as 0 if we didn't provide any numbers that is caled default parameters.


# In this case I do not want to specify science,english and hindi marks
def total_marks(physics, maths, science=0, english=0, hindi=0):
    print(f"your marks in physics = {physics}")
    print(f"your marks in maths = {maths}")
    print(f"your marks in science = {science}")
    print(f"your marks in english = {english}")
    print(f"your marks in hindi = {hindi}")
    total = physics + maths + science + english + hindi
    print(f"Your total marks = {total}")


total_marks(45, 67)


# now I do not want to specify any of the values then
def total_marks(physics=0, maths=0, science=0, english=0, hindi=0):
    print(f"your marks in physics = {physics}")
    print(f"your marks in maths = {maths}")
    print(f"your marks in science = {science}")
    print(f"your marks in english = {english}")
    print(f"your marks in hindi = {hindi}")
    total = physics + maths + science + english + hindi
    print(f"Your total marks = {total}")


total_marks()

# for example if you need some parameters as required parameters then you have to do like below in the below example i want physics and maths as required and rest are default parameters


def total_marks(physics, maths, science=0, english=0, hindi=0):
    print(f"your marks in physics = {physics}")
    print(f"your marks in maths = {maths}")
    print(f"your marks in science = {science}")
    print(f"your marks in english = {english}")
    print(f"your marks in hindi = {hindi}")
    total = physics + maths + science + english + hindi
    print(f"Your total marks = {total}")


total_marks(56, 78)

# now here also same case as like of initialization all required parameters are in left side and also default parameters in right side and remember should not right default parameters in the left side like below
# will get an error

# def total_marks(physics=0, maths, science=0, english=0, hindi=0):
#     print(f"your marks in physics = {physics}")
#     print(f"your marks in maths = {maths}")
#     print(f"your marks in science = {science}")
#     print(f"your marks in english = {english}")
#     print(f"your marks in hindi = {hindi}")
#     total = physics + maths + science + english + hindi
#     print(f"Your total marks = {total}")


# total_marks(56, 78)


