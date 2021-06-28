def ficha(a='<desconhecido>', b=0):
    print(f'O jogador {a} fez {b} gol(s) no campeonato')


nome = str(input('Digite o nome do jogador: '))
gols = str(input('Digite o número de gols feitos: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(b=gols)
else:
    ficha(nome, gols)
