PALAVRAS = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
            'mercado', 'programador', 'futuro')
for cont in PALAVRAS:
    print(f'\n  Na palavra {cont.upper()} temos as seguintes vogais: ', end='')
    for c in cont:
        if c.lower() in 'aeiou':
            print(c, end=' ')
