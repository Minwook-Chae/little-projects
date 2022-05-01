from tkinter import E


SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    while True:
        print("(e)ncrypt or (d)ecrypt?")
        response = input('> ').lower()
        if response.startswith('e'):
            mode = 'encrypt'
            break
        elif response.startswith('d'):
            mode = 'decrypt'
            break
        print("Please enter the letter e or d.")
    while True: 
        maxKey = len(SYMBOLS) - 1
        print(f"Please enter the key (0 to {maxKey}) to use.")
        response = input('> ').upper() 
        if not response.isdecimal():
            print(response)
            continue
        if 0 <= int(response) < len(SYMBOLS):
            key = int(response)
            break

    print(f"Enter the message to {mode}.")
    message = input('> ')
    message = message.upper()
    translated = ""
    for symbol in message: 
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol)
            if mode == 'encrypt':
                num = num + key
            elif mode == 'decrypt':
                num = num - key
            if num >= len(SYMBOLS):
                num = num -len(SYMBOLS)
            elif num < 0:
                num = num + len(SYMBOLS)
            translated = translated + SYMBOLS[num]
        else:
            translated = translated + symbol
    print(translated)
    


if __name__ == '__main__':
    main()
