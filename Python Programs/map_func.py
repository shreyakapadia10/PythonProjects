str_num_lst = ['2', '4', '6', '8', '5']

# Now suppose if we want to add 10 to any number than addition will generate error
# as the numbers are in str format

# Way 1 --> Less Efficient

for i in range(len(str_num_lst)):
    str_num_lst[i] = int(str_num_lst[i])

str_num_lst[2] = str_num_lst[2] + 10
print(str_num_lst[2])

# Way 2 --> More Efficient Way using map function
# Map function returns object thus we need to cast it to list type
# first we need to give name of function that we want to apply
# Second we need to give name of sequence on which we want to apply map function

str_num_lst = ['2', '4', '6', '8', '5']
num_lst = list(map(int, str_num_lst))
num_lst[2] += 10
print(num_lst[2])


'''Program 2'''


def square_no(a):
    return a*a


# Way 1
num_sq = list(map(square_no, num_lst))
print(f'Using simple function: {num_sq}')

# Way 2 Using Lambda function

num_sq_lambda = list(map(lambda n: n*n, num_lst))
print(f'Using lambda function: {num_sq_lambda}')


'''Program 3'''


def cube_no(n):
    return n*n*n


# Applying square and cube to numbers ranging from 0 to 5
func_lst = [square_no, cube_no]

for i in range(5):
    res = list(map(lambda x: x(i), func_lst))
    print(f'For {i}: {res}')