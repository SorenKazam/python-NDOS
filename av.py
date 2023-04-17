import os
import json
import requests
import sys
import shutil


def Nosav(activeUser):
    print("----- Niver NOSAV -----")
    print("Niver Open-Source Anti-Virus")

    i = input("Pretende verificar o sistema? (s/n) ")

    if i.lower() != "s":
        print("Saindo do NOSAV...")
        return

    i = input("Pretende utilizar o servidor default? (s/n): ")

    if i.lower() == "s":
        url = 'https://raw.githubusercontent.com/SorenKazam/NOSAV/main/list.json'
        print(f"Usando servido: {url}")
    else:
        url = input("Que servidor pretende utilizar?(cole o link aqui): ")

    print("Estabelecendo ligaçao com o servidor...")

    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Ligação bem sucedida!")
    except:
        print("ERRO NO REQUEST")
        return

    data = json.loads(response.text)

    # storage
    files = []
    infectedFilesList = []
    cleanFiles = 0
    infectedFiles = 0
    totalFiles = 0
    scannedFiles = 0

    i = input("Qual pasta deseja scanear? ")

    if i.lower() == "exit" or i == "":
        print("Saindo...")
        return
    else:
        folderExist = os.path.exists(i)
        if folderExist == False:
            print(f"A pasta '{i}' nao existe")
            return
        else:
            folder = i
            print(f"Pasta [{folder}] aceite")
            print(f"Verificando {folder}...")

    # Scan
    for file in os.listdir(folder):  # aqui é a pasta que ira ser analisado
        scannedFiles += 1
        print(
            f"Folder: {os.path.normcase(folder)} Fase 1: {scannedFiles} Ficheiros scaneados. Examinando ficheiro: {os.path.basename}")

        if os.path.basename(file[0]) == "av.py":
            continue

        files.append(folder)
        print(f"{files} isto é o que esta dentro de files")

    # Compare
    fase = 0
    for file in files:
        for item in data:
            totalFiles += 1
            fase += 1
            filelower = file.lower()
            filelower = os.path.splitext(file)[0]
            ficheiroPasta = os.path.join(folder, file)

            print(
                f"Fase: {fase} > Item: {ficheiroPasta}")
            if item['name'] == filelower:
                print(
                    f"Fase 2: O ficheiro: {os.path.basename(file[0])} no caminho: {file} existe na lista JSON com o tipo: {item['type']}.")
                infectedFiles += 1
                infectedFilesList.append(filelower)
                break
            else:
                cleanFiles += 1

    # Output
    print(
        f"{totalFiles} Ficheiros analisados | {cleanFiles} ficheiros limpos | {infectedFiles} ficheiros infetados ")
    print(f"{files}")

    if infectedFiles >= 1:
        print(f"Ficheiro infectados: {files}")
        while True:
            delete = input("Deseja eleminar os ficheiros infectados? (Y/n): ")

            if delete == "Y" or delete == "y":
                print("Apagando ficheiros...")

                for file in files:
                    print(file)
                    os.remove(file)
                    print(f"apagando: {file}")
            else:
                print("Saindo do AV...")
                return
        else:
            print("Sistema limpo, saindo...")
            return
