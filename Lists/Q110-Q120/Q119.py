# Q119. Write a program to split a given list into two halves

num_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
x = []
y = []

mid = len(num_list) // 2

print(mid)

for i in range(0, mid):
    x.append(num_list[i])
for j in range(mid, len(num_list)):
    y.append(num_list[j])
print(x)
print(y)
