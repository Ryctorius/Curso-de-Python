from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ')
    for c in range(0, 5):
        lista.append(randint(1, 11))
    for cont in lista:
        print(cont, end=' ')
        sleep(0.5)
    print('PRONTO!')


def somapar(listados):
    somatorio = 0
    for c in listados:
        if (c % 2) == 0:
            somatorio += c
    print(f'Somando os valores pares de {listados}, temos: {somatorio}')


numeros = []
sorteia(numeros)
somapar(numeros)
