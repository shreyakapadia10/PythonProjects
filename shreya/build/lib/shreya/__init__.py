import random


class StonePaperScissors:

    def __init__(self):
        self.lst = ['s', 'p', 'sc']
        self.win_counter = 0
        self.compute_win_counter = 0
        self.ties = 0
        self.result = ""

    def play_game(self):
        i = 1
        while i < 10:
            print("Press 's' for Stone, 'p' for Paper and 'sc' for Scissor")
            computer_choice = random.choice(self.lst)
            choice = input("Enter your choice: ")
            print(f'Computer\'s choice: {computer_choice}')

            # If Stone
            if choice == computer_choice:
                self.result = "Tie"
                self.ties += 1

            elif choice == 's' and computer_choice == 'p':
                self.result = "You Lost!"
                self.compute_win_counter += 1

            elif choice == 's' and computer_choice == 'sc':
                self.result = "You Won!"
                self.win_counter += 1

            # If Paper
            elif choice == 'p' and computer_choice == 'sc':
                self.result = "You Lost!"
                self.compute_win_counter += 1

            elif choice == 'p' and computer_choice == 's':
                self.result = "You Won!"
                self.win_counter += 1

            # If Scissor
            elif choice == 'sc' and computer_choice == 's':
                self.result = "You Lost!"
                self.compute_win_counter += 1

            elif choice == 'sc' and computer_choice == 'p':
                self.result = "You Won!"
                self.win_counter += 1

            print(self.result)
            i += 1

        print(f'You won {self.win_counter} times. Computer won {self.compute_win_counter} times. Total ties: {self.ties}!')
