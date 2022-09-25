#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    lenght = len(argv)
    print("{:d} {:s}{:s}".format(lenght - 1, "argument" if lenght <= 2 else "arguments",
                                "." if lenght == 1 else ":"))
    for i, s in enumerate(argv):
        if i > 0:
            print("{:d}: {:s}".format(i, s))