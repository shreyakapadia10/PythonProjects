"""
Problem Statement:-
A palindrome is a string that, when reversed, is equal to itself. Example of the palindrome includes:
676, 616, mom, 100001.
You have to take a number as an input from the user.
You have to find the next palindrome corresponding to that number.
Your first input should be the number of test cases and then take all the cases as input from the user.
Input:
3
451
10
2133

Output:
Next palindrome for 451 is 454
Next palindrome for 10 is 11
Next palindrome for 2311 is 2222
"""


def next_palindrome(nm):
    # Incrementing number until next palindrome number is found
    nm += 1
    while not is_palindrome(nm):
        nm += 1
    return nm


def is_palindrome(nm):
    # Reversing number and checking whether the number is palindrome or not
    return str(nm) == str(nm)[::-1]


if __name__ == '__main__':
    # Taking number of test cases
    n = int(input("Enter Number of Test Cases: "))

    # Taking n user inputs
    num = []
    for i in range(1, n + 1):
        num.append(int(input(f"Enter Test Case {i}: ")))

    # Printing next palindromes for each given number
    for number in num:
        print(f"Next Palindrome for {number} is {next_palindrome(number)}")