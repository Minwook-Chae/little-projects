import random

NUM_DIGITS = 3 
MAX_GUESSES = 10


def main():
    print("The bagels game.")
    print("Pico means a digit is correct but in the wrong position.")
    print("Fermi means a digit is correct and in the right position.")
    print("Bagels means nothing is correct.")

    while True:
        secretNum = makeSecretNum()
        print("There is a random number.")
        print(f"You have {MAX_GUESSES} chances to guess it.")

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ""
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f"Guess #{numGuesses}:")
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print("You are out of guesses.")
                print(f"The secret number was {secretNum}")

        print("Do you want to play again? (yes or no)")
        if not input('> ').lower().startswith('y'):
            break
    print("Thanks for playing!")


def makeSecretNum():
    digits = list('01234566789')
    random.shuffle(digits)

    secretNum = ""
    for i in range(NUM_DIGITS):
        secretNum += str(digits[i])
    return secretNum


def getClues(guess, secretNum):
    if guess == secretNum:
        return "You guessed it!"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)


if __name__ == '__main__':
    main()

