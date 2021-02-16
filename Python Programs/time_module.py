import time

initial = time.time()
i = 0
while i < 100:
    print(i)
    i += 1

diff1 = time.time() - initial
initial2 = time.time()

for i in range(100):
    print(i)

diff2 = time.time() - initial2
print(f'While loop took {diff1} seconds')

print('Going for sleep of 2 seconds...')
time.sleep(2)

print(f'For loop took {diff2} seconds')

# time.localtime returns localtime but not in much convenient way so
# we'll use time.asctime() which presents time in convenient way

localtime = time.asctime(time.localtime(time.time()))
print(f'localtime: {localtime}')