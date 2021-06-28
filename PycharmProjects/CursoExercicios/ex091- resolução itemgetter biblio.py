from random import randint
import time
from operator import itemgetter
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
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    time.sleep(.5)
