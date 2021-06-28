while True:
    SAQUE = int(input('Digite o valor que você deseja sacar: R$'))
    CINQ = SAQUE//50
    SAQUE -= (CINQ*50)
    VINTE = SAQUE//20
    SAQUE -= (VINTE*20)
    DEZ = SAQUE//10
    SAQUE -= (DEZ*10)
    if CINQ > 0:
        print(f'Você irá receber {CINQ} notas de 50 reais')
    if VINTE > 0:
        print(f'Você irá receber {VINTE} notas de 20 reais')
    if DEZ > 0:
        print(f'Você irá receber {DEZ} notas de 10 reais')
    if SAQUE > 0:
        print(f'Você irá receber {SAQUE} notas de 1 real')
