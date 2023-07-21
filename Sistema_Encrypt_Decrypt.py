import cryptocode
from colorama import init, Fore, Back, Style
init(autoreset=True)

opcao_do_menu = 0

def menu():
  print(Fore.GREEN + 47*"=")
  print(Back.GREEN + "** Bem-vindo ao Sistema de Encrypt e Decrypt **")
  print(Fore.GREEN + 47*"=")
  print("[1] -----> Criptografar")
  print("[2] -----> Descriptografar")
  print("[3] -----> Sair")
  print(Fore.GREEN + 47*"=")

menu()
opcao_do_menu = int(input("\nDigite a opção desejada: "))

while True:
    if opcao_do_menu == 1:
        print(Fore.GREEN + "Opção escolhida: 1 - Criptografar")
        opcao_do_menu = 0
        mensagem = input("Digite o texto a ser criptografado: \n") [::-1]
        chave = "1024"
        mensagemCriptografada = cryptocode.encrypt(mensagem, chave)
        print(mensagemCriptografada)
        print("\n")
        menu()
        opcao_do_menu = int(input("\nDigite a opção desejada: "))

    elif opcao_do_menu == 2:
        print(Fore.GREEN + "Opção escolhida: 2 - Descriptografar")
        mensagemCripto = input("Coloque a criptografia aqui: \n")
        chave = "1024"
        mensagemDescripto = cryptocode.decrypt(mensagemCripto, chave) [::-1]
        print(Fore.GREEN + mensagemDescripto)
        print("\n")
        opcao_do_menu = 0
        menu()
        opcao_do_menu = int(input("\nDigite a opção desejada: "))

    elif opcao_do_menu == 3:
        print(Fore.GREEN + "Opçaõ escolhida: 3 - Sair")
        resposta_de_saida = input("Deseja mesmo sair? (S/N) ").upper()
        if (resposta_de_saida == "S") or (resposta_de_saida == "SIM"):
            break
        else:
            print("\n")
            menu()
            opcao_do_menu = 0
            opcao_do_menu = int(input("\nDigite a opção desejada: "))