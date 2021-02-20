"""
    Serialization is a process of translating data structures or object state into a format
    that can be stored (for example, in a file or memory buffer) or transmitted and reconstructed later.

    In serialization, an object is transformed into a format that can be stored,
    so as to be able to deserialize it later and recreate the original object from the serialized format.

    1. Pickle, 2. JSON, 3. YAML  --> these can be used for serialization

    Pickle module can be used for preserving/storing any python object
"""

import pickle

# Pickling Process
# Storing file object as pickle
# wb mode to write python object in binary
lst = ['Shreya', 'Shivani', 'Harshil']

# the dump() method takes python object and a file object
with open('pickle_file.pkl', 'wb') as f:
    pickle.dump(lst, f)

# Unpickling Process
# Reading pickle object
# rb mode to read python object in binary
# the load() method takes a file object
with open('pickle_file.pkl', 'rb') as fp:
    new_lst = pickle.load(fp)
    print(new_lst)


# dumps() return the pickled representation of the object obj as a bytes object,
# instead of writing it to a file.

pickled_lst = pickle.dumps(lst)
print(f'Pickeled List: {pickled_lst}')

# loads() return the reconstituted object hierarchy of the pickled representation data of an object.
# data must be a bytes-like object.

unpickled_lst = pickle.loads(pickled_lst)
print(f'Unpickeled List: {unpickled_lst}')