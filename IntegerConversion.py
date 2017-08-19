def main():
    num = int(input("Enter a number: "))
    for i in range(1, num):
        print("Binary: \t", bin(i))
        print("Hexadecimal: \t", hex(i))


main()
