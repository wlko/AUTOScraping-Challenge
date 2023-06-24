import os

# Default parameters
class args:    
    # Opción para realizar todas las peticiones de manera asincrónica
    PARALLEL = False

    # Agregar lista o API de proxies
    # PROXIES = {
    #     "http": "",
    #     "https": ""
    #     }

    # Definir acá los registros a buscar
    REGISTROS = ['1236216', '1236222', '1236223', '1236224']
    
    SAVE_FILE_NAME = "scrape_24_06_2023"

    EXP_DIR =  f"{os.path.abspath(os.getcwd())}\data"

    HEADERS = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json; charset=utf-8',
        'Origin': 'https://ion.inapi.cl',
        'Referer': 'https://ion.inapi.cl/Marca/BuscarMarca.aspx',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    DATA = {
        "DATAPOST1": {
            "LastNumSol": 0,
            "Hash": "",
            "IDW": "",
            "responseCaptcha": "este texto no se validará",
            "param1": "",
            "param2": "",
            "param3": "",
            "param4": "",
            "param5": "",
            "param6": "",
            "param7": "",
            "param8": "",
            "param9": "",
            "param10": "",
            "param11": "",
            "param12": "",
            "param13": "",
            "param14": "",
            "param15": "",
            "param16": "",
            "param17": "1"
        },    
        "DATAPOST2": {
            "numeroSolicitud": "",
            "Hash": "",
            "IDW": ""
        }
    }