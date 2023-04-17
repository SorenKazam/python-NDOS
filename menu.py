from imports import *
from shutdown import Shutdown
from doctor import Doctor
from av import Nosav


def Menu(activeUser):
    user = activeUser['name']
    while True:
        i = input(f"{user}> ").lower()

        if i == "help":
            helpList()
        elif i == "users":
            Users(activeUser)
        elif i == "calc":
            calc.Calc()
        elif i == "shutdown":
            Shutdown()
        elif i == "clr":
            Clr()
        elif i == "nosav":
            Nosav(activeUser)
        elif i == "doctor":
            Doctor(activeUser)
        else:
            print("Comando invalido, veja a lista de comando digitando 'help'")
            continue
