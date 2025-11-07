"""
Q146. Ask a string from user. Display the dictionary where each key is a
character and value is the frequency of that character that comes in that
string.

"""

st = input("Enter a string: ")

# method 1
my_dict = {}
for i in st:
    # z = st.count(i)
    my_dict[i] = st.count(i)
print(my_dict)

# method 2
st = input("Enter a string: ")
freq = {}

for i in st:
    if i in freq:
        freq[i] = freq[i] + 1
    else:
        freq[i] = 1
print(freq)
