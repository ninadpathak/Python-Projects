def SimpleInterest(p, t, r):
    print(p * (1 + r * t))


def CompoundInterest(p, t, r):
    n = int(input("Enter the compounding frequency: "))
    print(p * (1 + (r / n)) ** (n * t))


def main():
    principal = int(input("Enter the invested amount: "))
    time = int(input("Enter then period for this investment: "))
    interest = float(input("Enter the rate of interest: "))
    type = input("Enter the type of interest (S = Simple, C = Compound): ")
    if type.lower() == 'c':
        CompoundInterest(principal, time, (interest / 100))
    elif type.lower() == 's':
        SimpleInterest(principal, time, (interest / 100))
    else:
        print("Invalid input, exiting program.")
        exit()


main()
