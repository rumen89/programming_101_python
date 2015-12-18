# Given an integer, implement a function, called sum_of_digits(n) that
# calculates the sum of n's digits.

# If a negative number is given, our function should work as if it was
# positive.


def to_digits(number):
    result = []

    if number < 0:
        number *= -1

    while (number > 0):
        digit = number % 10

        result = [digit] + result

        number = number // 10

    return result


def sum_of_digits(n):
    result = 0

    for number in to_digits(n):
        result += number

    return result


def to_number(digits):
    result = 0

    i = 0

    while i < len(digits):
        result = result * 10 + digits[i]

        i += 1

    return result


def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)


def fact_digits(n):
    result = 0

    for number in to_digits(n):
        result += factorial(number)

    return result


def fibonacci(n):
    fib = [1, 1]

    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]

    for i in range(2, n):
        fib += [fib[i - 1] + fib[i - 2]]

    return fib


def fib_number(n):
    fibonacci_number = 0

    for fib_number in fibonacci(n):
        fibonacci_number = fibonacci_number * 10 + fib_number

    return fibonacci_number


def palindrome(n):
    reversed_string = ""

    for i in range(0, len(str(n))):
        reversed_string = str(n)[i] + reversed_string

    if reversed_string == str(n):
        return True

    return False


def count_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']

    counter = 0

    for i in range(0, len(str)):
        if str[i] in vowels:
            counter += 1

    return counter


def count_consonants(str):
    consonants = "bcdfghjklmnpqrstvwxz"

    upper_consonants = "BCDFGHJKLMNPQRSTVWXZ"
    counter = 0

    for i in range(0, len(str)):
        if str[i] in consonants or str[i] in upper_consonants:
            counter += 1

    return counter


def char_chistogram(string):
    dict = {}

    for index in range(0, len(string)):
        if string[index] in dict:
            dict[string[index]] += 1
        else:
            dict[string[index]] = 1

    return dict


if __name__ == "__main__":
    print(to_digits(123))
    print(sum_of_digits(-10))
    print(to_number(to_digits(123)))
    print(factorial(5))
    print(fact_digits(999))
    print(fibonacci(3))
    print(fib_number(3))
    print(palindrome('kapa'))
    print(count_vowels("grrrrrrh"))
    print(count_consonants("Python"))
    print(char_chistogram("Python!"))
