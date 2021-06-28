from exe115.lib.arquivo import *
from exe115.lib.interface import *

arq = 'cursoemvideo.txt'

if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resp == 1:
        lerarquivo(arq)
    elif resp == 2:
        cabecalho('NOVO CADASTRO')
        n = str(input('Nome:')).title().strip()
        i = int(input('Idade:'))
        adicionar(arq, n, i)
    elif resp == 3:
        cabecalho('Saindo do sistema... Até logo')
        break
    else:
        cabecalho('\033[0;31mOpção invalida! Tente novamente...\033[m', 50)
    sleep(2)
