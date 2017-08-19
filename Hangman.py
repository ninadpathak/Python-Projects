from random import randint
from os import system
from sys import platform

HANGMAN = [
    '''
        _____
        |   |
            |
            |
            |
            |
          __|__
    ''',
    '''
        _____
        |   |
        O   |
            |
            |
            |
          __|__
    ''',
    '''
        _____
        |   |
        O   |
        |   |
            |
            |
          __|__
    ''',
    '''
        _____
        |   |
        O   |
       /|   |
            |
            |
          __|__
    ''',
    '''
        _____
        |   |
        O   |
       /|\  |
            |
            |
          __|__
    ''',
    '''
        _____
        |   |
        O   |
       /|\  |
       /    |
            |
          __|__
    ''',
    '''

        _____
        |   |
        O   |
       /|\  |
       / \  |
            |
          __|__
    '''
]

#######################################################
# Clear - Checks the OS platform and uses the apprproiate
# clear command
#######################################################
def clear():
    if platform == "linux" or platform == "linux2":
        a = system('clear')
    elif platform == "win32":
        a = system('cls')

#######################################################
# Add Blanks - This function adds blanks to the randomly selected word
# Returns a dictionary file with a word with blanks, a display word
# with spaced blanks and the number of blanks
#
# Had to add another for loop to count underscores. Not sure why it
# showed wrong number of underscores making the program stop without letting
# the game to complete
#######################################################
def add_blanks(word):
    total_blanks = len(word) // 2
    word = list(word)  # converting string to list for mutation
    display_word = list(word)
    count = 0

    for i in range(0, total_blanks):
        blank = randint(0, len(word) - 1)
        word[blank] = '_'
        display_word[blank] = ' _ '

    for char in word:
        if char == "_":
            count += 1

    word = "".join(word)    # converting mutated list back to string
    display_word = "".join(display_word)
    return {"word": word, "display_word": display_word, "count": count}

#######################################################
# Check Input = Checks the input to see if any of the blanks match the guess. 
# It
#######################################################
def check_input(word, word_blanks, guess):
    word = list(word)
    word_blanks = list(word_blanks)
    count = 0

    for i in range(0, len(word)):
        if word[i].lower() == guess.lower() and word_blanks[i] == "_":
            word_blanks[i] = word[i]
            count += 1
        else:
            continue

    word_blanks = "".join(word_blanks)

    data = {"word": word_blanks, "count": count}
    return data

#######################################################
# Get Word - Randomly selects a word from a predefined list file
# Go ahead and add anything or you can also create a loop of some sort to get
# words from a file and just assign the word to the variable "words"
# Everything else will keep working fine as long as "words" is a string
#######################################################
def get_word():
    words = ['test', 'testing', 'Ninad', 'anything', 'randomword']
    word = words[randint(0, len(words) - 1)]
    length = len(word)
    blanks = add_blanks(word)
    word_data = {
        "word": word,
        "word_blanks": blanks["word"],
        "total_blanks": blanks["count"],
        "display_word": blanks["display_word"],
        "length": length
    }

    return word_data

#######################################################
# Main function - Gets the word first and splits the data into
# different variables. We loop through the game until the variable
# "tries" becomes 0 which also marks shows the complete 
# hangman figure. Screen will keep clearing as required so
# we don't have multiple hangman figures on the screen.
# If the system function annoys you, just remove add the word "pass"
# to the clear function so there's not much editing required.
#######################################################
def main():
    word = get_word()
    blanks_left = word["total_blanks"]
    word_blnk = word["word_blanks"]
    display_word = word["display_word"]
    tries = 6
    i = 0
    clear()
    print("*" * 20, "Begin Hangman", "*" * 20)
    print("\n\nTry to guess the word: \n\n", display_word)
    print("\n\n")

    while tries >= 0:
        if blanks_left == 0:
            print(HANGMAN[i])
            print("Congrats! You successfuly completed it!")
            print("The word is: ", word["word"])
            print("You saved the hangman!")
            break

        print(HANGMAN[i])
        if tries == 0:
            print(tries, " tries left.")
            print("Hangman died. :( ")
            print("Game over")
            break

        guess = input("Enter your guess (one letter only): ")
        if len(guess) > 1:
            clear()
            print("Please enter only one letter at a time. Here, try again")
            continue

        else:
            clear()
            word_chk = check_input(word["word"], word_blnk, guess)
            blanks_left -= word_chk["count"]

            if word_chk["count"] > 0:
                if blanks_left == 0:
                    continue
                else:
                    print("\nGreat job! Correct guess!")
                    print("\nRemaining blanks: ", word_chk["word"])
                    print("\n", tries, " attempts left")
                    word_blnk = word_chk["word"]
                    continue

            elif word_chk["count"] == 0 and tries > 0:
                tries -= 1
                i += 1
                print("\nThe letter ", guess, " did not match any blank.")
                print("\nRemaining blanks: ", word_chk["word"])
                print("\n", tries, " tries left")
                continue

            else:
                pass


main()
