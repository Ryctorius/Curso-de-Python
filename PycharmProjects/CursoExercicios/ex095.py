futebol = dict()
lista = []
while True:
    futebol['Nome'] = str(input('Nome do jogador: ')).capitalize().strip()
    futebol['gols'] = []
    n = int(input(f"Quantas partidas {futebol['Nome']} jogou?"))
    c = 0
    while c < n:
        futebol['gols'].append(int(input(f'Quantos gols na partida {c+1}?')))
        c += 1
    futebol['total'] = 0
    for cont in range(0, n):
        futebol['total'] += futebol['gols'][cont]
    lista.append(futebol.copy())
    R = str(input('Deseja continuar? [S/N] ')).strip()[0]
    if R in 'Nn':
        break
    else:
        futebol.clear()
        print('-'*40)
print('-='*20)
print(f'{"COD Nome":<4}{"Gols":^10}{"Total":>15}')
for c in range(0, len(lista)):
    print(f"{c:<0} {lista[c]['Nome']:>8}  {lista[c]['gols']} {lista[c]['total']:>10}")
print('-='*20)
k = int(input('Mostrar dados de qual jogador?'))
while k != 999:
    if k < len(lista):
        print(f"--Levantamento do jogador {lista[k]['Nome']}:")
        for c in range(0, len(lista[k]['gols'])):
            print(f"    => Na partida {c+1}, fez {lista[k]['gols'][c]} gols")
    else:
        print('Opção inválida! 999 para cancelar')
    print('-=' * 20)
    k = int(input('Mostrar dados de qual jogador?'))
print("-"*15, 'FIM', "-"*15)
