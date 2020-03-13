import os
import sys
from fnmatch import fnmatch
from setpy import SetPy
from utils import Utils
from setting import Setting

def menu():
    print("************MENU PRINCIPAL**************")
    opcion = input(
    """
1: Get RUC files
2: Opcion 2
3: Opcion 3
q: Salir

Ingresar opcion: """)

    if opcion == "1":
        os.system('clear')
        setting = Setting()
        utils = Utils()
        utils.download(setting.url, setting.root + '/tmp/')
        utils.extract(setting.root + '/tmp/', setting.root + '/tmp/')
        menu()
    elif opcion == "2":
        os.system('clear')
        menu()
    elif opcion == "3":
        os.system('clear')
        setpy = SetPy()
        setting = Setting()
        print('RUC,RAZON SOCIAL,TIMBRADO,DOCUMENTO,FECHA,TOTAL')
        for month in range(1, 12):
            directory = setting.root + setting.receipts + setting.periodo + '/' + ('%02d' % month)
            if os.path.exists(directory):
                files = os.listdir(setting.root + setting.receipts + setting.periodo + '/' + ('%02d' % month))
                for file in files:
                    if fnmatch(file, '*.jpg'):
                        setpy.invoice_to_text(directory + '/' + file)
        menu()
    elif opcion == "9":
        os.system('clear')
        sys.exit(1)
    else:
        os.system('clear')
        print("Solo puede usar la opcion 1, 2, 3 y 9")
        print("Por favor intente de nuevo")
        menu()

if __name__ == "__main__":
    menu()