import sys, os
import importlib
from src.web_scraper import WebScraper
from src.custom_request import HTTPRequests
from src.utils import checkfilename
import json

#<----------------------------------------------------------->
# Capturar la configuración pasada como argumento en la terminal
if len(sys.argv) > 1:
    configfile = sys.argv[1]
else:
    configfile = input("Introduce un archivo de configuración: ")
#<----------------------------------------------------------->
# Importar la configuración pasada
cnf = importlib.import_module('cnf.'+configfile)
args = cnf.args
#<----------------------------------------------------------->
# Definir nombre del archivo donde se exportará la data
# Por terminal o por archivo de configuración
if len(sys.argv) > 2:
       namefile = sys.argv[2]
else:
       namefile = args.SAVE_FILE_NAME
#<----------------------------------------------------------->
# Crear directorio donde se exportará la data
if not os.path.isdir(args.EXP_DIR):
    os.makedirs(args.EXP_DIR)
#<----------------------------------------------------------->
# Instancias necesarias para realizar el web scraping
session = HTTPRequests(headers=args.HEADERS, data=args.DATA, parallel=args.PARALLEL)
scraper = WebScraper(session)
# Run Script
results = scraper.run(args.REGISTROS)
#<----------------------------------------------------------->
# Exportar resultados a archivo JSON
path = f"{args.EXP_DIR}/{namefile}"
with open(checkfilename(path)+".json", "w") as file:
    for result in results:
       file.write(json.dumps(result['Marca']['Instancias'], indent=4, ensure_ascii=False))
       file.write("\n")