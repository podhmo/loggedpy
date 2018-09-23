import sys


def main():
    for fpath in sys.argv[1:]:
        with open(fpath) as rf:
            for line in rf:
                print(line.rstrip())
