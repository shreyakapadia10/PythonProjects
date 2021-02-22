"""
Problem Statement:-
Generate a random integer from a to b.
You and your friend have to guess a number between two numbers a and b.
a and b are inputs taken from the user. Your friend is player 1 and plays first.
He will have to keep choosing the number and your program must tell
whether the number is greater than the actual number or less than the actual number.
Log the number of trials it took your friend to arrive at the number.
You play the same game and then the person with minimum number of trials wins!
Randomly generate a number after taking a and b as input and don’t show that to the user.
Input:
Enter the value of a
4
Enter the value of b
13

Output:
Player1 :
Please guess the number between 4 and 13
5
Wrong guess a greater number again
8
Wrong guess a smaller number again
6
Correct you took 3 trials to guess the number
Player 2:
Correct you took 7 trials to guess the number
Player 1 wins!
"""
import random


class GuessTheNumber:
    def __init__(self, n1, n2, p_name):
        # Setting trials for a player
        self.trial = 0
        # Generating random number
        self.n = random.randint(n1, n2)
        # Setting player name
        self.player_name = p_name

    def check_number(self):
        print(f'{self.player_name}: ')
        number = int(input("Guess The Number: "))
        # Taking user input till the user guesses the right number
        while number != self.n:
            if number < self.n:
                print(f"Wrong! Guess a  greater number")
                self.trial += 1
            elif number > self.n:
                print(f"Wrong! Guess a  lesser number")
                self.trial += 1
            else:
                print(f"Invalid Input")
            number = int(input("Guess The Number: "))
        print(f"Correct you took {self.trial} trials to guess the number")

    def __gt__(self, other):
        # Comparing trials of two players
        if self.trial > other.trial:
            return f'{self.player_name} wins!'
        elif self.trial < other.trial:
            return f'{self.player_name} wins!'
        else:
            return f"It's a tie!"


if __name__ == '__main__':

    name = input("Enter Your Name: ")
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))

    player1 = GuessTheNumber(a, b, name)
    player1.check_number()

    name = input("Enter Your Name: ")
    player2 = GuessTheNumber(a, b, name)
    player2.check_number()

    print(player1 > player2)