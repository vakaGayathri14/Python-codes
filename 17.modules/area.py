def circle(radius: float) -> None:
    area = 3.14 * radius * radius
    print(f"Area of circle with radius {radius} = {area}")


def rectangle(length: float, breadth: float) -> None:
    area = length * breadth
    print(f"area of rectange = {area}")


def triangle(base: float, height: float) -> None:
    area = 0.5 * base * height
    print(f"area of triangle = {area}")


# annotation for a variable
# x: int = 5
# name: str = "Honey"

# even though i haven't called the functions in the area file those function calls are executing automatically when i run this file  inorder to overcome that we have a concept of main
# if add name is main in the file then these won't be executed even if i run that other file only the below function calls will be executed if i run this file by default this file name will be main so
print(__name__)
if __name__ == "__main__":
    circle(56.996)
    rectangle(25,41)

# now if i want to calculate the area of circle, rectangle, triangle again in some where in code generally what we think okay let's copy paste the code but no inorder to ivercome this we have a concept of modules