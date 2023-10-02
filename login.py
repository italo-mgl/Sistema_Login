from os import system
from colorama import init, Fore, Back, Style
from getpass import getpass
import stdiomask
from time import sleep
init(autoreset=True)

# Criando Menu de Opções


def exibir_menu():
    print(Fore.GREEN + '''     Bem-Vindos ao Projeto Sstema de Login
          Escolha uma opção:
          [1] Cadastrar novo usuário
          [2] Fazer login
          [3] Sair ou digite Enter
          ''')
    try:
        opcao = int(input("Digite sua opção: "))
        return (opcao)
    except ValueError:
        print()


# Fazer login com nome e senha de usuario

def fazer_login():
    login = input("Nome: ")
    senha = stdiomask.getpass(prompt="Senha: ", mask="*")
    return (login, senha)

# Pesquisar no arquivo usuarios.txt


def buscar_usuario(login, senha):
    usuarios = []
    try:
        with open("usuarios.txt", "r+", encoding="Utf-8", newline='') as arquivo:
            for linha in arquivo:
                linha = linha.strip(",")
                usuarios.append(linha.split())

        # logi, senha = fazer_login()
        for usuario in usuarios:
            nome = usuario[0]
            password = usuario[1]
            if login == nome and senha == password:
                return True
    except FileNotFoundError:
        return False


while True:
    system("cls")
    opcao = exibir_menu()

    if opcao == 1:
        # Cadastrar novo usuario
        login, senha = fazer_login()
        if login == senha:
            print("Sua senha deve ser diferente do login.")
            senha = getpass("Senha: ")
        user = buscar_usuario(login, senha)
        if user == True:
            print(Fore.RED + "Usuario ja existe!")
            sleep(2)
            # exit()

        else:
            with open("usuarios.txt", "a+", encoding="Utf-8", newline="") as arquivo:
                arquivo.writelines(f"{login} {senha}\n")
                print(Fore.CYAN + "Cadastro aprovado !")
                exit()

    elif opcao == 2:
        # Fazer o login do usuario
        login, senha = fazer_login()
        user = buscar_usuario(login, senha)
        if user == True:
            print(Fore.CYAN + "Login realizado com sucesso!")
            sleep(2)
            exit()
    else:
        system("cls")
        print(Fore.LIGHTMAGENTA_EX + "Goodbay!!")
        break
