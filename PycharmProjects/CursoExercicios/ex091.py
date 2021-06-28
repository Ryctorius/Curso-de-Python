from random import randint
import time
dados = dict()
dados['Jogador 1'] = randint(1, 6)
dados['Jogador 2'] = randint(1, 6)
dados['Jogador 3'] = randint(1, 6)
dados['Jogador 4'] = randint(1, 6)
print('-'*20)
print('Valores sorteados:')
for k, v in dados.items():
    print(f"O {k} tirou {v}")
    time.sleep(0.75)
print('-'*20)
print('Ranking dos jogadores:')
n = 1
for k in sorted(dados, key=dados.get, reverse=True):
    print(f"{n}ºlugar: {k} com {dados[k]}")
    n += 1
    time.sleep(0.75)
