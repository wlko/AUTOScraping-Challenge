from custom_request import HTTPRequests
from scraper import MiniScraper
from dataForRequests import dataToPOST1, dataToPOST2
import json

class WebScraper(MiniScraper):

    def __init__(self, session:HTTPRequests):
        self.session = session
        

    def __setData(self, dataToSet:dict, nroRegistro:int):
        dataSet = dataToSet
        response = self.session.get("https://ion.inapi.cl/Marca/BuscarMarca.aspx")
        
        if "numeroSolicitud" in dataSet:
            dataSet["numeroSolicitud"], dataSet["Hash"] = self.getHdnSolicitudAndHdnHash(
                self.session.post(
                    url="https://ion.inapi.cl/Marca/BuscarMarca.aspx/FindMarcas",
                    data=self.__setData(dataToPOST1, nroRegistro=nroRegistro)
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
        

        
