lista = []
mulheres = []
D = dict()
SOMA = 0
while True:
    D['Nome'] = str(input('Nome: ')).strip().capitalize()
    while True:
        D['Sexo'] = str(input('Sexo:[M/F] ')).strip().upper()[0]
        if D['Sexo'] in 'MF':
            break
        else:
            print('Resposta inválida. Responda M para masculino e F para feminino')
    D['Idade'] = int(input('Idade: '))
    SOMA += D['Idade']
    lista.append(D.copy())
    if D['Sexo'] == 'F':
        mulheres.append(D['Nome'])
    while True:
        R = str(input('Deseja continuar?[S/N] ')).upper().strip()[0]
        if R in 'SN':
            break
        else:
            print('Resposta inválida. Responda apenas S ou N')
    if R == 'N':
        break
    else:
        D.clear()
print('-='*20)
print(f'-Foram cadastradas {len(lista)} pessoas')
print(f'-A média de idade do grupo é igual a: {SOMA/len(lista)} pessoas')
print(f'-As mulheres do grupo são: {mulheres}')
print(f'-Pessoas com idade acima da média: ')
for c in range(0, len(lista)):
    if lista[c]['Idade'] > (SOMA/len(lista)):
        print(f"Nome: {lista[c]['Nome']}; Sexo: {lista[c]['Sexo']}; Idade: {lista[c]['Idade']}.")
print('-'*15, 'FIM', '-'*15)
