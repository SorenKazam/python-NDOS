from imports import *

from os import system as system_command
from os import name as system_name


def Clr():

    # for windows
    if system_name == 'nt':
        _ = system_command('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system_command('clear')
