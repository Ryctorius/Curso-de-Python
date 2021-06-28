pessoas = {'Nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f"O {pessoas['Nome']} tem {pessoas['idade']} de idade.")
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k, v in pessoas.items():
    print(f'{k} = {v}')
for k in pessoas.keys():
    print(k)
del pessoas['sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}')
pessoas['Nome'] = 'Leandro'
for k, v in pessoas.items():
    print(f'{k} = {v}')
pessoas['Peso'] = 98.5
for k, v in pessoas.items():
    print(f'{k} = {v}')
