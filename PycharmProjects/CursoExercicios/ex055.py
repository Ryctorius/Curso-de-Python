MAIOR = 0
MENOR = 10000
for c in range(0, 5):
    PESO = float(input('Digite o peso em Kg:'))
    if PESO > MAIOR:
        MAIOR = PESO
    elif PESO < MENOR:
        MENOR = PESO
print('O maior peso digitado foi {:.2f}Kg e o menor peso digitado foi {:.2f}Kg'.format(MAIOR, MENOR))
