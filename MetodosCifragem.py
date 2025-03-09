import string
def inverter(string,arquivo):
    invertida = string[::-1]
    with open(f"{arquivo[:-4]}-inversão.txt", "w",encoding="utf-8") as cifrada:
        cifrada.write(invertida)
        cifrada.close()
    print(f"A mensagem cifrada é: {invertida}")

def deslocar(arquivo,texto,deslocamento):
    deslocamento = string.ascii_letters[deslocamento:] + string.ascii_letters[:deslocamento]
    tabela = str.maketrans(string.ascii_letters, deslocamento)
    deslocado = texto.translate(tabela)
    with open(f"{arquivo[:-4]}-deslocamento.txt", "w",encoding="utf-8") as cifrada:
        cifrada.write(deslocado)
        cifrada.close()
    print(f"A mensagem cifrada é: {deslocado}")

def substituicao(texto,arquivo):
    tabela = str.maketrans(string.ascii_letters,"0c|[<z4rM,V@;bjsWE-XN~25x#n`>e(fy^Bo.?gDC/FOlm!{3P9*")
    substituido = texto.translate(tabela)
    with open(f"{arquivo[:-4]}-substituição.txt","w",encoding="utf-8") as cifrada:
        cifrada.write(substituido)
        cifrada.close()
    print(f"A mensagem cifrada é: {substituido}")




