import requests
import DESC


new_data = {'name': 'hostname',
            'description': 'DESC',
            'ip_address': requests.get('https://ipv4-internet.yandex.net/api/v0/ip').text.strip('"'),
            }


response = requests.post('http://127.0.0.1:8000/api/servers/add', json=new_data)


print(response.json())


#print(requests.get('https://ipv4-internet.yandex.net/api/v0/ip').text.strip('"'))




