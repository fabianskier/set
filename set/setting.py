import os


class Setting:
    def __init__(self):
        self.root = os.getcwd()
        self.facturas = '/facturas'
        self.ruc = '2859784-2'
        self.periodo = '/2020'
        self.url = "https://www.set.gov.py/rest/contents/download/collaboration/sites/PARAGUAY-SET/documents/informes-periodicos/ruc/"
        self.extension = "ruc.zip"
        self.zip_files = []
        self.mode = ['compressed', 'extracted']
        self.slash = "/"
        self.file = "file.txt"