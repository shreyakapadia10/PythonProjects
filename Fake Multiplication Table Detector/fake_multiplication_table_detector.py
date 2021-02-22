"""
Python Practice problem 8 (Easy, 10 points)
Rohan Das Is A Fraud
Rohan das is a fraud by nature.
Rohan Das wrote a python function to print a multiplication table of a given number
and put one of the values (randomly generated) as wrong.
Rohan Das did this to fool his classmates and make them commit a mistake in a test.
You cannot tolerate this!
So you decided to use your python skills to counter Rohan’s actions by writing a python program
that validates Rohan’s multiplication table.
Your function should be able to find out the wrong values in Rohan’s table and expose Rohan Das as a fraud.
Note: Rohan’s function returns a list of numbers like this
Rohan Das’s Function Input:
rohanMultiplication(6)
Rohan’s function returns this output:
[6, 12, 18, 26, …., 60]
You have to write a function isCorrect(table, number) and
return the index where rohan’s function is wrong and print it to the screen!
If the table is correct, your function returns None.
"""
import random


def rohanMultiplication(num):
    random_num = random.randint(0, 10)
    # Same as commented code
    # table = [i * num if i != random_num else i*num+random_num for i in range(1, 11)]

    # table = []
    # for i in range(1, 11):
    #     if i == random_num:
    #         table.append(i * num + random_num)
    #     else:
    #         table.append(i * num)
    return [i * num if i != random_num else i*num+random_num for i in range(1, 11)]


def isCorrect(table, num):
    # Checking whether the multiplication table is right or not
    for i in range(1, 11):
        # If the particular index of table and the actual value of multiplication table
        # that it should be not matching than returning the index
        # Also returning correct multiplication table
        if table[i-1] != i*num:
            return i-1, [i*num for i in range(1, 11)]
    # If multiplication table is correct than returning None
    return None


if __name__ == '__main__':
    n = int(input("Enter any number: "))
    mul_table = rohanMultiplication(n)
    getResult = isCorrect(mul_table, n)
    print(f"Rohan's Table: {mul_table}")

    if getResult is None:
        print(f"The multiplication table is correct")
    else:
        print(f"There is an error at index {getResult[0]}.\nThe correct table is {getResult[1]}")
