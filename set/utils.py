import os
import sys
import requests
import zipfile
import glob
import configparser


class Utils():
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("set.ini")
        
    def download(self, url, path):
        if not os.path.exists(path):
            os.makedirs(path)
        for i in range(0, 10):
            filename = self.config['default']['ruc_extension'][:3] + str(i) + self.config['default']['ruc_extension'][3:]
            url = self.config['default']['ruc_url'] + filename
            print(url)
            try:
                r = requests.get(url)
                r.raise_for_status()
                with open(path + filename, "wb") as code:
                    code.write(r.content)
                    print(path + filename + " OK!")
            except requests.HTTPError as err:
                print(err)
                sys.exit(1)
            except requests.ConnectionError as err:
                print(err)
                sys.exit(1)

    def extract(self, origin, destiny):
        zip_files = []
        for file in os.listdir(origin):
            if file.endswith(".zip"):
                zip_files.append(os.path.join(origin, file))
        for x in zip_files:
            with zipfile.ZipFile(x, 'r') as zip_ref:
                zip_ref.extractall(destiny)
            read_files = sorted(
                glob.glob(self.config['default']['tmp']+'*.txt'))
            file = os.path.join(self.config['default']['rucs'], "ruc.csv")
            with open(file, "wb") as outfile:
                for f in read_files:
                    with open(f, "rb") as infile:
                        outfile.write(infile.read())
            for file in glob.glob(self.config['default']['tmp']+'ruc*.txt'):
                os.remove(file)
        for file in glob.glob(self.config['default']['tmp']+'ruc*.zip'):
                os.remove(file)