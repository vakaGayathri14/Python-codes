"""
Q41. Write a program that calculates a person's BMI based on their height
(in meters) and weight (in kilograms). Use the following formula: BMI =
weight / (height^2). Then, classify the BMI according to the following
ranges:
QUESTIONS 38 - 41
NESTED IF - ELSE
info@codeanddebug.in Code and Debug codeanddebug.in
Underweight: BMI less than 18.5
Normal weight: BMI 18.5 - 24.9
Overweight: BMI 25 - 29.9
Obesity: BMI 30 or greater

"""

Weight = float(input("Enter your weight: "))
Height = float(input("Enter your Height: "))

BMI = Weight/(Height**2)

print(BMI)

if BMI>=0:
    if BMI>=18.5 and BMI<=24.9:
        print("Normal weight")
    elif BMI>=25 and BMI<=29.9:
        print("Overweight")
    if BMI<18.5:
        print("underweight")  
    else:
        print("Obesity")
else:
    print("Invalid")