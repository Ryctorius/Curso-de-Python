s = 0
C = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        s = s + c
        C += 1
print('O somatório entre todos os números ímpares que são multiplos de 3')
print('e que se encontram no intervalo entre 1 até 500 é: {}'.format(s))
print(C)
