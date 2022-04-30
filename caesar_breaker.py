print("Enter Caesar Cipher to break.")
message = input('> ') 

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    for key in range(len(SYMBOLS)):
        translated = ''

        for symbol in message:
            if symbol in SYMBOLS:
                num = SYMBOLS.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(SYMBOLS)
                translated = translated + SYMBOLS[num]
            else:
                translated = translated + symbol
        print(f"Key #{key}: {translated}")


if __name__ == '__main__':
    main() 
