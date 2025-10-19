"""
Operators are used to perform operations on variables and values

Different types of Operators:
1. Arithmetic operators
2. Assignment operators
3. Comparison operators
4. Logical operators
5. Identity operators
6. Membership operators
7. Bitwise operators

"""

"""
1. Arithmetic operators: Airthmetical operators are used with numeric values to perform common mathematical operations.
Operator    Name          Example
+          Addition         x+y
-          Subtraction      x-y
*          Multiplication   x*y
/           Divison         x/y -> you will get this answer always in float
%           Modulus         x%y ->remainder EX:- 5%3=2, 5%10 = 5 
**         Exponentiation   x**y -> power EX:- 5^3 = 5*5*5 -> 5**3 = 125,7**9
//         Floor division   x//y ->10/4 =2.5 -> 10//4 =2 (quotient), 13/7 = 1.8571, 13//7 = 1 [here it is going to lower integer rather than round off], -10/4= -2.5, -10//4 = -3 (you will get this answer always in int)


"""

a=10
b=4

print("addition", a+b)
print("Subtraction", a-b)
print("multiplication", a*b)
print("division", a/b)
print("modulus",a%b)
print("Exponentiation",a**2)
print("Floor division",a//b)


