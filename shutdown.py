from imports import *
import sys


def Shutdown():
    print("Shutting down...")
    time.sleep(5)
    try:
        sys.exit()
    except:
        print(":( Fatal error ao desligar, desligue a maquina da energia.")
