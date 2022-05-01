import random, sys


NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN', 
            4: 'SHI', 5: 'GO', 6: 'ROKU'}

def main(purse=5000):
    while True:
        print(f"You have {purse} mon.")
        print('Place your bet: ')
        while True:
            pot = input('> ')
            if pot.upper() == 'QUIT' or pot.upper() == 'Q':
                sys.exit()
            elif not pot.isdecimal():
                print('Enter an amount to bet.')
            elif int(pot) > purse:
                print('You do not have enough to make that wager.')
            else:
                pot = int(pot)
                break
        
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        print('The house rolls the dice in a cup...')
        print('Is the sum CHO (even) or HAN (odd)?')

        while True:
            choice = input('> ').upper()
            if choice != 'CHO' and choice != 'HAN':
                print('Please enter CHO or HAN')
                continue
            else:
                break

        print('The house shows the dice...')
        print(f"{d1}: {NUMBERS[d1]}")
        print(f"{d2}: {NUMBERS[d2]}")

        if (d1 + d2) % 2 == 0:
            correct = 'CHO'
        else:
            correct = 'HAN'

        if choice == correct:
            print('You win!')
            print(f"You get {pot} mon!")
            purse += pot
            print(f"Your purse is now {purse}!")
            print(f"But the house collects a {pot // 10} fee...")
            purse -= pot // 10
            print(f"Your purse is now {purse}!")
        else:
            print('You lose!')
            purse -= pot
            print(f"Your purse is now {purse}!")

        if purse == 0:
            print('You have no more money!')
            print('You lose!')
            sys.exit()


if __name__ == '__main__':
    main()
