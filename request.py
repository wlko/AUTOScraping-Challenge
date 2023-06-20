from requests_html import HTMLSession
import request as req
import json

class Request:
    def __init__(self, headers:dict, render:bool = False):
        self.headers = headers
        if render: 
            self.session = HTMLSession()
        else: 
            self.session = req.Session()

    def __get(self, url:str):
        response = self.session.get(url, headers=self.headers)
        if self.render:
            return response.html.render(timeout=20)
        else:
            return response
            
    def __post(self, url:str, headers:dict, data:dict):
        response = self.session.get(url, headers=self.headers)
        if self.render:
            return response.html.render(timeout=20)
        else:
            return response

    def concurrent_requests(self, methods:dict, ):


def concurrent_requests (
        nrosRegistros:list = [],
        headers:dict = {}, 
        data1:dict = {},
        data2:dict = {}
    ):

    for registro in nrosRegistros:
        try:
            with HTMLSession as s:
                # Primer GET para obtener los valores de hdnIDW y hdnHash
                response = s.get("https://ion.inapi.cl/Marca/BuscarMarca.aspx", headers=headers)
                # Necesito renderizar el HTML para conseguir los valores de hdnIDW y hdnHash
                response.html.render(timeout=20)

                # Datos iniciales necesarios para las peticiones POST siguientes
                hdnIDW = response.html.find('#hdnIDW', first=True).attrs['value']
                hdnHash = response.html.find('#hdnHash', first=True).attrs['value']

                # Cookies almacenadas ya en la sesión, no es necesario enviarlas en las peticiones
                # Modificando data1 para la primera petición POST
                data1["Hash"] = hdnHash
                data1["IDW"] = hdnIDW
                data1["param2"] = registro

                # Primera petición POST
                response.post("https://ion.inapi.cl/Marca/BuscarMarca.aspx/FindMarcas", headers=headers, json=data1)
                
                # Extrayendo el próximo valor de hdnHash y el Número de Solicitud de la primera petición POST
                hdnHash = json.loads(response.json()['d'])['Hash']
                hdnSolicitud = json.loads(response.json()['d'])['Marcas'][0]['id']
                
                # Modificando data2 para la segunda petición POST
                data2["Hash"] = hdnHash
                data2["IDW"] = hdnIDW
                data2["numeroSolicitud"] = hdnSolicitud
                
                # Segunda petición POST
                response.post("https://ion.inapi.cl/Marca/BuscarMarca.aspx/FindMarcaByNumeroSolicitud", headers=headers, json=data2)

        except Exception as e:
            print(f"Error: {e}")
            continue
                