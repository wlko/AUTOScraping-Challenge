from requests_html import HTMLSession
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

URL = ["https://ion.inapi.cl/Marca/BuscarMarca.aspx",
       "https://ion.inapi.cl/Marca/BuscarMarca.aspx/FindMarcaByNumeroSolicitud",
       "https://ion.inapi.cl/Marca/BuscarMarca.aspx/FindMarcaByNumeroSolicitud"]

session = HTMLSession()
response = session.get(URL[0])
response.html.render(timeout=20)

print(response.html.find('#hdnIDW', first=True).attrs['value'])

# Con Selenium puedo hacer multiples peticiones mantiendo la sesión
# Me aseguro consiguiendo el IDW que se mantiene constante durante la sesión
# Pero no puedo hacer peticiones POST con Selenium para las llamadas subsiguientes

# Necesario para renderizar el HTML
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.maximize_window()
# driver.get(URL[0])

# soup = BeautifulSoup(driver.page_source, 'html.parser')

# print(soup.find('input', {"id":"hdnIDW"})['value'])
# print(soup.find('input', {"id":"hdnHash"})['value'])
# print(driver)

# driver.get(URL[1])

# print(soup.find('input', {"id":"hdnIDW"})['value'])
# print(soup.find('input', {"id":"hdnHash"})['value'])


# Buscando patrones para ver como intervienen los parametros HASH y IDW en las llamadas:
# <input id="hdnHash" type="hidden" value="3c1161197d02f8226b6aa52eb225b7f1">
# <input id="hdnIDW" type="hidden" value="638223680851630035">

# <input id="hdnHash" type="hidden" value="3b8b80dacbe071f8c4ee85b812b0bde7">
# <input id="hdnIDW" type="hidden" value="638223680851630035">

# <input id="hdnHash" type="hidden" value="b824805b8c05c690da4cc3e9aaf38f95">
# <input id="hdnIDW" type="hidden" value="638223680851630035">