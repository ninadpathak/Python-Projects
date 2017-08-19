# we can create an iterative list by using for loop while defining the list

end = int(input("Enter an ending number: "))
list = [x for x in range(0, end + 1)]
squares = []
square_root = []
cube_root = []

print("\n\nSquares from 0 to ", end)
for i in list:
    print(i ** 2)
    squares.append(i ** 2)

print("\n\nSquare roots from 0 to ", end)
for i in list:
    print(i ** (1 / 2))
    square_root.append(i ** (1 / 2))

print("\n\nCube roots from 0 to ", end)
for i in list:
    print(i ** (1 / 3))
    cube_root.append(i ** (1 / 3))


print("\n\n", squares)
print("\n\n", square_root)
print("\n\n", cube_root)