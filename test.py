from web_scraper import WebScraper
from custom_request import HTTPRequests
from dataForRequests import headers
import json

miSesion = HTTPRequests(headers)
miScraper = WebScraper(miSesion)

numeroSolicitud = 1236216

response = miScraper.getData(numeroSolicitud)

json_formatted_str = json.dumps(response['Marca']['Instancias'], indent=4, ensure_ascii=True)

print(type(response))

# FUNCIONA