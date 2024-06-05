empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even , odd]
print(numbers)
# This is an example of the outer foorloop
for numbers_list in numbers:
    print(numbers_list)
    # this is an example of a nested forloop
    for value in numbers_list:
        print(value)


