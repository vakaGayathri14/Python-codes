"""
Q48. Calculate how many numbers are divisible by both 6 and 7 between 1
to 200.
"""

i = 1
total_count = 0
while i<=200:
    if i%6==0 & i%7==0:
        total_count = total_count+1
    i+=1
print(total_count)