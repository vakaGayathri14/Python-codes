"""
Q50. Calculate how many numbers are divisible by 6 and 7 between 1 to
200.
"""

i = 1
res = 0
while i<=200:
    if i%6==0 & i%7==0:
        res = res+1
    i+=1
print(res)

