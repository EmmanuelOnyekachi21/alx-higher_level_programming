#!/usr/bin/python3

import sys

i = 1
length = len(sys.argv)
length -= 1

if length == 0:
    print(f"{length:d} arguments.")

elif length == 1:
    print(f"{length:d} argument:", end='\n')
    print("{}: {}".format(1, sys.argv[1]))
elif length > 1:
        print("{} arguments:".format(length), end='\n')

        for i in range(1, length + 1):
            print("{}: {}".format(i, sys.argv[i]), end='\n')
