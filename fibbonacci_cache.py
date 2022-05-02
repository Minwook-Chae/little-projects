def main():
    while True:
        print('Get the nth index of fibbonacci')
        response = input('> ')
        if response.isdecimal():
            break
    print(fibbo(int(response)))


def fibbo(n, cache={0: 0, 1: 1}):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        cache[n] = fibbo(n - 1, cache) + fibbo(n - 2, cache)
    print(cache.values())
    return cache[n]


if __name__ == '__main__':
    main()