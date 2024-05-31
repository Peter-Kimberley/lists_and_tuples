current_choice = "-"
computer_parts = []
print(input("Please press enter to start: "))
while current_choice != "0":
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
    else:
        print("Please add items from the list below:")
        print("1: computer")
        print("2: monitor")
        print("3: mouse")
        print("4: keyboard")
        print("0 to finish")
current_choice = input()
