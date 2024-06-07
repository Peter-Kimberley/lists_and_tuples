menu = [["eeg", "bacon"],
        ["egg", "sauasage", "bacon"],
        ["egg", "spam"],
        ["egg", "bacon", "spam"],
        ["egg", "bacon", "sausage", "spam"],
        ["spam", "bacon", "sausage", "spam"],
        ["spam", "egg", "spam", "spam" "bacon", "spam"],
        ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam" ]
]

for meal in menu:
    if "spam" not in meal:
        print(meal)
        # another example of a nested forloop
        for item in meal:
            print(item)
    else:
        print("{0} has spam count {1}"
              # Making use of the count method for the expression meal
              .format(meal,meal.count("spam")))
# The menu contains alot of spam, this was based of the famous
# Monty Python sketch.


        
