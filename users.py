from imports import *
import json
import shutil
from app import Main


def Users(activeUser):
    selectedUser = ""
    activeUser = activeUser['name']

    # mostra a lista de users
    with open('data.json', 'r') as data:
        data = json.load(data)

    users = data['users']
    print("----- Users -----")
    for user in users:
        if user.get('admin'):
            print("* " + user['name'])
        else:
            print(user['name'])
    print("-----------------")

    # cursor "users" a espera de comando
    while True:
        if selectedUser == "":
            i = input(f"{activeUser}@users > ")
        else:
            i = input(f"{activeUser}@[{selectedUser['name']}] > ")

        if i == "exit":
            break
        elif i == "delete":
            delete_user(selectedUser, users, activeUser)

        elif i == "select":
            i = input(f"{activeUser}@select user > ")

            for user in users:
                if user['name'] == i:
                    selectedUser = user
                    break

            if selectedUser != "":
                if selectedUser['admin'] == True:
                    print(f"Administrador {selectedUser['name']} selecionado.")
                else:
                    print(f"User {selectedUser['name']} selecionado.")
            else:
                print(f"Usuário {i} não encontrado.")
                continue


def delete_user(selectedUser, users, activeUser):
    activeUser = activeUser
    if selectedUser != "":
        i = input(
            f"You sure you want to remove the user {selectedUser['name']}? (y/n)")
        if i.lower() != "y":
            Users(activeUser)
        else:
            try:
                for user in users:
                    if user["name"] == selectedUser['name']:
                        users.remove(user)
                        # Salvar a estrutura JSON atualizada em um arquivo
                        with open("data.json", "w") as f:
                            json.dump({"users": users}, f)

                        # deleta a pasta do user
                        shutil.rmtree(f"users/{selectedUser['name']}")
                        print(f"Usuário {selectedUser['name']} foi removido.")
                        selectedUser = ""
                users()
            except:
                print("erro ao tentar remover")
    else:
        print("Nenhum usuário selecionado.")
