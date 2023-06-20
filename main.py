from requests_html import HTMLSession
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import json

# AL FIN
# Pude recuperar la data final despues de encadenar varias peticiones
# Por lo visto no necesito renderizar cada vez que hago una petición
# Pero no encuentro los valores hdnIDW y hdnHash del principio asi que si o si renderizo ahí
# Seguro hay formas mas eficientes de hacerlo, estaré viendo como avanzar
# Lo mas importante es que al menos ya dispongo de una forma de conseguir la data que necesito

numeroSolicitud = 1236216

URL = ["https://ion.inapi.cl/Marca/BuscarMarca.aspx",
       "https://ion.inapi.cl/Marca/BuscarMarca.aspx/FindMarcas",
       "https://ion.inapi.cl/Marca/BuscarMarca.aspx/FindMarcaByNumeroSolicitud"]

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json; charset=UTF-8',
    # 'Cookie': 'ASP.NET_SessionId=5jvnqbbd42hipwjnans0ph1r; pnctest=1; _gid=GA1.2.111741820.1686768550; _gat=1; _gat_gtag_UA_55154893_3=1; _ga_B2C27FPMYG=GS1.1.1686867269.18.1.1686868075.0.0.0; _ga=GA1.1.657243374.1686515091',
    'Origin': 'https://ion.inapi.cl',
    'Referer': 'https://ion.inapi.cl/Marca/BuscarMarca.aspx',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

with HTMLSession() as s:
  response0 = s.get(URL[0], headers=headers)
  response0.html.render(timeout=20)

  hdnIDW0 = response0.html.find('#hdnIDW', first=True).attrs['value']
  hdnHash0 = response0.html.find('#hdnHash', first=True).attrs['value']

  # print(hdnIDW0)
  # print(hdnHash0)

  cookies = s.cookies.get_dict()

  dataToPOST1 = {
    "LastNumSol": 0,
    "Hash": hdnHash0,
    "IDW": hdnIDW0,
    "responseCaptcha": "este texto no se validará",
    "param1": "",
    "param2": numeroSolicitud,
    "param3": "",
    "param4": "",
    "param5": "",
    "param6": "",
    "param7": "",
    "param8": "",
    "param9": "",
    "param10": "",
    "param11": "",
    "param12": "",
    "param13": "",
    "param14": "",
    "param15": "",
    "param16": "",
    "param17": "1"
  }

  response1 = s.post(URL[1], headers=headers, json=dataToPOST1)

  # hdnIDW1 = response1.html.find('#hdnIDW', first=True)
  # hdnHash1 = response1.html.find('#hdnHash', first=True)

  # print(hdnIDW1)
  # print(hdnHash1)
  json_data = json.loads(response1.json()['d'])

  hdnHash1 = json_data['Hash']
  hdnSolicitud = json_data['Marcas'][0]['id']

  print(response1.status_code)
  print(json.dumps(json_data, indent=4))

  dataToPOST2 = {
  "numeroSolicitud": hdnSolicitud,
  "Hash": hdnHash1,
  "IDW": hdnIDW0
  }

  response2 = s.post(URL[2], headers=headers, json=dataToPOST2)

  print(response2.status_code)

  response_data = response2.json()['d']
  json_data = json.loads(response_data)

  json_formatted_str = json.dumps(json_data['Marca']['Instancias'], indent=4, ensure_ascii=True)

  print(json_formatted_str)