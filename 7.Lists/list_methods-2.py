a = [55, 65, -95, "honey", True, 55.6, -95]

# pos= a.index(-95) #inorderto check the position of the number
# print(pos)

# a.sort() #by default ascending sort
# # print(a) # get an errorbecause this list has multiple data types
# a=[55,65,-95,55.6,-95]
# a.sort()

# a=["Honey","Anuradha","sailu","lasya","a","code and debug"],
# print(a)

# a.reverse()
# print(a)

# print values in desc order
a = [1, 2, 3, 45]
# a.sort()
# a.reverse()
# print(a)

# other method

# a.sort(reverse=True)
# print(a)


# a.append("honey")
# print(a)

# a.append(["honey","gayathri",100]) #here it will add like list in a list
# print(a)

# a.extend(["honey", "gayathri", 100])  # here these values will add to the existing list rather than creating another list like append
# print(a)

r = a.count(-95)
print(r)

a.clear()
print(a)
