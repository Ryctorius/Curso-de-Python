SOMA = 0
MAIOR = 0
MENOR = 0
VELHO = 'Nenhum homem'
for c in range(0, 4):
    NOME = str(input('Digite o nome:')).strip()
    IDADE = int(input('Digite a idade:'))
    SEXO = str(input('Digite M caso seja do sexo masculino ou F caso seja do sexo feminino:')).strip()
    SEXO = SEXO.upper()
    if SEXO != 'M' and SEXO != 'F':
        print('Gênero invalido!')
        quit()
    SOMA = SOMA + IDADE
    if SEXO == 'M' and IDADE > MAIOR:
        VELHO = NOME
    elif SEXO == 'F' and IDADE < 20:
        MENOR = MENOR + 1
print('A media de idade do grupo é: {}'.format(SOMA/4))
print('O nome do homem mais velho é: {}'.format(VELHO))
print('O número de mulheres que tem menos de 20 anos é: {}'.format(MENOR))
