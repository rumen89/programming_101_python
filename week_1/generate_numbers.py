# Implement a Python script, called generate_numbers.py that takes two
# arguments - a filename and an integer n.
#
# The script should create a file with the filename and print n random integers
# separated by " ".

import sys
from random import randint


def main():
    filename = sys.argv[1]
    number = int(sys.argv[2])

    file = open(filename, 'w')

    for i in range(0, number):
        file.write(str(randint(1, 1000)) + " ")

    file.close()

if __name__ == '__main__':
    main()
