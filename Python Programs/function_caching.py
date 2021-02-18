"""
    Sometimes we need to call one same function again and again and it takes some time to execute it
    Now if we want that we don't need to wait for that particular time,
    we can use lru_cache which will store the given number of maximum size of cache
"""

import time
from functools import lru_cache

choice = int(input('Enter the cache size: '))


@lru_cache(maxsize=choice)
def some_work(n):
    time.sleep(n)
    return n


if __name__ == '__main__':
    print('Doing work..')
    some_work(3)
    print('Done... Calling again')
    some_work(3)
    print('Done... Calling again')
    some_work(3)
    print('Done... Calling again')
    some_work(3)
    print('Done... Calling again')
    some_work(3)
    print('Called again')
