LISTA = list()
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
LISTA.sort(reverse=True)
print(f'Foram digitados {len(LISTA)} números')
print(f'A lista de valores ordenada em ordem decrescente é: {LISTA}')
if 5 in LISTA:
    print('Há o número 5 na lista!')
else:
    print('Não há número 5 na lista!')
