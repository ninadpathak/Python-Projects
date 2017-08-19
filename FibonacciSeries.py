a, b = 0, 1


while b < 10:
    print(b)
    # temp = a
    # a = b
    # b = temp + b
    # Or we can use the shortcut where a temporary variable is not needed
    a, b = b, a + b