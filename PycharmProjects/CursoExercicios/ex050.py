s = 0
for c in range(0, 6):
    n = int(input('Digite um número:'))
    if n % 2 == 0:
        s = s + n
print('O somatório dentre os números pares digitados é igual a: {}'.format(s))
