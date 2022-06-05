import requests
import json
#from config.rbr_srv_side import DESC


new_data = {
            'name': 'hostname',
            'ip_address': requests.get('https://ipv4-internet.yandex.net/api/v0/ip').text.strip('"'),
            'description': "DESC_123",
            'server_is_active': True
            }

url = 'http://127.0.0.1:8000/api/servers/add_post'
url_get = 'http://127.0.0.1:8000/api/servers'
response = requests.post(url, json=new_data)
response_get = requests.get(url_get)
print(response_get.json())
#print(response.json())


# print(requests.get('https://ipv4-internet.yandex.net/api/v0/ip').text.strip('"'))




