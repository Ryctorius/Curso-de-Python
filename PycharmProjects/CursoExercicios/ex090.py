aluno = dict()
aluno['nome'] = str(input('Nome: ')).capitalize().strip()
aluno['media'] = float(input(f"Média de {aluno['nome']}: "))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif aluno['media'] >= 5:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-'*20)
print(f"Nome é igual a {aluno['nome']}"
      f"\nMédia é igual a {aluno['media']}"
      f"\nSituação é igual a {aluno['situação']}")
print('-'*20)
