# python function to print even length words in a string.

"""
Input: "This is a Python program"

O/p:
Even-length words:

"This" → 4 letters

"is" → 2 letters

"Python" → 6 letters

"""
# normal way
x = "This is a Python program"
y = x.split()
print(y)
for i in y:
    if len(i) % 2 == 0:
        print(i)


def evenLengthWords(st):
    x = st.split()
    for i in x:
        if len(i) % 2 == 0:
            print(i)


evenLengthWords("This is a Python program")


def evenLengthWords(st):
    y = []
    x = st.split()
    for i in x:
        if len(i) % 2 == 0:
            y.append(i)
    return y


print(evenLengthWords("This is a Python program"))
