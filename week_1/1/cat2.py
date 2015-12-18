import sys


def main():
    file_number = 1

    for file in sys.argv[1:]:
        print("file{}:".format(file_number))
        with open(file) as data:
            print(data.read())

        print('\n')
        file_number += 1


if __name__ == '__main__':
    main()
