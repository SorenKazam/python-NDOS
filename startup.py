from imports import *
import os
import shutil
from app import Main
import getpass
import hashlib
from app import Main


def createUser():
    print("Welcome to NiverDOS")

    # Abrir o arquivo JSON em modo de leitura
    with open("data.json", "r") as f:
        data = json.load(f)

    # Obter informações do usuário
    name = input("Digite o nome do usuário: ")
    while True:
        psw = getpass.getpass("Digite password: ")
        psw_confirm = getpass.getpass("Repita sua password: ")
        if psw != psw_confirm:
            print("As passwords nao sao iguais...")
            continue
        else:
            break
    hsd_pwd = hashlib.sha256(psw.encode('utf-8')).hexdigest()
    admin = input("O usuário é administrador? (s/n): ")

    # Converter a resposta do usuário para um valor booleano
    if admin.lower() == "s":
        admin = True
    else:
        admin = False

    # Adicionar as informações do usuário à lista "users"
    if psw == "":
        data["users"].append({"name": name, "pass": "", "admin": admin})
    else:
        data["users"].append({"name": name, "pass": hsd_pwd, "admin": admin})

    # Abrir o arquivo JSON em modo de escrita e salvar as informações
    with open("data.json", "w") as f:
        json.dump(data, f)

    print(
        f"Bem-vindo, {name}! As informações do usuário foram salvas com sucesso!")

    # Criar uma pasta com o nome do usuário
    try:
        os.makedirs(os.path.join("users", name))
        Main()
    except:
        print("Conflito, pasta de user ja existe no sistema, pode ter ocurrido por uma má formatação anterior.")
        print(f"pasta: users\{name}")
        i = input("Pretende eleminar a pasta anterior? (s/n)")

        if i.lower() == "s":
            try:
                shutil.rmtree(f"users\{name}")
                print("Pasta removida com sucesso, criando a nova pasta!")
                print("Criando nova pasta...")
                os.makedirs(os.path.join("users", name))
                print("Pasta e user criados com sucesso!")
                Main()
                time.sleep(5)
            except OSError as e:
                print("Erro ao excluir a pasta:", e)

    time.sleep(5)
