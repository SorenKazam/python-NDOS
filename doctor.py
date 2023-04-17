from imports import *
import imports as imp
import string


def Doctor(activeUser):
    tests = 0
    problems = 0

    print("----- NIVER DOS DOCTOR -----")

    while True:
        try:
            x = input("Quantos testes pretende realizar em cada etapa? ")
            times = int(x)
            break

        except ValueError:
            print("Erro: não é um número válido.")
            continue

    print("Testing strings...")
    try:
        tests += 1
        for i in range(times):
            print(f"Stage: {i} Output: {string.ascii_uppercase}")
        print("Ok")
    except:
        problems += 1
        tests += 1
        print("Problem")
    print("----------------------------")

    print("Testing numbers...")
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    try:
        tests += 1
        for i in range(times):
            print(f"Stage: {i} Output: {nums}")
        print("Ok")
    except:
        problems += 1
        tests += 1
        print("Problem")
    print("----------------------------")

    print("Testing User info...")
    user = activeUser
    if user:
        try:
            tests += 1
            for i in range(times):
                print(f"Stage: {i} Output: {user}")
            print("Ok")
        except:
            problems += 1
            tests += 1
            print("Problem")
    else:
        problems += 1
        print("User nao detectado")
    print("----------------------------")

    print("Testing imports...")
    if imp:
        print("Imports detected")
        try:
            tests += 1
            for i in range(times):
                print(f"Stage: {i} Output: {imp}")
            print("Ok")
        except:
            problems += 1
            tests += 1
            print("Problem")
    else:
        print("Imports not detected!")
        problems += 1
    print("----------------------------")

    print("------ RESULTADOS DO DOCTOR ------")
    print(f"Efectuado: {tests} testes")
    print(f"Problemas detectados: {problems}")
    print("---------------------------------")
