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


def is_palindrome(nm):
    # Checking whether given number is palindrome or not
    temp_num = nm
    rev = 0
    while nm > 0:
        rem = nm % 10  # Taking last digit
        rev = rev * 10 + rem  # Multiplying reverse with 10 and adding remainder
        nm = nm // 10  # Integer modulo 10

    if temp_num == rev:
        return True
    else:
        return False


if __name__ == '__main__':
    # Taking number of test cases
    n = int(input("Enter Number of Test Cases: "))

    num = []
    # Taking n user inputs
    for i in range(1, n + 1):
        num.append(int(input(f"Enter Test Case {i}: ")))

    for number in num:
        foundPalindrome = False
        i = 1
        # Incrementing number until next palindrome number is found
        while not foundPalindrome:
            temp = number + i
            if is_palindrome(temp):
                print(f"Next Palindrome Number for {number} is {temp}")
                foundPalindrome = True
            else:
                i += 1
