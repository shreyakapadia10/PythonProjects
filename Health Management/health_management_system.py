def getdate():
    import datetime
    return datetime.datetime.now()


def getdetails(fname):
    with open(fname) as f:
        contents = f.read()
        print(contents)


def writedetails():
    if name == 1:
        if food_exercise == 1:
            food = input("Enter Food Details: ")
            with open("shreya_food.txt", "a") as f:
                f.write("[" + str(getdate()) + "] " + food + "\n")

        elif food_exercise == 2:
            exercise = input("Enter Exercise Details: ")
            with open("shreya_exercise.txt", "a") as f:
                f.write("[" + str(getdate()) + "] " + exercise + "\n")

    elif name == 2:
        if food_exercise == 1:
            food = input("Enter Food Details: ")
            with open("shivani_food.txt", "a") as f:
                f.write("[" + str(getdate()) + "] " + food + "\n")

        elif food_exercise == 2:
            exercise = input("Enter Exercise Details: ")
            with open("shivani_exercise.txt", "a") as f:
                f.write("[" + str(getdate()) + "] " + exercise + "\n")

    else:
        if food_exercise == 1:
            food = input("Enter Food Details: ")
            with open("harshil_food.txt", "a") as f:
                f.write("[" + str(getdate()) + "] " + food + "\n")

        elif food_exercise == 2:
            exercise = input("Enter Exercise Details: ")
            with open("harshil_exercise.txt", "a") as f:
                f.write("[" + str(getdate()) + "] " + exercise + "\n")

    print("Successfully Written!")


print("1. Read Data \n2. Enter Data")
choice = int(input("Enter your choice: "))

print("1. Shreya \n2. Shivani \n3. Harshil")
name = int(input("Enter your choice: "))

print("1. Food Details \n2. Diet Details")
food_exercise = int(input("Enter your choice: "))


if choice == 1:
    if name == 1:
        if food_exercise == 1:
            getdetails("shreya_food.txt")
        else:
            getdetails("shreya_exercise.txt")

    elif name == 2:
        if food_exercise == 1:
            getdetails("shivani_food.txt")
        else:
            getdetails("shivani_exercise.txt")
    else:
        if food_exercise == 1:
            getdetails("harshil_food.txt")
        else:
            getdetails("harshil_exercise.txt")

else:
    writedetails()
