from requests_html import HTMLSession
from random import choice

class HTTPRequests:

    def __init__(self, headers:dict, proxy:bool = False, proxy_list:dict | list = None):
        self.proxy = proxy
        self.session = HTMLSession()
        self.headers = headers
        # Definiendo proxies a utilizar
        if proxy:
            # Tipos de proxies segun configuración pasado por el usuario (lista o API)
            if proxy_list is dict:
                self.proxies = proxy_list
            else:
                self.proxies = self.__get_random_proxy(proxy_list)
    
    def get(self, url:str):
        # Si se utiliza proxy, se intentará la petición hasta que se obtenga una respuesta 200
        while True:
            if self.proxy:
                proxy_used = self.proxies
                response = self.session.get(url, headers=self.headers, proxies=proxy_used)
                print(f"Proxy: {proxy_used}")
                print(response.status_code, response.reason)
            else:
                response = self.session.get(url, headers=self.headers)
                print(response.status_code, response.reason)            
            if response.status_code == 200:
                break

        response.html.render(timeout=20)
        return response.text
            
    def post(self, url:str, data:dict):
        while True:
            if self.proxy:
                proxy_used = self.proxies
                response = self.session.post(url, headers=self.headers, json=data, proxies=proxy_used)
                print(f"Proxy: {proxy_used}")
                print(response.status_code, response.reason)
            else:
                response = self.session.post(url, headers=self.headers, json=data)
                print(response.status_code, response.reason)
            if response.status_code == 200:
                break
        return response
    
    def __get_random_proxy(proxy_list:list):
        return {"https": choice(proxy_list)}
        


# def concurrent_requests (
#         nrosRegistros:list = [],
#         headers:dict = {}, 
#         data1:dict = {},
#         data2:dict = {}
#     ):

#     for registro in nrosRegistros:
#         try:
#             with HTMLSession as s:
#                 # Primer GET para obtener los valores de hdnIDW y hdnHash
#                 response = s.get("https://ion.inapi.cl/Marca/BuscarMarca.aspx", headers=headers)
#                 # Necesito renderizar el HTML para conseguir los valores de hdnIDW y hdnHash
#                 response.html.render(timeout=20)

#                 # Datos iniciales necesarios para las peticiones POST siguientes
#                 hdnIDW = response.html.find('#hdnIDW', first=True).attrs['value']
#                 hdnHash = response.html.find('#hdnHash', first=True).attrs['value']

#                 # Cookies almacenadas ya en la sesión, no es necesario enviarlas en las peticiones
#                 # Modificando data1 para la primera petición POST
#                 data1["Hash"] = hdnHash
#                 data1["IDW"] = hdnIDW
#                 data1["param2"] = registro

#                 # Primera petición POST
#                 response.post("https://ion.inapi.cl/Marca/BuscarMarca.aspx/FindMarcas", headers=headers, json=data1)
                
#                 # Extrayendo el próximo valor de hdnHash y el Número de Solicitud de la primera petición POST
#                 hdnHash = json.loads(response.json()['d'])['Hash']
#                 hdnSolicitud = json.loads(response.json()['d'])['Marcas'][0]['id']
                
#                 # Modificando data2 para la segunda petición POST
#                 data2["Hash"] = hdnHash
#                 data2["IDW"] = hdnIDW
#                 data2["numeroSolicitud"] = hdnSolicitud
                
#                 # Segunda petición POST
#                 response.post("https://ion.inapi.cl/Marca/BuscarMarca.aspx/FindMarcaByNumeroSolicitud", headers=headers, json=data2)

#         except Exception as e:
#             print(f"Error: {e}")
#             continue
                