MAIOR = HOMENS = MENORES = 0
while True:
    IDADE = int(input('Digite sua idade:'))
    SEXO = str(input('Selecione o sexo Masculino ou Feminino [M/F]:')).upper().strip()
    while SEXO != "M" and SEXO != "F":
        print('OPÇÃO INVALIDA! TENTE NOVAMENTE')
        SEXO = str(input('Selecione o sexo Masculino ou Feminino [M/F]:')).upper().strip()
    if IDADE > 18:
        MAIOR += 1
    if SEXO == "M":
        HOMENS += 1
    elif IDADE < 20:
        MENORES += 1
    R = str(input('Deseja continuar? [S/N]')).upper().strip()
    while R != "S" and R != "N":
        print('OPÇÃO INVALIDA! TENTE NOVAMENTE')
        R = str(input('Deseja continuar? [S/N]')).upper().strip()
    if R == "N":
        print('Programa encerrado!')
        break
print(f'Há {MAIOR} pessoas maiores de 18 anos de idade nesse grupo')
print(f'Há {HOMENS} homens cadastrados')
print(f'Há {MENORES} mulheres com menos de 20 anos no grupo')
