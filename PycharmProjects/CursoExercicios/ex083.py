EXP = list(input('Digite uma expressão:'))
P1 = P2 = c = 0
while c < len(EXP):
    if EXP[c] == '(':
        P1 += 1
    elif EXP[c] == ')':
        P2 += 1
    c += 1
    if P2 > P1:
        print('Parenteses em ordem incorreta')
        quit()
if P1 > P2:
    print('Há mais parenteses abertos do que fechados')
elif P1 == P2:
    print('Parenteses informados de forma correta')
else:
    print('Há mais parenteses fechados do que abertos')
