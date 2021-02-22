"""Problem Statement:-
It's result day at school and not everyone is happy.
You decided to make your friends laugh by jumbling their names to come up with some funny names.

Your program should take the number of names and the names separated by space as input.
Output should be funny names in the same order.

Input:
Enter number of friends:
3
Enter the name of your 3 friends:
Rohan Das
Shubham Agarwal
Ritesh Arora

Output:
Ritesh Das
Shubham Arora
Rohan Agarwal"""
import random


def jumble_names():
    # If maxsplit is specified, the list will have the maximum of maxsplit+1 items.
    # Thus in case of lname, even if someone has specified middle name it'll be considered as a whole
    fname = [name.split()[0] for name in names]
    lname = [name.split(" ", 1)[1] for name in names]

    for _ in names:
        random_fname = random.choice(fname)
        random_lname = random.choice(lname)

        print(f"{random_fname} {random_lname}")

        fname.remove(random_fname)
        lname.remove(random_lname)


if __name__ == '__main__':
    n = int(input("Enter number of friends: "))
    names = []
    for i in range(n):
        names.append(input("Enter name of your friend: "))

    jumble_names()