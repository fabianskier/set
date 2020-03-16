import os
import sys
import csv
import configparser
from pathlib import Path
from fnmatch import fnmatch
from utils import Utils
from setpy import SetPy

class Command():
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("set.ini")

    def g(self):
        utils = Utils()
        #utils.download(self.config['default']['ruc_url'], self.config['default']['tmp'])
        utils.extract(self.config['default']['tmp'], self.config['default']['tmp'])
    
    def e(self):
        setpy = SetPy()
        with open('output.csv', 'w', newline='') as result:
            writer = csv.writer(result)
            for month in range(1, 12):
                directory = self.config['default']['receipts'] + self.config['default']['periodo'] + '/' + ('%02d' % month)
                if os.path.exists(directory):
                    files = os.listdir(self.config['default']['receipts'] + self.config['default']['periodo'] + '/' + ('%02d' % month))
                    for file in files:
                        if fnmatch(file, '*.jpg'):
                            print(directory + '/' + file)
                            a = setpy.invoice_to_text(directory + '/' + file)
                            writer.writerow(a)
    
    def c(self):
        config = configparser.ConfigParser()
        config.read("set.ini")
        for section in config.sections():
            print(section)
            for key in config[section]:
                print('\t' + config[section][key])