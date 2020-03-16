try:
    from PIL import Image
except ImportError:
    import Image
from dateutil.parser import parse
from datetime import datetime
import pytesseract
import re
import os
import csv
import configparser

class SetPy():
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("user.ini")
        pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'
        self.ruc = self.config['informante']['ruc'] + '-' + self.config['informante']['dv']
    
    def invoice_to_text(self, file):
        text = pytesseract.image_to_string(Image.open(file), lang='spa')
        ruc_pattern = re.compile('RUC|R.U.C.', re.I)
        timbrado_pattern = re.compile('TI.BRADO', re.I)
        fecha_pattern = re.compile("[0-9]{2}\/[0-9]{2}\/[0-9]{4}|[0-9]{2}\/[0-9]{2}\/[0-9]{2}|[0-9]{1}\/[0-9]{1}\/[0-9]{4}|[0-9]{1}\/[0-9]{1}\/[0-9]{2}")
        factura_pattern = re.compile('[0-9]{3}\-[0-9]{3}\-[0-9]{7}')
        total_pattern = re.compile('TOTAL', re.I)

        l_ruc = []
        l_fecha = []
        l_total = []

        r_ruc = ''
        r_razon_social = ''
        r_timbrado = ''
        r_documento = ''
        r_fecha = ''
        r_total = ''

        f = os.getcwd() + '/assets/rucs/ruc.csv'
        with open(f, 'rt' ) as f:
            reader = csv.reader(f, delimiter='|')
            for line in text.splitlines():
                if re.findall(ruc_pattern, line):
                    l_ruc = re.findall('\d+-\d', line)
                    if (self.ruc != l_ruc[0]):
                        r_ruc = l_ruc[0]
                        for row in reader:
                            if l_ruc[0] == row[0]+'-'+row[2]:
                                razon_social = 'RAZON SOCIAL: ' + row[1]
                                r_razon_social = row[1]
                            else:
                                razon_social = 'RAZON SOCIAL: '
                if re.findall(timbrado_pattern, line):
                    try:
                        r_timbrado = re.findall('\d+', line)[0]
                    except:
                        print('No se encontro TIMBRADO')
                if re.findall(factura_pattern, line):
                    try:
                        r_documento = re.findall(factura_pattern, line)[0]
                    except:
                        print('No se encontro DOCUMENTO')
                if re.findall(fecha_pattern, line):
                    fp = parse(re.findall(fecha_pattern,line)[0], yearfirst=False, dayfirst=True)
                    l_fecha.append(fp)
                if re.findall(total_pattern, line):
                    total_list = re.findall('\d+', line)
                    t = ''
                    for l in total_list:
                        t = t + l
                    if t != '':
                        l_total.append(t)
            i_total = list(map(int, l_total))
            r_total = str(max(i_total))
            s_fecha = l_fecha
            s_fecha = sorted(l_fecha)
            r_fecha = s_fecha[1].strftime("%d/%m/%Y")
            result = [r_ruc, r_razon_social, r_timbrado, r_documento, r_fecha, r_total]
            values = ','.join(result)
            return(result)