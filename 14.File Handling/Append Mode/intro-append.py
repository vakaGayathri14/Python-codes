# it is same as write mode but in write mode it overrides the previous one but in append it will add at the end
with open("appen.txt", "a") as f:
    f.write("A new Line\n")
    f.write("A new Line")
