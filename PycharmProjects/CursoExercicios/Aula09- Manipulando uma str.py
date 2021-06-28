print("""frase = ['Curso em Vídeo Python']
frase[9] -> seleciona o caracter na posição 9
frase[9:13] seleciona a seção sem incluir o ultimo número
frase[9:21:2] seleciona uma seção pulando uma casa
len(frase) -> mostrar o comprimento da frase
frase.count('o') -> contar quantas letras tem na frase
frase.count('o',0,13) -> contar quantas letras tem naquele intervalo
frase.find('deo') -> dizem onde começa a sequencia em destaque
frase.find('Android') -> se mostrar uma string q nao existe, o retorno será -1
'Curso' in frase -> existe curso em frase:? se sim, o retorno sera true
frase.replace('Python','Android') -> trocar sequencias dentro da string
frase.upper() -> colocar letras em maiusculo
frase.lower() -> coloca letras em minusculo
frase.capitalize() -> coloca apenas o primeiro caracter como maiusculo e o restante em letras minusculas
frase.title() -> coloca todas as palavras começando com letra maiuscula
frase.strip() -> remove os espaços inuteis(ou seja os q ficam antes ou depois da frase)
frase.rstrip() -> remover so os espaços a direita da frase
frase.lstrip() -> remove os espaços a esquerda da frase
frase.split() -> Quebra a frase formando uma lista com um conjunto de palavras
'-'.join(frase) -> o oposto do split, pega o conjunto q foi separado e junta novamente""")

