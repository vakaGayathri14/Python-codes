def add(x: int, y: int):
    total = x + y
    print(total)


add(10, 20)
add("10", "20")


def add(x: int, y: int):
    total = x + y
    return total


c = add(10, 20)
print(c)


# other way if you write -> int: then the output is also int just for display purpose
def add(x: int, y: int) -> int:  # [return is also integer]
    total = x + y
    return total


c = add(10, 20)
print(c)


def greet(name: str, age: int, percentage: float) -> None:
    print(name)
    print(age)
    print(percentage)


greet()

