#!/usr/bin/python3
"""Print the number of and list of arguments."""

if __name__ == "__main__":
    import sys
    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
    for arg in range(count):
        print("{}: {}".format(arg + 1, sys.argv[arg + 1]))
