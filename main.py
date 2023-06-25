from src.custom_request import HTTPRequests
from src.web_scraper import WebScraper
from src.scraper import MiniScraper
from src.utils import checkfilename
import importlib
import sys, os
import json

# <----------------------------------------------------------->
# Capturar la configuración pasada como argumento en la terminal
if len(sys.argv) > 1:
	configfile = sys.argv[1]
else:
	configfile = input("Introduce un archivo de configuración: ")
# <----------------------------------------------------------->
# Importar la configuración pasada
cnf = importlib.import_module('config_files.'+configfile)
args = cnf.args
# <----------------------------------------------------------->
# Definir nombre del archivo donde se exportará la data
# Por terminal o por archivo de configuración
if len(sys.argv) > 2:
	   namefile = sys.argv[2]
else:
	   namefile = args.SAVE_FILE_NAME
# <----------------------------------------------------------->
# Crear directorio donde se exportará la data
if not os.path.isdir(args.EXP_DIR):
	os.makedirs(args.EXP_DIR)
# <----------------------------------------------------------->
# Instancias necesarias para realizar el web scraping
session = HTTPRequests(headers=args.HEADERS, data=args.DATA, parallel=args.PARALLEL)
scraper = WebScraper(session)
# Run Script
results = scraper.run(args.REGISTROS)
# <----------------------------------------------------------->
# Creación de diccionario para almacenar los valores requeridos
data_extractor = MiniScraper()
extracted_data = {}

for result in results:
	try:
		nroRegistro = data_extractor.getNroRegistro(result)
		extracted_data[nroRegistro] = {
			"Observada_de_Fondo": data_extractor.getObservadaFechaFondo(result),
			"Apelaciones": data_extractor.getApelaciones(result),
			"IPT": data_extractor.getIPT(result),
		}
	except Exception as e:
		print("ERROR: {e}")
		continue
# <----------------------------------------------------------->
# Exportar valores a un archivo JSON
path = f"{args.EXP_DIR}/{namefile}"
with open(checkfilename(path)+".json", "w") as file:
	json.dump(extracted_data, file, indent=4)