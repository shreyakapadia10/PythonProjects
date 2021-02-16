# To take multiple no of arguments we can use *args
# *args will be unpacked to tuple
# We can use any name instead of args but it's a convention
# We can use any name instead of kwargs but it's a convention
# We can't write normal argument after *args or **kwargs

def print_names(normal_arg, *args, **kwargs):
    print(normal_arg)

    for name in args:
        print(name)

    for key, value in kwargs.items():
        print(f"{key} is a {value}")


if __name__ == '__main__':
    normal = "Use of *args: "

    # Though we use here lists/tuple it will be packed into Tuple and passed to *args
    names = ["Shreya", "Shivani","Harshil", "Jyoti", "Dipak"]
    print_names(normal, *names)

    # Dictionary can be passed to **kwargs
    normal = "\nUse of *args and **kwargs: "
    kw = {"Shreya": "Computer Engineer", "Shivani": "Data Analyst","Harshil": "CA"}
    print_names(normal, *names, **kw)