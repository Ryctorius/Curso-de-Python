def leiadinheiro(txt):
    valido = False
    while valido is False:
        resp = str(input(txt)).strip().replace(',', '.')
        if resp.isalpha() or resp == '':
            print(f"\033[0;31mERRO: {resp} é um DADO INVÁLIDO! TENTE NOVAMENTE...\033[m")
        else:
            valido = True
            return float(resp)
