matriz = []
dados = []
for c in range(0, 3):
    for v in range(0, 3):
        dados.append(int(input(f'Digite um número para a posição [{c}, {v}]:')))
    matriz.append(dados[:])
    dados.clear()
print('-'*40)
for c in range(0, 3):
    for v in range(0, 3):
        print(f'[ {matriz[c][v]:^5} ]', end='')
    print('')
