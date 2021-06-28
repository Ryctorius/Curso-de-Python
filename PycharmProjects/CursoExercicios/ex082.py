LISTA = list()
PAR = []
IMPAR = []
while True:
    LISTA.append(int(input('Digite um número:')))
    while True:
        R = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
        if R != 'S' and R != 'N':
            print('Resposta inválida, tente novamente...')
        else:
            break
    if R == 'N':
        print('Programa Finalizado!')
        break
c = 0
while c < len(LISTA):
    if (LISTA[c] % 2) == 0:
        PAR.append(LISTA[c])
    else:
        IMPAR.append(LISTA[c])
    c += 1
print(f'Lista completa {LISTA}')
print(f'Lista apenas com os números pares: {PAR}')
print(f'Lista apenas com os números impares: {IMPAR}')
