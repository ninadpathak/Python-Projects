from math import sqrt


def calc(a, b):
    return sqrt(a + b)


def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(calc(a, b))


main()