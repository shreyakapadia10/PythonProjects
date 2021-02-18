# We can use else with for loop will be executed when for loop executes properly,
# if there is a break then the statements in else part won't be executed if for loop
# is executed properly

names = ['shreya', 'shivani', 'harshil']

for name in names:
    print(name)
else:
    print('For loop executed properly')

# Use of for..else

for name in names:
    if 'Jyoti' in names:
        print('Found it!')
        break

else:
    print("Didn't find it")

