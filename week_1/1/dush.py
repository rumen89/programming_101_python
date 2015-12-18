import os
import sys

def main():
    path = sys.argv[1]

    try:
        path_size = os.path.getsize(path)
    except FileNotFoundError as error:
        print(error)

    return path_size


if __name__ == '__main__':
    print(main())
