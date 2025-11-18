# import area

# area.circle(56.874)
# area.rectangle(10, 20)


# # method 2
# # here i only want rectangle then

# from area import rectangle

# rectangle(2.5, 2.5)

# # method 3
# # here if i want circle also along with rectangle then


# from area import rectangle, circle

# rectangle(2.5, 2.5)
# circle(2)

# # method 4
# # now if you want triangle also along with circle and rectangle then

# from area import rectangle, circle, triangle

# rectangle(2.5, 2.5)
# circle(2)
# triangle(1.3, 4.5)

# # method 5
# # now if there are 10 functions it's difficult to write each name so rather you can call all functions ata a time using *

# from area import *

# rectangle(2.5, 2.5)
# circle(2)
# triangle(1.3, 4.5)

# # among all which is more preferrable that is
# # import area


from area import *

print("Hello")

# even though i haven't called the functions in the area file those function calls are executing automatically when i run this file  inorder to overcome that we have a concept of main
# if add name is main in the file then these won't be executed even if i run that other file only the below function calls will be executed if i run this file by default this file name will be main so
# i have added name in area file
