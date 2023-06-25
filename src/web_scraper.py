from src.custom_request import HTTPRequests
from src.scraper import MiniScraper

import json
import time
import asyncio

class WebScraper(MiniScraper):

    def __init__(self, session:HTTPRequests):
        self.session = session
    
    def getData(self, nroRegisto:int):
        intentos = 3

        while intentos > 0:
            try:
                response1 = self.session.get("https://ion.inapi.cl/Marca/BuscarMarca.aspx")

                self.session.dataPost1["Hash"] = self.getHdnHash(response1)
                self.session.dataPost1["IDW"] = self.getHdnIDW(response1)
                self.session.dataPost1["param2"] = nroRegisto

                self.session.dataPost2["IDW"] = self.getHdnIDW(response1)

                response2 = self.session.post("https://ion.inapi.cl/Marca/BuscarMarca.aspx/FindMarcas", data=self.session.dataPost1)

                self.session.dataPost2["numeroSolicitud"], self.session.dataPost2["Hash"] = self.getHdnSolicitudAndHdnHash(response2)

                response3 = self.session.post("https://ion.inapi.cl/Marca/BuscarMarca.aspx/FindMarcaByNumeroSolicitud", data=self.session.dataPost2)

                data_json = response3.json()['d']

                return json.loads(data_json)
            
            except Exception as e:
                print(f"\nError en la solicitud - ERROR {e}\nReintentando en 5 segundos...\n")
                intentos -= 1
                time.sleep(5)
        return None
    
    def getMultipleData(self, solicitudes:list):
        data = []
        start = time.perf_counter()

        for solicitud in solicitudes:
            start_reg = time.perf_counter()

            print(f"\nSolicitud: {solicitud}")
            solicitudData = self.getData(solicitud)
            if solicitudData != None:
                data.append(solicitudData)
            else:
                print(f"\nError en la solicitud: {solicitud}")
                continue

            end_reg = time.perf_counter()
            print(f"\nSolicitud: {solicitud} - {end_reg-start_reg} segundos")

        end = time.perf_counter()
        print(f"\n[>] Tiempo total: {end-start} segundos [<]".upper())
        
        return data

    # async def __asyncSetData(self, dataToSet:dict, nroRegistro:int):
    #     dataSet = dataToSet
    #     response = await self.session.async_get("https://ion.inapi.cl/Marca/BuscarMarca.aspx")
        
    #     if "numeroSolicitud" in dataSet:
    #         dataSet["numeroSolicitud"], dataSet["Hash"] = self.getHdnSolicitudAndHdnHash(
    #             await self.session.async_post(
    #                 url = "https://ion.inapi.cl/Marca/BuscarMarca.aspx/FindMarcas",
    #                 data = await self.__asyncSetData(dataToPOST1, nroRegistro=nroRegistro)
    #             )
    #         )
    #         dataSet["IDW"] = self.getHdnIDW(response)
    #     else:
    #         dataSet["Hash"] = self.getHdnHash(response)
    #         dataSet["IDW"] = self.getHdnIDW(response)
    #         dataSet["param2"] = nroRegistro;
    #     return dataSet
    
    # async def asyncGetData(self, nroRegisto:int):
    #     response = await self.session.async_post(
    #         url = "https://ion.inapi.cl/Marca/BuscarMarca.aspx/FindMarcaByNumeroSolicitud",
    #         data = await self.__asyncSetData(dataToPOST2, nroRegistro=nroRegisto)
    #     )
    #     data_json = response.json()['d']
    #     return json.loads(data_json)
    
    # async def asyncGetMultipleData(self, solicitudes:list):
    #     data = []
    #     for solicitud in solicitudes:
    #         start_reg = time.perf_counter()
    #         data.append(await self.asyncGetData(solicitud))
    #         end_reg = time.perf_counter()
    #         print(f"Solicitud: {solicitud} - {end_reg-start_reg} segundos")
    #     return await asyncio.gather(*data)
    
    def run(self, solicitudes:list):
        if self.session.parallel:
            return asyncio.run(self.asyncGetMultipleData(solicitudes))
        else:
            return self.getMultipleData(solicitudes)