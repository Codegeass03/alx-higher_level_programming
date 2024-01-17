#!/usr/bin/python3
for x in range(0, 10):
    for y in range(x + 1, 10):
        if y == 9 and x == 8:
            print('89')
        else:
            print('{}{}, '.format(x, y), end='')
