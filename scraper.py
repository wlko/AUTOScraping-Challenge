from bs4 import BeautifulSoup
import json

class MiniScraper:

    def getHdnIDW(self, response):
        soup = BeautifulSoup(response, 'html.parser')
        hdnIDW = soup.find(id="hdnIDW").get('value')
        return hdnIDW
    
    def getHdnHash(self, response):
        soup = BeautifulSoup(response.html, 'html.parser')
        hdnHash = soup.find(id="hdnHash").get('value')
        return hdnHash
    
    def getHdnSolicitudAndHdnHash(self, response):
        json_data = json.loads(response.json()['d'])
        return json_data['Marcas'][0]['id'], json_data['Hash']
        