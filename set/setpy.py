try:
    from PIL import Image
except ImportError:
    import Image
from dateutil.parser import parse
from datetime import datetime
import pytesseract
import re
from setting import Setting

class SetPy():
    def __init__(self):
        setting = Setting()
        pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'
        self.path = setting.root
        self.ruc = setting.ruc
    
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

        print("************ DATOS **************")
        for line in text.splitlines():
            if re.findall(ruc_pattern, line):
                l_ruc = re.findall('\d+-\d', line)
                if (self.ruc != l_ruc[0]):
                    print('RUC: ' + l_ruc[0])
            if re.findall(timbrado_pattern, line):
                print('TIMBRADO: ' + re.findall('\d+', line)[0])
            if re.findall(factura_pattern, line):
                print('FACTURA: ' + re.findall(factura_pattern, line)[0])
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
        print('TOTAL: ' + str(max(i_total)))
        s_fecha = l_fecha
        s_fecha = sorted(l_fecha)
        print('FECHA: ' + s_fecha[1].strftime("%d/%m/%Y"))