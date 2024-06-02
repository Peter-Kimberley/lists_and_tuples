available_parts = ["computer", 
                   "monitor",
                   "mouse",
                   "keyboard",
                   "hdmi cable"
                   ]
# valid_chioces = [str(i) for i in range(1, len(available_parts) + 1)]
valid_choices = []
for i in range (1, len(available_parts) + 1):
       valid_choices.append(str(i))
print(valid_choices)
input("please press enter ")
current_choice = "-"
computer_parts = []

while current_choice != '0':
     if current_choice in valid_choices:
          index = int(current_choice ) - 1
          chosen_part = available_parts[index]
          if chosen_part in computer_parts:
               print("removing {}".format(current_choice))
               computer_parts.remove(chosen_part)
          else:
               print("adding {}".format(current_choice))
               computer_parts.append(chosen_part)
          print("You're current list contains: {} ".format(computer_parts))     
     else:
        print("Please add items from the list below:")
        for number,part in enumerate(available_parts):
              print("{0} : {1}".format(number + 1, part))
     current_choice = input()
print(computer_parts)
