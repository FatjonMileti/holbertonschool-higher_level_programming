#!/usr/bin/python3
import sys
i = 1
sum_arg = 0
while i != len(sys.argv):
    if sys.argv[i].isnumeric():
        sum_arg += int(sys.argv[i])
    i += 1
print("{}".format(sum_arg))
