print('Você vai digitar dois valores e escolher a operção desejada')
P = float(input('Digite o primeiro valor:'))
S = float(input('Digite o segundo valor:'))
OP = 0
while OP != 5:
    print("""Escolha a opcão desejada:
          [1] - SOMAR
          [2] - MULTIPLICAR
          [3] - MAIOR
          [4] - Digitar outros valores
          [5] - Sair do programa""")
    OP = int(input())
    if OP == 1:
        print('O somatorio dos valores digitados é igual a: {}'.format(P + S))
    elif OP == 2:
        print('A multiplicação dos valores digitados é igual a: {}'.format(P * S))
    elif OP == 3:
        if P > S:
            print('O valor {} é maior que o {}'.format(P, S))
        elif P < S:
            print('O valor {} é maior que o {}'.format(S, P))
        else:
            print('O valor {} é igual ao {}'.format(P, S))
    elif OP == 4:
        print('Você vai digitar dois valores e escolher a operção desejada')
        P = float(input('Digite o primeiro valor:'))
        S = float(input('Digite o segundo valor:'))
    elif OP == 5:
        print('Fim')
    else:
        print('OPÇÃO INVALIDA')
