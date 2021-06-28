NUM = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
       'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    N = int(input('Digite o Número desejado: [0-20]'))
    while N < 0 or N > 20:
        N = int(input('Número inválido, tente novamente! Digite o Número desejado: [0-20]'))
    print(f'Você digitou o número {NUM[N]}')
    R = str(input('Você deseja continuar [S/N]:')).upper().strip()[0]
    if R == 'N':
        break
