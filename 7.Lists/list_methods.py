# mutable/immutable data type
"""
mutable-which can change [list is mutable]
immutable- which cannot change

"""

a = [54, 23, 10, 99, -90]
print(a)

a.append(100)  # it will add at the end
a.append(-100)
print(a)

a.insert(
    3, "python"
)  # where to add, what needs to be added, which value to be added- here it will add in 3rd position of string python
print(a)

a.insert(400, "python")  # if we don't have that index then it will add at the end
print(a)

a[0] = 100  # update
print(a)

a[-1] = 100  # update
print(a)

a[50] = 100  # update error as we don't have that index
print(a)

a.pop(2)  # remove by index
print(a)

a.pop(50)
print(a)

a.remove(99)  # it  remove by value
print(a)

# for example you have 2,99's in the list then first 99 will remove

del a[0]  # delete by index
print(a)

del a
print(a)

a.clear()  # it clears all the values in the list
print(a)


print(len(a))
print(sum(a))
print(max(a))
print(min(a))
print()
# id
# range
