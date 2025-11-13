# Lambda functions-> Anonymous functions


# normal way using functions
# def add_numbers(n1, n2, n3):
#     return n1 + n2 + n3


# print(add_numbers(10, 20, 30))

# write the above code using lambda functions
# lambda function is also called as one liner

y = lambda n1, n2, n3: n1 + n2 + n3 # here asa lambda is anonymous we have to store in a variable inorder to call that function some where and also  syntax is like lambda followed parameters followed by what needs to be reuturned here we don't need to specify the word return explicitly by default it returns
print(y(10, 20, 30))

