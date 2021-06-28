import random
PC = random.randint(0, 10)
N = int(input('Tente advinhar o número inteiro sorteado de 0 a 10:'))
CONT = 1
while PC != N:
    N = int(input('Tente novamente:'))
    CONT += 1
print('Parabéns o número sorteado foi {} e você advinhou com {} tentativas'.format(PC, CONT))
