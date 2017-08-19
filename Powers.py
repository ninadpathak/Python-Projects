from math import log


def main():
    num = int(input("Enter a number to end: "))
    for i in range(1, num):
        print(i)
        print(log(i))
        print(i * log(i))
        print(i ** 2)
        print(2 ** i)
        print("*" * 10)


main()
