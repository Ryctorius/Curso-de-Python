SOMA = C = 0
print("_"*40)
print('LOJA NOSTRADAMUS')
print("_"*40)
NOME = str(input('Digite o nome do produto:')).upper().strip()
PRECO = float(input('Digite o preço do produto: R$'))
MENOR = PRECO
BARATO = NOME
while True:
    SOMA += PRECO
    if PRECO > 1000:
        C += 1
    if MENOR > PRECO:
        BARATO = NOME
        MENOR = PRECO
    R = str(input('Deseja continuar? [S/N]')).upper().strip()
    while R != "S" and R != "N":
        print('Resposta invalida')
        R = str(input('Deseja continuar? [S/N]')).upper().strip()
    if R == 'N':
        print('Fim')
        break
    NOME = str(input('Digite o nome do produto:')).upper().strip()
    PRECO = float(input('Digite o preço do produto: R$'))
print('_'*40)
print(f'O total gasto nas compras foi R${SOMA :.2f}')
print(f'Temos {C} produtos custando acima de R$1000.00')
print(f'O produto mais barato foi {BARATO} que custa R${MENOR :.2f}')
