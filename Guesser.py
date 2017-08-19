from random import randint


def random_guessing():

    low_limit = 1
    high_limit = int(input("Enter the higher limit for the choice: "))
    guess = randint(low_limit, int(high_limit))
    count, answer = 0, 0

    while answer != 3:
        count += 1
        print("My guess is: ", guess)
        answer = int(input("Is that (1) Too High? (2) Too Low (3) Bang on! "))

        if answer == 1:
            high_limit = guess - 1
            if high_limit == 1:
                guess = 0
            else:
                guess = randint(low_limit, high_limit)

        elif answer == 2:
            low_limit = guess + 1
            guess = randint(low_limit, high_limit)

        elif answer == 3:
            print("Yippee! I guessed your number in ", count, "tries.")
            print("You chose ", guess)

        else:
            print("Terminating. You entered some random shit!")

    repeat = input("Would you like to play again? (Y)es or (N)o: ")
    if repeat.lower() == "y":
        random_guessing()
    else:
        exit()


def algo_guessing():

    low_limit = 1
    high_limit = int(input("Enter the higher limit for the choice: "))
    guess = (low_limit + high_limit) // 2
    count, answer = 0, 0

    while answer != 3:
        count += 1
        print("My guess is: ", guess)
        answer = int(input("Is that (1) Too High? (2) Too Low (3) Bang on! "))

        if answer == 1:
            high_limit = guess - 1
            guess = (low_limit + high_limit) // 2

        elif answer == 2:
            low_limit = guess + 1
            guess = (low_limit + high_limit) // 2

        elif answer == 3:
            print("Yippee! I guessed your number in ", count, "tries.")
            print("You chose ", guess)

        else:
            print("Terminating. You entered some random shit!")

    repeat = input("Would you like to play again? (Y)es or (N)o: ")
    if repeat.lower() == "y":
        random_guessing()
    else:
        exit()


def main():
    gtype = int(input('''Do you want to try
    (1)random
    (2)algorithm guessing? '''))

    if gtype == 1:
        random_guessing()
    elif gtype == 2:
        algo_guessing()
    else:
        print("Invalid input")


main()