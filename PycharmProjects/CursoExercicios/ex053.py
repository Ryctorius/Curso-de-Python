FRASE = str(input('Digite uma frase:'))
FRASE = FRASE.upper()
FRASE = FRASE.strip()
FRASE = FRASE.replace(' ', '')
X = len(FRASE)
for c in range(0, X):
    if FRASE[c] == FRASE[X-1]:
        X = X - 1
    else:
        print('A frase não é um palíndromo!')
        quit()
print('É um palíndromo!!!')

"""FRASE[::-1] -> inverte a str"""
