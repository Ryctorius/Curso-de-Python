def contador(*num):
    print(f'Há {len(num)} números.')
    for v in num:
        print(f'{v}', end=' ')
    print('\nFim!')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
