import datetime
pessoa = dict()
pessoa['Nome'] = str(input('Nome:'))
ano = int(input('Ano de nascimento:'))
pessoa['idade'] = (datetime.date.today().year - ano)
pessoa['CTPS'] = int(input('Carteira de Trabalho (0 não tem):'))
if pessoa['CTPS'] != 0:
    pessoa['Contratação'] = int(input('Ano de contratação:'))
    pessoa['Salário'] = float(input('Salário: R$'))
    pessoa['Aposentadoria'] = pessoa['idade'] + 35 - (datetime.date.today().year - pessoa['Contratação'])
print('-'*30)
for k, v in pessoa.items():
    print(f'-{k} tem o valor {v}')
print('-'*30)
