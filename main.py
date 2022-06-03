import requests
import json
#import DESC


new_data = {

            'name': 'hostname',
            'ip_address': requests.get('https://ipv4-internet.yandex.net/api/v0/ip').text.strip('"'),
            'description': 'DESC',
            }

url = 'http://127.0.0.1:8000/servers/add'
response = requests.get(url)


print(response.json())


# print(requests.get('https://ipv4-internet.yandex.net/api/v0/ip').text.strip('"'))




