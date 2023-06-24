from requests_html import AsyncHTMLSession
import asyncio
import time
from scraper import MiniScraper
from web_scraper import WebScraper
from custom_request import HTTPRequests
from dataForRequests import headers, dataToPOST1, dataToPOST2
import json

# miSesion = HTTPRequests(headers, parallel=True)
# miScraper = WebScraper(miSesion)

# response = miSesion.post("https://ion.inapi.cl/Marca/BuscarMarca.aspx/GetEstadosInstancias", data={})
# print(response.json())

# numerosSolicitud = [1236216, 1236222]

# responses = miScraper.run(solicitudes=numerosSolicitud)

# json_formatted_str = json.dumps(response['Marca']['Instancias'], indent=4, ensure_ascii=False)

# print(json_formatted_str)

# FUNCIONA

# ---------------------------------------------------------------------------- #
miScraper = MiniScraper()

async def async_get(session, url:str):
    response = await session.get(url, headers=headers)
    print(response.status_code, response.reason)
    await response.html.arender(timeout=20)
    
    return response.text

# async def async_post(session, url:str, data:dict):
#     response = await session.post(url, headers=headers, json=data)
#     print(response.status_code, response.reason)  
#     return response

# async def asyncSetData(session, scraper, dataToSet:dict, nroRegistro:int):
#     dataSet = dataToSet
#     response = await async_get(session, "https://ion.inapi.cl/Marca/BuscarMarca.aspx")
    
#     if "numeroSolicitud" in dataSet:
#         dataSet["numeroSolicitud"], dataSet["Hash"] = scraper.getHdnSolicitudAndHdnHash(
#             await async_post(
#                 session,
#                 url = "https://ion.inapi.cl/Marca/BuscarMarca.aspx/FindMarcas",
#                 data = await asyncSetData(session, scraper, dataToPOST1, nroRegistro=nroRegistro)
#             )
#         )
#         dataSet["IDW"] = scraper.getHdnIDW(response)
#     else:
#         dataSet["Hash"] = scraper.getHdnHash(response)
#         dataSet["IDW"] = scraper.getHdnIDW(response)
#         dataSet["param2"] = nroRegistro;
#     return dataSet

# async def asyncGetData(session, scraper, nroRegisto:int):
#     response = await async_post(
#     session,
#     url = "https://ion.inapi.cl/Marca/BuscarMarca.aspx/FindMarcaByNumeroSolicitud",
#     data = await asyncSetData(session, scraper, dataToPOST2, nroRegistro=nroRegisto)
#     )
#     data_json = response.json()['d']
#     return json.loads(data_json)

miScraper = MiniScraper()

async def main():
    session = AsyncHTMLSession()
    tasks = [async_get(session, "https://ion.inapi.cl/Marca/BuscarMarca.aspx") for _ in range(3)]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    await session.close()
    
    return results

start = time.perf_counter()
resultados = asyncio.run(main())
print(resultados)
end = time.perf_counter()
print(f"Tiempo de ejecución: {end - start:0.2f} segundos")
asyncio.close()