from random import choice
from time import sleep
lista = [0, 1, 2]
M = choice(lista)
print('SEJA BEM VINDO AO MEU JOKENPÔ!')
print('''Escolha uma das opções a seguir:
[0]- PEDRA
[1]- PAPEL
[2]- TESOURA''')
E = int(input())
if E != 0 and E != 1 and E != 2:
    print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE')
    quit()
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
print('=====================================')
if E == 0:
    print('Você escolheu PEDRA!')
elif E == 1:
    print('Você escolheu PAPEL!')
else:
    print('Você escolheu TESOURA!')

if M == 0:
    print('O computador escolheu PEDRA!')
elif M == 1:
    print('O computador escolheu PAPEL!')
else:
    print('O computador escolheu TESOURA!')
print('=====================================')
if E-M == 0:
    print('HOUVE UM EMPATE!')
elif E-M == 1 or E-M == -2:
    print('VOCÊ É O VENCEDOR!!!')
else:
    print('VOCÊ PERDEU!')
