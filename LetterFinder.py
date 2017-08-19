def FindLetter(inp, letter):
    a = 0
    while a != len(inp):
        character = inp[a]
        if character == letter:
            flag = 1
            break
        else:
            flag = 0
        a += 1
    if flag == 1:
        return "The word '" + inp + "' contains '" + letter + "'"
    else:
        return "The word '" + inp + "' does not contain '" + letter + "'"


def main():
    a = input("Enter a random string: ")
    b = input("Enter a letter you'd like to find: ")
    print(FindLetter(a, b))


main()
