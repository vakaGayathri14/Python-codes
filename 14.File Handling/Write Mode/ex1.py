file_name = input("Enter a file name(without extension)= ")
file_name=file_name+".txt"

#now i want to open that file

with open(file_name,"w") as f:
    # x=input("Enter something")
    # f.write(x)
    while True:
        sentence =input("Enter a sentence = ")
        if sentence == "q" or sentence =="Q":
            break
        f.write(sentence)
        f.write("\n")

