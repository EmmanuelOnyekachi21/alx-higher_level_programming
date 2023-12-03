#!/usr/bin/python3

for n in range(97, 123):
    if chr(n) == 'e' or chr(n) == 'q':
        continue
    print("".join("{:s}".format(chr(n))), end='')
