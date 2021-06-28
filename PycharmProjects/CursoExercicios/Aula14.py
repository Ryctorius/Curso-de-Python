"""c = 1
while c < 10:
    print(c)
    c += 1
print('FIM')"""

n = 1
PAR = 0
IMPAR = 0
while n != 0:
    n = int(input('Digite um valor'))
    if n != 0:
        if n % 2 == 0:
            PAR += 1
        else:
            IMPAR += 1
print('Há {} numeros pares e {} numeros impares'.format(PAR, IMPAR))

print('FIM')
