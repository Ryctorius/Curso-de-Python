matriz = []
dados = []
pares = []
PAR = soma = maior = 0
for c in range(0, 3):
    for v in range(0, 3):
        num = int(input(f'Digite um número para a posição [{c}, {v}]:'))
        dados.append(num)
        if num % 2 == 0:
            pares.append(num)
            PAR += num
        if v == 2:
            soma += num
        if c == 1:
            if v == 0:
                maior = num
            elif num > maior:
                maior = num
    matriz.append(dados[:])
    dados.clear()
print('-'*40)
for c in range(0, 3):
    for v in range(0, 3):
        print(f'[ {matriz[c][v]} ]', end='')
    print('')
print('-'*40)
print(f'Os numéros pares são {pares} e seu somatório vale {PAR}')
print('-'*40)
print(f'A soma da terceira coluna é igual a: {soma}')
print('-'*40)
print(f'O maior valor da segunda linha é: {maior}')
print('-'*40)
