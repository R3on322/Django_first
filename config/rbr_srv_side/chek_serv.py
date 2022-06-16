import requests
from bs4 import BeautifulSoup


def chek_server_ip_name():
    url_get = 'http://127.0.0.1:8000/api/servers/'
    req = requests.get(url_get).text
    soup = BeautifulSoup(req, 'lxml')
    find_all = [i.text.split() for i in soup.find_all("div", class_="alert-success mt-2")]
    name_list = []
    ip_list = []
    for i in range(len(find_all)):
        name_list.append(find_all[i][0])
        ip_list.append(find_all[i][2])
    return name_list, ip_list