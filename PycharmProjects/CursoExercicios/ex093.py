futebol = dict()
futebol['Nome'] = str(input('Nome do jogador: ')).capitalize().strip()
futebol['gols'] = []
n = int(input(f"Quantas partidas {futebol['Nome']} jogou?"))
c = 0
while c < n:
    futebol['gols'].append(int(input(f'Quantos gols na partida {c+1}?')))
    c += 1
futebol['total'] = sum(futebol['gols'])
print('-='*15)
print(futebol)
print('-='*15)
for k, v in futebol.items():
    print(f"O campo {k} tem o valor {v}")
print('-='*15)
print(f"O jogador {futebol['Nome']} jogou {n} partidas.")
for c in range(0, len(futebol['gols'])):
    print(f"    => Na partida {c+1}, fez {futebol['gols'][c]} gols")
print(f"Foi um total de {futebol['total']} gols")
