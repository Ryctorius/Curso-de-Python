VAL = list()
while True:
    NUM = int(input('Digite um valor:'))
    if NUM in VAL:
        print(f'Número {NUM} já consta na lista.')
    else:
        VAL.append(NUM)
        print('Valor adicionado!')
    while True:
        R = str(input(f'Você deseja continuar? [S/N]  ')).upper().strip()[0]
        if R != 'S' and R != 'N':
            print('Resposta invalida, tente novamente')
        else:
            break
    if R == 'N':
        break
print(f'Os valores em ordem crescente são: {sorted(VAL)}')
