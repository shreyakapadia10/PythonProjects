"""Problem Statement:-
You are given a list that contains some numbers.
You have to print a list of next palindromes only if the number is greater than 10;
otherwise, you will print that number.

Input:
[1, 6, 87, 43]

Output:
[1, 6, 88, 44]"""


def is_palindrome(number_ip):
    return str(number_ip) == str(number_ip)[::-1]


def next_palindrome(nm):
    if nm >= 10:
        nm += 1
        while not is_palindrome(nm):
            nm += 1
        return nm
    return nm


if __name__ == '__main__':
    n = int(input("Enter Number of Test Cases: "))

    num = []
    for i in range(1, n + 1):
        num.append(int(input(f"Enter Test Case {i}: ")))

    for number in num:
        print(f"Next Palindrome for {number} is {next_palindrome(number)}")