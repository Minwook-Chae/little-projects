def main():
    while True:
        print('Get the nth index of fibbonacci')
        response = input('> ')
        if response.isdecimal() and -1 < response.isdecimal():
            break
    print(fibbo(int(response)))


# are the first two numbers in fibbo 0, 1 or 1, 1? 
def fibbo(n, cache={0: 0, 1: 1, 2: 1}):
    if n in cache:
        return cache[n]
    else:
        cache[n] = fibbo(n - 1, cache) + fibbo(n - 2, cache)
    print(cache.values())
    return cache[n]


if __name__ == '__main__':
    main()