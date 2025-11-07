"""
Q143. Convert two lists into a dictionary. Make two list on your own of
same length, and convert them to dictionary.
"""
lst1 = ['Ten', 'Twenty','Thirty']
lst2 = [10,20,30]

my_dict = {}

for i in range(len(lst1)):
    # my_dict[lst1[i]]=lst2[i]
    my_dict.update({lst1[i]:lst2[i]})
print(my_dict)