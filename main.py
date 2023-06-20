from requests_html import HTMLSession
from dataForRequests import headers, dataToPOST1, dataToPOST2
import json


# AL FIN
# Pude recuperar la data final despues de encadenar varias peticiones
# Por lo visto no necesito renderizar cada vez que hago una petición
# Pero no encuentro los valores hdnIDW y hdnHash del principio asi que si o si renderizo ahí
# Seguro hay formas mas eficientes de hacerlo, estaré viendo como avanzar
# Lo mas importante es que al menos ya dispongo de una forma de conseguir la data que necesito


URL = ["https://ion.inapi.cl/Marca/BuscarMarca.aspx",
       "https://ion.inapi.cl/Marca/BuscarMarca.aspx/FindMarcas",
       "https://ion.inapi.cl/Marca/BuscarMarca.aspx/FindMarcaByNumeroSolicitud"]

numeroSolicitud = 1236216

with HTMLSession() as s:
  response0 = s.get(URL[0], headers=headers)
  response0.html.render(timeout=20)

  hdnIDW0 = response0.html.find('#hdnIDW', first=True).attrs['value']
  hdnHash0 = response0.html.find('#hdnHash', first=True).attrs['value']

  # print(hdnIDW0)
  # print(hdnHash0)

  # cookies = s.cookies.get_dict()

  # dataToPOST1["Hash"] = hdnHash0
  # dataToPOST1["IDW"] = hdnIDW0
  # dataToPOST1["param2"] = numeroSolicitud

  # response1 = s.post(URL[1], headers=headers, json=dataToPOST1)

  # hdnIDW1 = response1.html.find('#hdnIDW', first=True)
  # hdnHash1 = response1.html.find('#hdnHash', first=True)

  # print(hdnIDW1)
  # print(hdnHash1)
  # json_data = json.loads(response1.json()['d'])

  # hdnHash1 = json_data['Hash']
  # hdnSolicitud = json_data['Marcas'][0]['id']

  # print(response1.status_code)
  # print(json.dumps(json_data, indent=4))

  # dataToPOST2["Hash"] = hdnHash1
  # dataToPOST2["IDW"] = hdnIDW0
  # dataToPOST2["numeroSolicitud"] = hdnSolicitud

  # response2 = s.post(URL[2], headers=headers, json=dataToPOST2)

  # print(response2.status_code)

  # response_data = response2.json()['d']
  # json_data = json.loads(response_data)

  # json_formatted_str = json.dumps(json_data['Marca']['Instancias'], indent=4, ensure_ascii=True)

  # print(json_formatted_str)