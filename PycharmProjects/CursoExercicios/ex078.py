VALORES = list()
MENOR = MAIOR = 0
for c in range(0, 5):
    VALORES.append(int(input(f'Digite um valor para a posição {c}:')))
    if c == 0:
        MENOR = VALORES[c]
        MAIOR = VALORES[c]
    else:
        if VALORES[c] < MENOR:
            MENOR = VALORES[c]
        elif VALORES[c] > MAIOR:
            MAIOR = VALORES[c]
print(f'A lista formada foi: {VALORES}')
print(f'O maior valor digitado foi {MAIOR} nas posições', end=' ')
for cont in range(0, 5):
    if VALORES[cont] == MAIOR:
        print(f'{cont}...', end='')
print(f'\nO menor valor digitado foi {MENOR} nas posições', end=' ')
for cont in range(0, 5):
    if VALORES[cont] == MENOR:
        print(f'{cont}...', end='')
