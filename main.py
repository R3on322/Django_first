import requests, logging
import json
from rbr_srv_side import DESC
import time
from rbr_srv_side import chek_serv



def post_zapros():
    count_exceptions = 0
    descript = str(DESC.PCInfo.main_inf())
    logger.info('Отправляю массив данных на сервер...')
    while True:
        try:
            name_ip_chek = list(chek_serv.chek_server_ip_name())
            new_data = {
                'name': 'hostname_1',
                'ip_address': requests.get('https://ipv4-internet.yandex.net/api/v0/ip').text.strip('"'),
                'description': descript,
                'server_is_active': True
                }
            url = 'http://127.0.0.1:8000/api/servers/add'
            if new_data['name'] in name_ip_chek[0]:
                raise NameError
            elif new_data['ip_address'] in name_ip_chek[1]:
                raise ValueError
            else:
                response = requests.post(url, data=new_data)
        except requests.exceptions.RequestException:
            count_exceptions += 1
            logger.error(f'Попытка соединения с сервером... {count_exceptions}')
            if count_exceptions == 5:
                logger.error('Ошибка соединения с сервером. Проверьте подключение...')
                break
        except ValueError:
            logger.error('Ошибка в IP адресе сервера. Возможно данный IP уже есть на сервере...')
            break
        except NameError:
            logger.error('Ошибка в названии сервера. Возможно данное имя уже используется...')
            break
        except:
            logger.error('Возникла ошибка! Проверьте код...')
        else:
            logger.info('Массив успешно отправлен на сервер!')
        time.sleep(10)

def logg_info(name):
    logger = logging.getLogger(name)
    format_log = logging.Formatter('%(asctime)s :: %(name)s :: %(levelname)s :: %(message)s', datefmt='%d %b %Y %H:%M:%S')
    logger.setLevel(logging.DEBUG)
    str_handler = logging.StreamHandler()
    str_handler.setFormatter(format_log)
    str_handler.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler(filename='logs/log_file.log', mode='w')
    file_handler.setFormatter(format_log)
    file_handler.setLevel(logging.INFO)
    logger.addHandler(str_handler)
    logger.addHandler(file_handler)
    logger.info('Логгер запущен...')

logg_info('app')
logger = logging.getLogger('app.main')

if __name__ == "__main__":
    post_zapros()