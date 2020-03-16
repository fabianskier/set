from pathlib import Path
import configparser


class Init():
    def __init__(self):
        config = configparser.ConfigParser()
        config['default'] = {   'root': str(Path.cwd()) + "/", 
                                'tmp': str(Path.cwd().joinpath(Path("tmp"))) + "/",
                                'assets': str(Path.cwd().joinpath(Path("assets"))) + "/",
                                'receipts': str(Path.cwd().joinpath(Path("assets")).joinpath(Path("receipts"))) + "/",
                                'rucs': str(Path.cwd().joinpath(Path("assets")).joinpath(Path("rucs"))) + "/", 
                                'ruc_url': 'https://www.set.gov.py/rest/contents/download/collaboration/sites/PARAGUAY-SET/documents/informes-periodicos/ruc/',
                                'ruc_extension': 'ruc.zip',
                                'periodo': '2020'
                            }
        with open('set.ini', 'w') as configfile:
            config.write(configfile)