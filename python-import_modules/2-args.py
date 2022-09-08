#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 1
    if (len(sys.argv) == 2):
        print("{} argument:".format(len(sys.argv) - 1))
    elif (len(sys.argv) > 2):
        print("{} arguments:".format(len(sys.argv) - 1))
    else:
        print("0 arguments.")
    while i != len(sys.argv):
        print("{}: {}".format(i, str(sys.argv[i])))
        i += 1
