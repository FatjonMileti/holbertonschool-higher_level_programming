#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 1
    s = 0
    while i != len(sys.argv):
        s += int(sys.argv[i])
        i += 1
    print("{}".format(s))
