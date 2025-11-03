# # Q106. Remove all the even numbers from the list.

# # my_list = [1, 2, 3, 4, 5, 6]
# # new = []

# # for i in range(0, len(my_list)):
# #     if my_list[i] % 2 != 0:
# #         new.append(my_list[i])
# # print(new)

# my_list = [5, 10, 15, 25, 20, 15]
# res=[]
# for i in my_list:
#     if i%2!=0:
#         res.append(i)
# print(res)


a = [45, 66, 66, 66, 66, 78, 11, 11, 12, 12, 12]
print(len(a))
for i in range(len(a) - 1, -1, -1):
    if a[i] % 2 == 0:
        a.pop(i)
print(a)
