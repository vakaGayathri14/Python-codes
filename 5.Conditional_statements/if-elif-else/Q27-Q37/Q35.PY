"""
Q35. Take Salary as input from User and Update the salary of an employee

salary less than 10,000, 5 % increment
salary between 10,000 and 20, 000, 10 % increment
salary between 20,000 and 50,000, 15 % increment
salary more than 50,000, 20 % increment.

"""

salary = int(input("Enter your salary"))

if (salary<10000):
    print(f"Updated salary with 5% increment is: {salary + (salary*(5/100))}")
elif (salary>=10000 and salary<20000):
    print(f"Updated salary with 10% increment is: {salary + (salary*(10/100))}")
elif (salary>=20000 and salary<50000):
    print(f"Updated salary with 15% increment is: {salary + (salary*(15/100))}")
elif (salary>=50000):
    print(f"Updated salary with 20% increment is: {salary + (salary*(20/100))}")
else:
    print(f" enter the valid details")
