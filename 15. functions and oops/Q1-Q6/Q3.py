"""
write a python function that takes a list and returns a new list with distinct elements from the first list.
sample list =[10,20,20,20,10,10,50]
Unique list = [10,20,50]

"""

# normal way
sample_list = [10, 20, 20, 20, 10, 10, 50]
new = set(sample_list)
print(list(new))


def removeDuplicates(x):
    new = set(x)
    return list(new)


print(removeDuplicates([10, 20, 20, 20, 10, 10, 50]))


# removing duplicates without using set


def removeDuplicates(x):
    Unique_list = []
    for i in x:
        if i not in Unique_list:
            Unique_list.append(i)
    return Unique_list


print(removeDuplicates([10, 20, 20, 20, 10, 10, 50]))
