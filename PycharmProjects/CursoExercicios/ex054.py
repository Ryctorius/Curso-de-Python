import datetime
ATUAL = datetime.date.today()
X = 0
for c in range(0, 7):
    NOME = input(str('Digite a primeira data de nascimento (Formato: DD-MM-AAAA):'))
    if int(ATUAL.year) < int(NOME[6:]):
        print('FORMATO INCORRETO')
        quit()
    if int(NOME[3:5]) > 12:
        print('FORMATO INCORRETO')
        quit()
    if int(NOME[:2]) > 31:
        print('FORMATO INCORRETO')
        quit()
    if NOME[2] != '-' or NOME[5] != '-':
        print('FORMATO INCORRETO')
        quit()
    if int(ATUAL.year) - int(NOME[6:]) > 21:
        X = X + 1
    elif int(ATUAL.year) - int(NOME[6:]) == 21:
        if int(ATUAL.month) > int(NOME[3:5]):
            X = X + 1
        elif int(ATUAL.month) == int(NOME[3:5]):
            if int(ATUAL.day) > int(NOME[:2]):
                X = X + 1
print('O número de maiores de idade digitados é: {}'.format(X))
