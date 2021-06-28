import random
C = 0
print('SEJA BEM VINDO AO PAR OU IMPAR!!!')
while True:
    PC = random.randint(0, 10)
    ESCOLHA = str(input('Você deseja escolher PAR ou IMPAR?')).upper().strip()
    while ESCOLHA != "PAR" and ESCOLHA != "IMPAR":
        print('OPÇÃO INVALIDA')
        ESCOLHA = str(input('Você deseja escolher PAR ou IMPAR?')).upper().strip()
    MAO = int(input('Escolha seu número:'))
    print(f'Eu escolhi o número {PC}')
    if (ESCOLHA == "PAR" and (PC + MAO) % 2 == 0) or (ESCOLHA == "IMPAR" and (PC + MAO) % 2 != 0):
        print('Você venceu, jogue novamente!')
        C += 1
    else:
        print('Você perdeu!')
        break
print(f'Você venceu um total de {C} partidas consecutivas! Obrigado por jogar conosco.')
