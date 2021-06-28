print('Você vai digitar quatro números')
LISTA = (int(input('Digite o primeiro número:')),
         int(input('Digite o segundo número:')),
         int(input('Digite o terceiro número:')),
         int(input('Digite o quarto número:')))

print(f'O número 9 apareceu {LISTA.count(9)} vezes')
if 3 in LISTA:
    print(f'O primeiro número 3 apareceu na posição: {LISTA.index(3)+1}')
else:
    print('Não foi digitado nenhum número 3!')
print('Os números pares digitados foram:', end="")
for n in LISTA:
    if (n % 2) == 0:
        print(n, end=' ')
