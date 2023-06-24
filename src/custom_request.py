from requests_html import HTMLSession, AsyncHTMLSession
from random import choice

class HTTPRequests:

    def __init__(self, headers:dict, data: dict = None, proxy_list:dict | list = None, parallel:bool = False):
        # Tipo de sesión segun configuración pasado por el usuario (Async o no)
        self.session = HTMLSession() if not parallel else AsyncHTMLSession()
        self.headers = headers
        if data != None:
            self.dataPost1 = data["DATAPOST1"]
            self.dataPost2 = data["DATAPOST2"]
        self.parallel = parallel
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
                print(f"GET {response.status_code} {response.reason}")
                if response.status_code == 200:
                    break;
                else:
                    if self.proxy_list is list:
                        self.proxy = self.__get_random_proxy(self.proxy_list)
                    continue
        else:
            response = self.session.get(url, headers=self.headers)
            print(f"GET {response.status_code} {response.reason}")


        response.html.render(timeout=20)
        return response.text
            
    def post(self, url:str, data:dict):
        # Si se utiliza proxy, se intentará la petición hasta que se obtenga una respuesta 200
        if self.proxy_list != None:
            while True:
                response = self.session.post(url, headers=self.headers, json=data, proxies=self.proxy)
                print(f"Proxy: {self.proxy}")
                print(f"POST {response.status_code} {response.reason}")                
                if response.status_code == 200:
                    break;
                else:
                    if self.proxy_list is list:
                        self.proxy = self.__get_random_proxy(self.proxy_list)
                    continue
        else:
            response = self.session.post(url, headers=self.headers, json=data)
            print(f"POST {response.status_code} {response.reason}")
 
        return response
    
    # async def async_get(self, url:str):
    #     # Si se utiliza proxy, se intentará la petición hasta que se obtenga una respuesta 200
    #     if self.proxy_list != None:
    #         while True:
    #             response = self.session.get(url, headers=self.headers, proxies=self.proxy)
    #             print(f"Proxy: {self.proxy}")
    #             print(response.status_code, response.reason)
    #             if response.status_code == 200:
    #                 break;
    #             else:
    #                 if self.proxy_list is list:
    #                     self.proxy = self.__get_random_proxy(self.proxy_list)
    #                 continue
    #     else:
    #         response = await self.session.get(url, headers=self.headers)
    #         # print(response.status_code, response.reason)   

    #     await response.html.arender(timeout=20)
    #     return response.text
    
    # async def async_post(self, url:str, data:dict):
    #     # Si se utiliza proxy, se intentará la petición hasta que se obtenga una respuesta 200
    #     if self.proxy_list != None:
    #         while True:
    #             response = await self.session.post(url, headers=self.headers, json=data, proxies=self.proxy)
    #             print(f"Proxy: {self.proxy}")
    #             print(response.status_code, response.reason)
    #             if response.status_code == 200:
    #                 break;
    #             else:
    #                 if self.proxy_list is list:
    #                     self.proxy = self.__get_random_proxy(self.proxy_list)
    #                 continue
    #     else:
    #         response = await self.session.post(url, headers=self.headers, json=data)
    #         print(response.status_code, response.reason)  
    #     return response
    
    def __get_random_proxy(proxy_list:list):
        return {"https": choice(proxy_list)}