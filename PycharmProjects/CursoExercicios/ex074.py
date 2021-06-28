from random import randint
LIST = randint(0, 999), randint(0, 999), randint(0, 999), randint(0, 999), randint(0, 999)
print(f'Os números sorteados foram: {LIST}')
print(f'O menor número sorteado foi {min(LIST)} e o maior número sorteado foi {max(LIST)}')
