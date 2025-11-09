"""
Q171. Write a function that accepts a string and prints the frequency of
each character in the string.

"""

# def freq_of_character(st):
#     for i in range(len(st)):
#         count = 0
#         if st[i] == count:
#             count = count + 1
#             print(f"{st[i]} -> {count}")


# freq_of_character("Hi Hello")


def charCount(st):  # hellloooprree
    my_dict = {}  # -> you can declare the dictionary like this or like below
    my_dict = dict()
    for ch in st:
        if ch not in my_dict:
            my_dict[ch] = 1
        else:
            my_dict[ch] += 1
    # print(my_dict)

    for k, v in my_dict.items():
        print(f"{k} occurs {v} times")


charCount("Hi Hello")
