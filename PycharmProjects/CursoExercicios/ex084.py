Lista = []
maiores = []
menores = []
maior = menor = 0
dados = []
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    Lista.append(dados[:])
    dados.clear()
    R = str(input('Deseja continuar: [S/N]')).upper().strip()[0]
    if R in 'Nn':
        break
    else:
        print('-' * 40)
for p in Lista:
    if menor == 0:
        maior = p[1]
        menor = p[1]
    elif p[1] > maior:
        maior = p[1]
    elif p[1] < menor:
        menor = p[1]
for p in Lista:
    if p[1] == maior:
        maiores.append(p[0])
    elif p[1] == menor:
        menores.append(p[0])
print(f'Foram cadastradas {len(Lista)} pessoas')
print(f'As pessoas mais pesadas são {maiores} com {maior}Kg')
print(f'As pessoas menos pesadas são {menores} com {menor}Kg')
