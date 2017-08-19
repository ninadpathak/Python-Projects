import time


def main():
    a = input("Enter something: ")
    enum(a)


def enum(a):
    for i in range(0, len(a)):
        print(a[i], end=' ')
        time.sleep(0.1)
    print()


main()