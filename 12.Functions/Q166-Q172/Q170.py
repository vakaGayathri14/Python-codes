"""
Q170. Write a function that takes a list of numbers and prints the sum and
average of these numbers.

"""


def sum_avg_list(lst):
    total = 0
    for num in lst:
        total = total + num

    avg = total / len(lst)
    print(f"total of all numbers = {total}")
    print(f"average of all numbers = {avg}")


sum_avg_list([1, 2, 3, 4, 5])
