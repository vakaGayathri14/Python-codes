x = input("Enter your name = ")
print(x)

name = input("Enter your name: ")
age = int(input("Enter your age: "))
gender = input("Enter your gender: ")
print(f"your name is {name}")
print(f"your age is {age}")
print(f"your gender is {gender}")

#practice

# Q4. Write a Python program to add two numbers entered by the user.
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

z= x+y
print(f"sum of first number {x} and second number {y} is {z}")

# Q5. Convert a string to an integer and vice versa.
x = "100"
print(x,type(x))

y = int(x)
print(y,type(y))

z = str(y)
print(z,type(z))

# Q6. Write a Python program to calculate the area of a rectangle using user input for length and width
length = int(input("Enter the length: "))
width = int(input("Enter the width: "))

area = length * width
print(f"Area of rectangle of length {length} and width {width} is {area}")

# Q7. Write a Python program to calculate the average of three numbers entered by the user
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
z = int(input("Enter the third number: "))

average = (x+y+z)/3
print(f"Average of {x}, {y}, {z} is {average}")

# Q8. Convert a float to an integer and vice versa

x=float(input("Enter a number"))
print(x,type(x))

y = int(x)
print(y,type(y))

z=float(y)
print(z,type(z))

# Q9. Write a program that converts a temperature in Fahrenheit to Celsius.The formula is: Celsius = (Fahrenheit - 32) * 5/9

Fahrenheit = float(input("Enter the temperature:"))
Celsius = (Fahrenheit - 32) * 5/9

print(Celsius)

# Q10. Calculate sum of 5 subjects and Find percentage.

subject_1 = int(input("Enter the first subject marks"))
subject_2 = int(input("Enter the second subject marks"))
subject_3 = int(input("Enter the third subject marks"))
subject_4 = int(input("Enter the fourth subject marks"))
subject_5 = int(input("Enter the fifth subject marks"))

sum_of_subjects = subject_1 + subject_2 + subject_3 + subject_4 + subject_5
print(sum_of_subjects)
percentage = (sum_of_subjects/500)*100

print(f"Percentage of the student is {percentage}")

# Q11. Ask number of games played in a tournament. Ask the user number of games won and number of games loss. Calculate number of tie and total Points. (1 win= 4 points, 1 tie =2 points)

no_of_games_played = int(input("Enter the number of games in tournament: "))
no_of_games_won = int(input("Enter the number of games you won in tournament: "))
no_of_games_loss = int(input("Enter the number of games you loss in tournament: "))
no_of_games_tie = no_of_games_played - (no_of_games_won + no_of_games_loss )
points = (no_of_games_won * 4) + (no_of_games_tie * 2)

print(f"{no_of_games_tie}, {points} ")






