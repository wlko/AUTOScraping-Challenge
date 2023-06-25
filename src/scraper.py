from bs4 import BeautifulSoup
import json

class MiniScraper:

    def getHdnIDW(self, response):
        soup = BeautifulSoup(response, 'html.parser')
        hdnIDW = soup.find(id="hdnIDW").get('value')
        return hdnIDW
    
    def getHdnHash(self, response):
        soup = BeautifulSoup(response, 'html.parser')
        hdnHash = soup.find(id="hdnHash").get('value')
        return hdnHash
    
    def getHdnSolicitudAndHdnHash(self, response):
        json_data = json.loads(response.json()['d'])
        return json_data['Marcas'][0]['id'], json_data['Hash']
    
    #>-----------------------------------------------------------<

    # Métodos para obtener parametros dentro de los responses
    def getNroRegistro(self, response):
        return response['Marca']['NumeroRegistro']
    
    def getObservadaFechaFondo(self, response):
        instances = response['Marca']['Instancias']        
        observadasYFechas = []
        for instance in instances:
            if "Resolución de observaciones de fondo de marca" in instance['EstadoDescripcion']:
                observadasYFechas.append({"Observada_de_Fondo": True, "Fecha_Observada_Fondo": instance['Fecha']})        
        if len(observadasYFechas) == 0:
            return False
        else:
            return observadasYFechas
        
    def getApelaciones(self, response):
        instances = response['Marca']['Instancias']
        for instance in instances:
            if "Recurso de apelacion" in instance['EstadoDescripcion']:
                return True
        return False

    def getIPT(self, response):
        instances = response['Marca']['Instancias']
        for instance in instances:
            if "IPT" in instance['EstadoDescripcion'] or "IPTV" in instance['EstadoDescripcion']:
                return True
        return False       