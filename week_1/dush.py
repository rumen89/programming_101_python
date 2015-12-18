import os
import sys


def walk(dir):

<<<<<<< HEAD
    total_size = 0
=======
    total_size = os.path.getsize(dir)
>>>>>>> 214d83c807c734f327b70cb62f8738212001d7b7

    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
<<<<<<< HEAD
            print(path + "   {}".format(os.path.getsize(path)))
            total_size += os.path.getsize(path)
        else:
            walk(path)
=======
            # print(path + "   {}".format(os.path.getsize(path)))
            total_size += os.path.getsize(path)
        else:
            total_size += walk(path)
>>>>>>> 214d83c807c734f327b70cb62f8738212001d7b7

    return total_size


def main():
    dir = sys.argv[1]

<<<<<<< HEAD
    return walk(dir)
=======
    return str((walk(dir) / 1024) / 1024) + 'MB'
>>>>>>> 214d83c807c734f327b70cb62f8738212001d7b7

if __name__ == '__main__':
    print(main())
