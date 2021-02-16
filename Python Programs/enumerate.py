# Enumerate simply returns index and it's value
# So it helps to iterate over list/tuples/dictionary items i.e for any sequence 

lst = ("Shreya", "Shivani", "Harshil", "Jyoti", "Dipak")
d = {"Shreya":1, "Shivani":2, "Harshil":3, "Jyoti":4, "Dipak":5}

for index, item in enumerate(lst):
    print(f'Index {index} value is {item}')

for key, value in enumerate(d):
    print(f'Key is {key} and value is {value}')