def average(numbers):
    return sum(numbers) / len(numbers)

def average_of_squares(numbers):
    return sum(x ** 2 for x in numbers) / len(numbers)

def average_of_cubes(numbers):
    return sum(x ** 3 for x in numbers) / len(numbers)

print(average([1, 2, 3, 4, 5]))
print(average_of_squares([1, 2, 3, 4, 5]))
print(average_of_cubes([1, 2, 3, 4, 5]))


def greet(name):
    print(f"hello, {name}")