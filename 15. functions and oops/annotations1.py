def sum_of_list(x):
    print(sum(x))


sum_of_list([1, 2, 3, 4])
sum_of_list([100, 200])

# in the above when i hover on sum_of_list I can able to see x as any like not specified which data type I have to pass
# for that i will use module called typing

from typing import *


# here i can see I want list in that variable
def sum_of_list(x: List):
    print(sum(x))


sum_of_list([1, 2, 3, 4, "Honey"])
sum_of_list([100, 200])


# in the above case also not specified what is the data type inside the list for that
def sum_of_list(x: List[int]):
    print(sum(x))


sum_of_list([1, 2, 3, 4])
sum_of_list([100, 200])
