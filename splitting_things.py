# panagram = "The quick brown fox jumps over the lazy dog"

# # the split function is used to split strings
# words = panagram.split()
# print(words)

# numbers = "1,234,78,54,89,778,534"


# print(numbers.split(","))

# use a forloop to producde a list of int's rather than a list of
# strings.
# You can either modify the values of value_list in place 
# or create a new list of ints


numbers = "1,2,3,4,5,6,7,8,9"

values_list = numbers.split(",")
print(values_list)

# for item in values_list:
#     for value in item:
#         value = int(item)
    
#     print(value)
 
new_list = []
for place in values_list:
    new_list.append(int(place))
print(new_list)

