LISTA = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor',
         4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livros', 34.90)
print('-'*40)
print(f'{"Listagem de Preços":^40}')
print('-'*40)
for c in range(0, len(LISTA), 2):
    print(f'{LISTA[c]:.<30} R$ {LISTA[c+1]:>6.2f}')
print('-'*40)
