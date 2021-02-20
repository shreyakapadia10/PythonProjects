import argparse
import sys


def calc(arg):
    if arg.op == "add":
        return arg.num1 + arg.num2
    elif arg.op == "sub":
        return arg.num1 - arg.num2
    elif arg.op == "mul":
        return arg.num1 * arg.num2
    elif arg.op == "div":
        return arg.num1 / arg.num2
    else:
        return "Something went wrong!"


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--num1", type=float, default=1.0, help="Enter Number 1")
    parser.add_argument("--num2", type=float, default=2.0, help="Enter Number 2")
    parser.add_argument("--op", type=str, default="add", help="Enter Operation")

    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))