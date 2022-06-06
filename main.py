import requests
import json
from rbr_srv_side import DESC


def POST_zapros():
    new_data = {
                'name': 'hostname',
                'ip_address': requests.get('https://ipv4-internet.yandex.net/api/v0/ip').text.strip('"'),
                'description': str(DESC.PC_info.main_inf())
                }
    url = 'http://127.0.0.1:8000/api/servers/add_post'
    response = requests.post(url, json=new_data)
    print(response.json())

POST_zapros()