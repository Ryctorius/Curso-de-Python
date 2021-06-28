lista = []
notas = []
while True:
    NOME = str(input('Nome: ')).capitalize()
    notas.append(float(input('Primeira nota: ')).__round__(2))
    notas.append(float(input('Segunda nota: ')).__round__(2))
    MEDIA = (notas[0] + notas[1])/2
    lista.append([NOME, notas[:], round(MEDIA, 2)])
    notas.clear()
    R = str(input('Deseja continuar? [S/N]')).strip()[0]
    if R in 'Nn':
        break
print('_'*40)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('_'*30)
for c in range(0, len(lista)):
    print(f'{c:<4}{lista[c][0]:<10}{lista[c][2]:^30:>8}')
print('_'*30)
num = int(input('Deseja ver a nota de qual aluno: (999 interrompe)'))
while num != 999:
    print(f'Notas de {lista[num][0]} são {lista[num][1]}')
    print('_' * 30)
    num = int(input('Deseja ver a nota de qual aluno: (999 interrompe)'))
print('FINALIZANDO...')
print('Volte sempre!')
