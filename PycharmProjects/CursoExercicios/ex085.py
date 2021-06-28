numeros = [[], []]
for c in range(1, 8):
    NUM = int(input(f'Digite o {c}º valor:'))
    if NUM % 2 == 0:
        numeros[0].append(NUM)
    else:
        numeros[1].append(NUM)
print(f'Numeros pares {sorted(numeros[0])}')
print(f'Numeros impares {sorted(numeros[1])}')
"""numeros[0].sort()
    numeros[1].sort()"""
