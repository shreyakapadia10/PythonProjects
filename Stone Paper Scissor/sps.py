import random

lst = ['s', 'p', 'sc']

i = 1
win_counter = 0
result = ""
while i < 10:
    print("Press 's' for Stone, 'p' for Paper and 'sc' for Scissor")
    computer_choice = random.choice(lst)
    choice = input("Enter your choice: ")
    print(f'Computer\'s choice: {computer_choice}')

    # If Stone
    if choice == computer_choice:
        result = "Tie"

    elif choice == 's' and computer_choice == 'p':
        result = "You Lost!"

    elif choice == 's' and computer_choice == 'sc':
        result = "You Won!"
        win_counter += 1

    # If Paper
    elif choice == 'p' and computer_choice == 'sc':
        result = "You Lost!"

    elif choice == 'p' and computer_choice == 's':
        result = "You Won!"
        win_counter += 1

    # If Scissor
    elif choice == 'sc' and computer_choice == 's':
        result = "You Lost!"

    elif choice == 'sc' and computer_choice == 'p':
        result = "You Won!"
        win_counter += 1

    print(result)
    i += 1

print(f'You won {win_counter} times!')