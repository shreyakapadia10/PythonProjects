import random

# Will generate random number between given range
random_num = random.randint(1, 50)
print(random_num)

# Will generate random number between 0 to 1
random_random = random.random()
print(random_random)

# Will select random serial from given sequence
lst = ['Badi Door Se Aaye Hain', 'TMKOC', 'Anupama']
choice = random.choice(lst)
print(choice)