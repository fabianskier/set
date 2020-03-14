import os
import requests
import zipfile
import glob
from setting import Setting


class Utils():
    def download(self, url, path):
        setting = Setting()
        if not os.path.exists(path):
            os.makedirs(path)
        for i in range(0, 10):
            filename = setting.extension[:3] + str(i) + setting.extension[3:]
            url = setting.url + filename
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
        setting = Setting()
        for file in os.listdir(origin):
            if file.endswith(".zip"):
                setting.zip_files.append(os.path.join(origin, file))
        for x in setting.zip_files:
            with zipfile.ZipFile(x, 'r') as zip_ref:
                zip_ref.extractall(destiny)
            read_files = sorted(
                glob.glob(setting.root + '/tmp/'+'*.txt'))
            file = os.path.join(setting.root + '/assets/ruc/', "ruc.csv")
            with open(file, "wb") as outfile:
                for f in read_files:
                    with open(f, "rb") as infile:
                        outfile.write(infile.read())
            for file in glob.glob(setting.root + '/tmp/'+'ruc*.txt'):
                os.remove(file)
        for file in glob.glob(setting.root + '/tmp/'+'ruc*.zip'):
                os.remove(file)