#!/usr/bin/python3
for i in range(0, 8):
    for j in range(0, 9):
        if (j > i) and (i != 8) and (j != 9):
            print("{0}{1}, ".format(i, j), end="")
print("89")
