import requests
import json

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    # 'Content-Length': '0',
    'Content-Type': 'application/json; charset=utf-8',
    # 'Cookie': 'ASP.NET_SessionId=5jvnqbbd42hipwjnans0ph1r; pnctest=1; _gid=GA1.2.1567993955.1687202772; _ga_B2C27FPMYG=GS1.1.1687208679.26.0.1687208679.0.0.0; _ga=GA1.2.657243374.1686515091; _gat=1; _gat_gtag_UA_55154893_3=1',
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

s = requests.Session()
response = s.post('https://ion.inapi.cl/Marca/BuscarMarca.aspx/GetEstadosInstancias', headers=headers)

print(response.cookies.get_dict())
# response_data = response.json()['d']
# json_data = json.loads(response_data)

# save_file = open("savedata.json", "w")
# json.dump(json_data, save_file, indent=4)
# save_file.close()

# print(json_formatted_str)

