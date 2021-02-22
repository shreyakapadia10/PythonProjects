"""
Problem Statement:-
Take age or year of birth as an input from the user. Store the input in one variable.
Your program should detect whether the entered input is age or year of birth and
tell the user when they will turn 100 years old. (5 points).
Here are a few instructions that you must have to follow:
Do not use any type of modules like DateTime or date utils. (-5 points)
Users can optionally provide a year, and your program must tell their age in that particular year. (3points)
Your code should handle all sort of errors like: (2 points)
    You are not yet born
    You seem to be the oldest person alive
    You can also handle any other errors, if possible!
"""

user_ip = int(input("Enter your age or birth year: "))
current_year = int(input("Enter current year: "))

result = 0
birth_year = 0
age = 0

if len(str(user_ip)) >= 5:
    raise ValueError("Please provide valid input")

elif user_ip > current_year:
    raise ValueError("You're not yet born")

# If user give valid age
elif len(str(user_ip)) <= 3:
    age = user_ip

    birth_year = current_year - user_ip
    result = 100 + birth_year

# If user provides birth year
elif len(str(user_ip)) == 4:
    result = user_ip + 100
    age = current_year - user_ip
    birth_year = user_ip

if age >= 130:
    raise ValueError("You seem to be the oldest person alive!")

print(f"You'll of 100 years in {result}")

optional = input("Do you want to check your age in a given particular year? (Y/N): ")
optional = optional.lower()

if optional == 'y':
    year = int(input("Enter year: "))
    future_age = year - birth_year
    if year < current_year:
        print(f"Your age in {year} was {future_age}")
    elif year == current_year:
        print(f"Your age in {year} is {future_age}")
    else:
        print(f"Your age in {year} will be {future_age}")
else:
    exit(0)