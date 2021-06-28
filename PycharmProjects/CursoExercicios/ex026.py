FRASE = str(input('Digite uma frase:')).strip()
print('Sua frase contem {} vezes a letra A'.format(FRASE.upper().count('A')))
print('A primeira vez que aparece a letra A em sua frase é na posição: {}'.format(FRASE.upper().find('A')+1))
print('A ultima vez que aparece a letra A em sua frase é na posição: {}' .format(FRASE.upper().rfind('A')+1))
