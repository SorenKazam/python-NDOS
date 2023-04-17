from imports import *

import getpass
import hashlib

SEPARADOR = "-" * 17
NOME_APP = "|    NIVER DOS  |"

activeUser = "d"


def Main(activeUser):
    # primeira verificação: verifica se existem users na memoria
    with open('data.json', 'r') as data:
        data = json.load(data)

    users = data['users']
    print(SEPARADOR)
    print(f"{NOME_APP}")
    print(SEPARADOR)

    activeUser = ""

    if len(users) == 0:
        print("Não existem usuários no sistema...")
        time.sleep(5)
        startup.createUser()
    else:
        if activeUser == "":
            print("Selecione um usuário da lista")
            for user in users:
                if user.get('admin'):
                    print("* " + user['name'])
                else:
                    print(user['name'])

            while True:
                i = input("selecione o usuário > ")
                for user in users:
                    if user['name'] == i:
                        if user['pass']:
                            while True:
                                # pergunta a pass
                                i = getpass.getpass(
                                    f"Digite a senha para {user['name']}: ")

                                # pega na pass e encripta para o mesmo encript do db
                                password_to_hash = hashlib.sha256(
                                    i.encode('utf-8')).hexdigest()

                                # compara a pass encriptada com a pass da db
                                if password_to_hash == user['pass']:
                                    print(
                                        f"Password correcta, bem-vindo {user['name']}")
                                    break
                                else:
                                    print("Password incorrecta!")
                                    continue

                        activeUser = user
                        break

                if activeUser != "":
                    Menu(activeUser)


if __name__ == "__main__":
    Main(activeUser)
