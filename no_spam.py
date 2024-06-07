menu = [["eeg", "bacon"],
        ["egg", "sauasage", "bacon"],
        ["egg", "spam"],
        ["egg", "bacon", "spam"],
        ["egg", "bacon", "sausage", "spam"],
        ["spam", "bacon", "sausage", "spam"],
        ["spam", "egg", "spam", "spam", "bacon", "spam"],
        ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam" ]
]
# The challenge is to write all the meals in the menu but with spam,
# removed.
# remove spam from the list then print out the list?
# print out the items in the list as long as they are not spam?
# print(menu)

for meal in menu:
    for index in range(len(meal)-1, -1, -1):
        if meal[index] == "spam":
            del meal[index]
    print(", ".join(meal))



    