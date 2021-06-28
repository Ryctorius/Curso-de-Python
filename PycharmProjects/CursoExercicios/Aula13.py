"""n = int(input('Digite um número:'))
for c in range(1, n+1):
    print(c)"""

"""I = int(input('INICIO:'))
F = int(input('FIM:'))
P = int(input('INTERVALO:'))
for c in range(I, F+1, P):
    print(c)
print('FIM')"""

s = 0
for c in range(0, 4):
    n = int(input('Digite um numero:'))
    s = s + n
print('O somatório dos numeros digitados é: {}'.format(s))
