from requests_html import HTMLSession, AsyncHTMLSession
from random import choice

class HTTPRequests:

    def __init__(self, headers:dict, proxy_list:dict | list = None, parallel:bool = False):
        # Tipo de sesión segun configuración pasado por el usuario (Async o no)
        self.parallel = parallel
        self.session = HTMLSession() if not parallel else AsyncHTMLSession()
        self.headers = headers
        # Definiendo proxies a utilizar
        self.proxy_list = proxy_list

        if proxy_list != None:
            # Tipos de proxies segun configuración pasado por el usuario (lista o API)
            if proxy_list is dict:
                self.proxy = proxy_list
            else:
                self.proxy = self.__get_random_proxy(proxy_list)
    
    def get(self, url:str):
        # Si se utiliza proxy, se intentará la petición hasta que se obtenga una respuesta 200
        if self.proxy_list != None:
            while True:
                response = self.session.get(url, headers=self.headers, proxies=self.proxy)
                print(f"Proxy: {self.proxy}")
                print(response.status_code, response.reason)
                if response.status_code == 200:
                    break;
                else:
                    if self.proxy_list is list:
                        self.proxy = self.__get_random_proxy(self.proxy_list)
                    continue
        else:
            response = self.session.get(url, headers=self.headers)
            print(response.status_code, response.reason)   

        response.html.render(timeout=20)
        return response.text
            
    def post(self, url:str, data:dict):
        # Si se utiliza proxy, se intentará la petición hasta que se obtenga una respuesta 200
        if self.proxy_list != None:
            while True:
                response = self.session.post(url, headers=self.headers, json=data, proxies=self.proxy)
                print(f"Proxy: {self.proxy}")
                print(response.status_code, response.reason)
                if response.status_code == 200:
                    break;
                else:
                    if self.proxy_list is list:
                        self.proxy = self.__get_random_proxy(self.proxy_list)
                    continue
        else:
            response = self.session.post(url, headers=self.headers, json=data)
            print(response.status_code, response.reason)  
        return response
    
    async def async_get(self, url:str):
        # Si se utiliza proxy, se intentará la petición hasta que se obtenga una respuesta 200
        if self.proxy_list != None:
            while True:
                response = self.session.get(url, headers=self.headers, proxies=self.proxy)
                print(f"Proxy: {self.proxy}")
                print(response.status_code, response.reason)
                if response.status_code == 200:
                    break;
                else:
                    if self.proxy_list is list:
                        self.proxy = self.__get_random_proxy(self.proxy_list)
                    continue
        else:
            response = await self.session.get(url, headers=self.headers)
            # print(response.status_code, response.reason)   

        await response.html.arender(timeout=20)
        return response.text
    
    async def async_post(self, url:str, data:dict):
        # Si se utiliza proxy, se intentará la petición hasta que se obtenga una respuesta 200
        if self.proxy_list != None:
            while True:
                response = await self.session.post(url, headers=self.headers, json=data, proxies=self.proxy)
                print(f"Proxy: {self.proxy}")
                print(response.status_code, response.reason)
                if response.status_code == 200:
                    break;
                else:
                    if self.proxy_list is list:
                        self.proxy = self.__get_random_proxy(self.proxy_list)
                    continue
        else:
            response = await self.session.post(url, headers=self.headers, json=data)
            print(response.status_code, response.reason)  
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
                