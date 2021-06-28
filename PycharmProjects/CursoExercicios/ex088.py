from random import randint
import time
jogos = []
sorteados = []
print('-'*30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-'*30)
n = int(input('Quantos jogos voce quer que eu sorteie?'))
for c in range(0, n):
    for cont in range(0, 6):
        while True:
            num = randint(1, 60)
            if num not in sorteados:
                sorteados.append(num)
                break
    sorteados.sort()
    jogos.append(sorteados[:])
    sorteados.clear()
print('-='*3, f'SORTEANDO {n} JOGOS', '-='*3)
for c in range(0, n):
    print(f'Jogo {c+1}: {jogos[c]}')
    time.sleep(0.5)
print('-='*5, ' BOA SORTE! ', '-='*5)
