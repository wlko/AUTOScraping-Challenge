from request import HTTPRequest
from scraper import MiniScraper
from dataForRequests import dataToPOST1, dataToPOST2
import json

class WebScraper(MiniScraper):

    def __init__(self, session:HTTPRequest):
        self.session = session

    def __setData(self, dataToSet:dict, nroRegistro:int):
        dataSet = dataToSet
        response = self.session.get("https://ion.inapi.cl/Marca/BuscarMarca.aspx", headers=self.session.headers)
        
        if "numeroSolicitud" in dataSet:
            dataSet["numeroSolicitud"], dataSet["Hash"] = self.getHdnSolicitudAndHdnHash(
                self.session.post(
                    url="https://ion.inapi.cl/Marca/BuscarMarca.aspx/FindMarcas",
                    headers=self.session.headers,
                    data=self.setData(dataToPOST1, nroRegistro=nroRegistro)
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
            headers=self.session.headers,
            data=self.__setData(dataToPOST2, nroRegistro=nroRegisto)

        )
        data_json = response.json()['d']
        return json.load(data_json)
        

        
