from MetodosCifragem import *
import os

execucao = True

while execucao:
    arquivo = input("Digite o nome do arquivo a ser criptografado:")
    escolha = input("Selecione o método de cifragem: \n1 - Inversão\n2 - Deslocamento\n3 - Substituição\n4 - Encerrar programa\n")
    # if arquivo == "4":
    #     print("Encerrando programa...")
    #     break
    with open(arquivo,"r",encoding="utf-8") as mensagem:
        texto = mensagem.read()
        texto = str(texto)



    if escolha == "1":
        inverter(texto,arquivo)
    elif escolha == "2":
        deslocamento = int(input("Informe o deslocamento: "))
        deslocar(arquivo,texto,deslocamento)
    elif escolha == "3":
        substituicao(texto,arquivo)
    elif escolha == "4":
        print("Encerrando programa...")
        execucao = False
    else:
        print("Escolha inválida!")

    escolha = input("Deseja criptografar outro arquivo? S/N")
    escolha = escolha.upper()
    if escolha == "S":
        continue
    else:
        print("Encerrando programa...")
        break


