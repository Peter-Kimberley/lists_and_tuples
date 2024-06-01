available_parts = ["computer", 
                   "monitor",
                   "mouse",
                   "keyboard",
                   "hdmi cable"]
current_choice = "-"
computer_parts = []

while current_choice != '0':
     if current_choice in "12345":
          print("adding {}".format(current_choice))
          if current_choice == '1':
                  computer_parts.append("computer")
          elif current_choice == '2':
                  computer_parts.append("monitor")
          elif current_choice == '3':
                  computer_parts.append("mouse")
          elif current_choice == '4':
                  computer_parts.append("keyboard")
          elif current_choice == '5':
                 computer_parts.append("hdmi cable")
     else:
          print("Please add items from the list below:")
          for part in available_parts:
               print("{0} : {1}".format(available_parts.index(part) + 1, part))
     current_choice = input()
