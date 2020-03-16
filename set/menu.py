import os
from init import Init
from command import Command

class Menu():
    if os.path.isfile(os.getcwd() + '/set.ini'):
        pass
    else:
        Init()
    while True:
        print("\n"+ "*"*40)
        print("Commands:")
        print("q = (q)uit program")
        print("g = (g)et ruc data")
        print("e = (e)xtract data from receipts")
        print("c = (c)onfiguration file")
        print("*"*40)
        input_ = input(":")
        command = Command()

        if input_ == "q":
            break
        if input_ == "g":
            command.g()
        if input_ == "e":
            command.e()
        if input_ == "c":
            command.c()
