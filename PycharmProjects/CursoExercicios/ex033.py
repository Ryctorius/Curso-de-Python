A = float(input('Digite o primeiro número: '))
B = float(input('Digite o segundo número: '))
C = float(input('Digite o terceiro número: '))
MAIOR = A
MENOR = C
if B > A:
    if B > C:
        MAIOR = B
        if A < C:
            MENOR = A
    else:
        MAIOR = C
        MENOR = A
else:
    if C > A:
        MAIOR = C
        MENOR = B
    else:
        if B < C:
            MENOR = B
print('O maior número é {} e o menor número é {}'.format(MAIOR, MENOR))
