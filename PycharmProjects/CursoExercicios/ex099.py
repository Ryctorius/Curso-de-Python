from time import sleep


def maior(*num):
    print('-='*20)
    print('Analisando os valores passados...')
    ma = cont = 0
    for c in num:
        print(c, end=' ')
        sleep(.5)
        if cont == 0:
            ma = c
            cont += 1
        elif c > ma:
            ma = c
    print(f'\nForam informados {len(num)} valores ao todo.')
    print(f'O maior valor inserido foi o {ma}')


maior(2, 9, 4, 5, 7, 1)
maior(-11, -2, -5, -10)
maior(4, 7, 0)
maior(6)
maior()
