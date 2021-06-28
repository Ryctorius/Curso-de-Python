num = int(input('Digite um numero inteiro:'))
print('''Escolha a base para conversão:
[0] converter para BINÁRIO
[1] converter para OCTAL
[2] converter para HEXADECIMAL''')
opção = int(input())
if opção == 0:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opção == 1:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opção == 2:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida!')
