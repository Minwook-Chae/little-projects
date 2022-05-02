def main():
    while True:
        print('Enter number greater than 0 or QUIT')
        response = input('> ')
        if response.isdecimal() and int(response) > 0:
            break
        elif response.upper() == 'QUIT' or response.upper() == 'Q':
            break
    collatz(int(response))


def collatz(n):
    print(n, end='')
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        print(f", {n}", end='')

if __name__ == '__main__':
    main()