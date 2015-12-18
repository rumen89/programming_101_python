# Implement a Python script, called sum_numbers.py that takes one argument - a
# filename which has integers, separated by " ".
#
# The script should print the sum of all integers in that file.

import sys


def sum_numbers(string):
    result = 0
    number = '0'

    for char in string:
        if '0' <= char <= '9':
            number += char
        else:
            result += int(number)
            number = '0'

    return result


def main():
    filename = sys.argv[1]

    with open(filename) as file:
        file_to_string = file.read()

    return sum_numbers(file_to_string)


if __name__ == '__main__':
    print(main())
