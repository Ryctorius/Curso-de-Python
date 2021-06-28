from time import sleep


def linha():
    print('-'*40)


def contador(i, f, p):
    if p == 0:
        p = 1
    elif p < 0:
        p = -p
    linha()
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if f > i:
        f += 1
        for c in range(i, f, p):
            print(c, end=' ')
            sleep(0.5)
        print()
    else:
        f -= 1
        for c in range(i, f, -p):
            print(c, end=' ')
            sleep(0.5)
        print()
    linha()


contador(1, 10, 1)
contador(10, 0, -2)
inicio = int(input('Digite o valor inicial da sua sequencia personalizada:'))
fim = int(input('Digite o valor final da sua sequencia personalizada:'))
inter = int(input('Digite o intervalo que você deseja que seja feita a contagem:'))
contador(inicio, fim, inter)
