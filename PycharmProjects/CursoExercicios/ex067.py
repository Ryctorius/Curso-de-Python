while True:
    C = 1
    N = int(input('Digite o número desejado (Numero negativo para finalizar):'))
    print('-'*30)
    if N < 0:
        print('PROGRAMA ENCERRADO!!!')
        break
    while C <= 10:
        print(f'{N} x {C} = {N*C}')
        C += 1
    print('-' * 30)
