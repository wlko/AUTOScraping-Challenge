from custom_request import HTTPRequests
from scraper import MiniScraper
from dataForRequests import dataToPOST1, dataToPOST2
import json
import time
import asyncio

class WebScraper(MiniScraper):

    def __init__(self, session:HTTPRequests):
        self.session = session
    
    def __setData(self, dataToSet:dict, nroRegistro:int):
        dataSet = dataToSet
        response = self.session.get("https://ion.inapi.cl/Marca/BuscarMarca.aspx")
        
        if "numeroSolicitud" in dataSet:
            dataSet["numeroSolicitud"], dataSet["Hash"] = self.getHdnSolicitudAndHdnHash(
                self.session.post(
                    url = "https://ion.inapi.cl/Marca/BuscarMarca.aspx/FindMarcas",
                    data = self.__setData(dataToPOST1, nroRegistro=nroRegistro)
                )
            )
            dataSet["IDW"] = self.getHdnIDW(response)
        else:
            dataSet["Hash"] = self.getHdnHash(response)
            dataSet["IDW"] = self.getHdnIDW(response)
            dataSet["param2"] = nroRegistro;
        return dataSet
    
    def getData(self, nroRegisto:int):

        response = self.session.post(
            url="https://ion.inapi.cl/Marca/BuscarMarca.aspx/FindMarcaByNumeroSolicitud",
            data=self.__setData(dataToPOST2, nroRegistro=nroRegisto)
        )
        data_json = response.json()['d']
        return json.loads(data_json)
    
    def getMultipleData(self, solicitudes:list):
        data = []
        start = time.perf_counter()
        for solicitud in solicitud:
            start_reg = time.perf_counter()
            data.append(self.getData(solicitud))
            end_reg = time.perf_counter()
            print(f"Solicitud: {solicitud} - {end_reg-start_reg} segundos")
        end = time.perf_counter()
        print(f"Tiempo total: {end-start} segundos")
        return data

    async def __asyncSetData(self, dataToSet:dict, nroRegistro:int):
        dataSet = dataToSet
        response = await self.session.async_get("https://ion.inapi.cl/Marca/BuscarMarca.aspx")
        
        if "numeroSolicitud" in dataSet:
            dataSet["numeroSolicitud"], dataSet["Hash"] = self.getHdnSolicitudAndHdnHash(
                await self.session.async_post(
                    url = "https://ion.inapi.cl/Marca/BuscarMarca.aspx/FindMarcas",
                    data = await self.__asyncSetData(dataToPOST1, nroRegistro=nroRegistro)
                )
            )
            dataSet["IDW"] = self.getHdnIDW(response)
        else:
            dataSet["Hash"] = self.getHdnHash(response)
            dataSet["IDW"] = self.getHdnIDW(response)
            dataSet["param2"] = nroRegistro;
        return dataSet
    
    async def asyncGetData(self, nroRegisto:int):
        response = await self.session.async_post(
            url = "https://ion.inapi.cl/Marca/BuscarMarca.aspx/FindMarcaByNumeroSolicitud",
            data = await self.__asyncSetData(dataToPOST2, nroRegistro=nroRegisto)
        )
        data_json = response.json()['d']
        return json.loads(data_json)
    
    async def asyncGetMultipleData(self, solicitudes:list):
        data = []
        for solicitud in solicitudes:
            start_reg = time.perf_counter()
            data.append(await self.asyncGetData(solicitud))
            end_reg = time.perf_counter()
            print(f"Solicitud: {solicitud} - {end_reg-start_reg} segundos")
        return await asyncio.gather(*data)
    
    def run(self, solicitudes:list):
        if self.session.parallel:
            return asyncio.run(self.asyncGetMultipleData(solicitudes))
        else:
            return self.getMultipleData(solicitudes)