"""
Ask 5 marks from user calculate percentage and print it

if that percentage is in 
91-100 -> A grade
81-90 -> B grade
71-80 -> C grade
61-70 -> D grade
1-60 -> Fail
"""

sub1 = float(input("Enter the marks: "))
sub2 = float(input("Enter the marks: "))
sub3 = float(input("Enter the marks: "))
sub4 = float(input("Enter the marks: "))
sub5 = float(input("Enter the marks: "))

total = sub1+sub2+sub3+sub4+sub5

percentage = (total/500)*100

print(f"percentage of the user is {percentage:.2f} %")

if (percentage>=91 and percentage<=100):
    print(f" A grade")
elif (percentage>=81 and percentage<=90):
    print(f" B grade")
elif (percentage>=71 and percentage<=80):
    print(f" C grade")
elif (percentage>=61 and percentage<=70):
    print(f" D grade")
elif (percentage>=1 and percentage<=60):
    print(f" FAIL")
else:
    print(f"INVALID")

             
