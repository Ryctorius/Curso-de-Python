LANCHE = ['Hamburguer', 'Pizza', 'Refrigetante', 'Pudim']
print(LANCHE)
LANCHE.append('cookie')
print(LANCHE)
LANCHE.insert(0, 'cachorro quente')
print(LANCHE)
del LANCHE[3]
print(LANCHE)
LANCHE.pop(2)
print(LANCHE)
LANCHE.remove('Hamburguer')
print(LANCHE)
LANCHE.pop()
print(LANCHE)
if 'pizza' in LANCHE:
    LANCHE.remove('pizza')
print(LANCHE)
VALORES = list(range(4, 11))
print(VALORES)
print(VALORES[2])
VALORES = [8, 2, 5, 4, 9, 3, 0]
print(VALORES)
VALORES.sort()
print(VALORES)
VALORES.sort(reverse=True)
print(VALORES)
print(len(VALORES))
