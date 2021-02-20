import requests
import pickle

# Downloading iris.data
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
response = requests.get(url)
with open('iris_data.txt', 'w') as fp:
    fp.write(response.text)

with open('iris_data.txt') as fp:
    contents = fp.read()
    contents = contents.split('\n')
    iris_lst = [[con] for con in contents if len(con) != 0]

# print(iris_lst)

# Pickling iris_lst into 'iris_pickle.pkl'
with open('iris_pickle.pkl', 'wb') as fp:
    pickle.dump(iris_lst, fp)
    print("Successfully Pickled!")

# Unpickling from 'iris_pickle.pkl'
with open('iris_pickle.pkl', 'rb') as fp:
    iris_unpickled = pickle.load(fp)
    print("Successfully Unpickled!")

print(iris_unpickled)
