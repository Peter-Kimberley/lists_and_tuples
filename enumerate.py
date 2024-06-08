# for index, character in enumerate("abcdefghijklmnopqrstwvxyz"):
#     print(index,character)

for t in enumerate("abcdefgh"):
    index,character = t
    print(index, character)

index,character = (0, 'a')
print(index)
print(character)

# This is the enumerate function that will give us the index and the
# name of a iterable item within a list.
