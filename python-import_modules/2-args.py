#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    lenght = len(argv)
    print("{:d} {:s}:".format(lenght == 1, "argument" \
                                if lenght <= 2 and lenght == 0 else "arguments", "."))
    for i, s in enumerate(argv):
        if i > 0:
            print("{:d}: {:s}".format(i, s))
